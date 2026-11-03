# SCRIPT.md — PPTX (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-pptx` (Teardown, examining Anthropic's `pptx` skill) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
At first this reads as needing to learn python-pptx just to build a slide
deck. Cross that out — the real question is whether you can skip it
entirely. Liam, in for Bear.

## Act I — Stakes: the three paths, and the anchor ask

**NB01 — three paths, one skill** (source B01)
The PPTX skill routes across three paths depending on the task: markitdown
to read or analyze a deck, the editing workflow to rework an existing
template, and pptxgenjs to create one from scratch.

**NB02 — the ask, planted** (ANCHOR PLANTED)
Picture this ask: a five-slide investor pitch deck for a climate-tech
startup that makes carbon-capture hardware. Bold design, specific to the
topic. Hold onto that request — we'll come back to it.

## Act II — The wrong guess, and the case that breaks it

**NB03 — "one tool, both jobs?"** (WRONG GUESS)
So the natural guess: since pptxgenjs can build a deck from scratch, it can
also edit an existing template — one tool covers both jobs.

**NB04 — it's slide XML, not a library** (BREAK)
But editing a template means analyzing its thumbnails, unpacking the slide
XML, editing that directly, then repacking. pptxgenjs never touches an
existing file.

## Act III — What it actually does

**NB05 — designed for this deck, not any deck** (source B02)
Design is mandatory, and the first rule is specificity: if your color
choices would still work in some other deck, they aren't specific enough.
One color should dominate sixty to seventy percent of the visual weight,
with a sharp accent.

**NB06 — one motif, dark-light sandwich** (source B02)
Commit to one visual motif and carry it across every slide. Then structure
the deck like a sandwich: dark slides for the title and the close, light
slides in between for content.

**NB07 — never an accent line under a title** (source B02)
Never default to Arial — pick a header font with actual personality. And
never put an accent line under a title. That one detail is a known
hallmark of AI-generated slides.

**NB08 — two-stage QA, assume problems** (source B01/B02)
QA runs in two stages: content QA with markitdown plus a grep for
placeholder text, then visual QA — render every slide to an image and hand
it to a subagent with fresh eyes. Assume there are problems; the first
render is almost never correct.

## Act IV — The anchor returns

**NB09 — the same deck, now shipped right** (ANCHOR PAYOFF)
Back to that pitch deck: a palette built for carbon-capture hardware, not
recycled from another deck, one motif carried through, the dark-light
sandwich in place, no accent line under any title — and it doesn't ship
until a subagent has actually looked at the rendered slides.

## Act V — Both directions

**NB10 — what the QA pass catches** (DIRECTION A)
When it works, it works well: the subagent visual pass catches slides that
read fine in code but are visibly broken once rendered — the concrete
design rules replace vague guidance with real, checkable choices.

**NB11 — known failures, not all failures** (DIRECTION B — ONE FLAG)
One flag: needing npm for pptxgenjs, hand-edited XML on the template path,
and design rules that can clash with a client's brand guidelines are the
documented failure modes here. Nothing forces a check for one that isn't
on this list.

## Close

**BCRY — carry-out**
Making slides with Claude means picking the right tool for the job, not
writing one script. And no render counts as done until a subagent has
actually looked at it.

**BHTF — your turn**
Your turn. Paste this into Claude: create a 5-slide investor pitch deck
for a climate tech startup that makes carbon-capture hardware. Bold
design — pick a palette that feels specific to this topic, commit to one
visual motif, use the dark-light sandwich structure. Use the PPTX skill.
Then watch: does it read pptxgenjs.md before writing any code? And after
it generates, does it run visual QA — render the slides and inspect them
with a subagent — before calling it done? Check the slides themselves too:
is there an accent line under any title? If so, the design rules were
skipped.

**BOUT — outro**
PPTX. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| 1 stakes | NB01, NB02 | the skill's three paths, then the anchor ask planted |
| 2 wrong guess | NB03 (guess), NB04 (break) | "one tool, both jobs" broken by the slide-XML edit path |
| 3 mechanism | NB05, NB06, NB07, NB08 | color specificity, motif/sandwich, typography + accent-line rule, two-stage QA |
| 4 anchor | NB02 (plant) -> NB09 (payoff) | same pitch-deck ask, shipped correctly |
| 5 both directions | NB10, NB11 | holds: subagent QA catches renders that read fine but look broken. flips: npm/XML/brand-guideline gaps are the documented failures — an undocumented one can still slip through (flagged as this video's one inference) |
| 6 carry-out | BCRY | "the right tool, not one script... no render counts as done until a subagent has looked at it" |

## Beat-count note (redo)

Source has 7 filled beats (B00 `ClaudeComposerAsk` cold open + B01/B02
`PptxAnatomy`/`PptxDesign` two custom REMOTION body beats + B05 `PptxTell`
teardown beat + BVDT `ClaudeVerdictArtifact` verdict + BHTF handoff + BOUT
outro). This redo expands the three source body beats (B01, B02, B05) to
eleven (NB01-NB11) to give the WRONG-GUESS and BOTH-DIRECTIONS laws their
own dedicated beats (the Teardown source folded the "does not reach for
python-pptx" routing point, the design rules, and the "gets right / bites"
columns into three dense beats; Plain separates the wrong guess/break from
the both-directions pair, per hai-simple's spine) and to plant/pay off a
concrete ANCHOR (the 5-slide climate-tech pitch deck — NB02 -> NB09) that
the source's own BHTF handoff line used as its worked example but never
carried through as a recurring beat earlier in the reel.

Source's three `Pptx*.tsx` components (Anatomy, Design, Tell) are not
reused: direct read of each .tsx file confirmed they `import { CLAUDE,
CLAUDE_FONT } from '../tokens/claude'` directly with no ink/accent/bg
props, so they render in the Claude fidelity skin, not the humanitarians
palette — the identical seam already logged on the `claude-liam-docx`,
`claude-liam-claude-api`, and `claude-liam-brand-guidelines` siblings.
Built fresh instead as 11 GRAPHIC (Manim) chip-row beats (NB01-NB11) on the
same shared generic template (`scenes.py`/`render_scenes.py`/
`build_beat_sheet.py`, copied from the `claude-liam-docx` sibling's proven
pattern), carrying the same facts in the humanitarians palette
(#F3EBDD/#2F2A26/#E4572E). No source beat was ai-video-prompt, pantry, or a
human-drop slot — NO-GENAI/NO-PANTRY LAW required no substitution beyond
B00 (the source's B00 was already `ClaudeComposerAsk`, REMOTION, not a
puppet ask — only its role as a non-hesitant cold open needed replacing).

Landing at 15 beats total: B00 + 11 GRAPHIC body beats (NB01-NB11) + BCRY +
BHTF + BOUT.

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/pptx/SKILL.md`) does not exist at
that path in this workspace (verified before this build) — same
reorganization already noted on the `claude-liam-docx` sibling. Per the
redo contract, facts (the three-path routing, the design rules, the
two-stage QA mandate, the accent-line tell, the gets-right/bites points)
are carried over unchanged from the locked source script rather than
re-verified against a live skill file that cannot be located.
