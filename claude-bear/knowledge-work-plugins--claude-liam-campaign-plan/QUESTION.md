# QUESTION

**The question:** "Claude, Campaign Plan." — when you ask Claude for a
marketing campaign plan, is it inventing a bespoke strategy from its own
creative judgment, or is it filling in a fixed spec? Answered using the
`campaign-plan` skill (an Anthropic marketing skill) as the concrete case.

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-campaign-plan/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at a
`.../marketing/skills/campaign-plan/SKILL.md` on Bear's other machine — not
present in this tree, so this build reads the source beat_sheet's own
narration text, which already carries the skill's task and trigger language
verbatim, as the record of the source facts). 7 beats — B00 cold open
(`ClaudeComposerAsk`, already REMOTION, not AI-video/pantry, so NO-GENAI/
NO-PANTRY LAW required no substitution beyond the WRITER LAW swap), B01
anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT
outro. This build keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B03 "gets right / bites"
framing as a both-directions mechanism fact instead of a design judgment,
and closes with the Humanitarians AI skin.

**Why it earns a reel:** `campaign-plan` is a SKILL.md file Claude reads
before it acts — the file is the instruction set, not marketing expertise
baked into the model. Its job, verbatim from the source: "Generate a full
campaign brief with objectives, audience, messaging, channel strategy,
content calendar, and success metrics." It fires only on matching request
language: planning a product launch, a lead-gen push, or an awareness
campaign; needing a week-by-week content calendar with dependencies; or
translating a marketing goal into a structured, executable plan. Once
triggered, execution is a linear pipeline with no branching unless a step
says so: read `SKILL.md`, execute each step in order, return the result.
The output shape is fixed — the same six pieces, every time — which is what
a written spec buys over an improvised strategist. The corresponding limit:
anything outside what the file specifies isn't covered, and the newcomer's
obvious alternative guess — that Claude is exercising creative marketing
judgment, inventing a bespoke strategy per product — is wrong precisely
because the deliverable's shape never changes with the product.

**Naive framing (B00, corrected on screen):** "You ask for a campaign plan.
Claude must invent the whole strategy, right?" → corrects "invent" to
"assemble" (the newcomer's default assumption is that Claude is being
creative/strategic from scratch; the correction states the real mechanism —
Claude assembles a fixed set of pieces from a spec, not free invention).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; `campaign-plan`'s
  `SKILL.md` is the whole instruction set — one file, the file is the
  program
- the task, verbatim: generate a full campaign brief with objectives,
  audience, messaging, channel strategy, content calendar, and success
  metrics — always those six pieces
- the skill fires only on matching trigger language: planning a product
  launch, a lead-gen push, or an awareness campaign; needing a week-by-week
  content calendar with dependencies; or translating a marketing goal into
  a structured, executable plan
- execution is linear: read `SKILL.md` → execute each step in order →
  return the result — no branching unless a step says so
- the payoff of a written spec is repeatability: the same request run again
  later walks the same steps and returns the same six-piece shape
- the limit is exact: anything outside what the file specifies isn't
  covered — a request that doesn't match a trigger never starts the
  pipeline, and the question falls back to whatever Claude would say
  without the skill
- source's Your Turn: paste the campaign-plan trigger phrase (a campaign
  brief request) and ask Claude to walk through its steps before running
  them, watching whether it names the six pieces before writing them
