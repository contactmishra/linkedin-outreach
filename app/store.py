#!/usr/bin/env python3
"""Outreach Desk data store: one JSON file, locked writes, daily backups.

Used by server.py (the dashboard) and by Claude from the command line:

  store.py summary                        counts by status, what is due
  store.py list [--status S] [--country C] [--fields a,b,c]
  store.py get ID
  store.py update ID '<json patch>' [--event "text"] [--by Claude]
  store.py set ID file.json|-             create or replace a contact
  store.py import DIR                     one <id>.json per contact (set)
  store.py meta KEY '<json patch>'        e.g. meta run '{"lastRun": "..."}'
  store.py blacklist                      blacklisted contacts (for campaign de-dupe)

A patch merges into the contact (nested objects merge, arrays replace);
{"__delete__": true} as a value removes that key.
"""
import argparse, json, os, shutil, sys, tempfile
from contextlib import contextmanager
from datetime import datetime, timezone

try:
    import fcntl  # macOS, Linux
except ImportError:  # Windows
    fcntl = None
    import msvcrt

HERE = os.path.dirname(os.path.abspath(__file__))
# Private data lives next to the app, in <skill>/data (git-ignored). OUTREACH_DATA overrides it.
DATA = os.environ.get("OUTREACH_DATA") or os.path.join(os.path.dirname(HERE), "data")
DB = os.path.join(DATA, "db.json")
LOCK = os.path.join(DATA, ".lock")
BACKUPS = os.path.join(DATA, "backups")
DEFAULT_SETTINGS = {"cvDelayDays": 3, "followUpDays": 7, "closeDays": 7, "staleDays": 21, "weeklyCap": 80, "dailyCap": 15}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _empty():
    return {"rev": 0, "contacts": {}, "meta": {"settings": dict(DEFAULT_SETTINGS), "run": {}}}


@contextmanager
def _locked():
    os.makedirs(DATA, exist_ok=True)
    with open(LOCK, "a+") as fh:
        if fcntl:
            fcntl.flock(fh, fcntl.LOCK_EX)
        else:
            fh.seek(0)
            msvcrt.locking(fh.fileno(), msvcrt.LK_LOCK, 1)
        try:
            yield
        finally:
            if fcntl:
                fcntl.flock(fh, fcntl.LOCK_UN)
            else:
                fh.seek(0)
                msvcrt.locking(fh.fileno(), msvcrt.LK_UNLCK, 1)


def _read():
    if not os.path.exists(DB):
        return _empty()
    with open(DB, encoding="utf-8") as f:
        return json.load(f)


def _write(db):
    db["rev"] = int(db.get("rev", 0)) + 1
    os.makedirs(BACKUPS, exist_ok=True)
    today = os.path.join(BACKUPS, f"db-{datetime.now().strftime('%Y-%m-%d')}.json")
    if os.path.exists(DB) and not os.path.exists(today):
        shutil.copy2(DB, today)  # first change of the day keeps yesterday's state
    fd, tmp = tempfile.mkstemp(dir=DATA, prefix=".db-", suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, DB)


def _merge(dst, patch):
    for k, v in patch.items():
        if isinstance(v, dict) and v.get("__delete__") is True:
            dst.pop(k, None)
        elif isinstance(v, dict) and isinstance(dst.get(k), dict):
            _merge(dst[k], v)
        else:
            dst[k] = v
    return dst


def state():
    with _locked():
        return _read()


def rev():
    db = state()
    return db.get("rev", 0)


def update_contact(cid, patch, event=None, by="You"):
    with _locked():
        db = _read()
        if cid not in db["contacts"]:
            raise KeyError(cid)
        c = _merge(db["contacts"][cid], patch)
        c["updatedAt"] = now_iso()
        if event:
            c.setdefault("history", []).append({"at": now_iso(), "event": event, "by": by})
        _write(db)
        return c


