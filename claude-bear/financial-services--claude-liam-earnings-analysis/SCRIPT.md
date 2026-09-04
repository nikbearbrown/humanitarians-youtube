# SCRIPT.md — Claude, Earnings Analysis (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-earnings-analysis` (Teardown, skill-explainer format for
the `earnings-analysis` Anthropic Agent Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone wonders whether Claude needs special training to do earnings
analysis. It doesn't need training at all — it needs briefing. One file
tells it exactly what to do, every time.

## Act I — What a skill actually is

**NB01 — A skill is a folder** (source B01 — anatomy)
A Claude skill is a folder Claude reads before it acts. This one is called
earnings-analysis. Its SKILL.md holds plain-language instructions — no
hidden code. Claude reads the file, then acts on it.

**NB02 — Read, then execute** (source B02 — pipeline)
The instructions live in a Steps section. Claude reads each step in order,
then executes it. It's linear — no branching unless a step calls for it.

**NB03 — One job, stated plainly** (source B03 — design tell, de-judged)
This skill has one job: turn a company's quarterly numbers into a written
earnings update — eight to twelve pages, a few summary tables, several
charts. That's the whole brief. Anything outside it isn't part of what this
file does.

## Close

**BCRY — carry-out** (source BVDT — verdict, re-registered to Plain)
A Claude skill is a file, not training. It doesn't make Claude smarter — it
gives Claude one job, done the same way, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: "I want a professional equity-research
earnings update — eight to twelve pages, three to five thousand words,
covering beat-or-miss, updated estimates, and the revised thesis. Read the
earnings-analysis skill first, and walk me through what you'll do before
you do it." That clause matters — asking Claude to explain the plan before
running it surfaces the real constraints the file sets.

**BOUT — outro**
Claude, Earnings Analysis — what one skill file actually does. Liam, in for
Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive assumption that specialized output means special training |
| Wrong guess | B00 → NB01 | "trained" corrected to "briefed" in the writer open; NB01 falsifies it directly — Claude reads a file, it isn't retrained |
| Mechanism | NB01–NB02 | a skill is a folder with a SKILL.md; Claude reads it, then executes the steps in order |
| Anchor | N/A | the source is a short skill-explainer with no running scenario to plant/pay off — see note below |
| Both directions | N/A | the source states one mechanism and one scope, not a claim with two failure modes — see note below |
| Carry-out | BCRY | one sentence, survives repetition |

No anchor and no both-directions beat: the source (`claude-liam-earnings-
analysis`) is a compact 7-beat skill-explainer, not a deep-explainer with a
planted scenario or a claim requiring both failure directions. Per the
redo contract, the beat count and body argument are locked to the source;
inventing an anchor or a both-directions beat that the source never had
would add content the locked script doesn't support. Documented here as
N/A rather than fabricated, the same way the `books--claude-liam-what-
plugins-are` redo logged "N/A" on its one-flag audit when the source
genuinely supported every claim directly.

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the skill file specifies (a folder, a SKILL.md, a Steps section, the
8-12 page / 3,000-5,000 word / 1-3 table / 8-12 chart scope) — not an
inference about hidden internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (cold open, `ClaudeComposerAsk`), B01 (anatomy,
`SkillTeardownAnatomy`), B02 (pipeline, `SkillTeardownPipeline`), B03
(design tell, `SkillTeardownMechanism`), BVDT (verdict,
`ClaudeVerdictArtifact`), BHTF (your-turn handoff), BOUT (outro). This redo
is also 7 beats: B00 (now `BrutalistHesitantWriter`), NB01–NB03 (source
B01–B03, same facts, same order, Plain register), BCRY (source BVDT, Plain
carry-out sentence in place of the bulleted Teardown verdict), BHTF, BOUT
(now Humanitarians AI skin). No beat was dropped, merged, or added — the
source's argument was already exactly the size of hai-simple's spine minus
the anchor/both-directions moves it never had.

The only content change beyond register is NB03: the source's B03 named a
trade-off ("What it gets right: repeatable results. What it bites: anything
outside the spec.") — Teardown judgment on the design. Plain states the
same scope as a fact (one job, nothing outside it) without ruling on
whether that scope is a good trade-off, per the register audit's "no
judgment" check.

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's B00 was already `ClaudeComposerAsk` (Remotion) and every other
beat was already Remotion (`SkillTeardown*`, `ClaudeVerdictArtifact`,
`ClaudeComposerAsk`, `ClaudeTitleOutro`). NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00, which the WRITER LAW replaces regardless of what
it was.
