# Claude, Fx Carry Trade. — Narration Script (REDO, GATE P)

*Skill: `hai-simple`. Mode: **redo** of
`anthropics/financial-services/youtube/claude-liam-fx-carry-trade` (Teardown register,
7 beats: B00, B01, B02, B03, BVDT, BHTF, BOUT). Register here: **Plain**. Same
question, same facts, same 7-beat body argument. Voice: Liam, Kokoro `am_onyx`
(unchanged from source).*

**Source question kept verbatim in spirit:** what does the `fx-carry-trade` Anthropic
skill actually make Claude do? **Source facts kept:** the skill evaluates FX carry
trade opportunities by combining spot rates, forward points, interest rate
differentials, volatility surface analysis, and historical price trends; Claude reads
`SKILL.md`, then executes its Steps section in order; same input → same output, every
run; anything outside the file's scope isn't covered.

**What changed from the source:** B00 (was `ClaudeComposerAsk`, Teardown greeting
"Hola, Liam") → `BrutalistHesitantWriter` (WRITER LAW cold open, humanitarians
palette). BVDT ("Here is the Teardown moment... What it gets right / what it bites...
Verdict") → `BCRY`, reworded as a carry-out sentence with the verdict/judgment
language removed — the scope fact survives, the value judgment doesn't. BOUT
(`ClaudeTitleOutro`, `@NikBearBrown`) → two beats, `OutroSeries` + `OutroCTA`, the
Humanitarians AI channel skin — `ClaudeTitleOutro` is hardcoded to `@NikBearBrown`
per `OUTRO-LOCK.md` and is off-limits here. B01–B03 keep their source REMOTION
patterns (`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`)
verbatim in structure; only B03's on-screen eyebrow/heading/sparkline and the
`verdictLabel` pill were dropped (Teardown-coded "DESIGN TELL" / "Verdict" language) —
the underlying mechanism fact is unchanged.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks Claude to evaluate an FX carry trade, and it's tempting to picture Claude calculating the trade itself. It isn't. It's following a skill — a written specification. So what is a skill, really?" | `BrutalistHesitantWriter` — types "Ask Claude to evaluate / an FX carry trade. / Is Claude calculating? / What is a skill, really?"; "calculating" corrected to "following a skill" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is fx-carry-trade. The SKILL.md file holds the full instruction set, in plain language, no hidden logic. Claude reads it, then acts. The file is the program. | `SkillTeardownAnatomy` — one file, `SKILL.md`, 3k |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and executes it. Linear — no branching unless the step says so. | `SkillTeardownPipeline` — read → execute → return |
| B03 | mechanism | fx-carry-trade is a specification, written as an instruction set. Claude's job: evaluate FX carry trade opportunities using spot rates, forward points, interest rate differentials, volatility surface analysis, and historical price trends. Give it those inputs, and it returns the same result every time. Ask it something the file doesn't cover, and it has nothing to say. | `SkillTeardownMechanism` — no verdict pill |
| **BCRY** | **carry-out** | A skill is a spec Claude follows exactly: the same inputs give the same result, and anything outside the file simply isn't covered. | `WantQuote` — the sentence, alone |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me: I want to evaluate an FX carry trade using spot rates, forward points, interest rate differentials, volatility, and historical price trends. Walk me through what you'll check, step by step, before you calculate anything. Asking for the plan first shows you exactly what the skill checks — and what it leaves out. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro — series restate | Claude, Fx Carry Trade. Liam, in for Bear. | `OutroSeries` |
| BOUTB | outro — cta | More Claude basics, every week — from Humanitarians AI. | `OutroCTA`, `@HumanitariansAI` |

## Register audit (Plain, vs. source Teardown)

| Check | Where |
|---|---|
| No verdict / judgment language | BVDT's "Here is the Teardown moment," "what it gets right / what it bites," and the verdict pill are gone; B03/BCRY keep the same scope fact stated descriptively |
| Facts unchanged | Skill name, skill description, Steps-section pipeline, same-input/same-output behavior all carried over verbatim from the source narration |
| Beat count unchanged | 7 source beats kept 1:1 (B00→B00, B01→B01, B02→B02, B03→B03, BVDT→BCRY, BHTF→BHTF, BOUT→BOUT), plus one added beat (BOUTB) required by the HAI two-component outro (`OutroSeries` + `OutroCTA`) |
| Voice unchanged | Liam, Kokoro `am_onyx`, both source and redo |
| WRITER LAW | B00 text ends on the real question ("What is a skill, really?"); the one wrong word ("calculating") is the newcomer's actual misconception, corrected in place to "following a skill" |
| NO-GENAI / NO-PANTRY | Source B00 was already `ClaudeComposerAsk` (REMOTION, not AI-VIDEO/pantry) — no beat needed replacing on that ground; only the open and close changed per the hai-simple delta table |

## Known gap — logged, not fixed here

`OutroSeries`/`OutroCTA` import `tokens/vox.ts` (house default `teardown`: white /
near-black / red) and expose no `bg`/`ink`/`accent` props. They will not actually
render in the humanitarians cream/teal/crimson set despite `metadata.palette` above.
See `BUILD-LOG.md` for the full note — this is a shared-component wiring gap, not
something fixable from a single reel's beat sheet, and not a blocker for a review cut.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to evaluate an FX carry trade using spot rates, forward points, interest
> rate differentials, volatility, and historical price trends. Walk me through what
> you'll check, step by step, before you calculate anything."

Why it's worth running: asking for the plan before the number surfaces exactly which
inputs the skill uses and which ones it silently ignores.

---
**GATE P — signed:** REDO — carried over from source's approved teardown; no new
human sign-off required per hai-simple's unattended-loop contract.
