# Week 25 — Topic Selection

**Selected:** `claude-for-education/reinforcement-learning-an-introduction`
**Source:** Nik Bear Brown's book review of *Reinforcement Learning: An Introduction* (Sutton & Barto)
**Decided:** 2026-10-01

---

## How the topic was chosen

This is the same method as Week 24: a randomized draw over the singleton pool of
`humanitarians-youtube`, meaning topics that appear **exactly once** across the whole library
once naming variants are normalized.

### Fresh, isolated snapshot

- `git ls-remote --heads origin`: 55 live heads (54 fellow branches + `main`), saved in `_selection/heads.txt`
- `git clone --bare --reference <local checkout>` into the session scratchpad. Every command after
  that was `for-each-ref` / `ls-tree` / `show` / `grep` / `diff --name-only` / `log` against
  that mirror. Nothing was checked out, fetched into, pushed, or modified in `humanitarians-youtube`.
- Snapshot `main` = `5716c413f` (2026-10-01 00:11).

### Sweep (`_selection/sweep.py`, unchanged from W24)

`main`: **4,866** topic folders, plus **202** that exist only on fellow branches, for a combined
library of **5,068**. Those normalize to **2,899** keys, of which **1,791** are singletons.

### Exclusions, in order (`_selection/pool.py`)

| Filter | Removed |
|---|---|
| Not a `claude-for-*` collection | 1,320 |
| Collection used in Weeks 20–24 (quantum-mechanics, cancer, cancer-biology, mathematics, computer-science, **design**) | 399 |
| One of our own past sources (W17–W24) | 0 |
| Exists only on a fellow branch | 4 |
| Production evidence on `main` (SRT/VTT, YouTube metadata, BUILD-LOG, FACTCHECK, QC, STATUS, PROOF, MP4, concat) | 19 |
| Variant copy elsewhere under stricter normalization (`--` compound names, `-lecture`/`-mycroft`, chapter prefixes) | 30 |
| Near-duplicate by title-token overlap | 6 |
| Touched on any fellow branch (`diff main...<branch>`) | 0 |
| Fellow-authored source (`**Author:**` line) | 2 |
| Near-duplicate clusters W24 already documented: Subby ×2, fairness ×2, educational-sandbox | 5 |
| **Final pool** | **6** |

The pool is small because `claude-for-design`, which supplied most of W24's 130, is now excluded
as a used collection.

### Draw

`random.SystemRandom().shuffle` over the 6, unseeded. The full order is in `_selection/draw.json`:

```
1. claude-for-education/reinforcement-learning-an-introduction   <- ACCEPTED
2. claude-for-artificial-intelligence/ch80-lecture
3. claude-for-music/river-mumma-calling-how-a-song-crosses
4. claude-for-music/five-senses-one-song
5. claude-for-music/how-music-works-audible
6. claude-for-music/the-song-that-lied-to-you
```

---

## Uniqueness verification: `reinforcement-learning-an-introduction`

| Check | Result |
|---|---|
| Normalized key library-wide | appears **once** |
| History | a single commit, `e6e678cc9` 2026-08-27, Nik Bear Brown, "Integrated repository snapshot" (bulk import) |
| Source author | Nik Bear Brown, Founder, Humanitarians AI. **Not a fellow** |
| Build state | unbuilt 10-beat Kore auto-conversion: README, BUILD-PROMPT, SOURCES, beat_sheet only; no FACTCHECK, BUILD-LOG, SRT or YouTube metadata. The README topic label reads "GAME DESIGN" (template artifact) |
| Grep of `main` for `Sutton`, `Barto`, `short corridor`, `policy gradient` | only this folder, the `claude-for-education/README.md` index row, and unrelated `terms.json` place names |
| Same grep on every file changed on the 13 fellow branches that diverge from `main` | **zero hits** |
| Our own Weeks 1–24 | **zero hits** |

**Adjacent work, noted as boundaries:**

- `fellows/kehinde-o/2026-09-08-the-target-that-moved`: a fellow's DQN work video (a frozen target
  network takes Lunar Lander from −391 to −13.9 mean reward). It covers **value-based** RL stability,
  so this film must not restage the "moving target" fix.
- `claude/behind-the-model/*` and `fellows/aishwarya-p/2026-09-18-why-ai-models-refuse` cover
  **RLHF** for language models. That's a different subject from the book's core RL theory, and
  this film stays off it.

## What the source offers

The three checkable claims in `SOURCES.md`:

1. The short-corridor example (S&B Fig. 13.1): ε-greedy action-value methods are stuck with
   deterministic extremes (−44 / −82), while policy gradient finds the optimal **stochastic** policy
   (≈59% right).
2. An online-learning workload controller: +19% over the best conventional controller,
   closing 27% of the gap to the optimum.
3. AlphaGo: 30M expert moves, policy-gradient RL, value networks and MCTS beat Lee Sedol 4–1.

Everything still has to go through FACTCHECK against the book itself (2nd ed., 2018).

## Not yet decided

- Angle, structure, title, beat count
- The angle must also pass the narration audit against W15–W24 (see the work-video uniqueness
  rule) before scripting
