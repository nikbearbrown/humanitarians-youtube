# Claude, Account Research.

You ask Claude what's going on with an account, and it's tempting to assume
it already knows — the way it knows general facts. It doesn't. The
`account-research` skill is a `SKILL.md` file Claude reads before it acts:
instructions, not memory. It only fires when your words match its stated
triggers — `research [company]`, `tell me about [domain]`, `pull up signals
for [account]`, `what's going on with [company]`, or any account-level
question. Once matched, execution is linear: read the file, execute each
step in order, return the result. Run the same request again later and
Claude walks the same three steps — repeatable, not remembered. Phrase it
outside the trigger list, and the pipeline never starts; you're back to
Claude answering from what it already knows, which is exactly the guess this
reel opens by questioning.

**Topic:** ACCOUNT RESEARCH · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-account-research

---

## Chapters

0:00 You ask about an account — Claude must already check it, right?
0:10 Nothing dated today is in memory
0:34 Matched, then walked step by step
0:58 Same steps again, then nothing starts
1:22 Carry-out
1:34 Your turn
1:59 Outro

---

## YOUR TURN

"I want to research a company using the account-research skill. Read the
skill file and walk me through what you'll do, step by step, before you do
it."

Watch for two things when Claude answers: does it name the exact trigger
phrase your words matched, and does it lay out the steps before running
them?

---

## Deliberately not claimed

Not a verdict on the trigger-phrase design — the source framed the spec as
"what it gets right" against "where it bites," a Teardown trade-off
judgment; this reel keeps only the mechanism fact: matching words run the
pipeline, non-matching words don't. Not a claim that Claude has no general
knowledge of companies — it plainly does; the point is that knowledge is
frozen at training time, and an account's live signals are not. Not a claim
that a missed trigger errors loudly — the source describes no error state
for an out-of-spec request; the pipeline simply never starts.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
