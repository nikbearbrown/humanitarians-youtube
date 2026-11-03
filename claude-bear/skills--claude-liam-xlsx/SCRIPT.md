# SCRIPT.md — XLSX (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-xlsx` (Teardown, examining Anthropic's `xlsx` skill) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
At first this reads as: does Claude just type the number in, once a
total's computed? Cross that out — the real question is whether it types
the formula in instead. Liam, in for Bear.

## Act I — Stakes: the two tools, and the anchor ask

**NB01 — two tools, one decision** (source B01)
The xlsx skill splits into two tools. Pandas handles data analysis, bulk
operations, and simple export — no formulas involved. Openpyxl handles
formulas, formatting, and every Excel-specific feature. Which tool you
reach for depends entirely on whether the task needs a real formula.

**NB02 — the ask, planted** (ANCHOR PLANTED)
Picture this ask: a three-year revenue model, with a growth-rate
assumption driving a computed total for each year. Hold onto that model —
we'll come back to it once the rules are set.

## Act II — The wrong guess, and the case that breaks it

**NB03 — "just type the number in?"** (WRONG GUESS)
So the natural guess: once that total's already computed in Python, you
can just type the number straight into the spreadsheet cell — it's the
same number either way.

**NB04 — the formula mandate** (BREAK)
But the skill's one absolute rule says otherwise: never calculate a value
in Python and hardcode it. Write the actual Excel formula — equals SUM of
the range — so the sheet stays dynamic.

## Act III — What it actually does

**NB05 — six steps, one mandatory** (source B01)
The workflow is six steps: choose pandas or openpyxl, create or load the
workbook, modify it — add data, write formulas, apply formatting — then
save. If you wrote any formulas, one more step is mandatory.

**NB06 — recalc.py, under the hood** (source B01)
That step is scripts/recalc.py. It opens the file in LibreOffice — which
has to be installed already — recalculates every formula, and scans all
four Excel error types: ref, div-zero, value, and name. The result comes
back as JSON, with the exact cell address for each one.

**NB07 — blue, black, green** (source B02)
The financial-model standard has its own color code. Blue text for a
hardcoded input — a number someone might change. Black text for every
formula. Green text for a link pulling from another sheet in the same
workbook.

**NB08 — red, yellow, and the numbers** (source B02)
Red text for a link to an external file. Yellow background marks a key
assumption. And numbers follow their own format — negatives sit in
parentheses, never a minus sign, and zero shows as a dash.

## Act IV — The anchor returns

**NB09 — the same model, now correct** (ANCHOR PAYOFF)
Back to that revenue model: the yearly total isn't typed in anywhere. It's
a live formula, equals growth rate times last year's revenue, colored
black because it's a formula — and the growth rate itself sits in blue,
because that's the input someone can change.

## Act V — Both directions

**NB10 — what recalc.py catches** (DIRECTION A)
When it works, it catches exactly what it's built to catch: run recalc.py,
and any of those four error types gets flagged by cell address before the
file ever ships.

**NB11 — what it can't catch** (DIRECTION B — ONE FLAG)
One flag: a formula can be pointed at the wrong cell entirely and never
throw an error at all — because a DataFrame's row N lands one row lower in
Excel, at row N plus one. Recalc.py can't catch a formula that's simply
wrong, only one that's broken.

## Close

**BCRY — carry-out**
Write the formula, never the number it computes — that's what keeps a
sheet alive when inputs change. And a clean error scan proves the formulas
didn't break; it doesn't prove they point at the right cells.

**BHTF — your turn**
Your turn. Paste this into Claude: build a three-year SaaS revenue model
with a growth-rate assumption and a computed revenue total each year —
deliver it as an xlsx file, using the xlsx skill. Then watch two things:
does it write an actual formula for the total, instead of a hardcoded
number? And does it run scripts/recalc.py afterward, and read the JSON
result before calling it done?

