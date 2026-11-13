# Beat Sheet (APPROVED — Gate P, 2026-11-13): "Context Window Limits: The Budget That Doesn't Grow"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly project-update report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos: hallucination, tokenization, lost-in-the-middle, chain-of-thought
faithfulness, calibration, in-context learning limits, Goodhart's Law / proxy metrics)
**Phase:** 2 — approved for narration lock / audio generation. Fully generic worked example, no
real model/vendor named or benchmarked — see `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question test — "Count the Tokens / Share the Pool / Watch
the Edge" — for reasoning about a model's context window: a hard, fixed-size budget, measured in
tokens (not characters or words), shared by everything that goes into a prompt — instructions,
retrieved documents, conversation history, and the model's own output budget — all at once, not
in separate pools. Teaches the test before any example, walks it through a worked example (a
generic, invented-for-teaching scenario: a long document, a growing conversation, and a fixed
instruction block all competing for the same illustrative token budget, with the oldest
conversation turns silently dropped to make room), stress-tests it against a falsifiability case
designed to show the rubric isn't "going over the limit always causes a silent problem" (the
identical scenario and the identical overflow, but this time the system checks the total before
answering and refuses outright with a clear, visible error instead of dropping anything), and
closes on a concrete audit task the viewer can run today against any system they already use that
has a length or size limit.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or benchmark any specific real model, vendor, or product, and does not cite any
specific context-window size as if it were a universal fact (context windows vary enormously
across systems and change over time — this video describes the concept generically: "a few
thousand tokens" vs. "hundreds of thousands," never a specific current number for any named
system). This is also a distinct topic from this fellow's eight earlier videos: not hallucination
(fabrication), not tokenization (how text is chunked before any reasoning happens — this video
assumes tokenization already happened and is about what happens once the token count from that
process exceeds a fixed ceiling), not lost-in-the-middle (position of a fact within a context that
already fits — this video is about what happens when content does NOT fit at all), not
chain-of-thought faithfulness (whether a stated reasoning trace caused an answer), not calibration
(whether a stated confidence number tracks real accuracy), not in-context learning limits (what a
prompt can teach as a *mechanism* — pattern-completion within a prompt, not new learned
capability), and not Goodhart's Law (proxy metrics diverging from their real target under
incentive pressure). In-context learning limits and context window limits are closely related and
easy to conflate: in-context learning asks what a prompt can teach *within* the window; this video
asks what happens once the window itself runs out — a capacity-and-overflow-behavior question, not
a mechanism question, and this one-sentence distinction is the only place this video references
that topic. The worked example and its falsifiability case are both generic and hypothetical,
matching the pattern used in this fellow's prior STEM videos.

**Real-world tie-in (brief, generic, per the house rule):** this week's companion project-update
video separately covers a real bug where a UI had no cap matching a backend's hard limit on how
many items a single request could carry — a live instance of exactly the general phenomenon this
video explains: a hard capacity limit that bites you if nothing on the sending side respects what
the receiving side can actually hold, whether that's a context window or an API request size. That
specific incident is not named or described anywhere in this video; B06 carries one brief, fully
generic sentence acknowledging the pattern is not unique to language models. See `FACTCHECK.md`.

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format, opens with the required "Hi, I'm Sai Pranavi J., this video is about..." line |
| B03 Framework | All 3 tests shown together as a checklist, before any example | Framework-first, per the pattern that scored well on prior STEM videos |
| B04 Worked example | The fixed budget, what's competing for it (instructions, document, history), and what gets silently dropped, all shown together, tagged "TRUNCATED — SILENTLY" | The budget, the competing consumers, and the thing that quietly disappears must all be visible together so the mechanism is legible, not just asserted |
| B05 Falsifiability | The identical panel, numbers, and overflow, with the system now checking the total before answering and refusing outright, tagged "CAUGHT IMMEDIATELY" | Visibly different resolution from B04 — an explicit-error tag, not a silent-drop tag |
| B06 Task | The 3 tests restated as a concrete, runnable checklist | Actionable, not just a restatement of the framework |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Context Window Limits: The Budget That Doesn't Grow" + @HumanitariansAI.
No narration.

**B01. Exec summary (~0:04–0:18)**
VO: "Hi, I'm Sai Pranavi J. This video is about context window limits — the fixed, hard-capped
budget every prompt has to fit inside, measured in tokens, not words or characters — and three
questions for telling what actually happens when you go over it."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:18–0:38)**
VO: "Every prompt you send shares one fixed pool — the instructions, any document you paste in,
the whole conversation so far, even the room left over for the model's own answer. That pool
doesn't grow. It's measured in tokens, rough chunks of text, not characters, not words, so
counting by eye is already a guess. Fill it past the edge, and something has to give."
Visual: a generic "CONTEXT WINDOW (FIXED BUDGET)" panel filling up row by row, then an overlay
posing the real question: full — did it tell you?

**B03. Framework (~0:38–1:07)**
VO: "Here's the test, before any example: three questions. One, count the tokens: is this budget
actually measured in tokens, the model's own unit, not the characters or words you'd eyeball it
with? Two, share the pool: everything competing for room — the system instructions, any retrieved
documents, the conversation history, and the model's own output — draws from that one fixed
budget, not separate ones. Three, watch the edge: when the total goes over, does the system refuse
outright, or does it quietly drop something and keep going? A budget you can't see filling up is a
budget you can't manage."
Visual: checklist card, all 3 tests shown together (Count the Tokens / Share the Pool / Watch the
Edge).

**B04. Worked example (~1:07–1:35)**
VO: "Here's how it actually works. Picture a context window sized, for this illustration, at one
thousand tokens. System instructions take a fixed hundred and fifty. A long document you've pasted
in takes seven hundred more. That already leaves only a sliver of room for the conversation so
far, and for the model's own reply. Keep the conversation going, and that history keeps growing,
past the room that's actually left. One common way systems handle this: they quietly drop the
oldest turns to make room, say nothing about it, and answer anyway."
Visual: the fixed budget, the instructions and document rows, and the growing conversation history
shown together inside one panel — history crossing into "OVER BUDGET," then the oldest turns
fading out — tagged "TRUNCATED — SILENTLY."

**B05. Falsifiability case (~1:35–2:02)**
VO: "Now the case that would break this test if it were sloppy: the exact same budget, the same
document, the same growing conversation. But this system checks the total before it answers, and
when that total would go over, it refuses outright — one clear error, no answer, nothing quietly
dropped. The limit got hit just as hard as before. The difference was never whether you went over,
it's whether the system told you."
Visual: the identical panel, numbers, and overflow as B04, with an explicit on-screen error message
replacing a silent drop, tagged "CAUGHT IMMEDIATELY" instead of a truncation tag.
*[Stress-tests the framework against a naive "going over the limit always causes a silent problem"
over-trigger — the only variable changed from B04 is whether the system checks the total before
answering.]*

**B06. Scaffolded task (~2:02–2:30)**
VO: "Here's something to try today. Pick any system you already use that has a length or size
limit — a chat app, an upload form, an API call. Deliberately go a little over it, on purpose.
Watch what happens: does it refuse clearly, or does it just keep going? If something got silently
dropped, figure out exactly what — the oldest message, the middle of your document, the end of
your prompt. This isn't unique to language models either — it happens anywhere a sender doesn't
know what the receiver can actually hold."
Visual: the 3 tests restated as a checklist card.

**B07. Takeaway (~2:30–2:47)**
VO: "A context window isn't elastic. It's a fixed budget, shared by everything you put in and
everything you ask for back. Going over it was never really the question. Whether the system
tells you when you do — that's the one that matters."
Visual: statement card.

**B08. Sign-off (~2:47–2:49)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J.

---

## Production Gate Self-Check (pre-review)

- [x] Framework (B03) shown fully, before any example
- [x] B04's fixed budget, its competing consumers, and what silently gets dropped all visible
      together, mechanism legible without narration alone
- [x] Falsifiability case (B05) uses a genuinely different, explicit-error case — not a strawman —
      and is visibly distinct from B04's silent-truncation resolution
- [x] Scaffolded task (B06) is a concrete, runnable action, not a restatement of B03
- [x] Silent title card present; brand/fellow sign-off card present
- [x] Worked example and stress-test case are clearly generic/illustrative, not naming a real
      model, vendor, or benchmark; no specific real context-window size claimed as universal
- [x] Real-world tie-in (this week's companion project-update bug) acknowledged only in one brief,
      fully generic sentence (B06) — no specific project/company/bug named
- [x] One-sentence distinction from in-context learning limits included (Premise section), not
      re-explained as a mechanism

**Runtime:** 177.54s raw (Kokoro audio + silent B00, using B00's actual pipeline-used 4.0s — see
`FRICTIONAL.md` for a real, harmless duplicate-JSON-key bug that silently substituted this value
for the originally-intended 4.128s measured silent-track duration; B00 is silent and the visual
content is unaffected) — **Final render confirmed:** landscape 3840x2160 and vertical 2160x3840,
both 177.625s (frame-rounded), both GATE V clean (0 BLOCKER / 0 MAJOR) on the true final
candidates — see `BUILD-LOG.md` for the full build/bug history and `README.md` for the
production-state summary.

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-11-13. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
