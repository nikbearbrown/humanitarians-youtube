# Skill Creator — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-skill-creator`, Teardown). Register: **Plain**.
7 beats ≈ 2:20.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, no puppet host — hai-simple's WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Ask Claude to build a skill, and it feels like one good prompt should do it. It doesn't — it runs test cases first. So how does the skill creator actually decide a skill works?" | BrutalistHesitantWriter — types "Making a skill is / just writing a prompt. / Wait — how does / the skill creator actually decide?", trigger "prompt" → "test loop" |
| B01 | anatomy | The skill creator is a five-stage loop: capture intent, interview and research, write the SKILL.md (the frontmatter description is the primary trigger, deliberately a little pushy since Claude tends to undertrigger), test and grade (parallel with-skill/baseline runs, then the eval viewer), improve and repeat. Plus a separate description-optimization phase: 20 trigger evals, reviewed, then a loop that applies the best description. | SkillCreatorAnatomy — the five stages + optimization phase |
| B02 | self-demo | The eval loop, verbatim: spawn with-skill AND baseline in the same turn, never sequentially. Draft assertions while they run. Capture timing the moment runs complete — tokens and duration only exist in the task notification. Grade each assertion, aggregate into a benchmark, run an analyst pass, then generate the viewer — Outputs tab for qualitative review, Benchmark tab for pass rates and timing — **before** evaluating any of it yourself. | SkillCreatorEvalLoop — parallel runs, grading, viewer anatomy |
| B03 | **mechanism (resolves the wrong guess)** | The whole approach treats skill writing as an empirical loop, not a prompt-crafting exercise — draft, test with-skill against baseline in parallel, grade, repeat. Progressive disclosure keeps it lean: metadata loads first, then the SKILL.md body, then bundled resources, only as needed. Two limits worth knowing: on Claude dot ai there are no subagents, so runs happen one at a time with no baseline to compare against; and description optimization needs the Claude command line tool, so it only runs inside Claude Code. | SkillTeardownMechanism — heading "Test the loop. Never grade by feel." |
| **BCRY** | **carry-out** | Making a skill isn't writing a good prompt — it's proving, with a parallel with-skill-versus-baseline test, that it actually works. And the eval viewer has to reach you before the model judges the result itself. | WantQuote — the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: I want to create a skill that summarizes meeting transcripts into structured action items — start from scratch, help me define it, write the SKILL.md, and run the eval loop. Watch four things: does Claude ask about triggers and output format before drafting anything? Does it spawn with-skill and baseline runs in the same turn, not one after the other? Does it generate the eval viewer before it reads the outputs itself? And afterward, does it offer to run description optimization? | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Skill Creator. Liam, in for Bear. | OutroCTA — HAI skin, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the naive framing (one good prompt) before any mechanism is shown |
| Wrong guess surfaced *and corrected* | B00 types "prompt" → corrected to "test loop"; B03 resolves it in narration ("empirical loop, not a prompt-crafting exercise") |
| No inference — the reel makes no claim beyond the skill's own documented five-stage loop and eval architecture, so no flag is needed | n/a |
| Carry-out compresses the distinction, not the topic | BCRY: parallel proof-before-judgment, not "this video is about a skill-building skill" |
| No design judgment | B03 states the loop, progressive disclosure, and the two environment limits as fact, never "what it gets right / what it bites" — that framing is the source's Teardown language (`SkillCreatorTell`'s gets-right/bites card, `ClaudeVerdictArtifact`) and is dropped here |
| Host handoff | B00 is Remotion (BrutalistHesitantWriter), not a puppet — hai-simple's WRITER LAW substitution for `simple`'s HOST LAW |

## What changed from the source (redo contract)

