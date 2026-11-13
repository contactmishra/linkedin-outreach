#!/usr/bin/env python3
"""Start the Outreach Desk server if needed and open the dashboard in the browser.

  python3 app/launch.py              start (if needed) and open a tab
  python3 app/launch.py --if-closed  same, but no new tab if a dashboard tab is already open
  python3 app/launch.py --stop       stop the server

Works on macOS, Linux and Windows. Standard library only.
"""
import json, os, subprocess, sys, time, urllib.request, webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("OUTREACH_PORT", "4877"))
URL = f"http://localhost:{PORT}/"
DATA = os.environ.get("OUTREACH_DATA") or os.path.join(os.path.dirname(HERE), "data")


def ping():
    try:
        with urllib.request.urlopen(URL + "api/ping", timeout=1) as r:
            return json.load(r)
    except Exception:
        return None


def python_exe():
    """Prefer a .venv in the project that holds this skill (<project>/.claude/skills/<name>/app)."""
    root = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
    for cand in (os.path.join(root, ".venv", "bin", "python"), os.path.join(root, ".venv", "Scripts", "python.exe")):
        if os.path.exists(cand):
            return cand
    return sys.executable


def start():
    os.makedirs(DATA, exist_ok=True)
    log = open(os.path.join(DATA, "server.log"), "a")
    kw = {"stdout": log, "stderr": log, "stdin": subprocess.DEVNULL, "cwd": HERE}
    if os.name == "nt":
        kw["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        kw["start_new_session"] = True
    subprocess.Popen([python_exe(), os.path.join(HERE, "server.py")], **kw)
    for _ in range(40):
        if ping():
            return True
        time.sleep(0.15)
    return False


def stop():
    try:
        req = urllib.request.Request(URL + "api/stop", method="POST", data=b"{}",
                                     headers={"X-Outreach-Desk": "1", "Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=2)
        print("Outreach Desk stopped")
    except Exception:
        print("Outreach Desk was not running")


def main():
    if "--stop" in sys.argv:
        return stop()
    p = ping()
    if not p and not start():
        sys.exit(f"Could not start the server, see {os.path.join(DATA, 'server.log')}")
    if "--if-closed" in sys.argv and (ping() or {}).get("pageOpen"):
        print(f"Outreach Desk already open at {URL}")
        return
    webbrowser.open(URL)
    print(f"Opened {URL}")


if __name__ == "__main__":
    main()
