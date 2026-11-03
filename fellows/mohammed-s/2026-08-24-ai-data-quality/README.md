# The Rule, Not The Report.

*How AI manages data standards and data quality in an organization.*

- **Status:** built · QC-passed · not published
- **YouTube:** <!-- blank until shipped -->
- **Channel / handle:** @HussainShariff
- **Narrator:** Hussain (first person) · voice Kokoro `am_onyx` ("Onyx")
- **Resolution:** 3840×2160 (16:9) · 2160×3840 (9:16)
- **Runtime:** 3:07
- **Built with:** `ai-explainer` (brutalist toolkit) · Register: Teardown
- **Cost:** $0.00 — Kokoro + Remotion, entirely local, no API key
- **Last updated:** 2026-08-30

## The idea

The dashboard was never measuring meaning — it was measuring presence and
type. AI's real contribution here is not cleaning values; it is **proposing,
evidencing and maintaining the rules**, at a scale humans can't reach, while a
human still ratifies every one.

The test the reel leaves you with: *can this rule fail a row, and does that
failure reach a person?*

## Deliverables

| File | Aspect | Resolution | Size |
|---|---|---|---|
| `ai-data-quality.mp4` | 16:9 | 3840×2160 | 12.0 MB |
| `916/ai-data-quality-916.mp4` | 9:16 | 2160×3840 | 12.8 MB |

Copies also in `mp4/` and `916/mp4/` per the toolkit's deliverables layout.

**No review (`-slate`) cuts are kept.** One was built before the B07 fix and
was deleted rather than left lying around as a wrong-cut artifact. Regenerate
either on demand — they add beat labels and a timecode burn-in, which is also
why they must never be handed to GATE V (see `_qc/VISUAL-QC.md`):

```bash
python3 runtime/scripts/compile.py <reel>     --review --height 2160   # 16:9
python3 runtime/scripts/compile.py <reel>/916 --review --height 3840   # 9:16
```

Both cuts contain **all twelve beats** and the identical narration. The 9:16
is the vertical version of the video, not a trimmed Short — at 3:07 it is over
YouTube's 3:00 Shorts cap by design. If a true Short is wanted later,
`./art shorts` will derive one by dropping beats and rewriting the outro.

## Structure

```
B00  ASK         cold open — "Hi, I am Hussain…", the ask lands answered
B01  PROBLEM     98.7% green, six spellings of one country, all passing
B02  SCALE       12 written rules in 4,000 columns; 330 days to fix by hand
B03  DEFINITION  a wish vs a rule — the thing that can fail a row
B04  ASK         the prompt that works (and the one that doesn't)
B05  RESULT      evidence, then the rule, then 1,284 rows of blast radius
B06  GATE        318 proposals → 218 ratified / 59 to an owner / 41 rejected
B07  RUNTIME     rules on every load; failures to quarantine, with an owner
B08  TEARDOWN    three ways it bites: auto-correct · valid≠meaningful · rot
B09  VERDICT     the one-page recap
B10  HANDOFF     the prompt to run on your own table, read aloud
B11  OUTRO       title restate
```

## Paperwork

| File | What it is |
|---|---|
| `beat_sheet.json` | the reel; everything else is derived from it |
| `PEDAGOGY.md` | **GATE P** — signed narration/pedagogy review (VERDICT: PASS) |
| `FACTCHECK.md` | claim-by-claim ledger; declares every figure a worked example |
| `SOURCES.md` | provenance of every visual + the corrections applied |
| `SHOTLIST.md` | typed work order, lane histogram, terracotta ledger |
| `PROMPTS.md` | the on-screen prompts, verbatim, and why each is written that way |
| `BUILD-PROMPT.md` | paste-ready prompt to rebuild both masters end to end |
| `_qc/REPORT.md` | frame-level visual QC findings (VISUAL QC LAW) |

## Scripts in this folder

| Script | Why it exists |
|---|---|
| `sync_durations.py` | pins each Dq composition's length to its measured mp3 — without it, beats freeze or get trimmed |
| `make_916.py` | derives the full-length vertical cut (ONDA CHECK, no beat dropping, no symlinks) |
| `qc_frames.py` | samples each beat at 15/50/85% for the visual QC pass |
| `scenes.py` | deliberately empty — declares "no Manim here" and satisfies run.sh's guard |

## Notes

- **Narrator override.** The house `ai-explainer` bookends sign off "Liam, in
  for Bear". This reel is narrated in the first person by Hussain, so that
  sign-off is replaced and the folder chip reads `@HussainShariff`. Logged in
  `PEDAGOGY.md` and in the beat sheet metadata.
- **The figures are a worked example.** Every beat carrying a number prints
  `Worked example · illustrative figures`. Nothing here is presented as
  industry data; see `FACTCHECK.md`.
- **Never published from here.** The master stays in this folder; putting it
  in front of an audience is a human decision.

## Change notes

- 2026-08-31 — **both 4K masters built and QC-passed.** 3840×2160 and
  2160×3840, 187.49s each, 12/12 slots filled, GATE V 0 BLOCKER in both
  aspects. Full findings in `_qc/VISUAL-QC.md`.
  - Fixed a **collision GATE V could not see**: in 9:16, B07's diverted rows
    crossed the QUARANTINE card border and sat on the `country_code`
    descenders. The gate scored that frame clean — it has no collision check —
    so it was caught by reading the frame. B07 re-rendered in both aspects and
    both masters recompiled.
  - Corrected the channel key: the reel declared `brand: "claude"`, which maps
    to @NikBearBrown's "Computational Skepticism" series and made GATE L
    (branding rule 7) block the compile. Now `claude-hussain`, deliberately
    unregistered in `brand_labels.json` — see the beat sheet note.
  - `verify_clips.py` extended to probe the compiled masters, after two killed
    compiles each left a truncated `moov`-less mp4 that `ls` and the build log
    both made look finished.
- 2026-08-30 — first build: beat sheet, signed GATE P, audio locked at 3:07,
  and seven new concept-illustration components (`DataQualityIllus.tsx`) added
  to the toolkit, each registered for 16:9 and 9:16.
