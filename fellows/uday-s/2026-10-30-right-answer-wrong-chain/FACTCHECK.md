# FACTCHECK — Right Answer, Wrong Chain

Status: **GATE F SIGNED — 2026-10-30. 11 rows PASS, 1 title CORRECTED,
1 on-screen claim MARKED AS REASONING rather than a cited finding.**

Commissioned as **"Process-Supervised & Multi-Hop AI Agents"**, with permission
to retitle.

## The title, corrected

The phrase joins two things that are not the same category:

| In the phrase | What it actually is |
|---|---|
| **Process-supervised** | a **supervision method** — how you grade a model's work |
| **Multi-hop** | a **task type** — a question needing several facts chained |

Putting them together as one subject implies a thing called a
"process-supervised multi-hop agent" with properties of its own. There isn't
one. What genuinely connects them is a measured failure mode — a correct answer
produced from a chain that was never followed — and that is what the retitle
names. B01 separates the two and then joins them on the evidence.

## Verified claims

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B03 | DiRe answer F1: HotpotQA **68.8**, 2WikiMultihopQA **63.4**, MuSiQue **37.8** | PASS | MuSiQue paper, Table 4, read out of the PDF text directly |
| 2 | B03 | lower is harder to cheat; the probe measures scoring while bypassing reasoning steps | PASS | the paper's own wording: these scores are "high, indicating that even disconnected reasoning (bypassing reasoning steps) can achieve such high scores" |
| 3 | B03 | MuSiQue was built to resist shortcuts | PASS | the paper's stated construction goal |
| 4 | B04 | best model scores **57.9 / 47.9 / 28.1** answer F1 on 2-, 3- and 4-hop questions | PASS | same paper: "Our best model, EX(SA), scores 57.9, 47.9, and 28.1 answer F1 on 2, 3, and 4-hop questions" |
| 5 | B04 | another model "stays around 42% irrespective of the number of hops" | PASS | same paper, same paragraph — the EE model |
| 6 | B05 | a process-supervised model solves **78%** of problems from a representative subset of the MATH test set | PASS | Lightman et al. abstract |
| 7 | B05 | "process supervision significantly outperforms outcome supervision" | PASS | same abstract, quoted on screen |
| 8 | B05 | PRM800K is **800,000 step-level human feedback labels** | PASS | same abstract |
| 9 | B05 | the method grades steps and supervises up to the first incorrect one | PASS | the paper's described reward-model setup |
| 10 | B06 | an earlier study found outcome and process supervision reaching **similar final performance** on grade-school maths | PASS | Uesato et al. 2022, as restated in the Lightman paper's own framing |
| 11 | B06 | under standard data-coverage assumptions, outcome supervision is **no more statistically difficult** than process supervision, up to polynomial factors in horizon | PASS | arXiv 2502.10581, "Do We Need to Verify Step by Step?" |

## The one on-screen claim that is reasoning, and is labelled as such

B07 argues that when agent step labels are inferred from how an episode ended,
outcome information has re-entered under a new name.

**The contrast it rests on is sourced:**
- a maths step is locally checkable, and 800,000 human step labels exist for
  that setting (rows 6–9);
- no comparable public step-label corpus for agent trajectories was found.

**The inference is mine.** A survey encountered during research attributes to
Xi et al. (2025) the point that in agentic settings the correctness of an
individual action is not clear-cut and must be estimated from eventual
outcomes — but that paper was **not retrieved directly**, so it is not cited and
no figure from it appears. B07's citation strip says on screen: *"the contrast
is sourced; the inference about agent labelling is reasoning."*

That is the honest placement. The argument is sound from the verified facts; it
is not presented as an empirical result someone measured.

## Precision notes

- **DiRe is a probe, not a leaderboard.** It measures how well a model does
  when the supporting evidence is split so no single piece suffices. The reel
  states the direction (lower is harder to cheat) on screen, because a high DiRe
  number sounds like a good score and is the opposite.
- **The 78% is on a representative subset**, not the full MATH test set, and
  the card says so.
- **No numeric margin is claimed for process over outcome supervision.** The
  abstract gives none, so the reel quotes the qualitative sentence and nothing
  more — the same discipline applied to "minimal effect on other capabilities"
  in last week's reel.
- **"~42%" is the paper's own approximation** ("stays around 42%"), and the
  bars carrying it are labelled with a tilde.
- **The MuSiQue figures come from the PDF, not a summary.** A search result had
  described the metric correctly but the paper's table is the source used. The
  DiRe metric itself originates in a separate 2020 paper by the same first
  author, which is credited in the reel's sources but supplies no figure here.

## Claims deliberately NOT made

- **No claim that any specific agent system uses outcome labels dressed as
  process labels.** B07 describes a structural risk and names no system.
- **No claim that process supervision does not work.** B05 reports its headline
  result straight, before B06 bounds it.
- **No claim about which benchmark anyone should use.**
- **No cost, compute or training-time figure** — none was verified.
- **No claim that HotpotQA or 2Wiki are bad benchmarks.** The DiRe figures
  describe shortcut availability, which is what MuSiQue was built to reduce.
