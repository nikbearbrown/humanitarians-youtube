# FACTCHECK — vox-bainbridge-irony

Source chapter: `claude-agentic-ai/chapters/00-the-agent-arrives-in-ordinary-work.md`

---

## Claims audit

| Claim | Verdict | Source / note |
|---|---|---|
| Bainbridge (1983): the more capable the automated system, the more demanding the supervisory role | ✓ | Chapter 00: "Her observation was precise: the more capable the automated system, the more demanding the supervisory role, not less (Bainbridge, 1983)." |
| More automation creates new monitoring demands, new failure modes, new intervention responsibilities | ✓ | Chapter 00: "More automation creates new monitoring demands, new failure modes, new intervention responsibilities." |
| The AI agent does not reduce your role — it relocates it: upstream into design, and at checkpoints into verification | ✓ | Chapter 00: "The AI agent does not reduce your role. It relocates it — upstream into design, and at checkpoints into verification." |
| Developer delegates bug repair; agent reads, edits, reruns tests, reports resolved | ✓ | Chapter 00 example (code repair workflow): "The agent observes failing tests, edits the relevant files, reruns the tests, and reports the diff." |
| After agent finishes, developer must read diff, verify test results, decide on edge cases | ✓ | Derived from chapter 00 code repair workflow — the human reviews what changed before it leaves |
| Priya example: without agent — 20 files, 20 decisions; with agent — 200 files, 5 upstream decisions | ILLUSTRATIVE | Candidate card example seed. Numbers are illustrative; the principle is from chapter 00. Labeled illustrative. |
| A wrong scope statement at the start of an agent task is many wrong moves at scale | ✓ | Derived from chapter 00's discussion of blast radius and scope |
| Lisanne Bainbridge named this dynamic in 1983 | ✓ | Chapter 00, Sources: "Bainbridge, Lisanne. 'Ironies of Automation.' Automatica, 1983." |

---

## Exclusions confirmed

- No history of industrial automation (Bainbridge referenced only by name and year, mechanism only). Pass.
- No Parasuraman levels-of-automation formalism (no LOA scale, no Parasuraman taxonomy). Pass.
- No discussion of specific Claude surfaces (Code, Cowork, etc.). Pass.

---

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| supervisory role / supervisory load | B02 (shown), B06 (named) | B01 shows the delegated work; B02 shows the human's new task list |
| upstream | B09 (THE PRACTICE) | B05 explains work is "relocated" — B09 shows where it goes |
| scope statement | B09 (THE PRACTICE) | B07 shows the Priya example of what scope decisions look like |
