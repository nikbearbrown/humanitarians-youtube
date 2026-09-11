# Visual Question Answering, Blind?

- **Status:** needs-work — both masters built and gate-clean; GATE P needs a human signature
- **YouTube:** <!-- blank until shipped -->
- **Playlist / chapter:** Fellows Research
- **Channel:** @HumanitariansAI
- **Fellow:** Ritik B. · Kokoro `am_onyx` (series voice)
- **Skill:** `ai-explainer` (brutalist.art)
- **Runtime:** 1:55.7 (115.69s), 11 beats
- **Resolution:** 3840×2160 (16:9) **and** 2160×3840 (9:16) — two masters, same content
- **Last updated:** 2026-09-06

## What the video teaches

A transformer answers a question about an image in four moves — tokenize both inputs into
one currency, fuse them with attention, pool and decide, then **audit**. The fourth move is
the reusable part: hide the image and re-score. Whatever accuracy survives was never vision.

The video walks moves 1–3 on one worked example ("What color is the umbrella?") and then
runs move 4 on the published record. In the original VQA benchmark a model that never sees
the image scores **48.76** against a sighted model's **57.75** — and **78.20** on yes/no
questions alone. The fix, complementary image pairs, costs every model tested 5–7 points.
So the architecture is honest and the *benchmark* was broken, which is a narrower and more
useful claim than "VQA models don't see."

The viewer leaves with a four-axis audit they can run on a model they did not build: blind,
paired, grounded, attributed. B09 hands it over as a runnable prompt with pass/fail readings.

## The two cuts

Both masters are the **same content, same beats, same narration files** — the 9:16 is not a
derived Short and not a centre crop. Every beat is one responsive React component registered
at both canvases; `scenes/VqaKit.tsx` flips layout direction on portrait. The Claude UI
bookends use the toolkit's existing `*916` twins.

| | reel folder | canvas | aspect_ratio | compile height |
|---|---|---|---|---|
| landscape | `vqa-blind/` | 3840×2160 | `16:9` | `--height 2160` |
| portrait | `vqa-blind-916/` | 2160×3840 | `9:16` | `--height 3840` |

Remotion renders at `--scale=2`, so the 1920×1080 and 1080×1920 compositions come out at
true 4K in both orientations — no upscaling anywhere in the chain.

## Paperwork

| File | What it is |
|---|---|
| `beat_sheet.json` | the 16:9 reel — one beat per moment, everything else derives from it |
| `beat_sheet-916.json` | the 9:16 reel — same content, same audio, patterns rewired to their `916` twins |
| `PEDAGOGY.md` | GATE P: the teach, the reusable rubric, the PROOF self-assessment, the signature |
| `CHECKS-REPORT.md` | the authoring exit condition: SHOW/HOLD/CARD per beat, teaching-arc checklist |
| `FACTCHECK.md` | every on-screen number, its primary source, and the two figures that are illustrative |
| `NARRATION.md` | the spoken track with measured per-beat durations |
| `PROOF-REVIEW.md` | review against the PROOF rubric + production gate, both orientations |
| `BUILD-LOG.md` | what was built, what broke, what was patched |
| `remotion/scenes/` | the seven scene components + the responsive kit (`VqaKit.tsx`) |
| `patches/brutalist-toolkit.patch` | registers the 14 compositions, and fixes two 9:16 toolkit scenes |
| `scenes.py` | intentionally empty — pure-Remotion reel, no Manim beats |

## Rebuild it (free, local, ~$0.00)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art && ./setup --install
```

Copy `remotion/scenes/Vqa*.tsx` into `runtime/remotion/src/scenes/`, apply
`patches/brutalist-toolkit.patch` (it registers the 14 compositions in `Root.tsx`), then:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>
python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160     # 9:16 twin: --height 3840
```

The `.mp4` masters are **not** in this repo — they stay on the build machine. Only the beat
sheet, the scene source, and the paperwork are tracked here.

## Quality gates

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L — beat mix | clean | clean |
| GATE V — frame QC (22 frames each) | **0 BLOCKER · 0 MAJOR ✓** | **0 BLOCKER · 0 MAJOR ✓** |
| Motion cap (≤ ~40% per language) | pass — 36% max | pass — 36% max |
| Master law — no slates | 11/11 VIDEO | 11/11 VIDEO |
| GATE P — narration | ⚠️ self-signed, needs a human | ⚠️ same |

Both masters probe identically: 2776 frames, 115.69s, 24 fps, AAC mono — same content,
two canvases. `BUILD-LOG.md` records all 16 defects found and fixed, including three
blockers (an entrance animation that slid content into the title-safe margin, a
content-sized flex row that pushed a token strip past the edge, and a portrait verdict
beat that cited nothing).

## Change notes

- 2026-09-06 — Built. Both 4K masters cut at 1:55.7, GATE V clean in both orientations.
  Two toolkit bugs found and fixed along the way (`patches/`): the 9:16 verdict scene
  never rendered `sourceNote`, and the 9:16 outro had a box-model bug that let a long
  unbreakable word overflow the title-safe edge. **GATE P is self-signed by the build
  agent at the operator's instruction — it needs a human read before this is shown to
  anyone.** `PROOF-REVIEW.md` flags B05 as the one beat still asking for trust
  (illustrative softmax rather than a real checkpoint's output). Not published.
