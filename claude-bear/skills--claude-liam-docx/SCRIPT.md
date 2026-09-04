# SCRIPT.md — DOCX (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-docx` (Teardown, examining Anthropic's `docx` skill) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
At first this reads as needing to install something just to edit a Word
file. Cross that out — the real question is whether you need to unzip it
instead. Liam, in for Bear.

## Act I — Stakes: the two paths, and the anchor ask

**NB01 — two paths, one file format** (source B01)
The docx skill covers two paths: create a new Word file with the docx-js
library, or edit an existing one by unpacking its ZIP and rewriting the XML
directly. A quick reference maps five task types to whichever path fits.

**NB02 — the ask, planted** (ANCHOR PLANTED)
Picture this ask: a one-page memo as a Word document, U.S. Letter size,
with a two-column table and page numbers in the footer. Hold onto that
request — we'll come back to it once the rules are in place.

## Act II — The wrong guess, and the case that breaks it

**NB03 — "same library either way?"** (WRONG GUESS)
So the natural guess: editing a Word file you already have needs the same
library you'd use to build one from scratch.

**NB04 — it's a ZIP of XML** (BREAK)
But a docx file is just a ZIP archive holding XML. Unpack it, edit the XML
text directly, and repack it — the edit path never touches a library at
all.

## Act III — What it actually does

**NB05 — A4 is the default, not Letter** (source B02)
The create path has its own rules, and the first one is silent: docx-js
defaults to A4 paper, not U.S. Letter. Set the size explicitly, or the page
shape is simply wrong.

**NB06 — paragraphs and bullets, not characters** (source B02)
Two more rules: never use a line-break character for new lines — use
separate paragraph elements. And never type a bullet character — use the
numbering format built for lists.

**NB07 — tables need dual widths** (source B02)
Tables need dual widths — a width on the table and a matching width on
every cell, both in the same unit. Set that unit to DXA; the percentage
option silently breaks tables in Google Docs.

**NB08 — unpack, edit, repack, in order** (source B03)
The edit path is three steps in order: unpack the file into XML, edit that
XML directly with exact text replacement, then repack and validate. For
tracked changes, replace a whole element, not just the words inside it.

## Act IV — The anchor returns

**NB09 — the same memo, now correct** (ANCHOR PAYOFF)
Back to that memo: U.S. Letter gets set explicitly instead of the A4
default, and the two-column table gets DXA widths on the table and every
cell — so it won't quietly break when someone opens it in Google Docs.

## Act V — Both directions

**NB10 — what the rules catch** (DIRECTION A)
When it works, it works well: the five docx-js rules catch exactly the
failures that would otherwise ship silently — wrong page size, a table
that falls apart in another program.

**NB11 — what's outside the list** (DIRECTION B — ONE FLAG)
One flag: these five rules cover the failure modes that are documented.
Nothing forces a check for one that isn't — an edit outside this list can
still slip through untested.

## Close

**BCRY — carry-out**
A docx file is a ZIP of XML, so editing one takes no library — just
careful edits. Creating one from scratch does take a library, and its
defaults fail silently unless you set them yourself.

**BHTF — your turn**
Your turn. Paste this into Claude: I want a one-page technical memo as a
Word document, U.S. Letter, with a header, heading styles, a two-column
table, and a footer with page numbers. Use the docx skill. Then watch: does
it set the page size explicitly, and does it use DXA widths on the table
instead of percentage? That's the whole gate.

**BOUT — outro**
DOCX. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| 1 stakes | NB01, NB02 | the skill's two paths, then the anchor ask planted |
| 2 wrong guess | NB03 (guess), NB04 (break) | "same library either way" broken by the ZIP-of-XML case |
| 3 mechanism | NB05, NB06, NB07, NB08 | page size, paragraphs/bullets, table widths, then the edit-path steps |
| 4 anchor | NB02 (plant) -> NB09 (payoff) | same memo ask, corrected |
| 5 both directions | NB10, NB11 | holds: catches the five documented failures pre-ship. flips: an undocumented failure can still slip through (flagged as this video's one inference) |
| 6 carry-out | BCRY | "editing needs no library... creating does, and its defaults fail silently" |

## Beat-count note (redo)

Source has 8 filled beats (B00 `ClaudeComposerAsk` cold open + B01/B02/B03/B05
four custom REMOTION body beats — `DocxAnatomy`, `DocxCreate`, `DocxEdit`,
`DocxTell`, all hardcoded to the CLAUDE fidelity token palette — + BVDT
verdict + BHTF handoff + BOUT outro). This redo expands the four source body
beats to eleven (NB01-NB11) to give the WRONG-GUESS and BOTH-DIRECTIONS laws
their own dedicated beats (the Teardown source folded the ZIP-is-XML insight
and the "gets right / bites" columns into one B05 teardown beat; Plain
separates the wrong guess/break from the both-directions pair, per
hai-simple's spine) and to plant/pay off a concrete ANCHOR (the one-page
memo — U.S. Letter, two-column table, page numbers — NB02 -> NB09) that the
source's own BHTF handoff line used as its worked example but never carried
through as a recurring beat earlier in the reel.

Source's four `Docx*.tsx` components (Anatomy, Create, Edit, Tell) are not
reused: direct read of each .tsx file confirmed they `import { CLAUDE,
CLAUDE_FONT } from '../tokens/claude'` directly with no ink/accent/bg props,
so they render in the Claude fidelity skin, not the humanitarians palette —
the identical seam already logged on the `skills--claude-liam-claude-api`
sibling for its own `ClaudeApi*.tsx` set (built the same day), and on the
`skills--claude-liam-brand-guidelines` sibling before that. Built fresh
instead as 11 GRAPHIC (Manim) chip-row beats (NB01-NB11) on the same shared
generic template (`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`,
copied from the `claude-liam-claude-api` sibling's proven pattern), carrying
the same facts in the humanitarians palette (#F3EBDD/#2F2A26/#E4572E). No
source beat was ai-video-prompt, pantry, or a human-drop slot —
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (the source's B00
was already `ClaudeComposerAsk`, REMOTION, not a puppet ask — only its role
as a non-hesitant cold open needed replacing).

Landing at 15 beats total: B00 + 11 GRAPHIC body beats (NB01-NB11) + BCRY +
BHTF + BOUT.

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/docx/SKILL.md`) no longer exists at
that path as of this build (2026-09-04) — the skills tree has been
reorganized since the source reel's 2026-07-18 build. Per the redo contract,
facts (the two paths, the five docx-js rules, the three-step edit workflow,
the tracked-changes and element-order pitfalls) are carried over unchanged
from the locked source script rather than re-verified against a live skill
file that could no longer be located.
