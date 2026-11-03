# Week 22 — Topic Selection

**Selected:** `claude-for-mathematics/why-120-bpm-works-the-hidden-mathematics`
**Working angle:** the 2 Hz convergence — why three unrelated human systems land on the same rate
**Decided:** 2026-09-13

---

## How the topic was chosen

A randomized draw over the STEM collections of `humanitarians-youtube`, with three
exclusion rules applied in sequence. Two earlier draws were rejected on inspection; both
rejections are recorded here rather than quietly re-rolled.

### Draw 1 — `claude-for-astronomy/ai-vs-the-data-deluge` — REJECTED

The stage-2 winner was already a finished video (Om Mali, 19 beats, 4K master rendered
2026-08-01, 17-row `FACTCHECK.md` with primary sources). The proposed differentiating
angle was *"the AI never saw raw data — it ranked candidates a classical pipeline had
already flagged, and can only recognize what it was trained on."*

**That angle is already the explicit thesis of a fellow's episode in the same collection.**
`claude-for-astronomy/gravitational-wave-detection` (Om Mali, Ep. 03):

- Beat 10 — *"Be precise about scope. This classifier does not detect gravitational waves.
  Matched filtering does that, and it is classical signal processing, not a trained model."*
- Beat 9 — *"A trained classifier can only name a shape it has already seen... The people
  found them, not the network."*
- Beat 11 — *"The problem is trust, not detection... the limit is the shape nobody has named yet."*

Rejected to avoid restaging a fellow's argument in a different domain.

Adjacent ground also already held:
- `fellows/aishwarya-p/2026-08-28-survivorship-bias-datasets` — data filtered before you see it
- `computational-skepticism/why-99accurate-test-is-wrong-about-almost-everyone` — base rates

The astronomy collection is saturated: Ep. 01 data scale, Ep. 02 vetting/explainability,
Ep. 03 detection-vs-classification scope, Ep. 04 crowd labels, Ep. 05 real-time triage.
All five are built. No other branch holds astronomy work.

### Draw 2 — `claude-for-mathematics/compound-interest-simulator` — REJECTED

Most-duplicated topic in the library: `claude-for-education/compound-interest-calculator`,
its `nbb-` twin, `claude/claude-code/claude-liam-compound-interest-calculator`,
`claude/claude-youtube/claude-liam-compound-interest-simulator`, plus `exponential-growth`
in two further variants.

### Draw 3 — accepted

The randomizer was rebuilt to draw only from topics that appear **once across the entire
library**. Topic keys are normalized by stripping variant prefixes (`nbb-`, `claude-liam-`,
`medhavy-vox-`, `vox-`, `cli-`, `hai-`, `riff-`, `qmcg-`) and tooling suffixes
(`-simulator`, `-calculator`, `-explorer`, ...), then counted across all 23 collections
plus `fellows/`.

```
library topic keys   : 2249
keys appearing once  : 1267
eligible singletons  :   58   (AI 18 · CS 23 · math 4 · physics 2 · comp-skepticism 11)
```

Excluded collections: astronomy (saturated), quantum-mechanics (Week 20),
cancer + cancer-biology (Week 21), nanomedicine (no singletons).

---

## Uniqueness verification

| Check | Result |
|---|---|
| Topic key repo-wide | appears **once** (1 of 1267 singletons) |
| All 30 remote branches swept for `BPM` / `tempo` / `cadence` / `rhythm` | no competing treatment |
| `claude-for-music` (28 projects) reviewed | closest are `baby-language-window-neuroscience-music` and `born-bilingual-...`, both on **phoneme discrimination windows** (Zhao & Kuhl 2016), not tempo |
| Fellow authorship | none — the existing folder is an auto-converted essay by the founder, not fellow work |

**Scope line drawn to keep it unique:** the infant language-acquisition material in the
existing beat sheet belongs to the two music-collection essays above. This video drops it
and centers on the *mathematics of 2 Hz*. That boundary is what makes the topic
non-overlapping, and it should not be crossed.

---

## State of the existing source

`claude-for-mathematics/why-120-bpm-works-the-hidden-mathematics` is **not a finished
video**. It is one of a batch of automatic Substack-essay conversions, and it is broken:

- Folder slug says *120 BPM*; the content is titled *"The Sesame Street Conspiracy"*
- `Let's recap with Claude` sits at **beat 2**, before the body it claims to recap
- Beats are disconnected fragments — *"It's not that they can't process language. Baroque
  music achieves something similar through different means."* has no antecedent
- **Beat 5 asserts `"This is not a correlation."`** with nothing supporting it
- No `FACTCHECK.md`. `SOURCES.md` carries a single statistic, about Sesame Street
- `mp3/` holds only `timings.json`

The sibling `nbb-compound-interest-simulator` shows the same batch's failure mode — its
beat 13 tells the viewer to *"pick any cancer type or clinical scenario"* in a video about
compound interest. Template bleed, never caught.

So there is no fellow's work to differentiate from here. There is raw material and a real
question underneath it.

---

## The angle

Three independent human systems converge on **2 Hz**, and the interesting part is that one
of the three does not generalize the way the convergence story implies.

1. **Preferred musical tempo** ≈ 120 BPM = 2 Hz — and 2 Hz is the modal beat rate of Western pop
2. **Human locomotion** has a tuned resonance at 2 Hz, independent of height, weight, age, or sex
3. **Stressed syllables in speech** land near 2 Hz — *but the neural entrainment to it is
   language-dependent*

Leg 3 is where the video earns its keep. Native English speakers show enhanced entrainment
at 2 Hz stress and 4 Hz syllable rates; native Mandarin speakers do not. A "universal human
rhythm" framing survives legs 1 and 2 and breaks on leg 3 — which is the honest, falsifiable
result, and the direct correction to the source essay's unsupported *"This is not a correlation."*

Every claim above is verified in [`FACTCHECK.md`](FACTCHECK.md) against primary sources.

---

## Not yet decided

- Beat count and structure
- Whether the walking-cadence caveat (lab resonance 2 Hz vs. free-living cadence ~100–115
  steps/min) is its own beat or a line inside the locomotion beat
- Title — the existing slug and the existing content title disagree, and neither is right
