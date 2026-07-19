# FACTCHECK — code-runs-ships-wrong

Every claim in narration, viz, and card copy verified against source chapter and primary sources.

---

## Claims Table

| Beat | Claim | Verdict | Source / Notes |
|------|-------|---------|----------------|
| B01 | Seth writes GPA-ranking function with Claude, tuple sort key (-gpa, last_name) | ✓ illustrative | Chapter 02, the author's own worked example — labeled composite |
| B01 | All test rows have unique GPAs, tests pass | ✓ illustrative | Chapter 02 |
| B01 | Bell and Adams tie, Bell comes back first, spec said alphabetical | ✓ illustrative | Chapter 02 |
| B03 | Claude has seen standard binary search written ten thousand times | ✓ editorial | Chapter 02: "It has seen the standard binary search written ten thousand times" |
| B03 | AI assistance raised average productivity 14%, novices 34% (Brynjolfsson et al.) | NOT IN NARRATION — excluded | Chapter 02 cites this; excluded from this film per card scope |
| B05 | Same weights write and audit — audit is not independent | ✓ | Chapter 02: "the same weights that produced the output are the only weights available to do the audit" |
| B05 | If production was confidently wrong, audit will be confidently wrong in same direction | ✓ | Chapter 02 direct |
| B07 | Priya builds leaderboard, sorts by score descending, 12 unique scores, deploys | ✓ illustrative | Chapter 02 example seed from card — labeled composite |
| B07 | Zhao above Amir at tie, spec said alphabetical on ties | ✓ illustrative | Chapter 02 example seed |
| B07 | Bug was in the code the day it was written | ✓ | Chapter 02 direct: "The bug was in the code the day it was written." |
| B08 | Bug invisible because test set had all unique scores | ✓ | Chapter 02 |
| B09 | Claude's solve speed rising steeply; human verification roughly flat | ✓ | Chapter 02: "Claude's solve speed is rising fast... your verification speed is approximately constant" |
| B09 | "Your job is not to solve faster. Your job is to verify better." | ✓ | Chapter 02, near-verbatim |
| B10 | "Name the supervisory capacity before accepting" | ✓ | Chapter 02: "Before accepting a Claude output, name the supervisory capacity the step requires." |
| B11 | Run Two: problem formulation, plausibility audit, specific failure description, fix | ✓ illustrative | Chapter 02 "The Same Function, Run Twice" — labeled composite |
| B12 | "The model is fine. The supervision is missing." | ✓ | Chapter 02, verbatim last line |

---

## Illustrative Numbers

- Seth's sort function, Bell/Adams tie — illustrative (chapter 02 author's own example)
- Priya's 12 unique scores, Zhao/Amir tie — illustrative (chapter 02 example seed)
- Run Two sequence — illustrative composite (chapter 02 "The Same Function, Run Twice")

---

## Terms Table

| Term | Debut beat | Prior beat that creates need |
|------|-----------|------------------------------|
| pattern completion | B03 | B03 (first context — Claude's strength) |
| plausibility auditing | B06/B10 | B05 (same-weights limitation established) |
| problem formulation | B10 | B08 (gap between test and real requirement shown) |
| supervisory capacity | B10 | B09 (solve/verify split established) |
| dangerous middle | B12 (implied) | B08/B09 (the region where pattern work = judgment in disguise) |

---

## Exclusions Confirmed

- NO formal proof theory ✓
- NO full LLM hallucination taxonomy ✓
- NO Copilot vulnerability statistics (Pearce et al. referenced in chapter but not in this film) ✓
- NO RAG discussion ✓
- NO Brynjolfsson productivity statistics ✓ (excluded per scope)
