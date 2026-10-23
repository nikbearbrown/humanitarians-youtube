# 2026-10-09 - Documenting the system and making the demo repeatable

**Week covered:** 2026-10-05 - 2026-10-11

**Video:** [Mycroft_OmMali_09_10_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Private AI Valuation Agent works out a per-share price for private companies such as Anthropic, OpenAI, SpaceX and Databricks, using the quarterly reports that US mutual funds are required to file with the SEC: a fund must disclose what a holding is worth in dollars and how many shares it owns, and dividing one by the other gives a price for a company that has no share price.

This week documented how the whole thing works and built a demonstration of it
— and began by auditing the project against its own plan rather than trusting
memory.

- **The plan named six documents. Three did not exist at all** — the proposal,
  the system architecture and the data architecture. The audit compared the
  plan against the last saved version of the project, which is how they were
  found.
- **All three were written**, covering how the components fit together, where
  the fifteen data tables sit, and which of them may ever be changed.
- **One requirement had been missed for the entire project.** The plan requires
  the published documents to cite existing academic and commercial work in this
  area; a search found **zero mentions in either document**. There are now 22
  citations, and one of them changed a rule: published research on how funds
  value different share classes is the reason prices are compared at company
  level rather than per share class.
- **Any published figure can be traced back to its source.** The documentation
  follows one headline number down eight steps to the exact SEC file it came
  from.
- **The demonstration is a script that re-runs, not a recording.** Every figure
  it shows is queried live, so if it ever disagrees with the data that is a
  fault rather than an out-of-date file.
- **The demonstration changes nothing.** It shows a decision a person already
  made rather than making a new one, because recording a decision for the sake
  of a demonstration would defeat the point of requiring a person.
- **What is finished and what is not is stated plainly.** Five of the project's
  six completion criteria are met; the sixth needs SEC data that has not been
  published yet, and the write-up says so rather than claiming completion.

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
