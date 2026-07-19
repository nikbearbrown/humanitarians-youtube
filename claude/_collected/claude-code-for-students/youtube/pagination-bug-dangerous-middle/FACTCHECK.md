# FACTCHECK — pagination-bug-dangerous-middle

---

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Seth writes a pagination function; tests at 50, 100, 247 items all pass; commits | ✓ illustrative | Chapter 09: "Page 1 of 50, page 2 of 100... 247 items across 5 pages. Seth ticked the box. He committed." |
| B01 | Avery joins session with 251 items; page 6 returns empty; flashlight missing | ✓ illustrative | Chapter 09: "Avery joined a session... the host's inventory had grown to exactly 251 items... Page 6 returned an empty array. The 251st item — a flashlight..." |
| B03 | Calling loop uses `while page.size() == size` as termination; 251 causes early stop | ✓ illustrative | Chapter 09: "the calling loop used `while page.size() == size` as its termination condition" |
| B03 | Bug fires when total = page_size × n + 1 (e.g., 251 = 50 × 5 + 1) | ✓ | Chapter 09: direct logical consequence of the calling loop termination condition |
| B04 | The dangerous middle = code compiles, passes, looks right, is wrong in a way you weren't equipped to see | ✓ | Chapter 09: "The dangerous middle is the region of Claude's output where the code compiles, runs, passes the tests the student thought to write, and matches the style of the codebase — but is wrong in a way the student is not equipped to see." |
| B06 | A handoff condition is specific, testable, and binary | ✓ | Chapter 09: "It is specific... It is testable... It is binary." (three-property definition) |
| B07 | Handoff condition lives in the prompt before Claude runs the step, not in post-hoc review | ✓ | Chapter 09: "The handoff condition lives in the prompt, before Claude runs the step. Not after. Not as a code review. The condition you write before is the condition that constrains what Claude builds." |
| B08 | Priya's leaderboard: 41 players, 41st never appears, test set was multiples of 20 | ✓ illustrative | Chapter 09 example seed from video-ideas.md |
| B10 | "The most dangerous output passes every test you thought to write" | ✓ | Chapter 09 paraphrase: "It is not the easy bug... not the impossible bug... It is the middle." |

---

## Illustrative Numbers

- Seth's 247-item test, 251-item fail — illustrative (chapter 09)
- Avery's flashlight — illustrative (chapter 09)
- Priya's leaderboard, 41 players — illustrative composite (video-ideas.md)

---

## Terms Table

| Term | Debut beat | Prior beat creates need |
|------|-----------|------------------------|
| dangerous middle | B04 | B01-B03 (the bug lives in a specific gap the tests didn't cover — the gap is the dangerous middle) |
| handoff condition | B06 | B05 (joint failure established — the missing contract at the joint is what a handoff condition names) |

---

## Exclusions Confirmed

- NO formal Hoare-triple proof notation ✓
- NO security vulnerability taxonomy (slopsquatting is candidate 08) ✓
- NO property-based testing frameworks ✓
- NO Pearce et al. / Spracklen statistics cited in narration ✓
