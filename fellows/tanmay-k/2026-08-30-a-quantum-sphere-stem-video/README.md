# A Quantum Sphere Is Never the Size It Looks

Tanmay Kulkarni, in for Humanitarians AI · Week 20 topic video · built 2026-08-28

Text and code only. **The two masters live in the shared Google Drive**, not in this
repository — see the links below. The working folder and the full build record are outside
this repo.

---

## Watch

| Cut | Aspect | Link |
|---|---|---|
| **Long** | 16:9 | <!-- VIDEO_LINK_LONG --> [Watch on Drive](https://drive.google.com/file/d/1t0rMN1RNk7W9QAHmi1zDq2uAPDjDNTxu/view?usp=sharing) |
| **Short** | 9:16 | <!-- VIDEO_LINK_SHORT --> [Watch on Drive](https://drive.google.com/file/d/1pAGMHPdoRqDzHQefD2y-SNqToxqb6HjI/view?usp=sharing) |

## The two cuts

| File | Aspect | Resolution | Runtime | Loudness |
|---|---|---|---|---|
| `2026-08-28-a-quantum-sphere-is-never-the-size-it-looks.mp4` | 16:9 | 3840 × 2160 | **5:29.4** | −14.35 LUFS / −1.20 dBTP |
| `2026-08-28-a-quantum-sphere-short.mp4` | 9:16 | 2160 × 3840 | **1:54.1** | −14.23 LUFS / −1.45 dBTP |

Both are clean masters. Voice is Kokoro `am_onyx` — a documented departure from this series'
standing `af_bella`, because this film is narration over a measurement rather than a
walkthrough of a build.

**The Short is a trailer, not a shortened film.** It carries the finding whole — four at low
energy, two at high, never the classical one — with the gate frame as evidence and the source
line on it. The outro names the three things it withholds.

## What it teaches

Throw particles at a solid ball. Classical physics gives a one-line answer: it blocks its own
shadow, so the cross section is πa². Quantum mechanics says that number is **wrong at every
energy** — four times too small at low energy, twice too small at high energy, and never once
correct. Not near a resonance. Everywhere.

The method a viewer walks away with is the instrument, not the result: build the partial-wave
sum yourself, validate it against closed forms before trusting it, and read the limits off
your own curve.

## The evidence is a script, and it runs

```bash
python3 hard_sphere.py --all
```

About 200 lines of standard-library Python — no scipy, no install. It validates its own Bessel
functions against closed forms and the Wronskian identity (worst error 5.3e-15), reproduces the
curve, measures the approach to the high-energy limit, and runs a square-well control.

Every number on screen was computed in this folder, and the command that produced it is on the
same frame.

## What it claims, and what it does not

The low-energy limit of **4** and the high-energy limit of **2** are standard results, computed
here rather than quoted.

"Never equals the classical answer" is **verified numerically over 0 < ka ≤ 30** and stated on
screen with that scope. It is not proved for all ka, and the film says so on the frame that
makes the claim.

The exponent governing the approach to 2 measures **0.6659** by ka = 10⁴ and is consistent with
2/3 and with nothing else nearby: assuming 2/3 the coefficient flattens to 0.996, while 0.65
falls and 0.70 rises. That rules out the neighbours. **It does not derive the exponent**, and
the frame carries `measured — not derived`. The canonical analytic reference is Nussenzveig,
*Annals of Physics* 34 (1965) 23–95, which was identified but not accessible, so no coefficient
is quoted from it.

The factor of two is the **extinction paradox**; the resolution shown is van de Hulst's, and the
bookkeeping is the optical theorem.

## Where this topic came from

Drawn by the randomiser, not chosen — the point of the tool is to cut the time spent picking.

```bash
cd "Week 20/topic-video"
git -C ../../humanitarians-youtube fetch --all
python3 build_states.py && python3 scan_branches.py
python3 randomize.py --seed 20 -n 5
```

**Seed 20, drawn 2026-08-27, from a pool of 912 open topics** after rescanning 3,960 beat
sheets and re-checking other fellows' branches. The seed is recorded so the draw is
reproducible; `SELECTION.md` has the full record including the four alternates it offered.

Four of the five results landed in quantum mechanics. That is the draw and not a bias — QM is
166 of 912 open topics (18%), second only to design.

### The source project

The selected subject was **Hard Sphere Scattering with Claude**, which exists in this library
as two persona variants of one project:

| Path | Files | Beats |
|---|---:|---:|
| [`claude-for-quantum-mechanics/claude-liam-cli-vol3-hard-sphere-crosssection`](../../../claude-for-quantum-mechanics/claude-liam-cli-vol3-hard-sphere-crosssection/) | 41 | 12 |
| [`claude-for-quantum-mechanics/claude-liam-claude-liam-cli-vol3-hard-sphere-crosssection`](../../../claude-for-quantum-mechanics/claude-liam-claude-liam-cli-vol3-hard-sphere-crosssection/) | 38 | 12 |

A third folder, [`claude-for-design/vol3-hard-sphere-crosssection`](../../../claude-for-design/vol3-hard-sphere-crosssection/),
is the **same subject** filed under a different collection — 13 beats, same `af_kore` voice.
Finding it is what surfaced the third randomiser fix below.

Neither variant had a `.srt`, a description, a QC report, or a cut. Its existing assets were
pipeline output — narration audio, a concat, a contact sheet — not a human claim on the
subject, so the topic was genuinely open.

### Three randomiser fixes this draw forced

Both prior weeks' topics still read **OPEN** against the Week 19 tooling, meaning the
randomiser could have handed back a subject already shipped — the one thing it exists to
prevent. Fixing that came before the draw rather than after it.

1. **Taken-ness was scope-local.** Production evidence was gathered only from `claude-for-*`
   rows, so a subject produced under `fellows/<name>/<date> <slug>` never closed the family it
   was built from. Week 18's own episode has an MP4 *and* a QC report in this repo and still
   read OPEN.
2. **Work built outside the repo was invisible.** Topic videos assembled in `~/Humanitarians_AI/Week */`
   leave no trace here, so Week 19's subject read OPEN. Added `_local-claims.txt`, a
   hand-maintained subject list folded into the same normalisation.
3. **Builder prefixes were not stripped for dedup** — which is how the design-collection copy
   of this very subject stayed hidden.

Effect: **939 → 905 open topics**, with 33 families correctly closed — a more accurate pool
for every future draw, not just this one.

> **Upkeep:** this week's subject must be added to `_local-claims.txt`, or Week 21 can draw it
> again.

## What was inherited, and what was checked

The source project's generated simulation was **independently recomputed for this video and
found correct** — 2.328297 against its displayed 2.328, and 16 partial waves as it claimed —
on the beat where finding otherwise would have made the more dramatic story. The one thing
worth noting is a dropped π in an axis label.

Nothing else was inherited. The partial-wave sum in `hard_sphere.py` was written from scratch
for this film, and every number on screen comes out of it rather than out of the source
project.

## Files here

**The six core files**, the same set every episode in this series carries:

| | |
|---|---|
| `README.md` | this file |
| `PEDAGOGY.md` | Gate P, signed before any audio was generated |
| `FACTCHECK.md` | every claim, with what was checked and how |
| `QC-REPORT.md` | deliverable specs, loudness, resolution, gates — all `ffprobe`-verified |
| `beat_sheet.json` | the source of truth for the long cut |
| `beat_sheet-short.json` | the source of truth for the Short |

**Plus the experiment**, because this film's evidence is a program:

| | |
|---|---|
| `EXPERIMENT.md` | the method, the validation, the results, and what they do *not* establish |
| `experiment/hard_sphere.py` | ~200 lines, standard library only — **every number in the film comes out of this** |

Run it yourself:

```bash
cd experiment
python3 hard_sphere.py --validate     # do this first
python3 hard_sphere.py --all
```

Not included here: the build scripts, the Manim scene, the topic-selection tooling, and the
intermediate reviews. Those live in the working folder — this folder is the deliverable and
its evidence, not the workshop.

Captions (`.srt`/`.vtt`) and the YouTube description are produced at build time and kept with
the masters in the shared Drive, per this collection's convention.
