# Claude, Contact Center/android. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-contact-center/android`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone typed 'run' — as if Claude operates the contact center. There's a skill called contact-center slash android: it builds the app that connects to it. Does Claude build my contact center app? Let's look inside." | writer types "Does Claude\nRUN my\ncontact center\napp?", hesitates on RUN, corrects to "build" — lands "Does Claude build my contact center app?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is contact-center/android. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: RUNBOOK.md, SKILL.md + concepts/examples/references/troubleshooting |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → APP CODE |
| B03 | 3 mechanism | The scope is specific. contact-center/android covers the Zoom Contact Center SDK for native Android apps — chat, video, the virtual agent, scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling. Stay inside that, and the same request produces the same integration code every time; ask for anything outside the Android SDK, and the skill has nothing to say about it. | heading card: "The interesting constraint." + scope statement |
| **BCRY** | **6 carry-out** | Claude doesn't run your contact center. It writes the Android code that connects to one — the same integration, every time. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Read the contact-center/android skill in this folder. Before you run it, tell me exactly which Zoom Contact Center SDK features it covers and which Android lifecycle pieces it handles. Then help me wire up one feature in my app. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Contact Center/android. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the scope (covers named SDK feature areas, native Android only, nothing outside that) and stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (contact-center/android = Claude runs the contact center); B01–B02 explain the file and pipeline before B03's scope statement |
| Carry-out | BCRY compresses the distinction (writes the integration, doesn't operate it) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly via "Let's look inside"; no puppet host in hai-simple |
| Hedge words | none used — every claim is a confirmed, present-tense description of how contact-center/android and Claude Skills generally work |

## Deliberately not claimed

- **Not "Claude answers calls or operates the contact center."** The naive framing in
  B00 ("Does Claude RUN my contact center app?") is stated and corrected within the
  same beat — the skill is a coding aid: it helps build the native Android app that
  talks to Zoom's Contact Center SDK, and Claude never takes a call itself.
- **Not a claim about a specific trigger-phrase quote.** Unlike some siblings in this
  family, the source never gives an explicit "triggers on '...'" quote for this skill —
  none is invented here. B03 states only the SDK feature areas the source itself names
  (chat, video, ZVA, scheduled callback, campaign mode, service lifecycle, rejoin
  handling).
- **No verdict on the skill's design.** The source's Teardown register judged the
  skill ("what it gets right," "what it bites," "know the limit"); this Plain redo
  describes the same scope without ruling on whether it was well designed.

## Handoff prompt (BHTF, read aloud)

> "Read the contact-center/android skill in this folder. Before you run it, tell me
> exactly which Zoom Contact Center SDK features it covers and which Android
> lifecycle pieces it handles. Then help me wire up one feature in my app."

Why it's worth running: it forces Claude to state its own scope before acting — the
same "explain first" pattern this family's handoffs use to surface a skill's real
constraint logic before code gets written.

---
**GATE P — signed:** ______________________  (human)
