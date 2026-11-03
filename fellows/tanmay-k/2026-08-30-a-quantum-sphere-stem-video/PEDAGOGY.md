# PEDAGOGY — Gate 1 (Premise) · Week 20 topic video

**Working title:** *Four, Then Two, Never One*
**Subtitle:** the cross-section that refuses to be classical
**Series / channel:** Claude for Science · Humanitarians AI · `am_onyx` (Onyx), narration register
**Builder:** `deep-explainer` · estimated runtime ~8:29 (see `SCRIPT.md` runtime budget)

## The teachable claim

Fire particles at a hard sphere of radius `a`. Classically the answer is settled and boring:
it blocks πa², at every energy. Quantum mechanically it blocks **4πa² at low energy, 2πa² at
high energy, and πa² at no energy whatsoever.**

The sphere is never the size it looks. The video is about why, and about the one habit that
tells you which regime you are in before you compute anything.

## The framework the viewer walks away with — COUNT THE WAVES

The content is five questions applicable to any scattering target. **The delivery is an
instrument, not a recited list** — see `STRUCTURE-DIFF.md` for why that change was made
(the previous four reels all front-load a numbered framework, and a fifth would have been
the same film again).

| # | Question | Delivered as | Where |
|---|---|---|---|
| 1 | **What is ka?** target size ÷ wavelength | the instrument's single **dial** | B03 |
| 2 | **How many waves reach it?** `l_max ≈ ka` | the dial's **scale marking**, verified on screen | B03B |
| 3 | **Read the regime off the count.** one wave → 4× classical; many → 2× | the **readings** themselves | B05, B06 |
| 4 | **Does the target have an inside?** interior → resonances; none → smooth | a **gauge**, shown UNREAD at B03B, read at B10 | B10 |
| 5 | **Is the limit reached or only approached?** | a **gauge**, shown UNREAD at B03B, read at B09 — and priced at B09B | B09, B09B |

All five are visible as a structure at B03–B03B, **before any hard-sphere result** — which
is what the PROOF rubric requires. Items 4 and 5 are visibly present but deliberately
*unread*, so the structure is complete on screen while the film still has somewhere to go.

Step 2 is the load-bearing one, and it is why the rubric is honest rather than decorative:
the number of partial waves that matter is not a computational detail chosen for
convenience — it *equals* ka, so counting waves and measuring the target in wavelengths are
the same act. B03B verifies it on screen (100→102, 2000→2002) rather than asserting it.

### Applying it to a new case without guessing

**These two cases are the viewer's first task, not an illustration.** They sit in B11, where
the film hands the dial over: *"Put these on the dial yourself — slow neutrons on an atomic
nucleus, and red light on a droplet of fog. Where does each land?"* Answers follow on screen.

Neutrons: λ ≈ 1.8 Å against a ≈ 5 fm gives ka ≈ 1.8 × 10⁻⁴ → one wave → 4× geometric,
smooth, limit well reached. Fog droplet: λ = 633 nm, radius 10 µm gives ka ≈ 99 → ~99 waves
→ ≈2× geometric, but step 5 says 2 is still 4.5% off at that ka, and step 4 warns a droplet
*has* an inside, so expect structure.

They moved out of B03B deliberately: as illustration inside the setup they extended a 1:38
stretch with no payoff, and a viewer had no reason yet to care. As the warm-up task in the
CTA they do the same pedagogical work — PROOF's *reusable rubric* criterion, applying the
axes to a case the film never computes — while being something the viewer actually does.

*(Both cases are illustrative order-of-magnitude estimates for the framework, labelled as
such on screen — the video computes neither. See `FACTCHECK.md` C13.)*

## The friction the viewer has to resolve

Stated at ~1:40 and deliberately left hanging for a beat:

> At high energy, classical mechanics is supposed to *work*. The wavelength is tiny, the
> sphere is huge, this is the easy limit. So why is the answer 2πa² and not πa²?

