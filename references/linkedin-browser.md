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
Before sending: set the viewport to at least 1440×900 (`page.setViewportSize`), or LinkedIn's Send button can sit off-screen and the click times out. Check the person by the page title (`"<Name> | LinkedIn"`, sometimes prefixed with a notification count like `(1) `); profile pages have no reliable `h1`. Profile slugs can keep accented letters (`/in/j%C3%BCrgen-...`): if a stored URL with the accent stripped gives `/404/`, try the percent-encoded slug and save the working URL in `linkedinUrl`. Proven sequence per message, one `browser_run_code_unsafe` call each: open profile → check title → close open chat bubbles → click the top-card link `main a[href*="/messaging/compose/"][href*="NON_SELF_PROFILE_VIEW"]` → pick the `.msg-overlay-conversation-bubble` whose text contains the name → for a thank-you, stop if the thread already has any `.msg-s-message-list__event` (the user may have written by hand; ask before sending a second first message), and for any message stop if `.msg-s-event-listitem__body` already contains it → type into `div.msg-form__contenteditable` → stop (and clear) unless the typed text equals the approved text exactly → click `button.msg-form__send-button` → confirm the text now appears in the conversation and the box is empty → close the bubble.
On the profile click "Message" → the chat overlay opens. Type with `browser_type` into the message box (contenteditable "Write a message…"), check the text, press Send. For the CV message, attach the PDF first with the paperclip / "Attach a file" button and `browser_file_upload` (path from the CV line in `data/profile.md`). Close the overlay. Then write the contact (status, `<step>At`, `drafts.<k>.sentAt`, history).

## Checking replies
`https://www.linkedin.com/messaging/` lists threads with the latest line. Open threads with contacts in the sequence; if the last message is from them and newer than the user's last message, it's a reply.

## Withdrawing a stale request
On the Sent invitations page (`/mynetwork/invitation-manager/sent/`, newest first) scroll down until the card loads (old invites sit at the bottom), check the card's `/in/` link matches the contact, click its `a[aria-label="Withdraw invitation sent to <Name>"]`, then confirm with the visible `<button>` "Withdraw" in the "Withdraw invitation" box (it has no `role="dialog"`). Done when the card is gone and the toast says "Invitation to <first name> withdrawn." Note: LinkedIn blocks re-inviting the same person for about 3 weeks after a withdrawal.
