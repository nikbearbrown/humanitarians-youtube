# BUILD-PROMPT — Labels Are Not Decoration.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root —
the reel lives in the book, not the toolkit (CLAUDE.md rule 3).

```
Reel: D:\ai1-cli-main\youtube\2026-09-22-claude-rag-prompt-construction

0. Windows note — set UTF-8 for EVERY python step below:
   export PYTHONUTF8=1
   Without it, build_scene_index.py fails reading Root.tsx and compile.py's
   status-line arrow crashes a cp1252 console. Environmental, not a reel defect.

   Also: run `./art scene-index`, NOT `python runtime/scripts/build_scene_index.py`
   directly — the script resolves Root.tsx relative to CWD and fails from root.

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
   CHECKS-REPORT.md must show 0 PUNT-flagged before any render (PROOF GATE).

2. Audio (only if narration changed — it is the master clock):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   Add --only <BEAT_ID> for a single beat. NEVER hand-edit actual_duration_s.

   B01 is the EXECUTIVE-SUMMARY beat: its window must stay ≥9s and it carries an
   explicit `lead_silence_s: 0.8`. Current measured length 14.17s.

2b. *** RE-SYNC `beatSeconds` AFTER ANY AUDIO CHANGE ***
   The five bespoke components stage every reveal as a fraction of their measured
   duration. remotion_scenes.py renders each composition at its REGISTERED length
   (900f/30s) then truncates with `ffmpeg -t`, so keying to durationInFrames
   would push late reveals past the cut, where they are silently lost.

     python - <<'PY'
     import json
     p = r'<REEL>\beat_sheet.json'
     NEW = {'PromptTwoLayouts','LostMiddleCurve','EvidenceTiers',
            'GroundingDrift','AnnotatedPrompt'}
     d = json.load(open(p, encoding='utf-8'))
     for b in d['beats']:
         rem = b['shot']['remotion']
         if rem['pattern'] in NEW:
             rem['props']['beatSeconds'] = b['actual_duration_s']
     json.dump(d, open(p,'w',encoding='utf-8'), indent=1, ensure_ascii=False)
     PY

   Do this while NO render is running — remotion_scenes.py rewrites the beat
   sheet when it finishes and will clobber a mid-flight edit. Read it back after.

3. Visuals:
   python runtime/scripts/remotion_scenes.py <REEL>
   --force to re-render after a component edit; --only <BEAT_ID> for one.
   *** --only takes ONE id. `--only B05 B06` is an argparse error — loop instead. ***

   Bespoke components (runtime/remotion/src/scenes/, registered at BOTH aspects):
     PromptTwoLayouts  (B02) — Fig. 01 rebuild: one wall vs labelled sections
     LostMiddleCurve   (B03) — the position effect, shape only
     EvidenceTiers     (B04) — established finding vs vendor-internal rule
     GroundingDrift    (B05) — grounded sentence + unanchored one
     AnnotatedPrompt   (B07) — Fig. 02 rebuild, with the resolution added
   All sit on EmbedChrome's FigureFrame and ChunkChrome's useBeatClock.
   Do not fork that chrome. After ANY new component: ./art scene-index

   Reused unmodified: ClaudeComposerAsk (B00/BHTF), BrutalistHesitantWriter (B01),
   ProblemPredictCard (B06), ClaudeVerdictArtifact (BVDT), TitleOutroChannel (BOUT).

   BOUT must stay TitleOutroChannel. Do NOT swap to ClaudeTitleOutro: it is
   locked to claude-liam-* slugs (OUTRO-LOCK.md §Scope), hardcodes @NikBearBrown,
   and never renders a subline — silently dropping the author signature.

4. Assemble at 4K:
   python runtime/scripts/compile.py <REEL> --height 2160
   Explicit --height 2160 — compile.py's bare default is NOT 4K.

5. Visual QC — MANDATORY. ffprobe is a FILE check, never QC:
   ffmpeg -i <REEL>/claude-rag-prompt-construction.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read the PNGs, audit the 9-point rubric. Watch especially:
     B01 — VERIFY THE CORRECTION IS ON SCREEN. See the trap below.
     B02, B07 — the two tallest figures; confirm the headline is not hidden
           behind the cards and the caption does not run through them
     B07 — each callout must sit level with the section it annotates
     B06 — the commit line must be visible, not pushed off-frame
   Log defects in _qc/REPORT.md. Fix ROOT CAUSES in component source, re-render.

6. Confirm resolution:
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
     -of csv=p=0 <REEL>/claude-rag-prompt-construction.mp4   → 3840,2160

7. Never publish.
```

## Two traps this build hit — both silent, both cost a re-render

### 1. `BrutalistHesitantWriter` takes SINGLE-TOKEN triggers only

`buildActs` splits the text on `/(\s+)/` and matches `triggers.indexOf(core)`.
A multi-word `triggerWords` **never matches and fails silently** — no
correction fires and the beat ends holding the uncorrected text. On a Beat-2
BLUF that means the screen asserts the misconception while the narration states
the correction.

