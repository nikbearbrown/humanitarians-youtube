# Claude, Matter Intake — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-matter-intake`). Register: **Plain**.
11 beats ≈ 2:00. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** BrutalistHesitantWriter (Remotion, free, machine-rendered — no
puppet, no human step). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "You'd guess Claude decides whether to take on a new matter once it picks up matter-intake. It doesn't — it just logs answers to a fixed set of questions. Let's see what's inside that file." | Writer types "Does matter-intake / decide which matters / to take on?", hesitates on "decide", corrects to "log" — lands on the real question (revised post-render: the original 4-line statement+question draft measured at ~11.4s of expected typing against a 10.11s window and was cut off before reaching the question; shortened to a single 3-line question, same correction) |
| B01 | 1 stakes | Hear "Claude has a matter-intake skill" and it sounds like Claude is screening new clients — deciding which matters are worth the risk before anyone else looks. | chips: CLAUDE HAS A MATTER-INTAKE SKILL → SCREENS NEW MATTERS? |
| B02 | **2 wrong guess, broken** | But run it on a matter with an obvious conflict and matter-intake doesn't refuse it or flag it declined — it still asks the same nine questions and writes down the answers. The decision to decline was always the lawyer's, not the skill's. | chips: OBVIOUS CONFLICT → SKILL DECLINES IT? (struck) → STILL JUST LOGS IT |
| B03 | **4 anchor planted** | Here's what matter-intake actually does: it asks one uniform set of questions — identification, conflicts, source, risk, materiality, outside counsel, owners, legal hold, key dates — the same nine, every matter. | THE ANCHOR — grouped chips: Identification · Conflicts · Source / Risk · Materiality · Counsel / Owners · Hold · Dates |
| B04 | 3 mechanism | Claude reads the SKILL.md, then works the questions in order — no branching — and turns the answers into two files: matter.md and history.md, plus one structured row appended to a running log, _log.yaml. | chips: READ SKILL.md → ASK THE 9 QUESTIONS → WRITE matter.md + history.md → APPEND TO _log.yaml |
| B05 | 3 mechanism | That makes matter-intake a specification, not a judgment call. The payoff: identical intake, every matter, every lawyer. The limit: it only structures what's told to it — the decision to accept or decline the matter stays outside the file, with the human. | chips: SAME INTAKE, EVERY TIME → DECISION STAYS WITH THE HUMAN |
| B06 | **4 anchor payoff** | So matter-intake never screens a matter for you. It guarantees that whichever lawyer runs it, the same nine questions get asked and the same two files get written — that's the whole trick. | THE ANCHOR RETURNS — same grouped chips, one accented |
| B07 | **5 both directions** | Watching matter-intake come back clean on every field doesn't prove the matter is actually conflict-free — it only proves the checklist was filled in. And a flagged risk field doesn't prove there's a real problem — it may just be a case the lawyer still has to judge. | stack: EVERY FIELD CLEAN → PROVES NO CONFLICT? (struck) / ONE FIELD FLAGGED → PROVES A REAL PROBLEM? (struck) |
| **BCRY** | **6 carry-out** | A skill named matter-intake doesn't decide which matters to take — it's a fixed set of questions Claude asks and logs the same way every time, so the accept-or-decline call is still yours. | WantQuote — the sentence, alone |
| BHTF | handoff | Your turn. Paste this into Claude: pick one recurring decision you make the same way every time before it starts — like whether to open a new file, or approve a request. Write me a SKILL.md for it: plain language, the fixed questions in order. Then read it back to me and walk me through exactly what you'll ask, before you ask it. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Matter Intake. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B01 states the read; B02 breaks it — an obviously-conflicted matter still just gets logged, not declined by the skill |
| One anchor, planted early, paid off late | B03 → B06 (the nine fixed questions) |
| Both failure directions | B07 |
| No design judgment (Teardown → Plain) | Source's "design tell" / "verdict" framing ("What it gets right… what it bites…") rewritten as plain mechanism facts (B05's payoff/limit) — no verdict beat, no ranking of the skill's design choices |
| One flag | N/A — every claim here is generic, directly-stated skill mechanics carried from the source's own narration; nothing is inferred |

## Deliberately not claimed

- **No claim about what any specific intake question's wording is** — the
  source names the nine *categories* (identification, conflicts, source,
  risk triage, materiality, outside counsel, owners, legal hold, key dates)
  but never quotes the actual question text from the SKILL.md, which is not
  reachable from this machine. The reel names the categories only.
- **No ranking of whether nine questions is the "right" number** or whether
  the two-file output (`matter.md` / `history.md` / `_log.yaml`) is well
  designed — that would be Teardown judgment; Plain states the mechanism and
  stops.
- **The "obvious conflict" case in B02 is illustrative, not a documented
  test case from the source** — it is the WRONG-GUESS LAW's required
  falsifying case, built from the source's own stated fact that the skill
  only asks questions and writes files; it never asserts a decline/accept
  outcome.

## Handoff prompt (BHTF, read aloud)

> "Pick one recurring decision I make the same way every time before it
> starts — like whether to open a new file, or approve a request. Write me
> a SKILL.md for it: plain language, the fixed questions in order. Then
> read it back to me and walk me through exactly what you'll ask, before
> you ask it."

Why it's worth running: it forces the same distinction the reel just made —
a written checklist versus a judgment call — onto a decision the viewer
actually makes.

---
**GATE P — signed:** ______________________  (human)
