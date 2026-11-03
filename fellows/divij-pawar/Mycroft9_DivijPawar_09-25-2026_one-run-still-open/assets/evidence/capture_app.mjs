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
  // B03/B04: the gate form opened in place (view control only; nothing is submitted)
  { out: "B03_gate_open_1280.png", run: "ec1a3b44-8145-4d44-b8a2-7c7707deffcd", width: 1280, height: 1400, clicks: ["Review and record decision"], clip: "section.gate" },
  // B06: the same run at auditor and at investor scope (scope toggle is a view control)
  { out: "B06_auditor_1280.png", run: "ec1a3b44-8145-4d44-b8a2-7c7707deffcd", width: 1280, clip: 'section[aria-labelledby="cmp-head"]', maxHeight: 700 },
  { out: "B06_investor_1280.png", run: "ec1a3b44-8145-4d44-b8a2-7c7707deffcd", width: 1280, clicks: ["Investor"], clip: 'section[aria-labelledby="cmp-head"]', maxHeight: 700 },
  // B06 falsifiability: the one place the investor read still shows 1998 (a search result in the trace)
  { out: "B06_investor_trace_leak_1280.png", run: "ec1a3b44-8145-4d44-b8a2-7c7707deffcd", width: 1280, clicks: ["Investor"], openAll: true, clipText: "1998" },
  { out: "B07_gate_closed_1280.png", run: "ec1a3b44-8145-4d44-b8a2-7c7707deffcd", width: 1280, clip: "section.gate" },
]

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
      if (s.openAll) {  // expand every collapsed <details> (view control only)
        await evaluate(page, `(() => { document.querySelectorAll("details").forEach(d => d.open = true); return true; })()`);
        await sleep(800);
      }
      if (s.clipText) {
        // trace rows open one at a time: open each until a detail contains the text
        const n = await evaluate(page, `document.querySelectorAll(".trace-row").length`);
        for (let i = 0; i < n; i++) {
          const hit = await evaluate(page, `(() => { const r = document.querySelectorAll(".trace-row")[${i}];
            if (r.getAttribute("aria-expanded") !== "true") r.click(); return true; })()`);
          await sleep(300);
          const found = await evaluate(page, `[...document.querySelectorAll(".trace-detail pre")].some(p => p.textContent.includes(${JSON.stringify(s.clipText)}))`);
          if (found) { log.push(`${s.out}: text found in trace row ${i + 1} of ${n}`); break; }
        }
      }
      if (s.clipText) {  // tag the innermost element containing the text, then clip it
        const tagged = await evaluate(page, `(() => {
          const hits = [...document.querySelectorAll("body *")].filter(e => e.children.length === 0 && e.textContent.includes(${JSON.stringify(s.clipText)}));
          if (!hits.length) return false;
          const box = hits[0].closest(".trace-line, li, tr, pre, div") || hits[0];
          box.setAttribute("data-capture", "1"); box.style.outline = "3px solid #C8860E"; return true; })()`);
        log.push(`${s.out}: text "${s.clipText}" found=${tagged}`);
        s.clip = "[data-capture]";
      }
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
