# QUESTION

**The question:** "Claude, Deal Tracker." — does a Claude skill like
deal-tracker actually understand your deals, or is it just following a
written script? Answered using the `deal-tracker` skill's own SKILL.md job
description and trigger phrases as the concrete case.

**Mode:** redo — source is
`anthropics/financial-services/youtube/claude-liam-deal-tracker/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" reel:
metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at the investment-banking vertical plugin's
`skills/deal-tracker/SKILL.md`. 7 beats — B00 cold open, B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro — B00 was
already `ClaudeComposerAsk` REMOTION, not AI-video/pantry, so NO-GENAI/
NO-PANTRY LAW required no substitution beyond the WRITER LAW swap). This
reel keeps the question and the source's body facts, re-registers the
narration to Plain, replaces the cold open with the Brutalist Hesitant
Writer, folds the source's BVDT verdict recap into a proper carry-out beat,
restates the source's B03 "gets right / bites" framing as an
anchor-and-both-directions mechanism fact instead of a design judgment, and
closes with the Humanitarians AI skin.

**Why it earns a reel:** deal-tracker's SKILL.md is the whole program — a
plain-language instruction set with no hidden logic. Its job, verbatim from
the source: track multiple live deals with milestones, deadlines, action
items, and status updates; maintain a deal pipeline view; surface upcoming
deadlines and overdue items. It triggers on exactly six phrases: "deal
tracker", "deal status", "where are we on", "process update", "deal
pipeline", "weekly deal review". The Steps section runs linearly — Claude
reads each step in order and executes it, no branching unless a step says
so. Same input, same output, every run: that's the reliability. The limit is
symmetric with the reliability — anything outside the written spec (a
request the six trigger phrases don't cover, or a task outside milestones /
deadlines / action items / status) doesn't get a clever guess. It doesn't
get handled at all.

**Naive framing (B00, corrected on screen):** "Claude, Deal Tracker — it's a
SMART assistant that tracks my deals" → corrects "smart" to "scripted" (the
newcomer's default read of a Claude skill with a name like "deal tracker" is
that it understands deals; it doesn't reason about deals at all, it executes
a written spec).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it acts; deal-tracker's SKILL.md
  is the full instruction set, plain language, no hidden logic
- the job, verbatim: track multiple live deals with milestones, deadlines,
  action items, and status updates; maintain a pipeline view; surface
  upcoming deadlines and overdue items
- six trigger phrases, and only those six: "deal tracker", "deal status",
  "where are we on", "process update", "deal pipeline", "weekly deal
  review"
- the Steps section executes linearly, in order, no branching unless a step
  says so
- same input → same output, every run — the reliability
- the limit is the same shape as the reliability: anything outside the
  written spec doesn't get handled, it's simply outside scope — no
  fallback, no guess
