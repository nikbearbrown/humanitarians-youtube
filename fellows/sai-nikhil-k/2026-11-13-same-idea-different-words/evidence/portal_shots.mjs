// portal_shots.mjs — stills of three Portals worlds, rendered locally from
// emollick/ai-portals (CC BY-NC-SA 4.0) with the repo's own test harness:
//   index.html?world=<id>&freeze&grab&pr=1  then  window.__pose(u, t)  ->  window.__png
// The repo is served as static files (python -m http.server); none of its
// scripts are run outside the browser.
//
// usage: TOOLS=<dir with node_modules/playwright-core> node portal_shots.mjs <outDir> <base> id:u:t ...
import { writeFileSync, mkdirSync } from 'node:fs'
import { join } from 'node:path'
const { chromium } = await import(join(process.env.TOOLS, 'node_modules/playwright-core/index.mjs'))
const [out, base, ...shots] = process.argv.slice(2)
mkdirSync(out, { recursive: true })
const browser = await chromium.launch({ args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist'] })
const byWorld = {}
for (const s of shots) { const [id, u, t] = s.split(':'); (byWorld[id] ??= []).push([+u, +t]) }
for (const [id, poses] of Object.entries(byWorld)) {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } })
  page.on('pageerror', (e) => console.log(id, 'pageerror', String(e).slice(0, 160)))
  const t0 = Date.now()
  await page.goto(`${base}/index.html?world=${id}&freeze&grab&pr=1`)
  await page.waitForFunction(() => typeof window.__pose === 'function', null, { timeout: 300000 })
  const renderer = await page.evaluate(() => {
    const gl = document.createElement('canvas').getContext('webgl2')
    const ext = gl && gl.getExtension('WEBGL_debug_renderer_info')
    return ext ? gl.getParameter(ext.UNMASKED_RENDERER_WEBGL) : 'unknown'
  })
  for (const [u, t] of poses) {
    const stats = await page.evaluate(async ([u, t]) => window.__pose(u, t), [u, t])
    const png = await page.evaluate(() => window.__png)
    const file = join(out, `${id}_u${u}_t${t}.png`)
    writeFileSync(file, Buffer.from(png.split(',')[1], 'base64'))
    console.log(`${id} u=${u} t=${t} -> ${file}  (${((Date.now() - t0) / 1000).toFixed(1)}s, ${renderer}) ${JSON.stringify(stats).slice(0, 120)}`)
  }
  await page.close()
}
await browser.close()
