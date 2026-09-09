# BLIP: Noisier Data, Better Model?

- **Status:** needs-work — both masters built and gate-clean; GATE P needs a human signature
- **YouTube:** <!-- blank until shipped -->
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:58.7 (118.74s), 11 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content
- **Source:** Li, Li, Xiong & Hoi — *BLIP*, ICML 2022 · [arXiv:2201.12086](https://arxiv.org/abs/2201.12086)
- **Last updated:** 2026-09-08

## What the video teaches

BLIP's contribution is not its architecture. It is that BLIP treats **its own training
data as a hypothesis to be tested** — and publishes the run with the test switched off.

Web alt-text is bad supervision. So BLIP finetunes two copies of one pre-trained model:
a **captioner** (an image-grounded text decoder) writes a new caption for each web image,
and a **filter** (an image-grounded text encoder) throws out the ones that don't match —
web-written and machine-written alike. Retrain on the survivors and 14M images beat 129M
raw web images on retrieval: **80.6 against 79.6 TR@1**, same backbone, same benchmark.

The reusable part is the audit, and the video shows it before any BLIP number:

| # | Axis | The question a viewer asks of any paper | BLIP's own receipt |
|---|---|---|---|
| 1 | GENERATE | Who writes the new labels, and with what decoder? | §3.3 |
| 2 | JUDGE | Is the filter a separate copy, or the writer's twin? | **Table 4** |
| 3 | DIVERSITY | Does the writer sample, or play it safe? | **Table 2** |
| 4 | ABLATE | Is there a run with the bootstrap off, same data, same backbone? | **Table 1** |

Axis 2 carries the accent because it is the one usually skipped and BLIP measured its
cost: let the filter share weights with the captioner and rejection collapses from **25%
to 8%** — it stops recognising its twin's mistakes — and every downstream number falls
with it. Confirmation bias, with a measurement beside it.

Axis 3 is the friction the viewer has to resolve. Nucleus sampling gets rejected *more*
often than beam search (25% vs 19%) and wins anyway (80.6 vs 79.6). Noisier data, better
model — because diversity is what the captioner contributes and the filter is what makes
the extra noise affordable.

And the thesis is scoped out loud: on COCO **captioning** the raw 129M edges the
bootstrapped 14M, CIDEr 130.1 against 129.7. Quality beats quantity *here*, not everywhere.
That exception renders in the same frame as the claim.

## The two cuts

Both masters are the **same content, same beats, same narration files** — the 9:16 is not
a derived Short and not a centre crop. Every body beat is one responsive React component
registered at both canvases; `scenes/ReelKit.tsx` flips layout direction on portrait. The
Claude UI bookends use the toolkit's existing `*916` twins.

| | reel folder | canvas | `aspect_ratio` | compile height |
|---|---|---|---|---|
| landscape | `blip-bootstrap/` | 3840×2160 | `16:9` | `--height 2160` |
| portrait | `blip-bootstrap-916/` | 2160×3840 | `9:16` | `--height 3840` |

Remotion renders at `--scale=2`, so the 1920×1080 and 1080×1920 compositions come out at
true 4K in both orientations — no upscaling anywhere in the chain.

**Content parity is structural this time, not verified after the fact.** `author_sheets.py`
holds ONE beat list and emits both sheets; the portrait sheet is a mechanical transform
(slug, `aspect_ratio`, the `916` pattern suffix). The sibling reel maintained two
hand-edited sheets and diffed them afterwards — this cannot drift in the first place.

## Paperwork

| File | What it is |
|---|---|
| `author_sheets.py` | **the single source of truth** — emits both beat sheets |
| `conform_durations.py` | pushes each measured mp3 length into that beat's `durationS` |
| `check_clips.py` | asserts every rendered clip is the length its beat asked for — the check GATE V structurally cannot make |
| `beat_sheet.json` | the 16:9 reel (generated) |
| `beat_sheet-916.json` | the 9:16 reel (generated) — same content, same audio, `916` patterns |
| `PEDAGOGY.md` | GATE P: the teach, the reusable rubric, the PROOF self-assessment, the signature |
| `CHECKS-REPORT.md` | the authoring exit condition: SHOW/HOLD/CARD per beat, teaching-arc checklist |
| `FACTCHECK.md` | every on-screen number → its table; and the one illustrative element |
| `NARRATION.md` | the spoken track with measured per-beat durations |
| `PROOF-REVIEW.md` | review against the PROOF rubric + production gate, both orientations |
| `BUILD-LOG.md` | what was built, what broke, what was patched |
| `remotion/scenes/` | the eight scene components (three shared, five this reel's own) |
| `patches/brutalist-toolkit.patch` | registers the 14 compositions in `Root.tsx` |
| `scenes.py` | intentionally empty — pure-Remotion reel, no Manim beats |

## The scene set, and what moved

This is the **second** reel in the series, so two beats that were structurally identical to
the sibling reel's were promoted out of it rather than copy-pasted:

| File | Status |
|---|---|
| `ReelKit.tsx` | promoted from `VqaKit.tsx` — the orientation-aware stage, clock and card |
| `ReelExecSummary.tsx` | promoted from `VqaExecSummary.tsx` — the Beat 2 BLUF |
| `ReelFramework.tsx` | promoted from `VqaFourMoves.tsx` — the framework beat, now with an optional per-row `receipt` and a settable `accentIndex` |
| `BlipMed.tsx` | new — one transformer, three functionalities |
| `BlipCapFilt.tsx` | new — the worked example |
| `BlipIndependence.tsx` | new — Table 4, the confirmation-bias receipt |
| `BlipDiversity.tsx` | new — Table 2, the butterfly |
| `BlipLadder.tsx` | new — Table 1, the ablation on a declared truncated axis |

`VqaKit.tsx`, `VqaExecSummary.tsx` and `VqaFourMoves.tsx` become re-export shims in the
toolkit, so the sibling reel's fourteen registered compositions and its beat sheet are
untouched. **The snapshot in `../2026-09-06-vqa-blind/remotion/scenes/` is the
pre-promotion version and is what its masters were rendered from** — it is left alone on
purpose, so that reel stays byte-reproducible. `ReelExecSummary` also picked up a
canvas-fill fix here (its roadmap cards centred instead of top-anchored), which is a
deliberate improvement the sibling's snapshot does not carry.

## Rebuild it (free, local, ~$0.00)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art && ./setup --install
```

Copy `remotion/scenes/*.tsx` into `runtime/remotion/src/scenes/`, then apply
`../2026-09-06-vqa-blind/patches/brutalist-toolkit.patch` **first** and
`patches/brutalist-toolkit.patch` second — the second hunk's context sits directly below
the first reel's registrations, so the order matters. Then:

```bash
python3 author_sheets.py
python3 runtime/scripts/generate_audio_kokoro.py <reel>
python3 conform_durations.py
python3 runtime/scripts/remotion_scenes.py <reel>
python3 check_clips.py                                      # before compiling, not after
python3 runtime/scripts/compile.py <reel> --height 2160     # 9:16 twin: --height 3840
python3 runtime/qc/final_frame_check.py <reel>
```

The `.mp4` masters are **not** in this repo — they stay on the build machine, per the
`fellows/` contract. Only the beat sheets, the scene source and the paperwork are here.

## Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| PROOF GATE — authoring | 11 SHOW · 0 HOLD · 0 PUNT | same sheet, same result |
| GATE L — beat mix | clean | clean (2 expected `*916` skin-lint notes) |
| Clip lengths — `check_clips.py` | all clips match their beats ✓ | all clips match their beats ✓ |
| GATE V — frame QC (22 frames each) | **0 BLOCKER · 0 MAJOR ✓** | **0 BLOCKER · 0 MAJOR ✓** |
| Motion cap (≤ ~40% per language) | pass — 36% max | pass — 36% max |
| Runtime cap (≤ 2:00) | pass — 1:58.7 | pass — 1:58.7 |
| GATE P — narration | ⚠️ self-signed, needs a human | ⚠️ same |

## Change notes

- 2026-09-08 — Built. Both 4K masters cut at **1:58.7**, GATE V clean in both orientations,
  and both probe identically: 2849 frames, 118.74s, 24 fps, AAC mono. The first narration
  pass measured 2:02.3, so six beats each lost a trailing clause that was already on screen.
  `BUILD-LOG.md` records all 12 defects found and fixed — **two of them 9:16-only and
  invisible in the beat sheet, in `tsc`, and in the landscape frames**, which is the case for
  reading both orientations by hand rather than trusting one. One defect was of a class no
  frame gate can catch (a clip that was the wrong LENGTH, not the wrong pixels) and became
  `check_clips.py`. **GATE P is self-signed by the build agent at the operator's instruction
  — it needs a human read before this is shown to anyone.** `PROOF-REVIEW.md` flags B04's two
  caption strings as the reel's only element asking for trust. Not published.
