# CHECKS-REPORT — The Gatekeeper Needs Ground Truth

*Revision 2 (5-scene cut). Rendered and QC'd 2026-09-13.*
11 beats · **measured 147.4s (2:27)** against a 2:45 target
Cut on disk: `claude-hai-gatekeeper-ground-truth-slate.mp4` (12.5 MB)
**GATE V: 22 frames sampled · 0 BLOCKER · 0 MAJOR · clean ✓**
Narrator: Onkar Bhujbal, first person, Kokoro `am_onyx`.

## Per-beat classification (post-render)

| Beat | Scene | Class | Measured | Pattern |
|---|---|---|---|---|
| B00 | 1 HOOK | SHOW | 15.66s | ClaudeComposerAsk |
| B01 | — BLUF | SHOW | 10.50s | BrutalistHesitantWriter |
| B02 | 2 FRAMEWORK | SHOW | 15.19s | GatekeeperIngestFlow |
| B03 | 3 corpus | SHOW | 14.70s | GatekeeperCorpusTable |
| B04 | 3 ask | SHOW | 6.44s | ClaudeComposerAsk |
| B05 | 3 code | **HOLD (justified)** | 14.85s | ClaudeCodeBeat — PIPELINE slate |
| B06 | 3 intercept | SHOW | 10.75s | GatekeeperVerifyLoop |
| B07 | 4 FALSIFIABILITY | SHOW | 18.54s | GatekeeperDirectionalBlindspot |
| B08 | 5 task | SHOW | 11.67s | ClaudeCodeBeat — `payload.json` |
| BHTF | 5 handoff | SHOW | 19.35s | ClaudeComposerAsk |
| BOUT | 5 close | SHOW | 9.73s | GatekeeperTitleOutro |

**10 SHOW / 1 justified-HOLD / 0 PUNT-flagged.** Slots: 11/11 filled.

### The one HOLD — B05

The real `ingest.py` has never been supplied. The script describes it; the file is
not on disk, and DOUBLE-CHECK LAW forbids fabricating a listing and presenting it as
the project's code. B05 renders as a PIPELINE slate naming exactly what is needed
(SELF-DEMO LAW feasibility fallback). The narration is true of the real file, so it
needs no rewrite when the code lands.

**To resolve:** paste the real `ingest.py` into `media/B05.code.txt`, trim to ~16
lines (read path, `encode` call, `collection.add` call), set the `code` prop,
re-render. B05 then reclassifies SHOW.

## Teaching arc — the revision-2 script supplies most of this itself

```
FRAMEWORK ✓    B02 states the Intercept Framework before any code is shown —
               the script's own Scene 2, and exactly the right order.
WORKED EXAMPLE ✓ doc_01 carried end to end: B03 (the labeled row) → B06 (retrieved,
               proves the 15% claim a magnitude error) → B07 (the same row defeats
               a directional claim).
FALSIFIABILITY ✓ B07, the script's Scene 4 — directional errors defeat vector
               similarity. The reel names the condition under which its own
               system fails, in the author's own words.
SCAFFOLDED TASK ✓ B08 the JSON payload + pass/fail criterion, then BHTF the
               follow-up prompt. Bounded, runnable, with a stated expected result.
BOOKENDS ✓     B00 cold open · B01 BLUF · BHTF handoff · BOUT title restate.
NO-SOURCE-NO-VERDICT ✓ every figure traces to the script or is flagged in SOURCES.md.
```

## Law checks (verified on rendered frames)

- **COLD OPEN LAW** ✓ · **EXECUTIVE-SUMMARY LAW** ✓ (10.5s ≥ 9s, `lead_silence_s: 0.8`)
- **ILLUSTRATE LAW** ✓ Claude UI only at B00, B04, BHTF, BOUT. No two consecutive
  beats share a scheme.
- **ASK → RESULT LAW** ✓ B04 → B05.
- **SPARK-LINE LAW** ✓ every inner beat carries a ≤4-word serif line.
- **HANDOFF LAW** ✓ prompt read verbatim aloud, then discussed.
- **OUTRO LAW** ✓ exact title restate, terracotta period, handle beneath.
- **FILL-THE-CANVAS / title-safe** ✓ GATE V 0/0 across 22 frames.

## Defects found and fixed during this render

