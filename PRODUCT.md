# Product

<!-- impeccable:product-schema 1 -->

Written 2026-11-14 from the repository (README, SKILL.md, app code) without an interview: the owner asked for the redesign to go ahead on the designer's judgment. Every line below is an inference from the repo unless marked confirmed.

## Platform

web

## Users

One person: a job seeker running a LinkedIn referral campaign from their own computer. They open the desk for about ten minutes a day, usually alongside a Claude Code session, to read the drafts Claude wrote, edit and approve them, and see who accepted or replied.

## Product Purpose

Outreach Desk is the local dashboard of the LinkedIn Outreach skill for Claude Code. Claude finds people, sends connection requests, and drafts thank-you, CV and follow-up messages; the desk is where the person reviews every draft, approves it, queues the sending ("Run changes"), and tracks each contact through the pipeline. Success is a short daily session that ends with every pending draft decided and nothing sent that the person did not read.

## Positioning

The person approves every word. Claude drafts and does the clicking; nothing reaches LinkedIn without an explicit approval on this page. Everything runs on localhost with the contacts in one file on the person's machine.

## Operating Context

- Served by `app/server.py` at http://localhost:4877, opened by the skill or by `Outreach Desk.app`.
- Pipeline stages: To request, Requested, Accepted, Thanked, CV sent, Followed up, Replied, Done, plus Stale (automatic after 21 days without an answer) and Blacklisted.
- Daily loop: Review drafts, Approve (one or all), Run changes, Claude sends, page updates by polling.
- Brakes shown on the desk: 15 invites per 24 hours, 80 per 7 days.
- Contacts are grouped by country and by campaign.

## Capabilities and Constraints

- One self-contained `app/web/index.html`: no build step, no dependencies, no network requests. It must keep working offline, so no web fonts or CDN scripts.
- The JSON API (`/api/state`, `/api/contacts`, `/api/contacts/<id>`, `/api/run`) and the data model in `store.py` are fixed; Claude's skill workflow reads and writes the same data.
- Live view (2026-11-14): while Claude works on LinkedIn, its browser tab is mirrored into the dashboard (JPEG frames posted to `/api/live/frame`, shown from `/api/live/stream`), with per-item progress from `store.py step`. LinkedIn refuses to be embedded in another page, so the dashboard shows a live picture of Claude's browser rather than LinkedIn itself; the browser window still exists in the background and is where the owner logs in.
- Existing functions to preserve: views (Review drafts, Ready to send, Due, Replies, Stale invites, Everyone, per-stage, Blacklist), country filter, search, list and board layouts with drag and drop, the person inspector (journey, messages, details, status, notes, history), Approve / Approve all / undo, "I sent it myself", withdraw and blacklist with a two-click confirm, Add person, the Run changes button and the Live run panel (waiting, working, finished, shrunk to a floating preview), keyboard shortcuts (arrows or J/K, A, /, Esc), light and dark themes with a System / Light / Dark switch.
- The repo is public-facing code (MIT, currently private on GitHub); README screenshots in `docs/` show the dashboard.

## Brand Commitments

- Name: Outreach Desk (dashboard), LinkedIn Outreach (skill).
- Voice: plain, direct, second person ("Approve", "Run changes", "Answer these yourself").
- Standing preference (owner, 2026-11-14): the dashboard should look like a top-tier product site and sit alongside Linear, Attio and Superhuman, with smooth transitions and purposeful animation. Their craft level is the bar.
- Logo: the Outreach Desk mark (a flat violet tile with a white ring and a filling wedge, the same ring that marks pipeline stages), `docs/logo.svg`, made 2026-11-14.

## Evidence on Hand

- The owner's real contacts in the git-ignored `data/db.json` (private: never copied into screenshots that ship in the repo).
- README screenshots (`docs/dashboard.png`, `light.png`, `contact.png`, `board.png`, `live.png`), `docs/live.gif` and `docs/tutorial.mp4` show the current look with invented demo data. The browser inside the live panel in them is a stand-in demo page.

## Product Principles

1. Nothing is sent unread: approval is the central act and must be unmistakable.
2. The desk says what to do next, per person and for the day.
3. State is never ambiguous: drafted, edited, approved, queued, sent, each reads differently.
4. Ten minutes a day: the fastest path through the review queue wins over everything else.
5. Local and private by construction.

## Accessibility & Inclusion

Keyboard operable throughout, visible focus, reduced-motion and reduced-transparency respected, colour never the only carrier of state.
