# Documenting the system and making the demo re-runnable

Four figures and a 3:00 narration script. The last week of the build, and the only one whose
subject is finding out what had been assumed: the documents that explain the system, a stated
requirement met zero times, and a demo that re-runs instead of one that was true once.

| File | Beat | What it shows |
|---|---|---|
| `pantry/w12-docs.png` | 0:28 | Six documents named in the plan, audited against the last commit — three did not exist |
| `pantry/w12-priorart.png` | 1:05 | A stated requirement at zero, and the 22 citations that are in now |
| `pantry/w12-provenance.png` | 1:50 | One published number followed down eight links to the SEC archive file |
| `pantry/w12-demo.png` | 2:30 | Five acts, every figure queried live, zero write statements |

SVG sources sit beside each PNG. `figdata.json` is the measured data every figure was drawn
from, generated at build time by querying the live database, reading the generated findings
file, and running `git show HEAD` against the working tree.

---

## The built reel

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`) — free and local throughout:
Kokoro TTS, Remotion, ffmpeg. **$0.00 spent, no API key used.**

Twelve beats, 3:32, in **both orientations**: `Mycroft_OmMali_09_10_2026.mp4` (3840×2160) and
`vertical/documenting-the-system-and-making-the-demo-runnable-916.mp4` (2160×3840). The 9:16
cut is a **re-layout, not a crop** — both render from the same components and the same props,
and carry the identical narration MP3s.

The four figures travel in `pantry/` as **reference**. Every beat is rebuilt native
(REBUILD LAW); no PNG is slotted as media.

| Document | What it is |
|---|---|
| `BUILD-PROMPT.md` | the single paste-ready prompt that rebuilds this reel end to end |
| `BUILD-LOG.md` | decisions taken, every defect found by reading frames, the toolkit fix |
| `CHECKS-REPORT.md` | the PROOF GATE — per-beat SHOW/HOLD classification, written before the first compile |
| `FACTCHECK.md` | 20 rows. **Read rows 5, 6, 13, 17 and 19 before signing.** |
| `PEDAGOGY.md` | GATE P — what the author is being asked to sign off on |
| `description.txt` | the written version of the episode |

### Where the reel is narrower than the figure

**`w12-priorart.png` tabulates three documents at BEFORE 0. The reel says two.** `proposal.md`
carries `existed: false` — its zero is an absent file, not a document that failed the
requirement. The figure's own caption already agrees ("in either published document"); its
table does not. The build asserts 2 published zeroes against 1 non-finding zero, so a data
change cannot quietly re-merge them. 13 of the 22 citations went where the requirement bit.

### Two beats neither the script nor the figures contain

**One citation is load-bearing.** 22 were added and 21 are context. Gornall & Strebulaev
established that funds write up every share class to the latest round price; reproduced on this
cohort, it is why dispersion is measured per company with the share class recorded, and it
overturned an earlier draft's rule.

**Fifteen tables in three layers, keyed on mutability.** Immutable, append-only, rebuildable —
the architecture document's spine, which the script names but no figure draws. Every one of the
5,806 filed holdings carries exactly one match decision, and the 327 that are not marks are the
guards.

### What the reel limits about itself

The audit covers the six documents the plan names and no others. A citation count is not a
literature review. Zero write statements is a static scan of five files, not a proof. And the
run log that makes the provenance chain datable has **two rows** in it — a start, not a history.
All four are on B08, each attached to the claim it narrows.

### A defect in the source figures, not inherited

`w12-demo.png`'s layer-summary line runs off the right edge, ending "resolved 3 (rebuil". The
rebuild carries that summary as three cards on B05 instead.

Nothing here is published. The masters stay in this folder.
