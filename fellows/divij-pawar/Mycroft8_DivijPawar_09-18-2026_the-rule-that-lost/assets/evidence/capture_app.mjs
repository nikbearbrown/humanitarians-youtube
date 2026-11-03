// Capture real screenshots of the verification layer's React app (/app) for this reel.
//
// These are HOLD assets: pictures of the actual software the video talks about, rendered by
// headless Chrome from the locally running server. Nothing is mocked. The script clicks only
// view controls (scope toggle, "Review and record decision" to open the form); it never submits
// a decision.
//
//   node assets/evidence/capture_app.mjs            (server must be running on :8000)
//
// Node 22+ (global WebSocket). Uses a throwaway Chrome profile, not the user's.
import { spawn } from "node:child_process";
import { mkdtempSync, writeFileSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ASSETS = join(HERE, "..");
const APP = "http://127.0.0.1:8000/app/";
const CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe";
const PORT = 9333;

// Each shot: run id, viewport, optional clicks (button text), element to clip (or full page).
export const SHOTS = JSON.parse(process.env.SHOTS_JSON || "null") || [
  { out: "B10_recorded_verdict_1280.png", run: "20c538e4-ea77-4765-91a1-aad8c488d4b0", width: 1280, clip: 'section[aria-labelledby="cmp-head"]', maxHeight: 330 },
  { out: "B12_matrix_1280.png", run: "20c538e4-ea77-4765-91a1-aad8c488d4b0", width: 1280, clip: ".matrix-section" },
  { out: "B12_matrix_375.png", run: "20c538e4-ea77-4765-91a1-aad8c488d4b0", width: 375, mobile: true, clip: ".matrix-section" },
  { out: "B13_shared_rows_1280.png", run: "20c538e4-ea77-4765-91a1-aad8c488d4b0", width: 1280, clip: ".matrix" },
];

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function cdp(wsUrl) {
  const ws = new WebSocket(wsUrl);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  let id = 0;
  const pending = new Map();
  ws.onmessage = (m) => {
    const msg = JSON.parse(m.data);
    if (msg.id && pending.has(msg.id)) {
      const { res, rej } = pending.get(msg.id);
      pending.delete(msg.id);
      msg.error ? rej(new Error(msg.error.message)) : res(msg.result);
    }
  };
  const send = (method, params = {}) => new Promise((res, rej) => {
    const n = ++id;
    pending.set(n, { res, rej });
    ws.send(JSON.stringify({ id: n, method, params }));
  });
  return { send, close: () => ws.close() };
}

async function evaluate(page, expr) {
  const r = await page.send("Runtime.evaluate", { expression: expr, awaitPromise: true, returnByValue: true });
  return r.result?.value;
}

async function waitFor(page, selector, ms = 20000) {
  const t0 = Date.now();
  while (Date.now() - t0 < ms) {
    if (await evaluate(page, `!!document.querySelector(${JSON.stringify(selector)})`)) return true;
    await sleep(250);
  }
  return false;
}

async function main() {
  const profile = mkdtempSync(join(tmpdir(), "reel-capture-"));
  const chrome = spawn(CHROME, [
    "--headless=new", `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
    "--no-first-run", "--no-default-browser-check", "--hide-scrollbars", "about:blank",
  ], { stdio: "ignore" });
  const log = [];
  try {
    let targets;
    for (let i = 0; i < 40; i++) {
      try { targets = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json(); break; }
      catch { await sleep(250); }
    }
    const pageTarget = targets.find((t) => t.type === "page");
    const page = await cdp(pageTarget.webSocketDebuggerUrl);
    await page.send("Page.enable");
    await page.send("Runtime.enable");
    mkdirSync(ASSETS, { recursive: true });

    for (const s of SHOTS) {
      await page.send("Emulation.setDeviceMetricsOverride", {
        width: s.width, height: s.height || 900, deviceScaleFactor: 2, mobile: !!s.mobile,
      });
      await page.send("Page.navigate", { url: `${APP}#/runs/${s.run}` });
      await sleep(600);
      await page.send("Page.reload", { ignoreCache: true }); // hash routes: reload so state is fresh
      const ready = await waitFor(page, s.waitFor || ".verdict-line, .matrix, .gate-head, h1");
      for (const text of s.clicks || []) {
        const clicked = await evaluate(page, `(() => {
          const b = [...document.querySelectorAll("button")].find(x => x.textContent.trim() === ${JSON.stringify(text)});
          if (!b) return false; b.click(); return true; })()`);
        log.push(`${s.out}: click "${text}" -> ${clicked}`);
        await sleep(1200);
      }
      if (s.waitFor2) await waitFor(page, s.waitFor2);
      await sleep(800);
      let clip;
      if (s.clip) {
        // the fixed top bar would otherwise be painted over a cropped element
        await evaluate(page, `(() => { const t = document.querySelector(".topbar"); if (t) t.style.visibility = "hidden"; return true; })()`);
        const r = await evaluate(page, `(() => { const e = document.querySelector(${JSON.stringify(s.clip)});
          if (!e) return null; e.scrollIntoView({block: "start"}); const b = e.getBoundingClientRect();
          return {x: b.left + scrollX, y: b.top + scrollY, width: b.width, height: b.height}; })()`);
        if (r) clip = { ...r, height: Math.min(r.height, s.maxHeight || r.height), scale: 1 };
        await sleep(300);
      }
      const shot = await page.send("Page.captureScreenshot", { format: "png", captureBeyondViewport: true, ...(clip ? { clip } : {}) });
      writeFileSync(join(ASSETS, s.out), Buffer.from(shot.data, "base64"));
      log.push(`${s.out}: ready=${ready} clip=${s.clip || "viewport"} found=${!!clip} ${s.width}px @2x`);
    }
    page.close();
  } finally {
    chrome.kill();
  }
  const stamp = new Date().toISOString();
  writeFileSync(join(HERE, "out", "capture_log.txt"), [`captured ${stamp} from ${APP}`, ...log].join("\n") + "\n");
  console.log(log.join("\n"));
}

main().catch((e) => { console.error(e); process.exit(1); });
