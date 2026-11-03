# Week 24 — Topic Selection

**Selected:** `claude-for-design/introducing-theoristai`
**Underlying question:** Gardner's 1983 multiple-intelligences framework never had to ask which
intelligences technology endangers — so which ones does it endanger now?
**Decided:** 2026-09-26

---

## How the topic was chosen

A randomized draw over the singleton pool of `humanitarians-youtube`: topics that appear
**exactly once** across the whole library after naming variants are normalized.

### Fresh, isolated snapshot

The local checkout's remote-tracking refs were stale: `main` and most fellow branches had
moved since Week 23, and new branches had appeared (`komal-bg/2026-09-25-weekly`,
`kehinde-o-2026-09-24`). To read current state without touching the shared checkout:

- `git ls-remote --heads origin` to list the live branch tips (46 fellow branches + `main`)
- `git clone --bare --reference <local checkout>` into this session's scratchpad: a
  throwaway mirror, separate from the working repo
- Every command after that was `ls-tree` / `show` / `rev-parse` / `grep` / `log` /
  `diff --name-only` against that mirror. Nothing was checked out, fetched into, pushed, or
  modified in `humanitarians-youtube`. Snapshot `main` = `8e32b5fae`.

### Sweep

- A topic folder is any directory holding `beat_sheet.json`, `PEDAGOGY.md`, `FACTCHECK.md`,
  `BUILD-LOG.md`, `BUILD-NOTES.md`, `STATUS.md` or `SCRIPT.md`, with `short/`, `media/` and
  similar tooling subfolders stripped off.
- `main`: **4,697** topic folders. Across all 46 fellow branches: **224** more that exist
  only on a branch (fellow work in progress). Combined library: **4,921**.
- Normalized names: lowercase; stripped `nbb-`, `claude-liam-`, `medhavy-(vox-)`, `vox-`,
  `cli-`, `hai-`, `riff-`, `qmcg-`, `qmN-`, `volN-`, date/number prefixes, and `-vox`,
  `-4k`, `-final`, `-vN`, `-rebuild`, `-short`, `-lecture`, `-mycroft` suffixes; took the
  last `--` segment of compound names such as `branding-and-ai--youtube--X--short`.

### Exclusions, in order

| Filter | Removed |
|---|---|
| Not a `claude-for-*` collection (`fellows/`, `claude/`, `codex/`, etc.) | 1,223 |
| Collection we used in Weeks 20–23 (quantum-mechanics, cancer, cancer-biology, mathematics, computer-science) | 170 |
| Production evidence on `main` (SRT, YouTube metadata, BUILD-LOG, FACTCHECK, QC, STATUS, PROOF, MP4, concat) | 42 |
| Exists only on a fellow branch | 4 |
| Numbered Remotion audit folders (`claude-for-design/0015` …); tooling, not topics | 53 |
| A variant copy exists elsewhere after the stricter normalization (e.g. `branding-and-ai--youtube--*`, `unreal-reels--*`, `ai1-*-lecture`) | 44 |
| Near-duplicate by title-token overlap (≥ 0.5 Jaccard or ≥ 3 shared tokens) | 15 |
| Near-duplicate clusters the token check missed: 80-days ×4, Subby ×2, Calling Bullshit ×2, Rithanya ×2, fairness ×2, educational-sandbox | 13 |
| **Final pool** | **130** |

None of our own past sources is in the pool: W17 `nbb-cli-agent-self-verification-failure`,
W18 `claude-liam-bs-01-pick-and-scope`, W19 `indie-on-the-pitch`, W20
`cli-vol3-hard-sphere-crosssection`, W21 `hot-cold-excluded-tumors`, W22
`why-120-bpm-works-the-hidden-mathematics`, W23 `chinese-room-explainer-vox`.

### Draw

`random.shuffle` over the 130, unseeded (system entropy). Full order is in
`_selection/draw.json`. First ten:

```
1. claude-for-design/nintendos-family-friendly-platform   <- REJECTED: fellow-authored source
2. claude-for-design/the-paper-trail-in-the-studio        <- REJECTED: fellow-authored source
3. claude-for-design/introducing-theoristai               <- ACCEPTED
4. claude-for-design/the-testimony-machine-ai-empathy
5. claude-for-design/the-builder-who-said-no              (fellow-authored)
6. claude-for-design/what-you-cant-see-is-killing-you     (fellow-authored)
7. claude-for-design/free-the-em-dash
8. claude-for-design/pattern-language-for-game-design     (fellow-authored)
9. claude-for-design/how-light-works-and-why-it-controls  (fellow-authored)
10. claude-for-design/review-david-and-goliath-underdogs
```

