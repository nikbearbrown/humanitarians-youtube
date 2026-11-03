# QUESTION

**The question:** "Claude, Equity Research." — when Claude does equity
research, is that a trained financial analyst living inside the model, or
is it following a written file? Answered using the `equity-research`
skill's own stated purpose as the concrete case.

**Mode:** redo — source is
`anthropics/financial-services/youtube/claude-liam-equity-research/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `audience: "Claude"`,
`source_skill: "/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/lseg/skills/equity-research/SKILL.md"`
— that exact path is on Bear's machine and does not exist locally; unlike
the plugin-structure redo, no equivalent local copy of the full SKILL.md was
found either. 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF handoff, BOUT outro — B00 was already
`ClaudeComposerAsk` REMOTION, not AI-video/pantry, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap. This reel keeps the
question and every fact the source narration actually states (the skill's
one-paragraph purpose, its one-file anatomy, its linear read-then-execute
pipeline, its repeatable-but-bounded reliability claim), re-registers the
narration to Plain, replaces the cold open with the Brutalist Hesitant
Writer, folds the source's BVDT verdict recap into a proper carry-out beat,
and restates the source's B03 "gets right / bites" framing as an
anchor-and-both-directions mechanism fact instead of a design judgment.

**Why it earns a reel:** `equity-research` is a Claude Skill — a folder
Claude reads before it works, not a specialized or separately trained
model. It is one file, `SKILL.md`, written in plain language. Its stated
purpose: "Generate comprehensive equity research snapshots combining
analyst consensus estimates, company fundamentals, historical prices, and
macroeconomic context. Use when researching stocks, comparing estimates to
actuals, analyzing company financials, assessing equity valuations, or
building investment cases." Execution is linear: Claude reads the file,
executes each step in order, returns the result — no branching unless a
step says so. Because it is a written spec rather than trained judgment,
the same input produces the same output every run, and the skill only does
what the file specifies — a question the file's steps don't cover isn't
refused, it's simply not written down.

**Naive framing (B00, corrected on screen):** "Ask Claude for equity
research — is that a trained analyst inside it?" → corrects "trained
analyst" to "written file" (the newcomer's default read of "Claude does
equity research" is that some specialized financial training or judgment
lives in the model; what actually runs is a plain-language instruction
file it reads before acting).

**Body facts carried from source (unchanged):**
- a Skill is a folder Claude reads before it works; `equity-research` is
  one file total, `SKILL.md`, in plain language, no hidden logic
- the skill's stated purpose, verbatim: combine analyst consensus
  estimates, company fundamentals, historical prices, and macroeconomic
  context into a snapshot; used for researching stocks, comparing
  estimates to actuals, analyzing financials, assessing valuations,
  building investment cases
- execution is linear — read the file, execute each step in order, return
  the result; no branching unless a step specifies it
- same input produces the same output every run (repeatable)
- the skill only does what the file specifies; anything outside the
  written steps isn't covered
- source's Your Turn worked example: paste a request to run the
  equity-research skill and ask Claude to walk through what it will do
  before it does it
