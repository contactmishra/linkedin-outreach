# Live view: the run happens on the dashboard

When the user presses **Run changes**, the dashboard opens a **Live run** panel: a live picture of the browser tab Claude is working in, the step it is on (with the message being sent), and a checklist of the queue. The user stays on the dashboard and never has to look at the Playwright window.

LinkedIn does not allow itself to be embedded in another page, so the panel shows a live picture of Claude's tab, not LinkedIn itself. The Playwright window still exists in the background. The user only needs it to log in.

## What Claude does (workflow D)

1. After `S start-run`, with the LinkedIn tab as the current tab, start mirroring. Call the Playwright tool `browser_run_code_unsafe` with `filename: "<skill>/app/live-start.js"`.
2. Before each queue item: `S step <n> doing` (n counts from 1, in `S queue` order, the same order as `runRequest.items`).
3. After each item: `S step <n> done`, or `S step <n> failed --note "<short reason>"` and carry on with the next one.
4. After the last item, before `S finish-run`: `browser_run_code_unsafe` with `filename: "<skill>/app/live-stop.js"`.

Rules:
- Start the live view only on a tab that shows what the user asked for (their LinkedIn work). Never mirror another tab.
- Stop it at the end of every run, also when the run stops early (login needed, an error). The server also drops the picture by itself if no frame arrives for 3 minutes.
- Do not bring the Playwright window to the front during a run. If LinkedIn asks for a login or a checkpoint, say so in the terminal and with `S step <n> failed --note "LinkedIn login needed"`: the user has to do that in the Playwright window.
- If the tool refuses `filename`, paste the file's content as `code` instead. If the server runs on another port (`OUTREACH_PORT`), change `DESK` in both files' content before running.
- The mirroring listens on the tab's page object. If LinkedIn opens a new tab, switch back to the mirrored one or run `live-start.js` again on the new tab.

## How it works

- `live-start.js` opens a DevTools session on the tab and starts a screencast (JPEG, at most 1280×800). Each frame is POSTed to `http://localhost:4877/api/live/frame` with the `X-Outreach-Desk: 1` header and the tab's URL and title.
- `app/server.py` keeps only the newest frame, in memory. Nothing is written to disk. `GET /api/live` reports whether a picture is live; `GET /api/live/stream` serves the frames as one multipart response that the panel shows in an `<img>`. Both refuse requests that come from another website (`Sec-Fetch-Site`).
- `S step` writes `state` (`doing`, `done`, `failed`) and an optional `note` on the matching entry of `meta.runRequest.items`. The dashboard polls once a second while a run is waiting or running.
- A run without `S step` calls still works: the checklist stays unticked until `S finish-run`, then shows everything as done.
