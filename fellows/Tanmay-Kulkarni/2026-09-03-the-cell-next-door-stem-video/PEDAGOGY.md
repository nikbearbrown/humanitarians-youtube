# PEDAGOGY — *The Cell Next Door* · Week 21 topic video

**Subtitle:** the same mistake, three sizes
**Series / channel:** Claude for Science · Humanitarians AI · `am_onyx` (Onyx), Pragmatist register
**Presenter:** Tanmay Kulkarni, in for Humanitarians AI
**Builder:** `deep-explainer` · runtime 8:30 across 18 beats

> **Gate P verdict: PASS — Tanmay Kulkarni, 2026-09-03.** Signed after reviewing the
> narration and all slates at 4K; **listen-through completed and approved on the compiled
> cut, same date.**
>
> Recorded as the creator gave it: **a single blanket pass with named revisions**, not 18
> individual verdicts. Filling in per-beat notes nobody dictated would be inventing a record,
> which is the defect this whole project is about.
>
> **AMENDED — 2026-09-03, after signature.** The signed cut was 16 beats; it is now **18**.
> Ten beats changed after the signature and are marked *(amended)* in the table below. Every
> one was creator-requested and reviewed at frame level — the PROOF punch list, the
> framework-early chain on B02, the two splits out of B05, and the B15 sign-off. **None was
> re-read aloud.**
>
> **CLOSED — 2026-09-03.** The listen-through against generated audio is complete and
> approved by the creator. That was the outstanding item, and it covered the ten amended
> beats with the actual voice saying the actual words — a stronger check than the page pass
> it replaced. **Gate P is fully discharged for the 18-beat cut.**
>
> The inherited source variant's `PEDAGOGY.md` is 99 bytes and reads *"NBB wrapper reuses
> locked body pedagogy. VERDICT: PASS."* That is the anti-pattern: a pass with nothing under
> it. Rows first, verdict second.

---

## The teachable claim

A survival number in a cancer-immunotherapy video was wrong. Its own fact-check caught it and
supplied a correction that was **also wrong**. The real five-year figure is 38.7%; the
correction quoted the first-line subgroup; and the same trial reports **38.7 percent** and
**38.7 months** a few lines apart for different populations.

That is not a story about carelessness. It is a story about a specific, repeatable reading
error — **taking the number next to the number you want** — and about the fact that it does
not stay small. The same move appears in a field's favourite statistic (r = 0.74 quoted as
"mutation count predicts response," which leaves 45% unexplained), in a trial's own report of
itself ("a doubling," against a 50% bar it set and missed), and finally in this film.

## The framework the viewer walks away with — WHICH LINK MOVED?

Immunotherapy releases a brake on a T cell that is already attacking. For that to do
anything, a six-link chain must be intact:

```
mutations → antigens → priming → trafficking → infiltration → killing
```

The drug acts only on the last link. So any strategy for "warming up" a cold tumour is a claim
to have repaired one specific link, and it is graded with **two questions, in order**:

1. **Which link did this target — and did that link move?** Is there a measurement, in human
   tissue, not a mouse?
2. **Did the next link move?**

| Agent | Targeted link | Did it move? | Did the next one? | Broke at |
|---|---|---|---|---|
| STING agonist (ADU-S100) | priming (3) | Yes — systemically | **No** — biopsies showed no infiltration change | trafficking (4) |
| CXCR4 blocker (BL-8040) | trafficking (4) | Yes — measured in tissue | **No** — ORR 3.4% | killing (6) |

Two agents, two different broken links, one identical clinical result. **"Cold tumour" is a
symptom, not a diagnosis** — which is why a fix for one cause does nothing for the other.

### Why this framework is real and not reverse-engineered

PROOF Behavioral Rule 1 forbids calling a framework real if it maps one-per-example. Three
things defend it:

- **It is derived, not recited.** The two questions do not appear until **B10, ~70% in**, and
  they arrive *because* B08 and B09 produce opposite mechanistic findings with the same
  outcome. The viewer holds the contradiction before the question.
