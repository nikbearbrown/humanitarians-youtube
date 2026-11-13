# Weekly STEM Video: Context Window Limits — The Budget That Doesn't Grow

**Fellow:** Sai Pranavi J.
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering
work. Describes a well-established, generic architectural fact — a transformer-based language
model's context window is a fixed, hard-capped budget, measured in tokens, shared by everything in
a single request — qualitatively. No real model, vendor, product, or benchmark is named or
cited, and no specific context-window size is claimed as a universal, current fact for any named
system. The worked example (B04, an invented, illustrative 1,000-token budget) and its
falsifiability case (B05, the identical scenario with an explicit-error system instead) are both
fully generic/hypothetical illustrations. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): `deliverables/landscape/ContextWindowLimits_SaiPranaviJ.mp4`
- Vertical (4K 9:16): `deliverables/vertical/ContextWindowLimits_SaiPranaviJ.mp4`

This video teaches a reusable 3-question test — **Count the Tokens / Share the Pool / Watch the
Edge** — for reasoning about a model's context window: a fixed token budget (not a character or
word budget), shared all at once by system instructions, retrieved/pasted documents, conversation
history, and the model's own output allowance. The framework is taught in full before any example,
walked through a worked example (a generic, invented 1,000-token budget already mostly committed
to instructions and a pasted document, with a growing conversation quietly losing its oldest turns
once it crosses the remaining room), stress-tested against a falsifiability case where the
identical budget, numbers, and overflow do NOT produce a silent problem because the system checks
the total before answering and refuses outright, and closed with a concrete audit task the viewer
can run today against any system they already use that has a length or size limit.

## What this covers (and what it deliberately leaves out)

Covered: a hook showing a generic context-window panel filling row by row while posing the video's
real question (B02); all 3 tests shown together, before any example (B03); a worked example (B04)
where a fixed, illustrative token budget is already mostly spent on instructions and a document,
and a growing conversation's oldest turns are silently dropped once the remaining room runs out,
tagged "TRUNCATED — SILENTLY"; a falsifiability case (B05) where the identical budget, numbers, and
overflow are paired with a system that checks the running total before answering, catching the
same overflow immediately instead of hiding it, tagged "CAUGHT IMMEDIATELY"; a concrete audit task
distinct from the framework card (B06); and a closing takeaway.

Deliberately left out: this is not a report of any real system's actual context-window size or
behavior, and does not name or evaluate any specific real model, vendor, or product (fixed-size
context windows and their two broad overflow patterns — explicit rejection vs. implicit truncation
— are well-documented, generic architectural facts, not a single paper or vendor-specific claim).
This is also a distinct topic from eight adjacent, already-covered videos in this series: **not
hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`, fabrication), **not
tokenization** (`2026-09-29-tokenization-why-ai-cant-count-its-own-letters`, how text is chunked
before any reasoning happens — this video assumes that already happened and is about what happens
once the resulting count exceeds a fixed ceiling), **not lost-in-the-middle**
(`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`, position within content that DOES
fit), **not chain-of-thought faithfulness**
(`2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`, whether a stated reasoning
trace caused the answer), **not calibration**
(`2026-10-21-calibration-why-confidence-isnt-accuracy`, whether a stated confidence number tracks
accuracy for a single prediction), **not in-context learning limits**
(`2026-10-28-in-context-learning-limits`, what a prompt alone can teach a model with no weight
updates — a mechanism question; this video is about the capacity ceiling itself and what happens
at and past it, a distinct capacity-and-overflow question), and **not Goodhart's Law / proxy
metrics** (`2026-11-04-goodharts-law-proxy-metrics`, a tracked number diverging from its real
target under incentive pressure). This video asks a different question: how big is the budget
every request shares, and what actually happens — visibly or invisibly — once it's exceeded? No
specific context-window size is fabricated or claimed as a real system's measurement anywhere — the
1,000-token budget and its component counts are illustrative.

This week's companion project-update video separately covers a real bug where a UI had no cap
matching a backend's hard limit on how many items a single request could carry — a live instance
of exactly the general phenomenon this STEM video explains. Per the house rule, that specific
incident is not named or described anywhere in this video; B06 carries one brief, fully generic
sentence acknowledging the pattern is not unique to language models.

## Illustrative content chosen for B02 / B04 / B05

**B02 (hook):** a generic "CONTEXT WINDOW (FIXED BUDGET)" panel filling with rows (INSTRUCTIONS,
DOCUMENT, HISTORY), tagged "MEASURED IN: TOKENS" / "NOT CHARACTERS" / "NOT WORDS EITHER," then an
overlay asking the real question the rest of the video answers: full — did it tell you? No model,
vendor, or system is named.

**B04 (worked example):** an invented, illustrative 1,000-token budget — chosen as a clean, round
number for teaching clarity, not a claim about any real system's actual window size — with a fixed
850 tokens already committed to system instructions plus a pasted-in document, leaving 150 tokens
of room. A growing conversation history pushes that count to 310 tokens, past the room that's
actually left; the oldest turns are silently dropped to make room, with nothing surfaced about it.
Tagged "TRUNCATED — SILENTLY." Chosen because implicit/"sliding window" truncation of the oldest
conversation history is a broadly-documented implementation pattern across systems that wrap or
serve language models, with no real company named.

**B05 (falsifiability/stress-test case):** the identical budget, the identical before/after
numbers, and the identical overflow as B04 — the ONLY change is that this system checks the
running total before answering ("CHECKED BEFORE ANSWERING"). The same overflow happens, but it's
caught immediately with an explicit error instead of a silent drop, tagged "CAUGHT IMMEDIATELY."
Chosen to give B04's silent truncation a real, visibly distinct counterpart — stress-testing the
framework against a naive "going over the limit always causes a silent problem" over-trigger, per
`FACTCHECK.md`.

## Production state

- Plan: **approved (Gate P)** — signed 2026-11-13
- Fact-check gate: **resolved** — see `FACTCHECK.md`; kept fully generic, no real model/vendor
  named, no context-window size claimed as universal
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-11-13
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `ContextWindowLimits_SaiPranaviJ.mp4`, **3840x2160, 24fps,
  h264/aac, 177.625s**. GATE V on the true clean master (verified directly, not the review slate):
  **0 BLOCKER, 0 MAJOR.**
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `ContextWindowLimits_SaiPranaviJ.mp4`, **2160x3840, 24fps, h264/aac, 177.625s** — identical
  runtime to the landscape master, all 9 beats kept, no drops, no duration cap. GATE V on the true
  clean master (verified directly, not the review slate): **0 BLOCKER, 0 MAJOR.**
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires
  fellow/PM sign-off per `brutalist/docs/FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective
2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate
`deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K
2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every
beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review confirming the mechanism, worked example, and
  falsifiability/stress-test case are generic/qualitative
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no
  pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous build log of what resisted and what Claude contributed
