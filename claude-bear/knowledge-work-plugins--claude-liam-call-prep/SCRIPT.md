# Claude, Call Prep. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-call-prep`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone typed 'join' — but Claude doesn't sit in on the call. There's a skill called call-prep: it reads signals about the account beforehand. Does Claude prep me before the call? Let's look inside." | writer types "Does Claude\nJOIN me\nbefore the\ncall?", hesitates on JOIN, corrects to "prep" — lands "Does Claude prep me before the call?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is call-prep. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: SKILL.md + references |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → CALL BRIEF |
| B03 | 3 mechanism | The scope is specific. call-prep prepares for a customer or prospect call using signals from Common Room — account activity, product usage, recent conversations. It runs on phrases like "prep me for my call with a company" or "what should I know before talking to them." Stay inside that request, and the brief comes back the same way every time; ask for anything the file doesn't cover, and the skill has nothing to say about it. | heading card: "The interesting constraint." + scope statement |
| **BCRY** | **6 carry-out** | Claude doesn't join the call. It preps you for it — same signals in, same brief out, every time. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Read the call-prep skill in this folder. Before you run it, tell me exactly which signals it will pull and from where. Then prep me for a call with a company I name. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Call Prep. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the scope (prepares one call, from Common Room signals, nothing outside the request) and stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (call-prep = Claude handles the call); B01–B02 explain the file and pipeline before B03's scope statement |
| Carry-out | BCRY compresses the distinction (preps, doesn't participate) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly via "Let's look inside"; no puppet host in hai-simple |
| Hedge words | none used — every claim is a confirmed, present-tense description of how call-prep and Claude Skills generally work |

## Deliberately not claimed

- **Not "Claude joins or makes the call."** The naive framing in B00 ("Does Claude
  JOIN me before the call?") is stated and corrected within the same beat — the
  skill assembles a briefing beforehand; it never participates in the call itself.
- **Not a claim about specific Common Room data fields.** The source names "Common
  Room signals" without listing exact fields; B03 names account activity, product
  usage, and recent conversations as the generic *kind* of signal a CRM/community
  integration like Common Room carries — consistent with the source, not additional
  specifics it never gave.
- **Recovered, not invented, trigger phrases.** The source truncates its own quoted
  trigger-phrase list in B03/BVDT/BHTF ("Triggers on 'prep me for my call ."); the
  complete phrase survives intact in the source's own B00 and is used here instead
  of guessing at the cut-off text (see QUESTION.md).
- **No verdict on the skill's design.** The source's Teardown register judged the
  skill ("what it gets right," "what it bites," "know the limit"); this Plain redo
  describes the same scope without ruling on whether it was well designed.

## Handoff prompt (BHTF, read aloud)

> "Read the call-prep skill in this folder. Before you run it, tell me exactly
> which signals it will pull and from where. Then prep me for a call with a
> company I name."

Why it's worth running: it forces Claude to state its own scope before acting —
the same "explain first" clause the source reel's own handoff used to surface a
skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
