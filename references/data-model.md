# Outreach Desk data model

File `<skill>/data/db.json`: `{rev, contacts: {<id>: {...}}, meta: {settings, run}}`. Local only. Read/write with `store.py` (see SKILL.md); the first change each day copies the previous file to `data/backups/db-YYYY-MM-DD.json`.

## `contacts/<id>`
`id` = LinkedIn profile slug, URL-decoded, accents stripped, only `A-Za-z0-9_-` kept (e.g. `jurgen-weimer-22200076`).

| Field | Type | Notes |
|---|---|---|
| name, headline, company, location | string | from LinkedIn / Apollo |
| country | string | campaign country, `Unknown` if not clear (dashboard groups chips by it) |
| group | `peer` \| `lead` \| `recruiter` \| `other` | decides the ask in the CV message |
| linkedinUrl | string | canonical `https://www.linkedin.com/in/<slug>/` |
| apolloId | string | optional |
| status | `found` `requested` `accepted` `thanked` `cv_sent` `followed_up` `replied` `done` `stale` `blacklisted` | |
| prevStatus, blacklistedAt, blacklistReason | | set by the dashboard's Blacklist button |
| withdrawPending, withdrawnAt | bool, ISO | `withdrawPending: true` = Claude must withdraw the invite on LinkedIn next run |
| requestedAt, acceptedAt, thankedAt, cvSentAt, followUpAt, repliedAt | ISO string | `requestedAtApprox: true` when guessed |
| commonPoint | string | one line, why the user reached out |
| drafts | `{thanks, cv, followup}` each `{text, approved, sentAt?, editedByUser?}` | dashboard edits these |
| notes | string | the user's or Claude's notes, reply summaries |
| source | string | `Apollo`, `Manual outreach`, `LinkedIn search`, `Added by hand` |
| campaign | string | e.g. `luxembourg-2026-11`; `pre-pipeline` for requests sent by hand before setup |
| history | `[{at, event, by}]` | appended by `store.py update --event` (don't pass history in a patch) |
| updatedAt | ISO string | |

## `meta.settings`
`{cvDelayDays:3, followUpDays:7, closeDays:7, staleDays:21, weeklyCap:80, dailyCap:15}`

## `meta.run`
`{lastRun: ISO, lastRunNote: "one line"}` shown in the dashboard header.

## Writing
- New contacts: one `<id>.json` per contact in a scratchpad folder, then `store.py import <dir>`.
- Changes: `store.py update <id> '<patch>' --event "..."` (merge; `{"__delete__": true}` removes a key; history entry added automatically with `by: Claude`).