**Why draw 1 was rejected.** Its `SOURCES.md` credits the article to *Seth Brown —
Humanitarians AI Fellow*. Many `claude-for-design` folders are auto-converted Substack posts
written by fellows. A video built on one would restage that fellow's own argument, which
fails the uniqueness rule even though no fellow has built a video on it. I then checked the
`**Author:**` line for every pool topic (`_selection/authors.json`): **44 of 130** are
fellow-authored, and all 44 are excluded. Draw 2 is also Seth Brown's. Draw 3 is the first
one that survives.

---

## Uniqueness verification: `introducing-theoristai`

| Check | Result |
|---|---|
| Normalized key library-wide | appears **once** |
| `beat_sheet.json` blob on every branch | same `git rev-parse` hash as `main` on **all 46 fellow branches**, so no fellow has touched or extended it |
| History | a single commit: `e6e678cc9` 2026-08-27, Nik Bear Brown, "Integrated repository snapshot" (bulk import) |
| Source author | Nik Bear Brown, Founder, Humanitarians AI. **Not a fellow** |
| Build state | README says `beat sheet authored`; there is no FACTCHECK, BUILD-LOG, SRT or YouTube metadata. It is an unbuilt 10-beat, ~1:22 Kore auto-conversion |
| Grep of `main` for `theorist.ai`, `multiple intelligences`, `gardner` | only this folder, its README/conversion-log rows, one manifest row (below), and unrelated `terms.json` entries ("Gardner equation", etc.) |
| Same grep on every file each fellow branch added or changed vs `main` | **zero hits** |

**Adjacent idea, noted as a boundary.** `PROFILES-BATCH-MANIFEST.md:337` and
`essay-video-ideas.md` C27 list "Knowing Enough to Distrust the Machine" (NortheasternISE,
no individual byline). It is only an idea entry, with no folder, and it was skipped in the profiles
batch. It marks a line this video must not cross: the angle here is Gardner's taxonomy under
machine competition, **not** "schools teach the wrong things."

> **Correction, 2026-09-26 (source capture).** This entry originally called C27 a *different*
> article. It isn't. The live Humanitarians AI post "Introducing Theorist.ai" carries the subtitle
> **"Knowing Enough to Distrust the Machine"**, so C27 is the **same essay**, cross-posted to
> NortheasternISE. The uniqueness verdict is unchanged: C27 is an unbuilt idea entry, and no fellow
> or folder has built a video on it. But it confirms the boundary is the essay's *own* main thesis
> (the education mismatch), which this film deliberately doesn't take up. The film builds on the
> essay's one sentence about Gardner, not on its argument about schools.

---

## State of the existing source

The folder is a template auto-conversion, not a finished video:

- 10 beats, and 3 of 7 content slots were filled in the build metadata (`"filled": 3, "of": 7`)
- The substance is three lines: "not obsolescence, its opposite"; the forklift extends the
  human rather than replacing them; Gardner (1983) didn't have to ask which intelligences
  technology endangered, because none were threatened then
- The rest is boilerplate: "why this matters", program credit, "paste this into Claude" handoff
- `SOURCES.md`: "no statistics detected in article". No primary sources and no fact-check

So there is no fellow's finished work to differentiate from. What's there is raw material
with a real, checkable question underneath it.

---

## Candidate angle (not yet decided, and must survive FACTCHECK first)

The source argues by assertion. The checkable version asks: take Gardner's own list of
intelligences (*Frames of Mind*, 1983; later additions) and ask, one intelligence at a time,
**what evidence exists today of a machine performing it**, and where that evidence stops.
This follows the same discipline as Week 23: primary sources first (Gardner 1983 and his own
later statements), and the boundary held explicitly. Two things to verify before any beat
sheet:

1. Gardner's framework is contested in psychometrics (weak empirical support as distinct
   factors). The video can't treat it as settled science. Whether that criticism becomes the
   hook or a caveat is a FACTCHECK decision.
2. Has Gardner himself written on AI and the intelligences? If he has, that's the primary
   source for the video's central question, and it must be found before scripting.

## Not yet decided

- Final angle, beat count, title
- Whether the forklift analogy survives: it's the source's argument, not a sourced claim
