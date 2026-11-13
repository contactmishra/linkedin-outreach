# LinkedIn in the Playwright browser

Tools: `mcp__plugin_playwright_playwright__*`. The browser keeps the user's login between sessions (Playwright profile). If a page shows the login form or a security check, stop and ask the user to handle it.

Pace: 3 to 8 s random waits between page loads (`page.waitForTimeout(3000 + Math.random()*5000)` inside `browser_run_code_unsafe`). Loop over at most about 10 profiles per call.

Playwright writes snapshots and console logs into `.playwright-mcp/` in the working directory. They contain LinkedIn page data: delete that folder at the end of each run.

## Pending invitations
URL `https://www.linkedin.com/mynetwork/invitation-manager/sent/` (header shows "People N"). The list lazy-loads: in `browser_evaluate`, loop up to 20 times: collect `main a[href*="/in/"]`, walk up to the card containing "Sent ", scroll the last link into view and every scrollable element to its bottom, wait 1.5 s; stop when the count reaches N. Card text: `Name | headline | Sent 7 hours ago`.

## Accepted (connections, newest first)
URL `https://www.linkedin.com/mynetwork/invite-connect/connections/` (sorted by recently added). Same collection loop, card text ends `Connected on November 13, 2026`. Stop once dates are older than the last run. A connection in the dashboard as `requested` → accepted. LinkedIn notifications do NOT reliably list acceptances, and inbound connections (people who invited the user) also appear here: only contacts already in the dashboard, or clearly matching the campaign, count.

## Reading a profile
`https://www.linkedin.com/in/<slug>/`, wait, wheel down 2500 px, take `main.innerText`, cut at "Activity" / "Interests" / "People you may know". Gives name, headline, location, company, school, mutual connections, About.

## Sending a connection request (no note)
On the profile: click the "Connect" button (sometimes under "More"). In the dialog choose "Send without a note". Confirm the button changed to "Pending". Then write the contact: `status: requested`, `requestedAt`.

## Sending a message to a connection
On the profile click "Message" → the chat overlay opens. Type with `browser_type` into the message box (contenteditable "Write a message…"), check the text, press Send. For the CV message, attach the PDF first with the paperclip / "Attach a file" button and `browser_file_upload` (path from the CV line in `data/profile.md`). Close the overlay. Then write the contact (status, `<step>At`, `drafts.<k>.sentAt`, history).

## Checking replies
`https://www.linkedin.com/messaging/` lists threads with the latest line. Open threads with contacts in the sequence; if the last message is from them and newer than the user's last message, it's a reply.

## Withdrawing a stale request
On the Sent invitations page click "Withdraw" on that card and confirm. Note: LinkedIn blocks re-inviting the same person for about 3 weeks after a withdrawal.
