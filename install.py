#!/usr/bin/env python3
"""Set up LinkedIn Outreach for Claude Code.

Run it from the skill folder:  python3 install.py
It never installs anything without asking. Standard library only.
"""
import os, platform, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
ASK = "--no-input" not in sys.argv


def say(msg=""):
    print(msg, flush=True)


def ask(q, default=True):
    if not ASK:
        return False
    hint = "[Y/n]" if default else "[y/N]"
    a = input(f"{q} {hint} ").strip().lower()
    return default if not a else a.startswith("y")


def ok(msg):
    say(f"  ✓ {msg}")


def warn(msg):
    say(f"  ! {msg}")


def main():
    say("LinkedIn Outreach setup\n")

    # 1. Python
    if sys.version_info < (3, 9):
        sys.exit(f"Python 3.9 or newer is needed (this is {platform.python_version()}).")
    ok(f"Python {platform.python_version()}")

    # 2. Where the skill sits
    parts = HERE.replace("\\", "/").split("/")
    if len(parts) >= 3 and parts[-3] == ".claude" and parts[-2] == "skills":
        ok(f"Skill folder: {HERE}")
    else:
        warn("This folder is not inside a .claude/skills/ folder, so Claude Code won't find the skill.")
        say("    Move or clone it to ~/.claude/skills/linkedin-outreach (all projects)")
        say("    or <your project>/.claude/skills/linkedin-outreach (one project), then run this again.")

    # 3. Private data folder + profile
    os.makedirs(os.path.join(DATA, "backups"), exist_ok=True)
    ok("data/ folder ready (private, git-ignored)")
    if os.path.exists(os.path.join(DATA, "profile.md")):
        ok("data/profile.md exists")
    else:
        say("  · data/profile.md will be created by Claude on first run (it reads your LinkedIn profile)")

    # 4. Claude Code
    claude = shutil.which("claude")
    if not claude:
        warn("Claude Code (`claude`) not found on PATH. Install it first: https://claude.com/claude-code")
    else:
        ok("Claude Code found")
        try:
            listing = subprocess.run([claude, "mcp", "list"], capture_output=True, text=True, timeout=90).stdout
        except Exception:
            listing = ""
        # 5. Playwright (required)
        if "playwright" in listing.lower():
            ok("Playwright browser server is set up in Claude")
        else:
            warn("Playwright browser server not found in Claude (required: Claude uses it to work in LinkedIn).")
            if not shutil.which("npx"):
                say("    It needs Node.js (npx). Install Node.js first: https://nodejs.org")
            elif ask("    Add it now with `claude mcp add playwright -- npx @playwright/mcp@latest` (your user settings)?"):
                subprocess.run([claude, "mcp", "add", "--scope", "user", "playwright", "--", "npx", "@playwright/mcp@latest"])
            else:
                say("    Later: claude mcp add --scope user playwright -- npx @playwright/mcp@latest")
        # 6. Apollo (optional)
        if "apollo" in listing.lower():
            ok("Apollo is set up in Claude")
        else:
            say("  · Apollo (optional) finds people by company, title and country, free people search.")
            if ask("    Add Apollo now with `claude mcp add --transport http apollo https://mcp.apollo.io/mcp`?", default=False):
                subprocess.run([claude, "mcp", "add", "--scope", "user", "--transport", "http", "apollo", "https://mcp.apollo.io/mcp"])
                say("    Then in Claude Code: /mcp → apollo → sign in.")
            else:
                say("    Skipped. Without Apollo, Claude searches people on LinkedIn instead.")

    # 7. macOS app
    if platform.system() == "Darwin" and shutil.which("osacompile"):
        app = os.path.join(HERE, "Outreach Desk.app")
        if os.path.exists(app):
            ok("Outreach Desk.app exists")
        elif ask("  Build 'Outreach Desk.app' (double-click to open the dashboard; drag it to your Dock)?"):
            src = open(os.path.join(HERE, "app", "launcher.applescript"), encoding="utf-8").read()
            src = src.replace("__PYTHON__", sys.executable)
            tmp = os.path.join(DATA, ".launcher.applescript")
            open(tmp, "w", encoding="utf-8").write(src)
            subprocess.run(["osacompile", "-o", app, tmp], check=True)
            os.remove(tmp)
            ok("Built Outreach Desk.app")

    say("\nDone. Next:")
    say("  1. Open Claude Code in the project that holds this skill (or anywhere, if installed in ~/.claude/skills).")
    say("  2. Say: set up linkedin outreach")
    say("     Claude opens the dashboard, asks you to log in to LinkedIn in its browser window,")
    say("     reads your profile and asks a few questions.")
    say("  3. Then: start a campaign for <country>, and every day: run today's outreach")


if __name__ == "__main__":
    main()
