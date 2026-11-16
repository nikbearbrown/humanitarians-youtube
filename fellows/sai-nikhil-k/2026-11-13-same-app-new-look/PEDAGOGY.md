# PEDAGOGY — Same App, New Look

**Reel** `weekly_updates/2026-11-13-same-app-new-look/` · **slug** `claude-sai-same-app-new-look`
**Subject** Gavia's proposed interface redesign (Figma audit, branch `design/hai-brand`) · **week of** 2026-11-13 (built 2026-11-16)
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + one image plate (Gavia before/after, captured locally), no Manim, nothing paid
**Length** ~1 minute, at Sai's request — a 7-beat cut of the usual 9–10-beat spine (deliberate deviation)

---

## The ONE idea

> Gavia's new look is brand and taste, but part of it is measurable: the
> faintest grey went from 2.83:1 to 6.16:1 contrast, and axe went from 6
> failures and 106 undecided checks to none. And it is a proposal on a branch,
> not a release: nothing is approved yet.

Sai's brief (2026-11-16): "create a video for date 11-13-2026, about the UI
changes to the app", the Figma file `NE8nKjRT9eSQE6FA1pnOY1`, "around 1
minute", 9:16 and 16:9 in 4K. The Figma file is the content. Angle and title
("Same App, New Look", continuing 10-23 and 11-06) proposed by the assistant;
Sai can overrule.

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | A new look. Is a redesign just taste? Audit it and measure. |
| B01 | BEFORE AND AFTER | image plate · pair | The same result screen, 0.5.0 vs the branch: palette, Inter bundled offline, one button style, 12 px text. |
| B02 | CONTRAST IS ARITHMETIC | `TypesetMath` | WCAG's ratio; the old faint grey 2.83; the new grey 6.16; the bar is 4.5. |
| B03 | WHAT THE CHECKER SAW | `ExecutedData` | axe on six screens: 6 failures + 106 undecided before (the corner glow hid the background), 0 + 0 after. |
| B04 | VERDICT | `ClaudeVerdictArtifact` | Taste and measurement; all five are proposals; none ships until Sai approves. |
| B05 | HANDOFF | `ClaudeComposerAsk` | Paste your own colour tokens; ask for pairs under 4.5:1; check the worst by hand. |
| B06 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B05 and the verdict only. Body beats:
`plate → TypesetMath → ExecutedData`. No repeats; every beat has an ordered
`show` block.

## 9:16

Every Remotion pattern has a `*916` sibling; the plate has a re-composed
portrait plate in `pantry/B01-916.mp4` (stacked before over after).
Portrait-only edits: none planned.

## Evidence and honesty

- **Nothing is approved.** The audit ledger
  (`~/figma-webdesigner-work/gavia/audit/ledger.jsonl`, 26 events) records all
  five decisions as `proposed`, `decision.built_before_approval` on branch
  `design/hai-brand` (uncommitted), schema gate G1 and triage gate G2 still
  pending, and `audit/approvals/` empty. B04 says "None ships until I approve
  it." **If you approve before posting, change B04's last two sentences and the
  verdict card's line 4.**
- **The detections on screen are fake.** Both screenshots come from Gavia's
  browser preview, whose core is `src/dev/browserPreview.ts`: the box and the
  84% are a seeded sample, not a model run (and the box sits on the wrong part
  of the bird). The plate's credit line says so. Check ids were pinned so both
  sides show the same sample — the audit's own Figma crops show 73% vs 91% and
  "2 loons" vs "1 loon" between sides, which is the fake core, not the redesign.
- **Contrast, re-computed:** `evidence/contrast.py` reads the tokens from
  `index.css` at 5dd8471 and on the branch and applies WCAG 2.2's formula.
  Old `--text-subtle` #88979D on the page #F6F8F9: L 0.2980 / 0.9357 → 2.83:1.
  New #5E6265 on #FFFFFF: L 0.1205 / 1.0000 → 6.16:1. Worst new pair 5.32:1 on
  #F2EEE7 (light), 5.10:1 dark. Control edges 1.69:1 → 3.48:1.
