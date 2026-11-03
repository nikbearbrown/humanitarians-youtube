# SCRIPT.md — Feedback Before The Commit. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-submit-solution` (Teardown, walks the Anthropic
`submit-solution` cwc-workshops Skill — guiding a workshop attendee through
committing their starter-agent decomposition and opening a PR with their
solution plus workshop feedback) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed submitting a workshop solution is just a git task — commit,
push, open a PR. It isn't, quite. So: is submitting a solution actually a
feedback task?

*(Text typed on screen: "Claude, submit / my solution — / it's a git / task,
right?" — trigger word "git" corrects to "feedback", landing on: "Claude,
submit my solution — it's a feedback task, right?")*

## Body — anatomy, the ask-first mechanism, the design tell

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is
submit-solution — for a workshop attendee wrapping up the StockPilot
exercise. Inside are five steps, always in this order: ask about their
experience, show the diff, commit and push, open the PR, confirm. The
SKILL.md fixes that order — Claude doesn't skip ahead to committing.

**NB02 — Ask first, git second** (source B02, pipeline)
Step one comes before any git command: three questions. Which subagent
approach did they use for cycle three — callable agents, spawn subagent,
inline, or something else? What was the hardest part of the workshop? One
thing they'd change? Only after that does Claude check the diff. An empty
diff doesn't mean they're finished — it usually means they edited a
different file, so Claude asks rather than assumes. A full diff doesn't
mean the PR opens yet either — the feedback still has to be collected
first.

**NB03 — The PR body is the feedback form** (source B03 design tell + BVDT
verdict, merged; re-registered Teardown → Plain)
The PR body Claude writes carries two things in one document: the
technical summary — subagent approach, eval score, tools dropped, skills
enabled — and the workshop feedback, right below it. That's what makes
this a feedback task wearing a git task's clothes: the same PR facilitators
read for the code is the form they read for what to fix in the next
workshop. Skip the questions and the commit still happens — but the second
half of that document stays blank, every time.

## Close

**BCRY — carry-out**
Submitting a workshop solution isn't just a git task — the skill has
Claude ask what was hardest before it commits anything, because the same
PR that shows the code is the form that shapes the next workshop.

**BHTF — your turn**
Your turn. Paste this into Claude: I just finished a coding exercise and
want to submit my solution as a pull request. Before you touch git, ask me
what approach I used, what was hardest, and what I'd change — then show me
the diff, and write a PR description with two sections: my code summary,
and my feedback. Notice which questions come before the commit and which
come after.

**BOUT — outro**
Feedback Before The Commit. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a mechanics question — is submitting a solution just committing and opening a PR? |
| Wrong guess | B00 (WRITER LAW) | "git" corrected to "feedback" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill folder's fixed step order, and the exact interview gate (three questions) that runs before any git command |
| Anchor | the submit-solution flow itself, named at B00 and carried through NB01–NB03 without dropping it | source is a single worked mechanism throughout (one Skill, one submission flow), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB02 | "an empty diff doesn't mean they're finished — it usually means a different file" / "a full diff doesn't mean the PR opens yet either — the feedback still has to be collected first" — both failure directions of reading the diff as the whole signal, stated together |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct restatement of the
`submit-solution` Skill's own SKILL.md — the fixed five-step order, the
exact three interview questions (subagent approach, hardest part, one
change), the empty-diff-means-check-elsewhere case, the PR body template's
two sections (decomposition summary, workshop feedback), and the
confirmation step naming that facilitators read every PR. Per `simple`'s
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's design-tell text ("Here is the Teardown moment... What it gets
right: repeatable results. What it bites: anything outside the spec.") and
BVDT's verdict ("Same input, same output, every run. Know the limit: only
what the file says.") are merged into a single NB03, keeping the one fact
a general audience needs and can act on — the PR body carries both the
code summary and the feedback, in the same document — and dropping the
Teardown-only "what it bites" framing, which is a design verdict rather
than a mechanism description and fails the NO JUDGMENT register check;
BHTF kept as the your-turn handoff, rewritten as a fully self-contained
prompt (the source's version named "the submit-solution skill" and quoted
a truncated task string — "committing their starter-agent decomposition
a." — cut mid-word, carried over from the source's own generation defect;
this redo's prompt instead states the scenario directly — a finished
coding exercise, submit it as a PR — so it's runnable in any Claude
conversation today, no skill install required, while still testing the
same reasoning: questions before git, both halves in the PR body); BOUT
kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 +
BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