def create_contact(cid, doc, by="You"):
    """Add a new contact; refuses if the id already exists (used by the dashboard's Add person)."""
    with _locked():
        db = _read()
        if cid in db["contacts"]:
            raise FileExistsError(cid)
        doc = {k: v for k, v in dict(doc).items() if v not in (None, "")}
        doc.pop("id", None)
        doc.setdefault("status", "found")
        doc["updatedAt"] = now_iso()
        doc["history"] = [{"at": now_iso(), "event": "Added on the dashboard", "by": by}]
        db["contacts"][cid] = doc
        _write(db)
        return doc


def set_contact(cid, doc):
    with _locked():
        db = _read()
        doc = dict(doc)
        doc.pop("id", None)
        doc.setdefault("updatedAt", now_iso())
        db["contacts"][cid] = doc
        _write(db)
        return doc


def set_many(docs):
    with _locked():
        db = _read()
        for cid, doc in docs.items():
            doc = dict(doc)
            doc.pop("id", None)
            db["contacts"][cid] = doc
        _write(db)
        return len(docs)


def update_meta(key, patch):
    with _locked():
        db = _read()
        m = db.setdefault("meta", {}).setdefault(key, {})
        _merge(m, patch)
        _write(db)
        return m


DRAFT_LABEL = {"thanks": "thank-you", "cv": "CV message", "followup": "follow-up"}


def queue(db=None):
    """What the user has asked for on the dashboard that Claude still has to do on LinkedIn."""
    db = db or state()
    items = []
    for cid, c in sorted(db["contacts"].items()):
        for k, d in (c.get("drafts") or {}).items():
            if d and d.get("approved") and not d.get("sentAt"):
                items.append({"id": cid, "name": c.get("name"), "action": "send_" + k,
                              "label": f"Send {DRAFT_LABEL.get(k, k)} to {c.get('name')}"})
        if c.get("withdrawPending"):
            items.append({"id": cid, "name": c.get("name"), "action": "withdraw",
                          "label": f"Withdraw invite to {c.get('name')}"})
    return items


def claim_run(force=False):
    """Mark the run as started, unless another Claude session has already claimed it.
    Several sessions can watch the desk; the check and the write happen under one lock,
    so only one of them gets the run and the messages are never sent twice."""
    with _locked():
        db = _read()
        prev = db.get("meta", {}).get("runRequest") or {}
        if prev.get("status") == "running" and not force:
            return None
        rr = {**prev, "status": "running", "at": now_iso(), "startedAt": now_iso()}
        db.setdefault("meta", {})["runRequest"] = rr
        _write(db)
        return rr


def set_run(status, **extra):
    with _locked():
        db = _read()
        rr = {"status": status, "at": now_iso(), **extra}
        if status == "requested":
            rr["items"] = queue(db)
        else:
            prev = db.get("meta", {}).get("runRequest") or {}
            rr = {**prev, **rr}
        db.setdefault("meta", {})["runRequest"] = rr
        _write(db)
        return rr


def run_step(n, state, note=""):
    """Mark item n (1-based) of the current run as doing, done or failed, so the dashboard can show progress."""
    with _locked():
        db = _read()
        rr = db.setdefault("meta", {}).setdefault("runRequest", {})
        items = rr.get("items") or []
        if not 1 <= n <= len(items):
            raise IndexError(f"run has {len(items)} items")
        items[n - 1]["state"] = state
        if note:
            items[n - 1]["note"] = note
        _write(db)
        return items[n - 1]


def _summary(db):
    from collections import Counter
    cs = db["contacts"]
    st = Counter(c.get("status") for c in cs.values())
    drafts_waiting = [cid for cid, c in cs.items() if any(d and not d.get("approved") and not d.get("sentAt") for d in (c.get("drafts") or {}).values())]
    approved = [cid for cid, c in cs.items() if any(d and d.get("approved") and not d.get("sentAt") for d in (c.get("drafts") or {}).values())]
    withdraw = [cid for cid, c in cs.items() if c.get("withdrawPending")]
    return {"rev": db.get("rev"), "total": len(cs), "byStatus": dict(st), "draftsAwaitingOm": drafts_waiting,
            "approvedToSend": approved, "withdrawQueued": withdraw, "lastRun": db.get("meta", {}).get("run")}


