#!/usr/bin/env python3
"""Outreach Desk local server: http://localhost:4877 (this computer only).

Serves web/index.html and a tiny JSON API over store.py. Stops by itself
after IDLE_HOURS without any request (the open page polls, so it stays up
while the dashboard is open).
"""
import json, os, re, signal, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import store  # noqa: E402

PORT = int(os.environ.get("OUTREACH_PORT", "4877"))
IDLE_HOURS = 3
ALLOWED_HOSTS = {f"localhost:{PORT}", f"127.0.0.1:{PORT}"}
INDEX = os.path.join(HERE, "web", "index.html")
last_hit = time.time()
last_page = 0.0  # last time an open dashboard polled /api/state


class Handler(BaseHTTPRequestHandler):
    server_version = "OutreachDesk"

    def log_message(self, fmt, *args):  # keep the log quiet: errors only
        pass

    def _host_ok(self):
        # blocks DNS-rebinding: only answer requests addressed to localhost
        return self.headers.get("Host", "") in ALLOWED_HOSTS

    def _send(self, code, body=b"", ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _json(self, code, obj):
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        global last_hit, last_page
        last_hit = time.time()
        if not self._host_ok():
            return self._send(403)
        path, _, qs = self.path.partition("?")
        if path in ("/", "/index.html"):
            with open(INDEX, "rb") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if path == "/api/ping":
            return self._json(200, {"ok": True, "pageOpen": time.time() - last_page < 15})
        if path == "/api/state":
            last_page = time.time()
            m = re.search(r"(?:^|&)rev=(\d+)", qs)
            db = store.state()
            if m and int(m.group(1)) == db.get("rev"):
                return self._send(204)
            contacts = [{"id": k, **v} for k, v in db["contacts"].items()]
            return self._json(200, {"rev": db.get("rev"), "contacts": contacts, "meta": db.get("meta", {})})
        return self._send(404)

    def do_POST(self):
        global last_hit
        last_hit = time.time()
        # custom header = browsers must preflight cross-site requests, which we never allow
        if not self._host_ok() or self.headers.get("X-Outreach-Desk") != "1":
            return self._send(403)
        if self.path == "/api/contacts":
            try:
                n = int(self.headers.get("Content-Length", "0"))
                body = json.loads(self.rfile.read(n) or b"{}")
                cid = str(body.get("id", ""))
                if not re.fullmatch(r"[A-Za-z0-9_\-]{1,200}", cid):
                    return self._json(400, {"error": "Bad id"})
                allowed = {"name", "headline", "company", "location", "country", "group", "linkedinUrl", "status", "requestedAt", "acceptedAt", "notes", "source", "campaign"}
                doc = {k: v for k, v in (body.get("contact") or {}).items() if k in allowed and isinstance(v, str)}
                if not doc.get("name"):
                    return self._json(400, {"error": "Name is required"})
                c = store.create_contact(cid, doc)
                return self._json(200, {"ok": True, "contact": c, "rev": store.rev()})
            except FileExistsError:
                return self._json(409, {"error": "This person is already on the desk"})
            except Exception as e:  # noqa: BLE001
                return self._json(400, {"error": str(e)})
        if self.path == "/api/stop":
            self._json(200, {"ok": True})
            threading.Thread(target=self.server.shutdown, daemon=True).start()
            return
        if self.path == "/api/run":
            rr = store.set_run("requested")
            return self._json(200, {"ok": True, "runRequest": rr, "rev": store.rev()})
        m = re.fullmatch(r"/api/contacts/([A-Za-z0-9_\-]{1,200})", self.path)
        if not m:
            return self._send(404)
        try:
            n = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(n) or b"{}")
            c = store.update_contact(m.group(1), body.get("patch") or {}, body.get("event"), body.get("by") or "You")
            return self._json(200, {"ok": True, "contact": c, "rev": store.rev()})
        except KeyError:
            return self._json(404, {"error": "No such contact"})
        except Exception as e:  # noqa: BLE001
            return self._json(400, {"error": str(e)})

    def do_OPTIONS(self):
        return self._send(403)


def idle_watch(srv):
    while True:
        time.sleep(60)
        if time.time() - last_hit > IDLE_HOURS * 3600:
            srv.shutdown()
            return


if __name__ == "__main__":
    if hasattr(signal, "SIGHUP"):
        signal.signal(signal.SIGHUP, signal.SIG_IGN)  # survive the launcher (app / terminal) closing
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    threading.Thread(target=idle_watch, args=(srv,), daemon=True).start()
    print(f"Outreach Desk on http://localhost:{PORT}", flush=True)
    srv.serve_forever()
