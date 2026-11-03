# CHECKS-REPORT — `yatra-this-week-gordy`

Written BEFORE the first slate compiled, per the PROOF GATE in
`skills/make/ai-explainer/SKILL.md`.

```
12 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification (nopunt § SHOW / HOLD / CARD)

| Beat | Class | Scene | Why it is SHOW |
|---|---|---|---|
| B00 | SHOW | `ClaudeComposerAsk` | the composer is the subject; the ask lands answered with three result lines |
| B01 | SHOW | `WkBluf` | three stated facts with status chips; the unfinished one lands in the accent |
| B02 | SHOW | `WkPipeline` | five stages draw on cue with connectors — the method is a drawn artifact |
| B03 | SHOW | `WkTool` | the tool page's own sentence as a quoted block, with chips, URL and citation |
| B04 | SHOW | `ClaudeComposerAsk` | ask micro-beat of the reel's one ask→result pair |
| B05 | SHOW | `WkStatus` | the five stages fill in narration order; the open one stays hollow |
| B06 | SHOW | `WkShip` | made → destination routes with a status chip on the wire |
| B07 | SHOW | `WkReview` | two dashed empty slots under a withheld band, then the review track |
| B08 | SHOW | `WkNotClaiming` | claims and refusals side by side, each landing on its spoken clause |
| B09 | SHOW | `ClaudeVerdictArtifact` | the artifact page; four lines per spoken clause |
| B10 | SHOW | `ClaudeComposerAsk` | the handoff prompt types itself as it is read aloud |
| B11 | SHOW | `ClaudeTitleOutro` | title restate |

No bare CARDs, no PUNTs. Every beat whose narration names a visual renders it.

## Teaching-arc checklist (nopunt § Whole-sheet)

Adapted honestly to the recap genre — this is a first-person report, so the arc
items map to the series' method rather than to a scientific claim.

- **FRAMEWORK beat — ✓ B02.** The five-stage method is presented before any of
  this week's state appears, and the stages are deliberately UNLIT. `WkPipeline`
  has no per-stage `state` field at all, so the framework cannot leak B05's
  status board.
- **WORKED EXAMPLE — ✓ B05.** This week run through that exact framework, stage
  by stage, while the framework is on screen. Four close; one stays open. B06
  and B07 then expand the two stages that carry this week's actual work.
- **FALSIFIABILITY — ✓ B08.** A full beat, not a caveat: a two-column ledger of
  what is and is not being claimed. For a first-person recap the failure mode is
  overclaiming, so the stress-test is the explicit refusal — including that the
  narrator's read on Gordy comes from use, not from its one-line page.
- **SCAFFOLDED TASK — ✓ B10.** A real prompt plus a three-item rubric
  ("does it separate finished from published?" / "does it name the stage you're
  stuck on?" / "would a stranger know what is not done yet?").
- **FOUR BOOKENDS — ✓.** Cold open B00 · verdict B09 · your turn B10 · title
  restate B11.
- **NO SOURCE, NO VERDICT — ✓.** The only externally-checkable claim in this
  reel is Gordy's description, and B03 renders it as a verbatim quote with
  `Source: humanitarians.ai/ai1/tools/gordy-tool (page description, verbatim)`
  plus its URL on screen. Every other claim is the narrator's own first-person
  account of her own week, which is the genre's evidence; B08 draws the line
  between what that account does and does not support, and B09 repeats the
  review state rather than letting the summary imply completion.

## Legibility contract

- Every SHOW beat names its artifact in `shot.show`.
- Comparisons that matter (B01's three states, B02/B05's five stages, B07's
  three-stage review track, B08's two columns) are all held well past 2s at
  their measured beat lengths.
- Dimmest resting state on content is the stagger-in floor, well above the ~40%
  bound; `opacity: 0.3` applies only to the brand bug, which is chrome.
- Frame-level verification after render in `_qc/QC-LOG.md`.

## Notes for the reviewer

- **Duration 2:23 (143.1s)** — an output, not a target. Inside the 1–3 minute
  brief with headroom under the hard 3:00 Shorts cap, so the vertical is the
  complete video rather than an auto-shortened cut.
- **Series continuity.** This is the next episode after
  `yatra-one-tool-a-week-brandy`. All seven illustration components are new;
  the `Rcp*` family from that reel and the `Lnk*` family from
  `yatra-nobody-wrote-this` are both untouched. See FACTCHECK.md § series-continuity.
- **Manim is not installed** in this environment (`./art doctor` reports it
  blocked; Kokoro, Remotion, Pillow and captions are READY). No beat here needs
  it — every beat is Remotion — so `run.sh` skips the Manim stage cleanly.
  Recorded so the skip is not mistaken for a dropped beat.
- **Two known pipeline traps to avoid on rebuild**, both learned the hard way on
  the previous reel and both recorded in BUILD-PROMPT.md: point GATE V at the
  clean master (it flags the review cut's own burned-in timecode as 28
  edge-bleed blockers), and pass `--handle "@Yatra"` to `shorts.py` (its default
  is `@nikbearbrown`, which would end this vertical on the wrong channel).
