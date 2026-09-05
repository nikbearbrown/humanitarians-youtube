# An Agent That Finishes First Can Be Worse Than One That Stops — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-liam-vox-silent-omission`
("Why an Agent That Finishes First Can Be Worse Than One That Stops",
Teardown register, vox-editorial 12-beat spine) — question, facts, and
argument kept; body recompressed to one idea per beat; cold open replaced;
close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes a confident "done" means an agent checked everything. It doesn't — it only reports what it actually reached. So what happens to the part it never reached? | writer types "Claude finished the job and said it's done — so it checked everything, right?", hesitates on "everything", corrects to "only what it reached" |
| B01 | 1 stakes | An agent can read ninety files, finish the job, and report "done" — in exactly the same confident tone whether it saw everything in scope or missed a third of it. | same "DONE" stamp over two different coverage counts, 90/90 and 60/90 |
| B02 | 2 wrong guess | So the natural read: if the agent says the task is complete, it must have gone through everything there was to go through. A confident finish feels like proof of a full pass. | a checklist, a checkmark forming under "task complete" |
| B03 | **2 BREAK IT — ANCHOR PLANTED** | Here's the case that breaks it. An agent drafted a six-bullet brief with a clear recommendation, and it shipped to leadership. Two days later, someone found three dissenting documents sitting in a subfolder the agent never opened — one of them said the opposite of the recommendation. No error had ever appeared. | THE ANCHOR — a folder tree, five documents glowing teal "read", three documents in a "dissenting/" subfolder glowing crimson "unopened", a summary box glowing "COMPLETE" |
| B04 | 3 mechanism | Here's the mechanism. An agent works through a job one operation at a time: open a file, success. Summarize it, success. Move to the next, success. Each step only reports on itself. | a chain of operation boxes — READ, SUMMARIZE, NEXT — filling teal with a checkmark in sequence |
| B05 | 3 mechanism | But the agent doesn't know what it couldn't reach. A subfolder it lacked permission for. A scanned page that wouldn't parse as text. A file that scrolled past when a long listing got cut off. | the teal operation chain on the left; three crimson file icons on the right — no access, unreadable scan, not listed |
| B06 | 3 mechanism | A crash tells you something went wrong — you see the failure. A silent omission doesn't. The agent that stops and flags a file it couldn't read is giving you information. The one that quietly skips it and reports "done" is giving you none. | two columns — CRASH (a visible error box) vs. SILENT OMISSION (a green "complete" box, an arrow to "gap in brief") |
| B07 | **3 ONE FLAG** | One flag: this is about agents whose completion report only tallies successful operations. Some tools do log every skipped or unreadable file in a separate section — but you can't tell which kind you're looking at from a confident "done" alone. You have to check whether skips get surfaced at all. | THE FLAG — a single terracotta flag marker over two paths: one where a skip lands in a visible log, one where it disappears |
| B08 | 3 mechanism | Maya ran an agent over twelve client PDFs to draft a digest. It read nine — three were scanned images it couldn't parse — and reported the digest done. Those three held the revised targets. The digest shipped with the old numbers, and nothing in the report said anything was missing. | twelve file icons, nine teal "read", three crimson "scan — unreadable"; an arrow to a "DIGEST" document labeled "old targets" |
| B09 | **3 mechanism + 5 both directions — ANCHOR PAYOFF** | Go back to the six-bullet brief: ask for the inventory instead of the summary — documents in scope, documents opened, documents skipped. Three skipped against twenty-six in scope is the mismatch that catches it. But a matching inventory doesn't prove every document was read correctly, only that none went silently missing — and one skipped file doesn't mean the whole brief is wrong, just that one document needs a second pass. | THE ANCHOR RETURNS — the same folder tree, the three dissenting documents now stamped "CONFIRMED: SKIPPED"; two dimmed captions beneath |
| **BCRY** | **6 carry-out** | A confident "done" only tells you what finished — never what got skipped. Ask for the count, not just the completion. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why an Agent That Finishes First Can Be Worse Than One That Stops. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 falsifies it with the six-bullet-brief case — a confident finish can still sit on top of a folder scan that silently skipped three contradicting documents |
| One anchor, planted early, paid off late | B03 (the six-bullet brief, three unopened dissenting documents) → B09 (the same folder tree, run through an inventory check and stamped confirmed) |
| Exactly one inference flag | **B07** — the report-only-tallies-successes structure assumes the tool doesn't separately surface skips; some do, and you can't tell which from a confident "done" alone |
| Both failure directions | B09 — what a matching inventory proves (nothing went silently missing) vs. does not prove (every document was read correctly); what one skipped file does not prove (that the whole brief is wrong) |
| No design judgment | Beats describe why a confident completion isn't proof of full coverage; none rules on whether any specific agent architecture was built well |

## Deliberately not claimed

- **Not "a matching inventory proves every document was read correctly."**
  B09's first direction bounds this: the check confirms nothing went silently
  missing, not that every opened document was interpreted right.
- **Not "one skipped file means the whole brief is wrong."** B09's second
  direction bounds this: a failed check means that one document needs a
  second pass, not a verdict on the whole brief.
- **No accusation that any specific model omits more than another** — the
  six-bullet brief and Maya's example are generic illustrations of why a
  confident completion report can't stand in for a coverage count.

## Handoff prompt (BHTF, read aloud then discussed)

> "I'm using an agent to process a folder of files and summarize them. Give
> me the exact three questions to ask afterward — about scope, what was
> processed, and what was skipped — so I can catch anything it silently
> missed, and tell me what a mismatch should make me do next."

Why it's worth running: naming the exact three questions — scope, processed,
skipped — turns "I trust the summary" into a five-minute check you can
actually run before you act on the report.

---
**GATE P — signed:** ______________________  (human)
