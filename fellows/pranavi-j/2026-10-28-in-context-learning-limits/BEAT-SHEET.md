# Beat Sheet (APPROVED — Gate P, 2026-10-28): "In-Context Learning: What the Prompt Can (and Can't) Teach"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly work report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos: hallucination, tokenization, lost-in-the-middle, chain-of-thought
faithfulness, calibration)
**Phase:** 2 — approved for narration lock / audio generation. Fully generic worked example, no
real model/vendor benchmarked — see `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question test — "Spot the Mapping / Shuffle the Set / Push
Past the Window" — for telling what in-context learning (a model conditioning on examples or
instructions given in its prompt at inference time, with no weight updates at all) can actually
do versus what it only looks like it's doing. Teaches the test before any example, walks it
through a worked example (a toy, invented substitution rule taught entirely by a handful of
examples in the prompt, correctly applied to a new, unseen case), stress-tests it against a case
designed to break it (the same style of task, but with the examples reordered and one mapping
deliberately flipped against what the model's pretraining would "expect" — showing the pattern
is fragile exactly where the rubric predicts it should be), and closes on a concrete audit task
the viewer can run today against any system they have access to.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or benchmark any specific real model, vendor, or product. This is also a distinct
topic from this fellow's five earlier videos: not hallucination (fabrication), not tokenization
(how text is chunked before any reasoning happens), not lost-in-the-middle (where in a long
context a fact sits), not chain-of-thought faithfulness (whether a stated reasoning trace caused
an answer), and not calibration (whether a stated confidence number tracks real accuracy). This
video is specifically about a different question: when a model is only given examples or
instructions in its prompt — nothing written to its weights — what can that prompt actually teach
it, and where does that stop working? The worked example and its stress-test case are both
generic and hypothetical, matching the pattern used in this fellow's prior STEM videos.

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Framework | All 3 tests shown together as a checklist, before any example | Framework-first, per the pattern that scored well on prior STEM videos |
| B04 Worked example | The example pairs shown in the prompt, then a new input resolving to the correctly inferred output, with a "LOCATED, NOT LEARNED" tag | The rule, the new input, and the output must all be visible together so the mechanism (pattern-completion within context) is legible, not just asserted |
| B05 Falsifiability | The same example-pairs layout, reordered + one mapping flipped, with the model's output now visibly wrong/inconsistent | Visibly different resolution from B04 — a mismatch tag, not a match |
| B06 Task | The 3 tests restated as a concrete, runnable checklist | Actionable, not just a restatement of the framework |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "In-Context Learning: What the Prompt Can (and Can't) Teach" +
@HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:21)**
VO: "Hi, I'm Sai Pranavi J. This video is about in-context learning — when a model picks up a
pattern from examples in its own prompt, with no weight updates at all — and three questions
that test what that actually can and can't do."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:21–0:40)**
VO: "Show a model a handful of examples right in its prompt, and it'll often complete a brand new
case perfectly. That looks exactly like learning something new. But nothing gets written to a
single weight. Whatever it picked up has to already be reachable from what's in that prompt and
whatever it already knew going in. Sometimes that's enough. Sometimes it only looks like enough."
Visual: a prompt window with a few example pairs, a new query resolving to a correct answer — then
an overlay posing the real question: is this learning, or is this locating?

**B03. Framework (~0:40–1:10)**
VO: "Here's the test, before any example: three questions. One, spot the mapping: can you tell,
just from the examples, what pattern they're pointing the model toward? Two, shuffle the set:
reorder the examples, change how many there are, or swap which ones you pick — does the answer
survive? If it flips, that's fragile pattern-matching, not a stable rule. Three, push past the
window: does the task need more than fits in the prompt, or a capability the model never had
to begin with? If so, no number of examples will produce it. If the pattern only holds for one
ordering, one count, or something already latent — that's the boundary, not a bug."
Visual: checklist card, all 3 tests shown together (Spot the Mapping / Shuffle the Set / Push
Past the Window).

**B04. Worked example (~1:10–1:36)**
VO: "Here's how it actually works. Put a made-up rule entirely inside the prompt: a handful of
examples, each one an input and the output that rule produces, no explanation given. Then hand it
a brand-new input the rule was never shown directly. A model can often produce the right output
anyway — not because it learned a new capability, but because it located a pattern its own
architecture is already built to complete, using nothing but what's sitting in the context
window right now."
Visual: 4 example pairs stacking into a prompt panel, a new input arriving, the correct output
resolving, tagged "LOCATED, NOT LEARNED."

**B05. Falsifiability case (~1:36–2:02)**
VO: "Now the case that would break this test if it were sloppy. Take the exact same style of
task. Reorder the same examples, and flip just one of the mappings so it goes against what the
model's own training would expect. Ask the identical new question. This time the output gets
inconsistent, or quietly reverts to the more familiar pattern instead of the one actually
demonstrated. Same task shape, same number of examples, a completely different, and much less
reliable, result."
Visual: the same example-panel layout, reordered, one mapping visibly flipped, the output tagged
"MISMATCH" instead of a clean resolution.
*[Stress-tests the framework against a naive "a few examples always teach the model the rule"
over-trigger.]*

**B06. Scaffolded task (~2:02–2:24)**
VO: "Here's something to try today, on any system you have access to. Invent a small rule with no
real-world meaning, so you know any correct answer has to come from the prompt itself. Give it
four or five examples, then test it on new inputs it hasn't seen. Now shuffle the same examples
and test the same inputs again. Then flip one example's mapping and test once more. If the answers
only hold for the original order, you've just found the edge of what that prompt can actually
teach."
Visual: the 3 tests restated as a checklist card.

**B07. Takeaway (~2:24–2:38)**
VO: "In-context learning is powerful pattern-location, not instant new learning. It's bounded by
what the model already had latent going in, and by what actually fits, in a stable way, inside
the prompt."
Visual: statement card.

**B08. Sign-off (~2:38–2:43)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [x] Framework (B03) shown fully, before any example
- [x] B04's example pairs, new input, and resolved output all visible together, mechanism
      legible without narration alone
- [x] Falsifiability case (B05) uses a genuinely different, order-shuffled + flipped-mapping
      case — not a strawman — and is visibly distinct from B04's clean resolution
- [x] Scaffolded task (B06) is a concrete, runnable action, not a restatement of B03
- [x] Silent title card present; brand/fellow sign-off card present
- [x] Worked example and stress-test case are clearly generic/illustrative, not naming a real
      model, vendor, or benchmark

**Runtime:** 173.375s (2:53.4) — measured from Kokoro audio + silent B00, confirmed identical on
both final masters via `ffprobe` (not the ~2:43 draft estimate above, per the toolkit's
audio-first rule). **Final render confirmed:** landscape 3840x2160 and vertical 2160x3840, both
173.375s, both GATE V clean (0 BLOCKER / 0 MAJOR) on the true final candidates — see
`BUILD-LOG.md` for the full build/bug history and `README.md` for the production-state summary.

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-28. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
