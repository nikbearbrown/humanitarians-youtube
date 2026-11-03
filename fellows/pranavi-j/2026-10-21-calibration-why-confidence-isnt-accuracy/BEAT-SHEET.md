# Beat Sheet (APPROVED — Gate P, 2026-10-21): "Calibration: Why Confidence Isn't Accuracy"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly work report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos)
**Phase:** 2 — approved for narration lock / audio generation. Fully generic worked example, no
real model/vendor benchmarked — see `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question test — "Bucket the Claims / Count the Cases / Spot the
Bluff" — for telling whether a model's stated or implied confidence in an answer actually tracks
how often that answer is right, or just sounds equally confident whether it's correct or wrong.
Teaches the test before any example, walks it through a worked example (a model whose "90%
confident" answers are only right 60% of the time — overconfident), stress-tests it against a case
where the same bucketing shows a genuinely well-calibrated result (a "90% confident" bucket that
really is right about 90% of the time), and closes on a concrete task the viewer can run today.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or benchmark any specific real model, vendor, or product. This is also a distinct
topic from this fellow's earlier videos: not "hallucination" (fabrication — whether a claim is
invented) and not "chain-of-thought faithfulness" (whether a stated reasoning trace caused the
answer) — this video is specifically about whether stated confidence corresponds to real accuracy.
The worked example is generic and hypothetical, matching the pattern used in this fellow's prior
STEM videos (describes a well-documented, generically-named class of behavior — "model
calibration" / "expected calibration error" — without claiming it as a live test of any one
system).

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Framework | All 3 tests shown together as a checklist, before any example | Framework-first, per the pattern that scored well on prior STEM videos |
| B04 Worked example | A confidence bucket's stated % and its actual accuracy % shown as two bars, side by side, with the gap visibly highlighted | Both numbers must be visible together so the mismatch is legible, not just asserted |
| B05 Falsifiability | The same bucket-and-bars layout, this time with stated and actual nearly matching | Visibly different resolution from B04 — bars that line up, not a gap |
| B06 Task | The 3 tests restated as a concrete checklist | Actionable, not just a restatement of the framework |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Calibration: Why Confidence Isn't Accuracy" + @HumanitariansAI. No
narration.

**B01. Exec summary (~0:04–0:21)**
VO: "Hi, I'm Sai Pranavi J. This video is about whether a model's confidence in its own answer
actually matches how often that answer is right, and three questions that test whether its
stated confidence means anything at all."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:21–0:36)**
VO: "Ask a model how sure it is of an answer, and it'll often tell you, in words, or even a
number. The trouble is, that confidence can sound exactly the same whether the model is right or
completely wrong. Sounding sure and being right are two different claims."
Visual: two answer cards, identically confident in tone, one marked correct, one marked wrong —
same stated confidence, opposite outcome.

**B03. Framework (~0:36–1:03)**
VO: "Here's the test, before any example: three questions. One, bucket the claims: group every
answer by how confident it sounds, and check, within each bucket, how often is it actually right?
Two, count the cases: one lucky or unlucky answer proves nothing, does the pattern hold across
many questions, not just one? Three, spot the bluff: would a genuinely hedged, uncertain answer
ever get miscounted as a confident claim? If the buckets don't match reality, it isn't calibrated,
it's just confident-sounding."
Visual: checklist card, all 3 tests shown together (Bucket the Claims / Count the Cases / Spot
the Bluff).

**B04. Worked example (~1:03–1:29)**
VO: "Here's a documented pattern. Take every answer a model gave at roughly the same stated
confidence, say, ninety percent sure, across many different questions, and bucket them together.
Count how many were actually correct. If that bucket is only right sixty percent of the time, the
model's confidence number isn't tracking its real accuracy. It's overconfident, and the gap shows
up no matter which question in the bucket you check."
Visual: a "90% confident" bucket of answer chips, a stated-confidence bar next to an
actual-accuracy bar, the gap between them highlighted.

**B05. Falsifiability case (~1:29–1:53)**
VO: "Now the case that would break this test if it were sloppy. Take a model that hedges on
genuinely hard questions and sounds confident only on the easy ones. Bucket its ninety-percent
confident answers the same way. This time, the actual accuracy in that bucket is also close to
ninety percent. Same bucket, same test, a completely different, and genuinely well-calibrated,
result."
Visual: the same bucket-and-bars layout, this time the bars nearly match — a checkmark where B04
had a gap.
*[Stress-tests the framework against a naive "any confident answer is overconfident" over-trigger.]*

**B06. Scaffolded task (~1:53–2:13)**
VO: "Here's something to try today. Ask a model several factual questions you already know the
answers to, and have it state a confidence number for each one. Group the answers by that number.
Check, in each group, what fraction were actually correct? If a ninety-percent-confident group is
only right half the time, you've just measured a real calibration gap."
Visual: the 3 tests restated as a checklist card.

**B07. Takeaway (~2:13–2:27)**
VO: "Sounding sure and being right are different claims. The only way to know if a model's
confidence means anything is to check whether it tracks real accuracy across many cases, not
just one."
Visual: statement card.

**B08. Sign-off (~2:27–2:32)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] Framework (B03) shown fully, before any example
- [ ] B04's stated-confidence and actual-accuracy bars both visible together, gap legible without
      narration alone
- [ ] Falsifiability case (B05) uses a genuinely different, well-calibrated bucket — not a
      strawman — and is visibly distinct from B04's resolution
- [ ] Scaffolded task (B06) is a concrete action, not a restatement of B03
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] Worked example is clearly generic/illustrative, not naming a real model or vendor

**Estimated runtime:** ~2:32 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-21. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