- **axe, re-run:** `evidence/recapture.mjs` serves both versions with vite
  under the app's own CSP and runs axe-core 4.10.2 on check-empty,
  check-result and settings, light and dark (six screens each). Before: 4
  colour-contrast failures (banner 4.31:1, theme options 4.27:1) + 2 unnamed
  file inputs = 6; 106 colour-contrast checks undecided with `bgGradient`
  (the corner glow). After: 0 and 0. The audit's own Figma table lists 11
  findings; axe sees only the automated ones.
- **"The old fonts never loaded":** with the app's CSP applied, the old build
  loads no web font at all (it asks for Fraunces and DM Sans from Google, which
  the CSP blocks), so it renders a system serif. The branch loads `Inter
  Variable` from the bundle. Recorded per screen in `recapture.json`.
- **"Small text, up to twelve pixels"** is the decision record's proposal
  (sentence text 12 px; uppercase labels 11 px) and the R-02 re-run's
  "sentence text ≥ 12px" — taken from the ledger, not re-measured here.

## Attribution

Hosted by Sai; Gavia is his project (commit 5dd8471 is his). The audit,
decision records and the branch changes were drafted by Claude Code with the
figma-webdesigner skill at his request, on 2026-11-16 — the reel says "I
audited it" because he commissioned and owns the approval. Loon photo:
Glennice Burns, Unsplash (Unsplash License), from loonet's manifest.

## Pronunciation (narration only)

- `Inter` → "Inntur" (raw reads in-TUR, like the prefix).

## Dates

The reel is dated 11-13 at Sai's request; the audit and the re-measurements
ran on 2026-11-16. The narration makes no claim about which day the work happened.

## Expected build noise (not bugs)

- SKIN LINT at B06 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Title and angle "Same App, New Look" — keep, or overrule?
- [ ] OK to say on camera that none of the five changes is approved yet?
- [ ] OK to credit the audit as "I audited it" (Claude Code ran it at your request)?
- [ ] Anything here better left out of a public video?

VERDICT: __________ — reviewer: ___ date: ___

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 9.8s measured (30 words)

> This is Sai. Gavia has a new look: Humanitarians AI colours, a new typeface,
> one button style. Is a redesign just taste? I audited it, and measured what I
> could.

### B01 · BEFORE AND AFTER — `image plate · pair` · 12.7s measured (39 words)

> Same check, before and after. Teal and serif became white, blood red and
> Inntur, now bundled in the app, since Gavia runs offline and the old fonts
> never loaded. One main button style. Small text, up to twelve pixels.

### B02 · CONTRAST IS ARITHMETIC — `TypesetMath` · 11.6s measured (38 words)

> Contrast is a ratio of two luminances, each plus zero point zero five. The
> faintest old grey: two point eight three to one. Text needs four and a half.
> The new grey on white: six point one six.

### B03 · WHAT THE CHECKER SAW — `ExecutedData` · 10.9s measured (33 words)

> The automated checker, axe, found six failures on six old screens, and
> couldn't decide a hundred and six text checks: a decorative glow hid the
> background. On the new screens, zero and zero.

### B04 · VERDICT — `ClaudeVerdictArtifact` · 9.2s measured (29 words)

> So the new look is taste, and also measurement. Contrast and labels now pass.
> But all five changes are proposals on a branch. None ships until I approve it.

### B05 · HANDOFF — `ClaudeComposerAsk` · 7.4s measured (25 words)

> Your turn. Paste your app's colour tokens, ask which text falls below four and
> a half to one, then check the worst pair by hand.

### B06 · OUTRO — `LogoOutro` · 2.3s measured (5 words)

> Same app, new look. Sai.

**Total: 199 words** → 63.9s measured (1:03). Audio remains the master clock.

<!-- NARRATION:END -->
