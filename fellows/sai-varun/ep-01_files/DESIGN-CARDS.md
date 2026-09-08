# DESIGN CARDS — four new components (GATE L punts, resolved)

GATE L was run before any beat was authored. Results:

**LIBRARY HITS (reused, nothing authored):** `ClaudeComposerAsk`,
`BrutalistHesitantWriter`, `HaiGlaucomaStakes`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`.

**GENUINE MISSES (4):** the searches below returned nothing usable. Per GATE L a
miss is a design card, never a licence to slate — so all four are specified here
and built before the first slate. Logged to `TEMPLATE-MISSES.md`.

| Search run | Best score | Verdict |
|---|---|---|
| "optic nerve fibers dying from the edges inward" | 2.0 (CoworkHourClock) | MISS |
| "signal below the threshold of human perception, detection line" | 9.0 (BrandGuidelinesTypography — a type-size rule) | MISS |
| "two things that look identical but one is diseased" | 6.0 (LookPlate — a fashion plate) | MISS |
| "machine reads a pattern a person cannot see" | 5.5 (derived-text ruben-substack scenes) | MISS |

`SourceFlow` (structural library) was evaluated for B07 and **rejected**: its
geometry is fixed as a dark server rack feeding an app window — wrong imagery for
an eye and a measurement, and it would break the cream fidelity stage.

House pattern followed: all four live in one reel-local file
`runtime/remotion/src/UncertainEyeE01.tsx`, registered in `Root.tsx` under a
`<Folder name="UncertainEyeE01">`, exactly as `HaiGlaucoma.tsx` does. They reuse
that file's proven `Stage` / `HaiBug` / `Caption` / `SparkLine` / `useP` chassis,
so palette, logo bug, and safe-area behaviour are inherited, not reinvented.
Remotion (not Manim) for all four — matches the sibling reel's decision to keep
this lane LaTeX-free. This deviates from the nopunt catalog's "moving mechanism →
Manim" row; logged here as a deliberate decision.

---

## 1. `UeNerveBundle` — B03

**Teaches:** the nerve is a bundle of over a million fibers, and glaucoma
subtracts them from the outside in.

Props: `sparkLine`, `fiberCount` (default 132), `countLabel`, `caption`.

Geometry: a nerve-head disc at frame centre-left; `fiberCount` fiber strokes fan
radially outward, seeded jitter in length and angle so the bundle reads organic
but is identical every render (`rng` from `HaiGlaucoma.tsx`).

Motion (pure function of `useP()`):
- `0.02–0.28` strokes draw outward from the disc
- `0.30` `countLabel` sets
- `0.52–0.86` fibers extinguish to ghost `#C3BFAE` ordered by **descending
  radius** — outermost first, the loss front moving inward
- terracotta marks ONLY the currently-extinguishing ring (the advancing edge) —
  one accent, sequenced, never a field of orange
- extinguished fibers vanish rather than blur. The beat's last line is "Not a
  blur. A subtraction." — if they blurred, the visual would contradict the voice.

Fill: bundle spans ~70% of `SAFE` height. Count label in serif at ≥64px.

## 2. `UeSilentWindow` — B04 (THE FRAMEWORK)

**Teaches:** damage accumulates while perception reports nothing, up to ~40%.
This is the model the rest of the season hangs on — it returns as an inset in
B05 and is the reason tier-one screening exists at all.

Props: `sparkLine`, `xLabel`, `damageLabel`, `noticeLabel`, `gateLabel`,
`windowLabel`, `caption`.

Geometry: one axis, fibers-lost left→right, filling the `SAFE` width. Two traces.

Motion:
- `0.05` axis draws
- `0.18–0.55` `damageLabel` trace climbs steadily from origin (ink)
- `0.42` `noticeLabel` trace drawn FLAT ON ZERO beneath it — the whole point;
  it must be visibly, boringly flat while the damage trace climbs
- `0.62` the flat span fills with a soft ink wash labelled `windowLabel`
  ("THE SILENT WINDOW")
- `0.78` terracotta gate drops at `gateLabel` ("up to 40%") — the ONE accent
- `0.90` only past the gate does the notice trace lift; a one-way arrow marks
  irreversibility

Legibility: both traces stay ≥40% opacity throughout. Labels ≥28px, set at the
traces, not in a legend box.

## 3. `UeLooksNormal` — B05 (WORKED EXAMPLE + FALSIFIABILITY)

**Teaches:** looking harder does not work.

Props: `sparkLine`, `leftLabel`, `rightLabel`, `verdictLabel`, `caption`.

Geometry: two schematic optic-nerve-head discs, side by side, identical scale and
baseline, each ~40% of `SAFE` width. Their cup geometry differs by a genuinely
small margin — the graphic must be honestly hard to call.

Motion:
- `0.05` both discs draw on, **unlabelled**
- `0.30–0.52` **held ≥2s, unlabelled** — the viewer is invited to pick the sick
  one and cannot. This hold is the beat; it satisfies the legibility contract's
  ≥2s comparison rule and must not be shortened to save runtime.
- `0.52` labels resolve; the right disc was early glaucoma all along
- `0.70` a small inset of the B04 silent-window axis appears, both eyes plotted
  inside the window — the worked example visibly USES the framework
- `0.86` `verdictLabel` "To the eye: indistinguishable." sets in terracotta

## 4. `UePatternProblem` — B07 (the concept, and the ask→result payoff)

**Teaches:** early detection is pattern recognition, not perception.

Props: `sparkLine`, `humanLane` (string[]), `machineLane` (string[]),
`verdictLabel`, `caption`.

Geometry: two horizontal lanes stacked, each spanning `SAFE` width. Top = the
human reading and it dead-ends. Bottom = the machine reading and it resolves.

Motion:
- `0.05` human lane draws: eye → judged by appearance → "reads: normal", ending
  in a visible dead-end stop (ink, no accent — this lane fails)
- `0.35` machine lane begins on "start measuring it": the same eye becomes a
  thickness field
- `0.55` the field resolves into a grid of numbers on "turn the nerve into numbers"
- `0.72` the numbers sort into two separable clouds on "find the pattern" —
  terracotta marks the separation boundary, the ONE accent of the beat
- `0.90` `verdictLabel` "A pattern-recognition problem." sets

Honesty: the two clouds are drawn as a **schematic separation**, not a plotted
result. No axis values, no score, no AUROC — the caption states "Conceptual. No
performance claim is made in this episode." The season's first number arrives in
E03; this beat must not imply one.

---

## After building

Run `./art scene-index` so all four land in `scenes.json` and E02–E08 can find
them. `UeSilentWindow` in particular is intended for reuse: the silent-window
framework is the spine of the whole season.
