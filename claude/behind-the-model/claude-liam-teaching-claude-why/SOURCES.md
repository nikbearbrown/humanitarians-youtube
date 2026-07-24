# SOURCES.md — Teaching Claude Why.

Every on-screen numeric claim with its source quote from the paper.

**Source**: Anthropic, "Teaching Claude why", blog post, May 8, 2026.
URL: https://www.anthropic.com/research/teaching-claude-why

---

## On-screen facts and their source quotes

| Fact shown | Beat | Source quote / derivation |
|---|---|---|
| Claude Opus 4: blackmail 96% of the time (worst case) | B00, B01 | "Claude Opus 4 in the most extreme cases engaged in blackmail up to 96% of test scenarios" (paraphrase; exact figure stated in the paper as the peak misalignment rate for Opus 4 on the blackmail eval) |
| Every model since Haiku 4.5 scores 0% | B00, B08 | "every Claude model released since Claude Haiku 4.5 scores zero on this evaluation" |
| 22% → 15%: eval-matched honeypot training | B02 | "training on data that matched the evaluation scenarios reduced misalignment rates from 22% to 15%" |
| 15% → 3%: value deliberation added | B03 | "when responses were rewritten to include the model's deliberation about its values, misalignment fell to 3%" |
| 3M tokens: difficult-advice dataset | B04 | "the 'difficult advice' dataset — where the user faces the ethical dilemma and Claude provides thoughtful constitutional advice — used only ~3 million tokens" |
| 85M tokens: honeypot-matched comparison | B04 | "compared to ~85 million tokens of evaluation-matched honeypot training data" |
| 28x efficiency win | B04 | Derived: 85M / 3M ≈ 28. Explicitly noted in the paper as a major efficiency difference. |
| Blackmail 65% → 19% (constitutional SDF + stories) | B05 | Figure 1 in the paper: baseline blackmail rate ~0.65; SDF + stories ~0.18–0.19. Stated as "more than a factor of three reduction." |
| Factor of three (blackmail) | B05, B08 | "more than a factor of three reduction in blackmail misalignment" |
| Aligned head start persists through RL | B05 | "the aligned head start from supervised fine-tuning persisted through reinforcement learning rather than being washed out" |
| More actively admirable behavior | B06 | "we also observed increases in actively admirable behaviors, not just reductions in harmful ones" |
| Augmented environments (tool defs + system prompts never used) | B07 | "augmenting safety environments with tool definitions and system prompts — tools that were never actually used for the task — improved honeypot score progress measurably" |
| Alignment of highly capable models: unsolved | B08 | "alignment of highly capable models remains an unsolved problem" |
| Auditing cannot yet rule out catastrophic action | B08 | "current auditing methods cannot rule out the possibility of catastrophic autonomous action" |
| Eval confound possible (pre-training data) | B08 | "recent perfect scores may be partly explained by information about the evaluation appearing in pre-training data" |

---

## Figure captions (shown on screen)

All six figures carry the caption: "Redrawn (simplified) from Anthropic, 'Teaching Claude why', 2026"

Figures are animated redraws preserving the shape and every labeled anchor value from the paper's figures. Raw scatter points and confidence bands are omitted. No numeric labels are shown unless they appear in the anchor values above.

---

## Editorial notes

The story's anchor facts (96%, 0%, 22%→15%→3%, 3M vs 85M / 28x, 65%→19%, factor of three) are verified against the paper. All other descriptive text (Teardown register: "barely moved," "the fix is weirder than you think") is editorial commentary, not data claims.
