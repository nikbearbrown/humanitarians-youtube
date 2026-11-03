# Automating the YouTube Review Pipeline — Vikhyat R

A pitch reel on what part of the fellow-video review loop can be automated and
what cannot. 12 beats, ~3 min, 16:9, `@HumanitariansAI`. Built 2026-09-04.

Source only. The rendered master is not in this repo.

## This week's contribution

**Question.** How much of the review loop can be automated?

**What I built.** A four-stage answer: check the file before uploading, sort the
Drive folder, move the check upstream into the toolkit, and upload — with the
last stage blocked on two decisions only the organisation can make.

**Observed result.** Most of the sorting is automatable. The judging is not, and
the uploading needs an approved Google project and a one-time authorisation from
the channel owner that cannot be delegated.

## Human and AI work

**My decisions:** scope, framing, register (state findings flatly, blame nobody),
the fact-checking discipline below, and the decision to cut a beat rather than
ship a claim I could not source.

**AI tools:** Claude Code for the beat sheet and the eight custom Remotion
components. Narration is Kokoro TTS (`am_michael`), local and free.

**What I rejected or corrected — the part worth reading:**

`FACTCHECK.md` records three claims cut as **false** and one whole beat removed:

- **B05 was cut entirely.** It argued that failures come from fellows running an
  older copy of the toolkit where the render default was 1080. Checking the
  commit history disproved it — `279e925`, the first commit of `brutalist.art`,
  already reads `HEIGHT=2160`. No version of that repo ever shipped 1080. The
  claim had survived two rounds of hedging; a one-minute `git log` killed it.
- **"Roughly six uploads a day is a constraint"** — false. Taken from the
  toolkit's own out-of-date `docs/PUBLISHING.md`. `videos.insert` costs 1 unit
  against a dedicated 100/day allowance.
- **"The script has to be authorised as a manager"** — false. Delegation is
  impossible; the owner authorises personally.
- **"Liam in for Bear is a branding mistake"** — false. It is required behaviour
  under the IN-FOR-BEAR LAW. Flagging it would have flagged correct work.

**What remains unverified:** nothing on screen. The standing rule for this reel
was that no claim goes on camera without a row in `FACTCHECK.md`.

## Reproduce — read this before trying

**This beat sheet cannot currently be rebuilt as-is.** Eight of its twelve beats
use components authored specifically for it:

`HaiPipelineReviewLoop` · `HaiPixelThreshold` · `HaiSoftFourK` ·
`HaiRenderDefaultDrift` · `HaiStageOneSort` · `HaiOutroMismatch` ·
`HaiStageTwoThree` · `HaiStageFourNeeds`

They were written into a working copy of `brutalist.art` that has since been
replaced, and they are not in the current toolkit — `HaiReviewPipeline.tsx` is
absent and none of the ids are registered in `Root.tsx`.

What survives is enough to reconstruct them:

- `PROMPTS.md` — a full build prompt per component, with its prop contract
- `_props_B*.json` — the exact props each beat was rendered with
- `BUILD-PROMPT.md` — the end-to-end rebuild instruction
- `beat_sheet.json` — narration, timing and the `show` block for every beat

The four remaining beats (B00, B01, B10, B11) use `ClaudeComposerAsk`,
`BrutalistHesitantWriter` and `OutroSeries`, which are registered in the toolkit.

This is a genuine reproducibility gap and I would rather record it than let
someone discover it mid-build. Rebuilding the eight components from `PROMPTS.md`
is the route back.


## Notes

- `metadata.channel` is deliberately omitted. Setting it to `claude-hai` makes
  GATE L rule 7 enforce the fixed series kicker "Irreducibly Human". This is an
  outsider's pitch, not an episode of that series, so it carries the HAI chip
  without claiming the series name.
- The outro is `OutroSeries`, never `ClaudeTitleOutro` — that one is locked to
  `@NikBearBrown`. The reel passes its own B07 check.
- `STATUS.md`, `ToDo.md` and `todo.json` are excluded from this folder. They are
  derived from `beat_sheet.json` and were stale: they report 0/12 filled when the
  build stamp shows 11/11, and `todo.json` names a voice the sheet does not use.
