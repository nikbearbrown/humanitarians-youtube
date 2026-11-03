# SCRIPT.md — Claude API (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-claude-api` (Teardown, examining Anthropic's
`claude-api` skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked whether Claude just knows its own API by heart. It doesn't —
it checks. So here's the real question: when Claude writes API code, what
makes it check instead of guessing from memory?

## Act I — Stakes: the skill, and the anchor ask

**NB01 — a reference, read first** (source B01)
The claude-api skill is a reference Claude reads before it touches your
file — not after a mistake, before one. It fires whenever a prompt names
Claude or Anthropic, or asks about an LLM with no provider named.

**NB02 — the ask, planted** (ANCHOR PLANTED)
Picture this ask: add extended thinking to a Python app that calls the
Claude API. Hold onto that exact request — we'll come back to it once the
skill has done its work.

## Act II — The wrong guess, and the case that breaks it

**NB03 — "Doesn't it already know?"** (WRONG GUESS)
So the natural guess: Claude already knows the current Claude API. It's
Anthropic's own product, presumably trained on its own freshest
documentation.

**NB04 — one old parameter, one 400** (BREAK)
But extended thinking used to take a parameter called budget_tokens. On
today's models that same parameter is rejected outright — a 400 error, not
a warning. Memory alone would have shipped broken code.

## Act III — What it actually does

**NB05 — the trigger, not a lookup** (source B01/B05)
The fix is a trigger that fires before the file even opens: any time a
prompt names Claude or Anthropic, or describes an LLM task with no provider
given. It covers eight languages, from Python to plain cURL.

**NB06 — three surfaces, not one** (source B02)
It also maps the job to one of three surfaces: a single API call for tasks
like summarizing or classifying, API plus tool use where you run the loop,
or a managed agent where Anthropic runs the loop for you.

**NB07 — four questions decide** (source B02)
Which surface to pick comes down to four questions: how complex is the
task, how much is a good answer worth, is it even viable, and what does a
mistake cost. A no to any one means stay simpler.

**NB08 — the exact ID is the contract** (source B04)
And it insists on one exact model ID string, never a guess and never a date
tacked onto the end — the ID is the contract, not a label you can
approximate.

## Act IV — The anchor returns

**NB09 — the same ask, now correct** (ANCHOR PAYOFF)
Back to that Python request: the skill catches that budget_tokens is the
old shape, swaps in the current one, and hands back the exact model ID to
use — before a single line of broken code gets written.

## Act V — Both directions

**NB10 — what it catches** (DIRECTION A)
When it works, it works well: a parameter that would have failed gets
caught and fixed before the request ever goes out, for any change the
skill already knows about.

**NB11 — what it misses** (DIRECTION B — ONE FLAG)
Here's the one limit worth flagging: the skill documents dozens of these
pitfalls, but nothing forces Claude to check them — a change nobody wrote
down yet can still slip straight through.

## Close

**BCRY — carry-out**
Claude doesn't recall the current Claude API from memory — it checks a
reference before writing. It only catches the drift someone bothered to
document.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to call the Claude API from
Python using extended thinking. Check the claude-api skill for the current
parameter shape, the exact model ID, and any drift from your training.
Show me a working example. Then watch what happens before any code
appears — does Claude check first, or does it guess? That is the whole
gate.

**BOUT — outro**
Claude API. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| 1 stakes | NB01, NB02 | the skill's role (pre-scan reference), then the anchor ask planted |
| 2 wrong guess | NB03 (guess), NB04 (break) | "already knows" broken by the budget_tokens -> 400 case |
| 3 mechanism | NB05, NB06, NB07, NB08 | trigger, then three surfaces, decision rule, exact model ID |
| 4 anchor | NB02 (plant) -> NB09 (payoff) | same Python/extended-thinking ask, corrected |
| 5 both directions | NB10, NB11 | holds: catches documented drift pre-write. flips: undocumented drift can still slip through (flagged as this video's one inference) |
| 6 carry-out | BCRY | "checks a reference... only catches what's documented" |

## Beat-count note (redo)

Source has 9 filled beats (B00 `ClaudeComposerAsk` cold open + B01-B05 five
`ClaudeApi*` REMOTION body beats, hardcoded to the CLAUDE fidelity token
palette + BVDT verdict + BHTF handoff + BOUT outro). This redo expands the
five source body beats to eleven (NB01-NB11) to give the WRONG-GUESS and
BOTH-DIRECTIONS laws their own dedicated beats (the Teardown source folded
"training data becomes the fallback" and "44 pitfalls, none enforced" into
a single B05 teardown beat; Plain separates the wrong guess/break from the
both-directions pair, per hai-simple's spine) and to plant/pay off a
concrete ANCHOR (the Python + extended-thinking ask, NB02 -> NB09) that the
source's B00 line implied (it used the same example: "add adaptive thinking
to your Python app") but never carried through as a recurring beat. Source
B01's language-count fact (eight SDKs) is folded into NB05's narration
rather than kept as a separate beat. Source's five `ClaudeApi*.tsx`
components (Anatomy, Surfaces, Drift, Models, Tell) are not reused: direct
read of each .tsx file confirmed they import the CLAUDE token file directly
(`import { CLAUDE, CLAUDE_FONT } from '../tokens/claude'`) with no
ink/accent/bg props, so they render in the Claude fidelity skin, not the
humanitarians palette — the same seam already logged on the
`skills--claude-liam-brand-guidelines` sibling for its own
`BrandGuidelines*.tsx` set, and on multiple `books--claude-liam-*` /
`k12-teacher-skills--*` reels besides. Built fresh instead as 11 GRAPHIC
(Manim) chip-row beats (NB01-NB11) on the shared generic template
(`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`, same pattern as the
`brand-guidelines` sibling), carrying the same facts in the humanitarians
palette (#F3EBDD/#2F2A26/#E4572E). No source beat was ai-video-prompt,
pantry, or a human-drop slot — NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00 (the source's B00 was already `ClaudeComposerAsk`,
REMOTION, not a puppet ask — only its role as a non-hesitant cold open
needed replacing).

Landing at 15 beats total: B00 + 11 GRAPHIC body beats (NB01-NB11) + BCRY +
BHTF + BOUT.

**Fact-currency note:** the source skill file
(`anthropics/skills/skills/claude-api/SKILL.md`) no longer exists at its
logged path as of this build (2026-09-04) — the skills tree has been
reorganized since the source reel's 2026-07-18 build. Per the redo
contract, facts (the exact `budget_tokens` -> 400 drift, the eight-language
coverage, the four-question decision rule, the "exact ID, no date suffix"
rule) are carried over unchanged from the locked source script rather than
re-verified against a live skill file that could no longer be located.
Illustrative specifics that name a model ID in the source (`claude-opus-4-8`)
were deliberately NOT repeated in this redo's narration or on-screen chips —
this video is itself about training priors going stale, and asserting a
specific "current default" model name would risk demonstrating the exact
failure mode it teaches about. The mechanism (trigger timing, decision
tiers, drift-table habit) is what's carried over; the specific model-ID
example is generalized to "the exact model ID" rather than naming one.
