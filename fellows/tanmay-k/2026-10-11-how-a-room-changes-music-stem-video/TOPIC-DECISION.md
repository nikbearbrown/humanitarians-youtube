# Week 26 — Topic Selection

**Selected:** `claude-for-music/how-music-works-audible`
**Source:** Nik Bear Brown's book review of *How Music Works* (David Byrne)
**Decided:** 2026-10-10

---

## How the topic was chosen

Same method as Weeks 24–25: a randomized draw over the singleton pool of `humanitarians-youtube`,
meaning topics that appear **exactly once** across the whole library once naming variants are normalized.

### Fresh, isolated snapshot (read-only)

- `git ls-remote --heads origin`: 61 live heads (60 fellow branches + `main`), saved in `_selection/heads.txt`
- `git clone --bare --reference <local checkout>` into the session scratchpad. Every command after that
  was `for-each-ref` / `ls-tree` / `show` / `grep` / `diff --name-only` / `log` against that mirror.
  Nothing was checked out, fetched into, pushed, or modified in `humanitarians-youtube`, and no
  fellow's branch or file was touched.
- Snapshot `main` = `dfa851048` (2026-10-09 17:39).

### Sweep (`_selection/sweep.py`, unchanged from W25 except the mirror path)

`main`: **4,948** topic folders, plus **215** that exist only on fellow branches, for a combined
library of **5,163**. Those normalize to **2,965** keys, of which **1,855** are singletons.

### Exclusions, in order (`_selection/pool.py`)

| Filter | Removed |
|---|---|
| Not a `claude-for-*` collection | 1,381 |
| Collection used in Weeks 20–25 (W25 adds **education**) | 405 |
| One of our own past sources (W17–W25) | 0 |
| Exists only on a fellow branch | 7 |
| Production evidence on `main` (SRT/VTT, YouTube metadata, BUILD-LOG, FACTCHECK, QC, STATUS, PROOF, MP4, concat) | 17 |
| Variant copy elsewhere under stricter normalization | 30 |
| Near-duplicate by title-token overlap | 4 |
| Touched on any fellow branch (`diff main...<branch>`) | 0 |
| Fellow-authored source (`**Author:**` line) | 2 |
| Near-duplicate clusters W24 documented: Subby ×2, fairness ×2 (`_selection/draw.py`) | 4 |
| **Final pool** | **5** |

### Draw

`random.SystemRandom().shuffle` over the 5, unseeded. The full order is in `_selection/draw.json`:

```
1. claude-for-music/how-music-works-audible                  <- ACCEPTED
2. claude-for-music/river-mumma-calling-how-a-song-crosses
3. claude-for-artificial-intelligence/ch80-lecture
4. claude-for-music/the-song-that-lied-to-you
5. claude-for-music/five-senses-one-song
```

---

## Uniqueness verification: `how-music-works-audible` (`_selection/verify.py`, `verify.json`)

| Check | Result |
|---|---|
| Normalized key library-wide | appears **once** |
| History | a single commit, `e6e678cc9` 2026-08-27, Nik Bear Brown, "Integrated repository snapshot" (bulk import) |
| Source author | Nik Bear Brown, Founder, Humanitarians AI. **Not a fellow** |
| Build state | unbuilt 10-beat Kore auto-conversion: README, BUILD-PROMPT, SOURCES, beat_sheet, `mp3/timings.json` only. No FACTCHECK, BUILD-LOG, SRT or YouTube metadata. The README topic label reads "GAME DESIGN" (template artifact); the music-collection index lists it as "beat sheet authored" |
| `git grep` on **all 61 refs** for `Byrne`, `How Music Works`, Edison/wax cylinder, `Talking Heads`, `CBGB`, `reverberation time`, "written for the room" | only this folder and the `claude-for-music/README.md` index row. Every other hit is incidental: Wikipedia entries in `claude-for-design/json/terms.json` (Rhonda Byrne, Pete Byrne, the CBGB club) and letter runs inside base64 PNG data in two fellow beat sheets/scripts. No fellow has covered the book or its argument |
| Our own Weeks 1–25 | zero hits, apart from the library inventory CSVs (`_readme-states.csv`) in W18–W20 |

## What the source offers

The SOURCES.md says no statistics were detected. The review's claims are qualitative and all need
FACTCHECK against the book itself (Byrne, *How Music Works*, 2012):

1. **Context comes first.** Bach wrote for rooms with particular echo; Mozart played palace chambers, not
   symphony halls. The space shaped the music.
2. **Technology shapes form.** Edison's cylinders were fragile and mechanical, so bands had to play the same
   song again for each batch of recordings, and recording changed what music *becomes*, not just how it is heard.

## Not yet decided

- Angle, structure, title, beat count (the film needs its own shape, not the template's ASK → HANDOFF skeleton)
- The angle must also pass the narration audit against W15–W25 before scripting