- **It has a falsifiability case, on screen.** B13: the hot/cold/excluded taxonomy the chain
  depends on **is not a property of a tumour type at all**. Pancreatic tumours split into
  myeloid-enriched and adaptive-enriched, with divergent survival (C15). Asking "is pancreatic
  cancer cold?" is the wrong shape of question — and the film has been asking it.
- **It survives being turned on the film.** Act III applies it to our own work and it finds
  three things (below).

### The transferable skill

`B14` hands over the two questions as a worked example on a real readout, with a stated
pass/fail: **you pass if you can name the link and point at the measurement; you fail if the
report gives you the clinical endpoint or the mechanism and never both.** Every number in the
film is reproducible with `python3 experiment/tmb_orr_audit.py` — stdlib only, ~2 s.

## What the film convicts itself of

Act III is not a confession beat in the usual slot; it is the destination the escalation points
at, and it escalates in kind as well as proximity:

| Beat | Kind of error | What we got wrong |
|---|---|---|
| B11 | **arithmetic** | Said 45% of variance is unexplained by mutation count — the naive 1−r². Modelling small-trial attenuation puts it nearer **40%**. Used twice before being corrected. |
| B12 | **selective** | Reported that the radiation trial missed its bar, and omitted that the largest benefit was in PD-L1-negative tumours — a point *for* the conversion hypothesis. Half a trial, chosen because it fitted. |
| B13 | **structural** | Called pancreatic cancer "an excluded tumour" as though that were a fact about pancreatic cancer. A category error, invisible from inside. |

## Structure

**CONCENTRIC** — the same mistake at three scales, each closer to the narrator. Not the
lab-notebook shape of W20 topic, not the A/A′ card of W20 work, not the cross-section of W19
topic. First draft scrapped for repeating two of those at once; see
[`STRUCTURE-DIFF.md`](STRUCTURE-DIFF.md).

Two structural rules are **enforced by the build**, not trusted: no framework language before
B10, and B02 must not announce the shape.

---

## Beat-by-beat review — sign here

Read each beat **aloud**, at pace, against its slate. Verdict: `PASS` / `FIX` / `CUT`. If
`FIX`, say what you heard — not what you would write.

All beats **PASS** under the blanket sign-off. The one revision is recorded against B15.

| Beat | Act | Est. | Tone as written | Words | Claims | Verdict | Note |
|---|---|---|---|---|---|---|---|
| B00 | GREETING | 1 s | neutral ident | 3 | — | PASS |  |
| B01 | COLD OPEN | 32 s | confident, then not | 107 | C1 | PASS |  |
| B02 | INTRO | 16 s | plain, direct, unpromising | 53 | — | PASS *(amended)* | slate now carries the greyed six-link chain (framework-early, PROOF 12/12) |
| B03 | THE TABLE | 39 s | procedural, unhurried | 129 | C1 C23 | PASS |  |
| B04 | IT DIDN'T NEED HELP | 27 s | level, slightly warm | 89 | C1 C24 | PASS *(amended)* | PROOF punch list |
| B05 | THE SAME MOVE, ONE SIZE UP | 29 s | brisk; the pattern starting to show | 95 | C12 | PASS *(amended)* | split — narration shortened |
| B05B | WHERE THE FORTY-FIVE PERCENT LIVES | 17 s | diagnostic | 55 | C2 C3 C4 C17 C18 | PASS *(amended)* | NEW — residuals split out of B05 |
| B05C | INSIDE ONE CANCER | 16 s | quieter; the cleanest evidence in the act | 53 | C19 | PASS *(amended)* | NEW — Merkel counterexample split out of B05B |
| B06 | AND AGAIN, IN A TRIAL'S OWN REPORT | 41 s | dry | 137 | C14 | PASS *(amended)* | PROOF punch list |
| B07 | THE CHAIN | 34 s | instructive; gear change | 114 | C5 C6 C7 C22 | PASS *(amended)* | PROOF punch list |
| B08 | THE FIRST DRUG | 40 s | even; let the finding do the work | 134 | C11 C21 | PASS |  |
| B09 | THE SECOND DRUG | 31 s | even, building | 104 | C10 | PASS |  |
| B10 | THE COLLISION | 42 s | the payoff; slow right down | 138 | C10 C11 C22 | PASS *(amended)* | PROOF punch list |
| B11 | OUR TURN | 32 s | flat, unsentimental | 105 | C12 C20 | PASS |  |
| B12 | THE HALF I GAVE YOU | 33 s | caught out; no theatrics | 108 | C14 | PASS |  |
| B13 | THE SENTENCE I KEPT SAYING | 44 s | the retraction; steady, not dramatic | 146 | C15 | PASS |  |
| B14 | YOUR TURN | 33 s | handover, concrete | 109 | — | PASS *(amended)* | PROOF punch list |
| B15 | OUTRO | 4 s | ident | 13 | — | PASS *(amended)* | creator revision — presenter credit, URL cut, sign-off added |

