# QUESTION — financial-services--claude-liam-macro-rates-monitor

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-macro-rates-monitor/beat_sheet.json`.
This source sheet's narration states the Anthropic `macro-rates-monitor` skill's
function directly: it builds macroeconomic and rates dashboards **combining four
named inputs** — macro indicators, yield curves, inflation breakevens, and swap
rates — and is used when monitoring macro conditions, analyzing yield curve
shape, decomposing real vs. nominal rates, assessing policy rate expectations, or
evaluating financial conditions. The Teardown beats (B01 anatomy, B02 pipeline,
B03 design tell, BVDT verdict) are otherwise the shared skill-teardown template:
"a skill is a folder Claude reads before it works," "the pipeline is in the Steps
section... linear, no branching," "same input, same output, every run... only
what the file says." The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/lseg/skills/macro-rates-monitor/SKILL.md`)
does not exist on this machine (different machine's home directory — same
situation as the `initiating-coverage` and `clean-data-xls` siblings), but the
source *beat_sheet.json*'s own narration states the skill's function in enough
detail to redo faithfully. No reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
"design tell" framed the skill as "what it gets right: repeatable results / what
it bites: anything outside the spec" — Teardown judgment on the design choice
itself. Plain keeps only the mechanism (four named inputs, combined by one fixed
procedure) and its two failure directions, no verdict on whether the skill was
built well. The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new:

- **The wrong guess:** a newcomer assumes asking Claude for a "macro rates
  monitor" dashboard means it is forming its own economic view — reading the
  data and telling you where rates are headed, the way an analyst would. It
  isn't. The skill is a fixed procedure that combines four named inputs — macro
  indicators, the yield curve, inflation breakevens, and swap rates — using the
  definitions already written for them (a breakeven is nominal yield minus real
  yield, the market's implied average inflation expectation; it is not the
  skill's own forecast). Falsifying case: ask it to forecast what the central
  bank will actually do next quarter, and there's nothing to run — a genuine
  forecast isn't one of the four things the spec combines.
- **The anchor:** one pull of market data moving through all four building
  blocks — macro indicators, yield curve, breakevens, swap rates — in order,
  before it reaches the finished dashboard. Planted at B02, paid off at B03.
- **Both directions (B03):** the dashboard finishing proves the four blocks
  were combined the way the file defines them — nothing skipped, nothing
  improvised. It does not prove the economic read inside the dashboard will
  hold up: a correctly computed breakeven can still be a poor predictor of
  actual inflation. And if one input (say, swap-rate data) isn't available and
  that block can't populate, that's a data gap, not evidence the other three
  blocks are wrong.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("predict" → "combine four indicators
about" — the naive assumption that the dashboard is forecasting where rates go,
corrected to: it combines four named indicators per a fixed definition). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. No source beat was AI-VIDEO, pantry, or a human-drop
slot — every source beat was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required
no beat replacement beyond B00 itself.

**Question this reel actually answers:** When you ask Claude to run a "macro
rates monitor" and build you a dashboard, is it forecasting where rates are
headed — or is it doing something more mechanical?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