def main(argv=None):
    p = argparse.ArgumentParser(description="Outreach Desk data store")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("summary")
    sp = sub.add_parser("list"); sp.add_argument("--status"); sp.add_argument("--country"); sp.add_argument("--fields")
    sp = sub.add_parser("get"); sp.add_argument("id")
    sp = sub.add_parser("update"); sp.add_argument("id"); sp.add_argument("patch"); sp.add_argument("--event"); sp.add_argument("--by", default="Claude")
    sp = sub.add_parser("set"); sp.add_argument("id"); sp.add_argument("file")
    sp = sub.add_parser("import"); sp.add_argument("dir")
    sp = sub.add_parser("meta"); sp.add_argument("key"); sp.add_argument("patch")
    sub.add_parser("blacklist")
    sub.add_parser("queue")
    sp = sub.add_parser("wait-request"); sp.add_argument("--timeout", type=int, default=0, help="seconds, 0 = forever")
    sp = sub.add_parser("start-run"); sp.add_argument("--force", action="store_true", help="take over a run left 'running' by a session that stopped")
    sp = sub.add_parser("step"); sp.add_argument("n", type=int); sp.add_argument("state", choices=["doing", "done", "failed"]); sp.add_argument("--note", default="")
    sp = sub.add_parser("finish-run"); sp.add_argument("--note", default="")
    a = p.parse_args(argv)
    out = None
    if a.cmd == "summary":
        out = _summary(state())
    elif a.cmd == "list":
        cs = state()["contacts"]
        rows = [{"id": k, **v} for k, v in sorted(cs.items())
                if (not a.status or v.get("status") in a.status.split(",")) and (not a.country or v.get("country") == a.country)]
        if a.fields:
            f = ["id"] + a.fields.split(",")
            rows = [{k: r.get(k) for k in f} for r in rows]
        out = rows
    elif a.cmd == "get":
        c = state()["contacts"].get(a.id)
        if c is None:
            sys.exit(f"no contact {a.id}")
        out = {"id": a.id, **c}
    elif a.cmd == "update":
        out = update_contact(a.id, json.loads(a.patch), a.event, a.by)
    elif a.cmd == "set":
        doc = json.load(sys.stdin if a.file == "-" else open(a.file, encoding="utf-8"))
        out = set_contact(a.id, doc)
    elif a.cmd == "import":
        docs = {}
        for fn in sorted(os.listdir(a.dir)):
            if fn.endswith(".json"):
                docs[fn[:-5]] = json.load(open(os.path.join(a.dir, fn), encoding="utf-8"))
        out = {"imported": set_many(docs)}
    elif a.cmd == "meta":
        out = update_meta(a.key, json.loads(a.patch))
    elif a.cmd == "blacklist":
        out = [{"id": k, "name": v.get("name"), "company": v.get("company"), "linkedinUrl": v.get("linkedinUrl"), "apolloId": v.get("apolloId")}
               for k, v in state()["contacts"].items() if v.get("status") == "blacklisted"]
    elif a.cmd == "queue":
        out = queue()
    elif a.cmd == "wait-request":
        import time
        t0 = time.time()
        while True:
            rr = (state().get("meta") or {}).get("runRequest") or {}
            if rr.get("status") == "requested":
                out = {"runRequest": rr, "queue": queue()}
                break
            if a.timeout and time.time() - t0 > a.timeout:
                print(json.dumps({"timeout": True})); sys.exit(2)
            time.sleep(3)
    elif a.cmd == "start-run":
        out = claim_run(a.force)
        if out is None:
            sys.exit("Another Claude session is already running this queue. Do nothing; start the watcher again.")
    elif a.cmd == "step":
        try:
            out = run_step(a.n, a.state, a.note)
        except IndexError as e:
            sys.exit(str(e))
    elif a.cmd == "finish-run":
        out = set_run("done", doneAt=now_iso(), note=a.note)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
