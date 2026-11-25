// recapture.mjs — re-capture Gavia's interface before and after the proposed
// redesign, at 2x pixel density, and re-run axe on every captured state.
//
// Before = commit 5dd8471 (Gavia 0.5.0 merge), extracted with `git archive`.
// After  = branch design/hai-brand working tree (uncommitted, built before
//          approval), copied with rsync. Both served by `vite` from desktop/ —
//          the browser preview with its fake core (src/dev/browserPreview.ts),
//          so every detection on screen is MADE UP, not a model run.
//
// crypto.randomUUID is pinned to one fixed sequence on both sides, so the
// preview's seeded sample result is the same on both screenshots.
//
// usage: TOOLS=<dir with node_modules/{playwright-core,axe-core}> \
//        node recapture.mjs <outDir> before=http://localhost:5181/ after=http://localhost:5182/
import { createHash } from 'node:crypto'
import { mkdirSync, writeFileSync, readFileSync } from 'node:fs'
import { join, dirname } from 'node:path'

const TOOLS = process.env.TOOLS
const { chromium } = await import(join(TOOLS, 'node_modules/playwright-core/index.mjs'))
const AXE = readFileSync(join(TOOLS, 'node_modules/axe-core/axe.min.js'), 'utf8')
const AXE_VERSION = JSON.parse(readFileSync(join(TOOLS, 'node_modules/axe-core/package.json'))).version
const out = process.argv[2]
const sides = Object.fromEntries(process.argv.slice(3).map((a) => a.split('=')))
const PHOTO = `${process.env.HOME}/Documents/loonet/data/annotated/loonnet_v1/images/web_20260818_0042.jpg`

// The app's own CSP (tauri.conf.json), as in the audit's capture: fonts and
// requests behave as in the shipped, offline app.
const csp = (port) =>
  "default-src 'self'; script-src 'self' 'unsafe-inline'; img-src 'self' blob: data: gavia: http://gavia.localhost; " +
  "media-src 'self' blob:; style-src 'self' 'unsafe-inline'; " +
  `connect-src ipc: http://ipc.localhost gavia: http://gavia.localhost ws://localhost:${port}`

const sha = (buf) => createHash('sha256').update(buf).digest('hex')
const record = { axe: AXE_VERSION, photo: PHOTO, photo_sha256: sha(readFileSync(PHOTO)), states: {} }
const save = (rel, data) => {
  const p = join(out, rel)
  mkdirSync(dirname(p), { recursive: true })
  writeFileSync(p, data)
  return sha(data)
}

async function snap(page, side, state, theme) {
  await page.waitForTimeout(900)
  await page.evaluate(() => document.fonts.ready)
  const png = await page.screenshot({ fullPage: true, animations: 'disabled' })
  const hash = save(`${side}/${state}-${theme}.png`, png)
  await page.addScriptTag({ content: AXE })
  const axe = await page.evaluate(async () =>
    // eslint-disable-next-line no-undef
    axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] }, resultTypes: ['violations', 'incomplete'] }),
  )
  // nodes axe could not decide: on the old theme, the corner-glow gradient hides the background
  const undecided = {}
  for (const x of axe.incomplete.filter((x) => x.id === 'color-contrast'))
    for (const n of x.nodes) {
      const key = n.any?.[0]?.data?.messageKey ?? 'other'
      undecided[key] = (undecided[key] ?? 0) + 1
    }
  const h1 = await page.evaluate(() => {
    const el = document.querySelector('h1')
    // fonts actually loaded into the page (a blocked remote font never appears here)
    const loaded = [...new Set([...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family))]
    return el ? { text: el.textContent.trim(), font: getComputedStyle(el).fontFamily, loaded } : null
  })
  const v = Object.fromEntries(axe.violations.map((x) => [x.id, x.nodes.length]))
  // what axe measured on each failing node: selector, text colours and ratio
  const nodes = axe.violations.flatMap((x) =>
    x.nodes.map((n) => {
      const d = n.any?.[0]?.data ?? {}
      return { rule: x.id, target: n.target.join(' '), fg: d.fgColor, bg: d.bgColor, ratio: d.contrastRatio, fontSize: d.fontSize, expected: d.expectedContrastRatio }
    }),
  )
  record.states[`${side}/${state}-${theme}`] = { png_sha256: hash, violations: v, nodes, contrast_undecided: undecided, h1 }
  console.log(`${side.padEnd(6)} ${`${state}-${theme}`.padEnd(20)} axe ${JSON.stringify(v)}  contrast-undecided ${JSON.stringify(undecided)}  fonts loaded ${JSON.stringify(h1?.loaded)}`)
}

const browser = await chromium.launch()
for (const [side, base] of Object.entries(sides)) {
  const port = new URL(base).port
  for (const theme of ['light', 'dark']) {
    const context = await browser.newContext({ viewport: { width: 1280, height: 880 }, colorScheme: theme, deviceScaleFactor: 2 })
    await context.addInitScript((t) => {
      localStorage.setItem('gavia.theme', t)
      let n = 0
      crypto.randomUUID = () => `00000000-0000-4000-8000-${String(++n).padStart(12, '0')}`
    }, theme)
    await context.route(base, async (route) => {
      const res = await route.fetch()
      await route.fulfill({ response: res, headers: { ...res.headers(), 'content-security-policy': csp(port) } })
    })
    const page = await context.newPage()
    await page.goto(base)
    await page.waitForSelector('.page-intro h1')
    await snap(page, side, 'check-empty', theme)
    // The fake core draws 0-2 boxes per id; with the pinned ids the same try wins on both sides.
    for (let tries = 0; tries < 8; tries++) {
      await page.locator('input[type=file]').first().setInputFiles(PHOTO)
      await page.locator('.check-button').click()
      await page.waitForSelector('.result-layout')
      if (await page.locator('.result-found').count()) break
      await page.getByRole('button', { name: /Check another image/ }).first().click()
    }
    await snap(page, side, 'check-result', theme)
    await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('button', { name: 'Settings', exact: true }).click()
    await page.waitForTimeout(300)
    await snap(page, side, 'settings', theme)
    await context.close()
  }
}
await browser.close()
writeFileSync(join(out, 'recapture.json'), JSON.stringify(record, null, 1))
