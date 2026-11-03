# Claude, Exam Forecast — Narration Script (Plain register)

*Skill: `hai-simple` (redo of `simple`/Teardown source). Register: **Plain**
— explain, then stop. 13 beats ≈ 2:45.*

*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion, machine-rendered.
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "A newcomer assumes Claude can read the textbook and tell you exactly what's on the exam. It can't — it ranks topics by how likely they are to appear. So what does 'exam forecast' actually promise?" | writer types "Claude reads my textbook and tells me EXACTLY what's on the exam." → corrects to "roughly" → "What does it really promise?" |
| B01 | 1 stakes | Finals season means weeks of reading compressed into days. Read everything from the first page again, and you run out of time before you reach the end. | 14 weeks of reading vs. days left to study |
| B02 | **4 anchor planted** | Say your Contracts final is three weeks out. Feed it your syllabus and past exams, and exam-forecast hands back a ranked list — topics one, two, three. | THE ANCHOR — three blank ranked slots |
| B03 | 2 wrong guess | The natural assumption: forecast means Claude has somehow seen this year's actual exam, and can hand you the real questions early. | "HAS SEEN THE REAL EXAM?" |
| B04 | **2 break it** | It hasn't, and it can't — a professor's exam file is locked until exam day. What it reads instead is the pattern already sitting in public course material. | locked exam, struck; public syllabus + past exams, accented |
| B05 | 3 mechanism | A skill is a folder Claude reads before it works. Its SKILL.md lists the steps in order: gather the sources, count how often each topic was tested before, then rank what's left. | SKILL.md → gather sources → count past topics → rank |
| B06 | **3 ONE FLAG** | One flag: this only works where a pattern already exists. A brand-new course, or a professor who rewrites the format every year, leaves nothing to count — and no record means no forecast. | a course with a record vs. a brand-new course, struck |
| B07 | **4 anchor payoff** | Back to that Contracts final: the same three slots come back filled in — consideration doctrine first, it's been tested four of the last five years, then the statute of frauds, then the narrower exceptions. | THE ANCHOR RETURNS — same three slots, now filled in |
| B08 | **5 direction A** | Ranked first doesn't mean guaranteed. Consideration doctrine could still sit out this particular year, the way any pattern can break once. | RANKED FIRST → still might not appear |
| B09 | **5 direction B** | And ranked low doesn't mean safe to skip — a topic near the bottom of the list can still be the one curveball on the page. | RANKED LAST → still could be on the page |
| **BCRY** | **6 carry-out** | Exam forecast doesn't show you the exam. It shows you where the class has been leaning, so you know what to study first. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: I have a final in three weeks. Here's my syllabus and reading list — read them, and if I share past exams for the course, count which topics come up most often. Then rank what's left by how often it's actually been tested, and tell me where to start studying first. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Exam Forecast. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B05 |
| Wrong guess surfaced *and falsified by a case* | B03 states the read; B04 breaks it with the locked-exam-file case |
| Exactly one inference flag | **B06** — the forecast only holds where a testing record already exists |
| One anchor, planted early, paid off late | B02 → B07 (the same three-slot ranked list, blank then filled in) |
| Both failure directions | B08 (ranked first, not guaranteed) and B09 (ranked low, not safe to skip) |
| No design judgment | B04–B06 describe why the mechanism behaves as it does; no verdict on whether it's a good skill |

## Deliberately not claimed

- **Not that Claude has seen any real exam.** B04 states plainly that a
  professor's exam file is locked until exam day — the skill reads public
  material (syllabus, reading list, past exams), never the sealed one.
- **Not a guarantee.** B07's ranked list is a probability read from
  pattern, not a leak. B08/B09 both state the failure modes explicitly so
  the reel never oversells the forecast as certainty.
- **No invented Anthropic product name.** "A skill is a folder Claude
  reads before it works" and "SKILL.md lists the steps" describe Claude's
  actual Agent Skills mechanism generically; "exam-forecast" itself is a
  custom teaching skill in this family's law-student folder, not an
  official Anthropic feature, and the reel never implies otherwise.
- **Source-completeness note.** The source sheet's topic-specific lines
  (what exam-forecast's mechanism/verdict actually says) were left as
  unresolved `>` placeholders and its `SKILL.md` doesn't exist on this
  machine. The general skill anatomy is kept verbatim from the source; the
  exam-forecast-specific facts above were reconstructed generically from
  the skill's name and its family's sibling law-student skills — see
  QUESTION.md and BUILD-LOG.md.

## Handoff prompt (BHTF, read aloud)

> "I have a final in three weeks. Here's my syllabus and reading list —
> read them, and if I share past exams for the course, count which topics
> come up most often. Then rank what's left by how often it's actually
> been tested, and tell me where to start studying first."

Run that today, against your own next exam.
