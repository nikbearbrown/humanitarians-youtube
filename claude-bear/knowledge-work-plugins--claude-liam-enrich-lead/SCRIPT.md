# Claude, Enrich Lead. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-enrich-lead`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumes enrich-lead needs a full LinkedIn profile before it can help. It doesn't — a name works too, or a company, or an email. Enrich-lead needs a full name to start. Right?" | writer types "Enrich-lead needs\na full PROFILE\nto start.\nRight?", hesitates on PROFILE, corrects to "name" — lands "Enrich-lead needs a full name to start. Right?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is enrich-lead. The SKILL.md holds the full instruction set — plain language, no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: SKILL.md (1 file) |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → RESULT |
| B03 | 3 mechanism | Here's the part worth knowing. Enrich-lead is a specification written as an instruction set: drop a name, a company, a LinkedIn URL, or an email, and it hands back a full contact card — email, phone, title, company intel, and next actions. Ask about the same lead twice, and you get the same card both times; ask for something the file doesn't cover, and the skill has nothing to say about it. | heading card: "The interesting constraint." + one-instruction-file statement |
| **BCRY** | **6 carry-out** | Enrich-lead isn't code Claude runs — it's one instruction file. Give it just a name, a company, a link, or an email, and get back the same full contact card, every time. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I have a lead — just a first name, nothing else. Read the enrich-lead skill in this folder and walk me through exactly which steps you'll run, in order, before you actually run them. Watching it explain first shows you which single detail it's working from, and where the file's instructions stop. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Enrich Lead. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the one-instruction-file mechanism and the same-input/same-output scope, then stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (enrich-lead needs a near-complete profile already); B01–B02 explain the file and pipeline before B03's scope statement |
| Wrong guess surfaced and falsified | B00: the naive read is "needs a full LinkedIn profile"; the source's own spec falsifies it in the same beat — "name, company, LinkedIn URL, **or** email" means any one suffices |
| Carry-out | BCRY compresses the distinction (one detail in, same full card out, every time) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly; no puppet host in hai-simple |
| Hedge words | none used — every claim is read directly off the source's own intact narration text |

## Deliberately not claimed

- **Not "you need a LinkedIn profile to use enrich-lead."** B00 states that guess and
  corrects it in the same beat: a name, a company, a LinkedIn URL, or an email each work
  on their own — the source's "or" is the operative word.
- **No invented field beyond the source's own list.** The contact card is stated exactly
  as the source names it — email, phone, title, company intel, next actions — nothing
  added (unlike a source with a missing description, there is nothing here that needed
  reconstruction; see QUESTION.md).
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites," "know the limit"); this Plain redo describes the
  same one-file, same-input/same-output scope without ruling on whether it was well
  designed.

## Handoff prompt (BHTF, read aloud)

> "I have a lead — just a first name, nothing else. Read the enrich-lead skill in this
> folder and walk me through exactly which steps you'll run, in order, before you
> actually run them."

Why it's worth running: it forces Claude to state its own steps before acting, on the
thinnest possible input — the same "explain first" clause the source reel's own handoff
used to surface a skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