**BOUT — outro**
XLSX. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| 1 stakes | NB01, NB02 | the skill's tool decision, then the revenue-model anchor planted |
| 2 wrong guess | NB03 (guess), NB04 (break) | "just type the number in" broken by the skill's own formula mandate |
| 3 mechanism | NB05, NB06, NB07, NB08 | six-step workflow, recalc.py internals, color code (blue/black/green, then red/yellow + number formats) |
| 4 anchor | NB02 (plant) -> NB09 (payoff) | same revenue model, corrected |
| 5 both directions | NB10, NB11 | holds: catches the four documented error types pre-ship. flips: a formula pointed at the wrong cell throws no error at all (flagged as this video's one inference) |
| 6 carry-out | BCRY | "write the formula... a clean scan doesn't prove the cells are right" |

## Beat-count note (redo)

Source has 7 filled beats (B00 `ClaudeComposerAsk` cold open + B01/B02 two
custom REMOTION body beats — `XlsxAnatomy`, `XlsxStandards` — + B05
teardown beat `XlsxTell` + BVDT verdict + BHTF handoff + BOUT outro). This
redo expands the three source body beats to eleven (NB01-NB11) to give the
WRONG-GUESS and BOTH-DIRECTIONS laws their own dedicated beats (the
Teardown source folded the formula-mandate insight and the "gets right /
bites" columns into one B05 teardown beat; Plain separates the wrong
guess/break from the both-directions pair, per hai-simple's spine) and to
plant/pay off a concrete ANCHOR (the three-year revenue model — NB02 ->
NB09) that the source's own BHTF handoff line used as its worked example
but never carried through as a recurring beat earlier in the reel.

Source's three `Xlsx*.tsx` components (Anatomy, Standards, Tell) are not
reused: direct read of each .tsx file confirmed they `import { CLAUDE,
CLAUDE_FONT } from '../tokens/claude'` directly with no ink/accent/bg
props, so they render in the Claude fidelity skin, not the humanitarians
palette — the identical seam already logged on the `skills--claude-liam-docx`,
`skills--claude-liam-claude-api`, and `skills--claude-liam-brand-guidelines`
siblings for their own hardcoded-palette component sets. Built fresh
instead as 11 GRAPHIC (Manim) chip-row beats (NB01-NB11) on the same shared
generic template (`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`,
copied from the `claude-liam-docx` sibling's proven pattern), carrying the
same facts in the humanitarians palette (#F3EBDD/#2F2A26/#E4572E). No
source beat was ai-video-prompt, pantry, or a human-drop slot —
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (the source's
B00 was already `ClaudeComposerAsk`, REMOTION, not a puppet ask — only its
role as a non-hesitant cold open needed replacing).

The row-offset trap (DataFrame row N = Excel row N+1; column 64 is BL not
BK in the openpyxl API) and the `data_only=True` re-save trap both appear
in the source's B05 teardown beat. This redo carries the row-offset fact
forward into NB11 as the BOTH-DIRECTIONS "flip" case (a wrong-but-not-broken
formula that recalc.py's error scan cannot catch) because it pairs cleanly
with NB10's "what recalc.py catches" as a genuine positive/negative-proof
pair per BOTH-DIRECTIONS LAW. The `data_only=True` trap is a separate,
unrelated failure mode (destroys formulas on re-save; not a recalc-detection
gap) and was judged not to fit either direction beat without diluting the
pairing — it is documented here rather than invented a twelfth beat to
carry it, per the redo contract's instruction to preserve facts without
mechanically expanding beat count past what the spine needs.

Landing at 15 beats total: B00 + 11 GRAPHIC body beats (NB01-NB11) + BCRY +
BHTF + BOUT.

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/xlsx/SKILL.md`) no longer exists at
that path as of this build (2026-09-04) — the skills tree has been
reorganized since the source reel's 2026-07-18 build. Per the redo contract,
facts (the two tools, the six-step workflow, the mandatory recalc.py step
and its four error types, the financial-model color code and number
formats, the formula mandate, the row-offset and data_only=True traps) are
carried over unchanged from the locked source script rather than
re-verified against a live skill file that could no longer be located.