ai-explainer's SKILL.md says to put a whole phrase in `triggerWords` when the
misconception lives in one. **That guidance does not hold for this component.**
Restructure the sentence so one token carries it; the *replacement* may be
multi-word. Here: `concatenation` → `a set of deliberate choices`.

After rendering B01, always confirm the corrected text is on screen before the
cut — the law requires it and the failure is invisible to a duration check.

### 2. Figure height is BUDGETED, not accumulated

`FigureFrame`'s band is `flex: 1; minHeight: 0`; `ChunkChrome`'s `Panel` sets
`flexShrink: 0`. Content taller than the band does not clip — it overflows
symmetrically and **paints over the headline above and the caption below**.

Every vertical dimension in the five components is a fraction of `m.figHeight`,
and sections divide the leftover by weight. If you add content to one of these
figures, do not add a constant — change the weights. The landscape band is
roughly `0.47 × height`; anything past it silently eats the chrome.

## What's already done (as of this build)

- `beat_sheet.json` — 11 beats on the ai-explainer spine, audio generated
  (Kokoro `am_onyx`, $0.00), `beatSeconds` synced.
- `PEDAGOGY.md` (VERDICT: PASS) / `SOURCES.md` / `CHECKS-REPORT.md`
  (10 SHOW / 1 justified-HOLD / 0 PUNT) / `_qc/REPORT.md`.
- Five new components registered at both aspects, typechecked, indexed.
- Master: 3840×2160, 24fps, 191.01s (3:11), 12.1 MB.

## If re-running after a content edit

- **B03 must not gain numbers.** The chapter reports the direction of the
  Lost-in-the-Middle effect and publishes no per-position figures. The accuracy
  axis is deliberately unlabelled and the caption says so on screen. Adding
  plausible percentages would convert a real finding into a fabricated one.
- **B04 must keep both tiers distinct.** The chapter explicitly declines to
  promote the top-of-prompt ordering rule to a law. Flattening the two into one
  "best practices" list is the easiest and most misleading edit available.
- **B05 must keep both sentences equally confident.** Greying or striking the
  ungrounded sentence destroys the point — in a real answer the drift is
  invisible, which is why it survives review.
- **4K is a hard requirement** per the original build request: step 4 must pass
  `--height 2160` and step 6 must confirm `3840,2160`.

## Deriving the 9:16 Short

All five components register `916` twins and re-band rather than crop. The
ai-explainer spine has no revision cycle to drop, so the cut is a length
decision rather than a structural one — drop the predict/reveal pair or the
falsifiability beat, not the BLUF or the verdict.

```
python runtime/scripts/shorts.py <REEL> --drop B03 B04 --keep BHTF \
       --handle "@VedanshuDaxeshPatel" \
       --next "Full video: where the ordering rule stops being settled."
python runtime/scripts/compile.py <REEL>/short --height 3840
```

Three Windows notes if you do: pre-copy `mp3/beat-*.mp3` into `short/mp3/`
(`shorts.py` symlinks them and that needs privileges Windows withholds —
`OSError 1314`); regenerate the endcard at 2160×3840 with a font from
`runtime/fonts/` (its `find_serif()` probes only macOS/Linux paths and silently
falls back to an ~11px bitmap); and hand-write the rewritten outro narration,
because the auto-rewrite truncates dropped beats' `narration_text` into unusable
output.

**If you drop B04, rewrite BVDT.** Verdict line 4 ("The ordering rule is a
default, not a law. One vendor's tests.") reports what B04 shows. A short that
keeps the line but cuts the beat asserts a distinction it never drew.

### As built (the short exists — `short/claude-rag-prompt-construction-short.mp4`)

2160×3840, 24fps, 145.92s (2:26), 9 beats, `am_onyx`, $0.00. Full record in
`short/_qc/REPORT.md`. Five things a rebuild must repeat:

1. **Dropped B03, B04 AND B06** — then rewrote BVDT down to four lines, cutting
   the two that reported the position effect and the evidence tiers, plus the
   matching narration clause. The warning above fired exactly as written.
2. **Hand-write the outro.** The auto-rewrite produced the documented garbage
   ("also covers Where the information sits inside…"). The shipped version
   points at what was actually cut.
3. **B01 `fontSize` 74 → 96 for portrait.** `BrutalistHesitantWriter` scales by
   `min(w/1920, h/1080)`, so portrait takes the width ratio (0.5625). Measure,
   don't guess: at 74 the longest line was 1293px against `maxWidth` 1858px;
   at 96 it is 1678px (90.3%). Lines use `whiteSpace:'pre'` and do NOT wrap, so
   overshooting clips.
4. **Portrait starves one-line sections.** `PromptTwoLayouts` and
   `AnnotatedPrompt` now carry `plainW = portrait ? 1.35 : 1` and cap
   `chipFont` by `minSec * 0.30`. Without it the chips collide with their text
   bars (B02) or squeeze them out entirely (B07). Portrait-only by design —
   landscape geometry is unchanged.
5. **Compile clean and portrait-4K:** `compile.py <REEL>/short --height 3840`.
   Not `--review --height 1920` as `shorts.py`'s own "next steps" suggests.