- **Facts kept, unchanged:** the five-stage loop (capture intent → interview/research →
  write SKILL.md, description as primary trigger, deliberately pushy since Claude
  undertriggers → test and grade via parallel with-skill/baseline runs + eval viewer →
  improve and repeat); the eval loop architecture (parallel spawn, draft assertions
  while running, capture timing immediately since it's only in the task notification,
  grade → aggregate → analyst pass → viewer generated **before** self-evaluation,
  viewer's two tabs — Outputs qualitative, Benchmark quantitative); the separate
  description-optimization phase (20 trigger eval queries, human review, `run_loop.py`,
  best description applied); progressive disclosure (metadata → SKILL.md body →
  bundled resources); the two environment limits (Claude.ai has no subagents so runs
  degrade to serial with no baseline; description optimization needs the Claude CLI,
  so Claude Code only); the eval-set-overfit risk if test prompts aren't representative.
- **Register: Teardown → Plain.** The source's B05 (`SkillCreatorTell` — "what it gets
  right" / "where it bites" judgment) and BVDT ("Verdict" artifact,
  `ClaudeVerdictArtifact`) explicitly rank the design's trade-offs. Plain states the
  identical mechanics and limits as fact (this reel's B03) and lands the source's own
  "key rule" — generate the viewer before evaluating inputs yourself — as the
  carry-out (BCRY) instead of a verdict artifact or gets-right/bites card.
- **B00:** `ClaudeComposerAsk` (source's cold open — an Opus-session composer ask
  showing the loop's first two stages) → `BrutalistHesitantWriter`, per hai-simple's
  WRITER LAW. The naive framing ("one good prompt should do it") is the exact
  misconception PEDAGOGY.md's own PREDICT question named for the source build: "Isn't
  creating a skill just writing a good prompt? Why does it need its own workflow?" —
  restated here as the wrong guess instead of an opening ask.
- **B05 (`SkillCreatorTell`) + BVDT (`ClaudeVerdictArtifact`) → B03
  (`SkillTeardownMechanism`) + BCRY (`WantQuote`):** the source's two judgment-carrying
  beats (gets-right/bites card, verdict artifact) collapse into one factual mechanism
  beat (the empirical-loop framing, progressive disclosure, the two environment
  limits) and the bare carry-out sentence — matching `simple`'s law that the
  verdict-recap position becomes the carry-out line in Plain register. Same beat count
  (7 → 7), renumbered sequentially (B00, B01, B02, B03, BCRY, BHTF, BOUT vs. source's
  B00, B01, B02, B05, BVDT, BHTF, BOUT).
- **BHTF:** kept the source's meeting-transcript skill-building prompt near-verbatim —
  already a real, paste-ready Claude prompt a general viewer can run today, and it
  drills the exact wrong guess (skip the test loop) B00 opened with, via the same four
  watch-for gates the source specified (trigger/output interview, parallel spawn,
  viewer-before-self-review, description optimization offer).
- **Close:** BOUT's `ClaudeTitleOutro` (`@NikBearBrown`) → `OutroCTA` (Humanitarians AI
  skin, `@HumanitariansAI`), per hai-simple's channel-skin law. Voice/persona
  unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source already used this voice).
- **No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source
  beat was already a registered Remotion component (`ClaudeComposerAsk`,
  `SkillCreatorAnatomy`, `SkillCreatorEvalLoop`, `SkillCreatorTell`,
  `ClaudeVerdictArtifact`). B01/B02 reuse `SkillCreatorAnatomy`/`SkillCreatorEvalLoop`
  as-is — their content is purely factual (the five stages, the eval architecture),
  no judgment baked into either component, so no NO-GENAI/NO-PANTRY substitution was
  needed beyond B00 (mandatory writer-open swap), B03 (mandatory judgment-card swap,
  since `SkillCreatorTell`'s gets-right/bites columns are baked into the component
  pixels and can't be neutralized by narration alone), and BOUT (mandatory HAI-skin
  swap).
- **Beat count:** 7 → 7 (B00, B01, B02, B03, BCRY, BHTF, BOUT). Unchanged.

## Handoff prompt (BHTF, read aloud in full)

> "I want to create a skill that summarizes meeting transcripts into structured
> action items. Start from scratch — help me define the skill, write the SKILL.md,
> and run the eval loop."

Why it's worth running: it hands Claude the exact scenario the Skill Creator is built
for, and the four things to watch — does it interview before drafting, does it spawn
with-skill AND baseline in the same turn, does it generate the eval viewer before
reading the outputs itself, does it offer description optimization afterward — are
the gates that tell you whether the loop actually ran or whether Claude just wrote a
SKILL.md and called it done.

---
**GATE P — signed:** ______________________  (human)