| Beat | Defect | Fix |
|---|---|---|
| B03 | row slide-in crossed the title-safe **left** edge (`dx: -40→0`) | tried `+40→0`, which then crossed the **right** edge — the row is exactly `SAFE.w` wide, so any horizontal offset bleeds. Now settles vertically (`dy: 18→0`). |
| B07 | verdict block grew from its padding past the title-safe **bottom** edge | explicit `VERDICT_H` anchored to `SAFE.b` with 26px clearance — flush-on-the-line still scored edge-bleed. |

## Dual render — BOTH ASPECTS DELIVERED

| | File | Format |
|---|---|---|
| 16:9 master | `claude-hai-gatekeeper-ground-truth-slate.mp4` | 3840×2160 @ 24fps · 2:27 |
| 9:16 companion | `vertical/claude-hai-gatekeeper-ground-truth-vertical-slate.mp4` | 1080×1920 @ 24fps · 2:27 |

**All 11 beats rewired to registered `916` compositions — zero flagged, zero centre-cut.**
Genuine reflows, not crops (RENDER-TARGETS.md §3): the four-column corpus table becomes
one stacked CARD per row (four columns cannot be legible at 1080px wide), and the ingest
band and verify chain serialize top-to-bottom.

`shot.type` on B05 was changed `SLATE` → `REMOTION`. `shorts.py` decides what to rewire
by that field, so as a SLATE the code card would have been **centre-cut** — chopping a
card full of text mid-word. It is a Remotion beat; its slate state lives in
`build.status`, where it belongs.

The format spec is fully met: `compile.py` defaults to `--fps 24`, so both cuts probe as
24fps, and the 16:9 master is true 4K UHD.

### Portrait-pass defects found and fixed

GATE V does not run on `compile.py --review`, so the portrait cut was inspected frame by
frame. Three defects, none of which any gate would have caught:

| Where | Defect | Fix |
|---|---|---|
| `ClaudeCodeBeat` (shared toolkit component) | Type sized from canvas HEIGHT (`height * 0.022`). Portrait gives a *larger* font (42px) in a *narrower* card (~929px); with `white-space: pre` inside `overflow: hidden` the code was **clipped mid-word** — `"[obscure ind…"`, `"asymme…"`. | Size from card width against the longest line, floored at 15px. Landscape unaffected unless it was already overflowing. Every reel with a code beat benefits. |
| `GatekeeperDirectionalBlindspot` | Claim/ledger cards divided the whole band, leaving a one-line claim floating over ~400px of dead card. | Card height capped in both aspects; the pair is centred and the similarity bar now follows the cards rather than the band. |
| `GatekeeperDirectionalBlindspot` | The responsive rewrite turned the highlighted polarity words into props, but the beat sheet never passed them — so they arrived `undefined` and rendered as plain text. **This silently broke the landscape cut too.** | `claimHot` / `ledgerHot` passed explicitly in both sheets; verified terracotta in both aspects. |

## Open items

1. **B05 slate** — needs the real `ingest.py`.
2. **B03 rows 2–4 are illustrative.** Only `doc_01` is from the script. Swap in real
   corpus rows before publish or keep the SOURCES.md flag.
3. **Runtime 2:27 vs the 2:45 target** — 18s under. Duration is an output, not a
   target (`duration-planner`), and the script's VO is used near-verbatim. If you
   want the extra 18s, B06 (10.75s) is the thinnest beat and could carry one more
   sentence about what the webhook actually posts.
4. **24 fps not met.** The script header asks for 24; every registered composition is
   `fps={30}`. That is a toolkit-wide change, not a per-reel prop. Currently 4K/30.
5. **Sign-off wording.** Revision 2's Scene 5 still reads "Liam, for Onkar Bhujbal and
   Humanitarians AI", which contradicts the instruction to use the author's own name.
   Built as **"Onkar Bhujbal, for Humanitarians AI."** — one word reverts it.
6. **Lane-mix warning (not blocking).** `remotion` carries 10/11 beats (90%) against
   MOTION.md's ~40% guidance. Deliberate: a systems explainer with no maths beat and
   no archival footage. B02 is the natural Manim candidate if it matters.
7. **SKIN LINT warning (not blocking, expected).** `BOUT` uses `GatekeeperTitleOutro`
   where the linter expects `ClaudeTitleOutro` — deliberate, see BUILD-LOG D3.
8. **Paperwork.** Built with `ART_FACTS=0`. A fully gated `./art run` needs
   `FACTCHECK.md`, `SHOTLIST.md` and `PROMPTS.md` in the reel folder.
9. **`./art final` has not been run** — no 4K master yet.
