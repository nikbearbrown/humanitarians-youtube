# State Space Models and Mamba Architecture

**Fellow:** Uday Sonawane
**Date:** 2026-08-27
**Format:** `ai-explainer` chassis on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:35 (215.31s measured) · 12 beats
**Master:** 1920×1080; assets are 4K (Manim 2160p24, Remotion `--scale=2`), so `./art final` yields a true 4K master with no re-render
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Audience:** students — smart people getting started with AI
**Deliverable (local):** `StateSpaceModelsAndMamba_UdaySonawane_08_28_2026.mp4`

## What this video is about

What problem is the Mamba architecture actually solving, and what does it give
up to solve it?

The reel shows a **rubric before any architecture is scored** (B02, on screen at
**22.98s**) — three axes:

```text
STATE    how much does it carry forward, and does that grow?
UPDATE   is the update the same every token, or input-dependent?
COST     how does compute scale with sequence length?
```

The rubric is then applied live to an RNN and a Transformer (B03), and the arc
runs **SSM → S4 → Mamba** (B04–B06). The framework is load-bearing rather than
reverse-engineered: axis 1 says the state is fixed size, and the falsifiability
beat (B08) is the *proven consequence* of exactly that — a fixed-memory model
cannot copy arbitrary strings unless its state grows with the sequence
(Jelassi et al. 2024). Remove B02 and B08 becomes an unmotivated caveat.

## Sourcing

Nothing was narrated from memory. Three papers were checked against their own
abstracts before any narration was written:

- **S4** — Gu, Goel & Ré 2021, [arXiv:2111.00396](https://arxiv.org/abs/2111.00396)
- **Mamba** — Gu & Dao 2023, [arXiv:2312.00752](https://arxiv.org/abs/2312.00752)
- **Copying limits** — Jelassi et al. 2024, [arXiv:2402.01032](https://arxiv.org/abs/2402.01032)

Four beats (B05–B08) carry a visible arXiv citation at the moment of the claim,
not in an end card. Two claims were **weakened** after checking: "non-trivial
result on Path-X" rather than "solved Path-X", and "streaming" marked as author
inference rather than a paper claim. The 5× throughput figure is **attributed on
screen** rather than asserted — nothing was benchmarked locally. Full ledger,
including the claims deliberately *not* made, is in `SOURCES.md`.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Claim-by-claim sourcing + claims deliberately not made |
| `FACTCHECK.md` | Claim-level verdicts, including the two weakened claims |
| `CHECKS-REPORT.md` | PROOF gate: 12 SHOW / 0 HOLD / 0 PUNT, with the teaching arc |
| `BUILD-LOG.md` | Channel choice, gate record (A / W / B / V), and the B06 defect story |
| `PROOF-REVIEW.md` | Scored against the PROOF rubric |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the reel |
| `scenes.py` | Authored Manim scenes for the nine explainer beats |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `layout_audit_frames/*.png` | Sampled stills from that audit |
| `mp3/timings.json` | Measured per-beat narration durations (the clock) |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/*.mp3`, `qc-sheet.png`, and the masters
(`StateSpaceModelsAndMamba_UdaySonawane_08_28_2026.mp4`,
`state-space-models-and-mamba{,-slate}.mp4`).

## 9:16 Short — `short/`

A derivative vertical cut for YouTube Shorts, built with `./art shorts`.

**`state-space-models-and-mamba-short.mp4`** · 1080×1920 · ~1:48 (107.63s) ·
6 beats + silent endcard · GATE V **BLOCKER 0**

Six beats were dropped to get under the 3:00 Shorts cap and to leave one insight
standing — **the axis that makes Mamba cheap is the axis that limits it**. Kept:
B00 INTRO, B01 BLUF, B02 FRAMEWORK, B06 MECHANISM, B08 FALSIFIABILITY, plus a
rewritten funnel outro. Full cut list and reasoning in
[`short/SHOTLIST.md`](./short/SHOTLIST.md).

Both surviving citation beats keep their arXiv line on screen at the moment of
the claim. The 5× throughput figure is **not** in the Short — it lived in B07,
which was cut, so no number appears that is not sourced on screen.

The audio is the parent's, byte for byte; only the outro was regenerated, per
the Shorts Law. Manim run-times are copied verbatim — geometry changed, timing
did not. Both bookends render from `ClaudeComposerAsk916` /
`ClaudeTitleOutro916`; the four body beats are re-laid-out in
[`short/scenes.py`](./short/scenes.py) for the 4.5 × 8 portrait frame.

## Rendered video

The rendered cuts are not in this repo. Review copies of both of this fellow's
2026-08-27 reels — landscape and Short — are in Google Drive:

<https://drive.google.com/drive/folders/1T7zrj41hh10qB0qOU1LD3qJF6VL0qV0K>

This folder is for review only and is not a publication channel — see
**Publishing** below. The `.mp4` in the repo working tree stays gitignored; the
beat sheet, `scenes.py`, and `mp3/timings.json` here are what actually rebuild it.

## Environment constraints carried in the build

- **No LaTeX.** `dvisvgm` is absent, so `MathTex`/`Tex` would fail. The SSM
  equations in B04 are plain `Text` — which is why they read
  `h'(t) = A h(t) + B x(t)` in mono rather than as typeset math.
- **Fonts registered at runtime** via `manimpango.register_font()`; the
  installer copies EB Garamond to a Linux path Windows ignores.
- **B01 built around a centred origin** — the static checker reads coordinates
  as authored, before `fit()` re-centres them.

## Known accepted deviations

- **Framework lands at 22.98s**, ~3s past PROOF's "first ~20s". Reported rather
  than rounded down; it is still ahead of every example.
- **GATE V on the clean cut: 431 frames, BLOCKER 0, MAJOR 64** (60 underfill ·
  4 low-contrast). The underfill frames are staggered reveals still filling the
  canvas plus the sparse outro card; the low-contrast flags co-occur with
  10–11% fill, i.e. near-blank beat openings with too little ink to measure
  luminance separation. Accepted and documented, not silenced with
  `ART_STRICT=0` — see `PROOF-REVIEW.md`.
- The `24 BLOCKER` headline from `./art run` is GATE V reading the `*-slate.mp4`
  review cut, whose timecode burn-in sits outside title-safe by construction.
- **REBUILD LAW:** no figure is lifted from any paper. B01's curves are a
  schematic of quadratic-vs-linear *shape*, carrying no axis numbers, because no
  measured data backs them.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only, no API keys. Full prompt path is in `PROMPTS.md`.

## Publishing

Not authorized by this package. The master stays local until a human decides to
share or upload.
