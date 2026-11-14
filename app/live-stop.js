// Outreach Desk live view: stop mirroring this tab (see live-start.js). Safe to run when nothing is live.
async (page) => {
  if (page.__deskLive) { const n = page.__deskLive.sent(); await page.__deskLive.stop(); return `Live view stopped after ${n} frames.`; }
  try { await fetch('http://localhost:4877/api/live/stop', { method: 'POST', headers: { 'X-Outreach-Desk': '1' } }); } catch {}
  return 'Live view was not running.';
}