### The tone arc, to check against your ear

confident → *a small doubt* → procedural → level → brisk → dry → instructive → even → even,
building → **the payoff** → flat → caught out → the retraction → handover → close

The peak is **B10**. B11–B13 must not compete with it; they should feel like the air going out
of the room, not a second climax.

### Questions the read has to answer — a machine cannot

1. **Do the two 38.7s land in B03?** They are distinguished only by the final word — *percent*
   vs *months*. If the ear cannot separate them, the film's central beat fails and the fix is
   the frame or the phrasing, not the fact.
2. **Does B10 feel derived or announced?** The framework is supposed to arrive as a
   consequence of the contradiction in B08/B09. If it lands as a rubric being introduced, the
   structure has failed and B08/B09 need re-pointing.
3. **Does B13's retraction read as honest or as performance?** Three self-corrections in a row
   risk sounding pleased with themselves.
4. **Is B03 (~43 s, four dense numbers) holdable, or does it need air?**
5. **Confirm 13 pronunciations by ear** — full table in [`GATE-P.md`](GATE-P.md). The
   antibody names (*pembrolizumab* ×4, *ipilimumab* ×2) are the likeliest failure in the film;
   *Yarchoan* is new as of the naming decision below.

Two earlier questions are **closed**: B05 names Yarchoan aloud (a film about receipts should
say whose receipt it is), and B13's "ladder" stays, paying off B02's "it doesn't stay that
size." Both decided by the creator, 2026-09-03.

---

## Verdict

**Gate P: ✅ PASSED.**

Signed: **Tanmay Kulkarni**  ·  Date: **2026-09-03**

### Revisions requested, and applied

| # | Beat | Requested | Applied in |
|---|---|---|---|
| 1 | B15 | Drop `nikbearbrown.com`. Replace the doubled brand mention with a presenter credit — `Tanmay Kulkarni · @HumanitariansAI`. Add the sign-off to the narration after the title. | `SCRIPT.md` narration; `scenes.py` B15 slate; `build_beat_sheet.py` `ClaudeTitleOutro` props (which still carried the URL and would have re-surfaced it in the real Remotion outro) |

Consequential change made while applying it, flagged rather than smuggled: the spoken
*"sources in the description, and the numbers are all reproducible"* was **cut**, because a
line after "signing off" undercuts the sign-off. The claim is not lost — B14 hands over the
script and the run command aloud, and the line stays legible on the B15 slate.

### Still outstanding after the pass — audio-time checks only

These could not be settled by a read of the page or the frames, and are carried to audio
generation rather than being marked closed:

- **13 pronunciations** (`GATE-P.md`). The antibody names — *pembrolizumab* ×4,
  *ipilimumab* ×2 — are the likeliest failure in the film. If one mangles, the fix goes in the
  **narration spelling**, never in hand-edited audio.
- **Measured durations** replace every estimate and become the master clock.

### Audio generation: UNBLOCKED

The source project generated audio without ever running this gate — which is how a fact-check
that had already caught the error shipped it anyway. This one ran.
