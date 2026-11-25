# Fellowship renewal: Charitha Sree Veluru, MoE Causal Atlas (Medhavy)

**Request:** please renew my fellowship from **12/01/2026 through 01/31/2027**. My current agreement runs 09/01/2026 – 11/30/2026 and ends **11/30/2026**. This report covers **Aug 31 – Nov 22, 2026**.

**Fellow:** Charitha Sree Veluru · Unique ID 271 · GitHub [@VelCharitha77](https://github.com/VelCharitha77) · fellows folder [`fellows/charitha-v`](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/charitha-v)

---

## Completed results

1. **Interactive physics figures, Physics Vol. 1 (Aug 31 – Sep 13).** I built the interactive canvas simulations for Chapter 4, placed each one beside the figure it illustrates, and rolled the simulation contract out book-wide.
   - Evidence: [commit 2bc49aa, Sep 7: sims added in all chapters](https://github.com/Medhavy/physics-vol-1/commit/2bc49aa)
   - Episodes: [2026-08-31 green build, broken demo](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/charitha-v/2026-08-31-why-a-green-build-still-ships-a-broken-physics-demo) · [2026-09-07 sim contract book-wide](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/charitha-v/2026-09-07-what-shipped-when-chapter-4s-sim-contract-went-book-wide)

2. **MoE Causal Atlas: research design and gate experiments (Sep 14 – Nov 22).** I wrote the research plan and pre-registration, built the G0 gate scripts, and caught a masking bug that would have produced a fake "no collapse" result. I then completed and reproduced the G0(b) collapse experiment: pruning Moonlight-16B to 50% of its experts drops ARC-Easy from 0.96 to 0.615 and GSM8K from 0.83 to 0.16, and all 15 results reproduced exactly on a second node.
   - Evidence: [plan v0.1 b713a3f](https://github.com/GeneralMing/moe-causal-atlas/commit/b713a3f) · [masking fix 4216dc5](https://github.com/GeneralMing/moe-causal-atlas/commit/4216dc5) · [G0(b) done d54b861](https://github.com/GeneralMing/moe-causal-atlas/commit/d54b861) · [reproduction a26f677](https://github.com/GeneralMing/moe-causal-atlas/commit/a26f677)

3. **Weights scan, published-labels dataset and next-study plan (Nov 16 – 22).**
   - Scanned 11 public MoE checkpoints with byte-range reads (about 28 GB, no GPU).
   - Built a dataset of 395 published pruning results from 18 papers, independently re-checked, with 18 corrections logged.
   - Ran a pre-specified join analysis (ρ = 0.30, n = 5) and turned the result into the D4 homogeneous-label plan, with a power simulation.
   - Evidence: [labels aa29d5c](https://github.com/GeneralMing/moe-causal-atlas/commit/aa29d5c) · [join analysis cbb3528](https://github.com/GeneralMing/moe-causal-atlas/commit/cbb3528) · [D4 plan 2fcb0a6](https://github.com/GeneralMing/moe-causal-atlas/commit/2fcb0a6)

Both project repositories (`Medhavy/physics-vol-1`, `GeneralMing/moe-causal-atlas`) are private. I can grant read access to anyone who needs to open the commit links.

## Hours status

At least 20 hours worked in every reported week. Per-week evidence is in the index below.

## Degree relevance and supervision

The work is graduate-level machine learning research and engineering: experimental design, pre-registration, statistics (exact McNemar tests, rank correlation, power simulation), large-model evaluation on an HPC cluster, and interactive simulation software. It applies directly to my graduate degree at Northeastern University. Supervisor: Nik Bear Brown.

## Next period (12/01/2026 – 01/31/2027)

| Deliverable | Target date |
|---|---|
| Pre-registration lock decision recorded in PREREG.md | Dec 5, 2026 |
| Hugging Face revisions pinned for every G0(c) checkpoint | Dec 12, 2026 |
| G1 random-vs-criteria pilot run and written up | Dec 19, 2026 |
| D4 label harness, Phase A, verified on all 5 architecture classes | Jan 16, 2027 |
| arXiv note draft, reviewed with CRITIQ | Jan 30, 2027 |
| Every week: two Brutalist videos, a Frictional log entry, and `slides.html` in a dated folder | Weekly from Dec 1 |

## Outstanding issues

- **Weekly videos from Oct 5.** Each week's video is one topic in two formats (16:9 and 9:16), not two distinct videos. The Oct 5 – Nov 22 videos were produced and uploaded on Nov 23. From Dec 1 I will post two distinct videos each week.
- **Missing dated work records.** For Sep 28 – Oct 4 and Oct 12 – Nov 15, the only dated record is the video. There are no dated commits or log entries for those weeks.
- **Frictional logs.** These start with this folder's [FRICTIONAL.md](./FRICTIONAL.md). Earlier weeks don't have one.

---

## Weekly evidence index

Each video has a 16:9 and a 9:16 version. Every Drive link opens for anyone who has it.

| Week | Hours | Videos | Log and work evidence |
|---|---|---|---|
| Aug 31 – Sep 6 | 20+ | Ch. 4 video 1 [16:9](https://drive.google.com/file/d/1ploT53hYg8Bbc4JRAb_--LAHV3YQlcbi/view) · [9:16](https://drive.google.com/file/d/1cPBg9fJ4KP6IrV2-RRzgxsOZx5GBiGm8/view) · Ch. 4 video 2 [16:9](https://drive.google.com/file/d/1vXNi9CpgmgVIbsH0fM0k7TMj9HTWGZ-6/view) · [9:16](https://drive.google.com/file/d/1sJ27h73gHRB1LYRb3FFfi_faAY8CB1vj/view) | [2026-08-31 episode folders](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/charitha-v) · [physics commit 30f066b](https://github.com/Medhavy/physics-vol-1/commit/30f066b) |
| Sep 7 – 13 | 20+ | Book-wide video 1 [16:9](https://drive.google.com/file/d/1YNgRVQjSq6Gb_xJc5VrcRBH5qYnlt9hH/view) · [9:16](https://drive.google.com/file/d/1Ye9NQ0B3syGpRhvwwNQQ0Pf66pQBSYor/view) · Book-wide video 2 [16:9](https://drive.google.com/file/d/1NrZQ6Thc29LDIA8ZYmv1TS0KztH4EE04/view) · [9:16](https://drive.google.com/file/d/11d8ydQtbnvys9XLwmsVJlRWBfHWT83vq/view) | [physics commit 2bc49aa](https://github.com/Medhavy/physics-vol-1/commit/2bc49aa) · [2026-09-07 episode folders](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/charitha-v) |
| Sep 14 – 20 | 20+ | Physics video 1 [16:9](https://drive.google.com/file/d/1auN1oU2trJSGiWd8M3eH6DPrTQA2pozc/view) · [9:16](https://drive.google.com/file/d/17YxTponk0xyQqLEFJT6e8z3mvEG741wj/view) · Physics video 2 [16:9](https://drive.google.com/file/d/19obrmJ2rK5pXzQdG1RH8SaDOPSJar-6E/view) · [9:16](https://drive.google.com/file/d/1HVv_H0mUyzCj0NF7SrWEubHXgZwKAOyI/view) | [plan v0.1 b713a3f](https://github.com/GeneralMing/moe-causal-atlas/commit/b713a3f) · [plan v0.2 2ddb328](https://github.com/GeneralMing/moe-causal-atlas/commit/2ddb328) · [G0(a) gate 4ef047d](https://github.com/GeneralMing/moe-causal-atlas/commit/4ef047d) |
| Sep 21 – 27 | 20+ | Physics video 3 [16:9](https://drive.google.com/file/d/1kvISCvrpAmahUo1erW0e2WcfmiE8to12/view) · [9:16](https://drive.google.com/file/d/1AxpqX9lBpM0LOYl4SUoW-BCqR59R3Q3U/view) · Physics video 4 [16:9](https://drive.google.com/file/d/1s912wRwZVFMPSkVJz8m0OcQJez-LIhGs/view) · [9:16](https://drive.google.com/file/d/17giaLcWcyQMsDRdWOv_g_S2AmPAvSGqh/view) | [masking fix 4216dc5](https://github.com/GeneralMing/moe-causal-atlas/commit/4216dc5) · [G0(d) 8357564](https://github.com/GeneralMing/moe-causal-atlas/commit/8357564) · [G0(c) scanner 12e07e3](https://github.com/GeneralMing/moe-causal-atlas/commit/12e07e3) · [explainer 5227c4e](https://github.com/GeneralMing/moe-causal-atlas/commit/5227c4e) |
| Sep 28 – Oct 4 | 20+ | Physics video 5 [16:9](https://drive.google.com/file/d/1CUoYIKBotp_Y3NKPWoJuRJGWa34FfWvP/view) · [9:16](https://drive.google.com/file/d/1kXkNnHjXwq_Gzwscjl8kpBor5uEV9TtE/view) · Physics video 6 [16:9](https://drive.google.com/file/d/1MZ9Jbynq6oYuW4V5Pz3K7tzSAmhKkRCm/view) · [9:16](https://drive.google.com/file/d/1nh0Iv9ud-2UtiGnzC7mvnoixyqCjw0vz/view) · Physics video 7 [16:9](https://drive.google.com/file/d/1mvg4wIOqpsSo3wBgC27pxpKh56FMurCe/view) | Videos only (uploaded Oct 4) |
| Oct 5 – 11 | 20+ | MoE video 1, *Check the Proxy Before You Trust It* [16:9](https://drive.google.com/file/d/1AhNfJmxfhsZw3Zg-lHwgzswNkdYudEDa/view) · [9:16](https://drive.google.com/file/d/1det-cXdkbbDOlp98USmqaSXLtp58EeQt/view) | [physics commit cc1bf92](https://github.com/Medhavy/physics-vol-1/commit/cc1bf92) |
| Oct 12 – 18 | 20+ | MoE video 2, *The Fix That Did Nothing* [16:9](https://drive.google.com/file/d/1zQh87NLrNp9qPzkzYhOXsOLIhYo2zAZn/view) · [9:16](https://drive.google.com/file/d/1zWICjGYIRb41dIgna_dccv8_v54TcArj/view) | Video only |
| Oct 19 – 25 | 20+ | MoE video 3, *Scratch Is Not Storage* [16:9](https://drive.google.com/file/d/1oEXGkVOV1pROzaT8z1cbm9oVhkNkQvOa/view) · [9:16](https://drive.google.com/file/d/1lqMCZYBxQxaguvuFfDMInjI8Eal-juLs/view) | Video only |
| Oct 26 – Nov 1 | 20+ | MoE video 4, *Read Only the Bytes You Need* [16:9](https://drive.google.com/file/d/1C8j2P2Dk6_HujGbXLGQuqhmOdHH1TmBe/view) · [9:16](https://drive.google.com/file/d/1Y4LQpEy0UiaJM88rJ5W2tDoiyeQjVE_y/view) | Video only |
| Nov 2 – 8 | 20+ | MoE video 5, *Measure the Network Before You Blame the Library* [16:9](https://drive.google.com/file/d/1fj8vrqXdOUjeVZFZH-pDVlgVZIZcGLM4/view) · [9:16](https://drive.google.com/file/d/1P15uRuh1Msqb1-oEdW7Y6c0U12xbB0PX/view) | Video only |
| Nov 9 – 15 | 20+ | MoE video 6, *Write the Rule Before You Read the Result* [16:9](https://drive.google.com/file/d/1wPQn3VBo1VOIW50Ee1FDkZ5ya1JyPVcl/view) · [9:16](https://drive.google.com/file/d/1C8qgHI1zbWlu4xl-UWW-Hzrh-couVbXw/view) | Video only |
| Nov 16 – 22 | 20+ | MoE video 7, *Count Models, Not Rows* [16:9](https://drive.google.com/file/d/1r1YiNL7vUa94aq6yIfIqD4UiuDk1qt-U/view) · [9:16](https://drive.google.com/file/d/1r7lL-8_wS77lxx_UnaeqfMgiKQZfH0mm/view) | [G0(b) done d54b861](https://github.com/GeneralMing/moe-causal-atlas/commit/d54b861) · [reproduction a26f677](https://github.com/GeneralMing/moe-causal-atlas/commit/a26f677) · [labels aa29d5c](https://github.com/GeneralMing/moe-causal-atlas/commit/aa29d5c) · [join cbb3528](https://github.com/GeneralMing/moe-causal-atlas/commit/cbb3528) · [D4 plan 2fcb0a6](https://github.com/GeneralMing/moe-causal-atlas/commit/2fcb0a6) · [FRICTIONAL.md](./FRICTIONAL.md) |