The resolution is the payoff, not the setup: **to cast a sharp shadow you have to bend
waves into the space behind the sphere.** That bending is scattering — those particles
changed direction, so they count — and it adds up to exactly another πa². The shadow is not
free. You pay for it in cross section, at par.

This is the beat the source video does not contain in any form.

## The falsifiability case

Step 4 is the axis that could be decorative, so the video tests it on a target that breaks
the pattern. Same code, same grid, an attractive square well instead of a hard sphere:
**10 resonance peaks vs. 0** (R4 control). The framework predicted the difference from the
"does it have an inside?" question alone.

Without this, "count the waves" would be a story reverse-engineered onto one example —
PROOF Behavioral Rule 1. With it, the axis has a case that could have falsified it and did
not.

## The active task (CTA scaffold)

Not "ask Claude." The viewer gets a prompt **and the check that grades it**:

> Extend the simulation: plot σ/πa² for a hard sphere **and** an attractive square well of
> depth 2mV₀a²/ħ² = 900 on the same axes, for 0 < ka < 18.
>
> **Your build passes if:** the hard-sphere curve reads 2.328 at ka = 13.6 and falls
> monotonically with zero turning points, while the well shows ~10 peaks, the first near
> ka = 2.88.
>
> **Your build is broken if** the hard-sphere curve wobbles — that is not physics, that is
> your partial-wave sum truncating too early, or `j_l` computed by upward recurrence past
> l ≈ ka.

Good result vs. bad result is stated, with the specific numeric tell and the specific cause.

## PROOF rubric — self-assessment at Gate 1

| Criterion | Target | How this premise meets it |
|---|---|---|
| Explicit framework | 2 | COUNT THE WAVES shown as a 5-row structure before any result |
| Reusable rubric | 2 | Worked on neutron/fog-droplet cases the video never computes |
| Worked example | 2 | Hard sphere walked through all five steps live, reasoning shown |
| Falsifiability / edge | 2 | Square-well control: 10 peaks vs 0, same code |
| Active task | 2 | Runnable prompt + numeric pass/fail + named failure cause |
| Friction | 2 | The 2-vs-1 shadow paradox, posed and held before resolution |

Projected **12/12**. The score is a target, not a claim — it is re-scored against the actual
cut in `PROOF-REVIEW.md`, where the production gate is the binary that can veto regardless.

## GATE P — narration review

Machine pass complete: `GATE-P.md`. 30 lint flags resolved to 3 accepted-with-reason, plus
seven items the continuous read-through caught — including a continuity slip at B08
("all three readings" before reading three existed) and a wrong value at B04 introduced while
shortening a spoken digit chain.

**GATE P: PASSED.**

```
Read aloud by: Tanmay Kulkarni            Date: 2026-08-27
VERDICT: PASS
Notes: Voice set to am_onyx (Onyx) — narration register. Script wording unchanged.
```

Audio generation is unblocked. Measured Kokoro durations become the master clock and replace
the 140 wpm estimates; every beat must then be re-rendered to its measured length.

## GATE 1 VERDICT

**PASS — cleared to script.**

The method a viewer walks away able to apply is COUNT THE WAVES (five steps above), not
"hard spheres are weird." The falsifiability case exists, is run, and is reported with
numbers. The premise rests on nine measured claims in `experiment/RESULTS.md`, all
reproducible from this folder with stdlib Python.

**Carried into Gate 2 as binding constraints:**

1. The framework graphic lands **before** the first hard-sphere number.
2. Every claim beat names its on-screen artifact and holds it ≥2 s at the moment of
   assertion (§ production gate).
3. The 4 / 2 / 1 comparison is **side-by-side on one frame**, not three sequential cards —
   this is the specific gate item the source video leaves open.
4. No `[parameter]` placeholders survive into the beat sheet.
5. `[VERIFY]` markers stay in `FACTCHECK.md` until sourced; nothing gets filled by guessing.
