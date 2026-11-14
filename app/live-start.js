// Outreach Desk live view: mirror this browser tab into the dashboard's Live run panel.
// Run with the Playwright MCP tool browser_run_code_unsafe (filename: this file) on the LinkedIn tab,
// once per run, right after `store.py start-run`. Frames go only to the local Outreach Desk server and
// are kept in memory there. Stop with live-stop.js. Change the port if OUTREACH_PORT is not 4877.
async (page) => {
  const DESK = 'http://localhost:4877';
  const HEAD = { 'X-Outreach-Desk': '1' };
  if (page.__deskLive) await page.__deskLive.stop();
  const cdp = await page.context().newCDPSession(page);
  let busy = false, sent = 0;
  cdp.on('Page.screencastFrame', async (f) => {
    cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }).catch(() => {});
    if (busy) return;            // the desk is still taking the last frame: skip this one
    busy = true;
    try {
      let title = '';
      try { title = await page.title(); } catch {}
      await fetch(DESK + '/api/live/frame', {
        method: 'POST',
        headers: { ...HEAD, 'Content-Type': 'image/jpeg', 'X-Live-Url': encodeURIComponent(page.url()), 'X-Live-Title': encodeURIComponent(title) },
        body: Buffer.from(f.data, 'base64'),
      });
      sent++;
    } catch {} finally { busy = false; }
  });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 60, maxWidth: 1280, maxHeight: 800, everyNthFrame: 1 });
  page.__deskLive = {
    sent: () => sent,
    stop: async () => {
      try { await cdp.send('Page.stopScreencast'); } catch {}
      try { await cdp.detach(); } catch {}
      try { await fetch(DESK + '/api/live/stop', { method: 'POST', headers: HEAD }); } catch {}
      delete page.__deskLive;
    },
  };
  return 'Live view started: this tab is now mirrored in the Outreach Desk.';
}
