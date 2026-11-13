# FRICTIONAL — Both Sides of the Table.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-PROMPT.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, QC-LOG.md, SHOTLIST.md, beat_sheet.json),
> not kept week by week during the build.

## 2026-10-21

**Tried / expected.** A 1–3 minute data explainer on hiring as a standoff between two AIs —
employers screening with AI, candidates using it to get through. Supplied figures with
citations from five publishers (Gartner via CI CoPilot, Greenhouse, Greenhouse Candidate AI
Interview Report, Pew, SelectSoftwareReviews), with the instruction to cite as shown,
not alter the numbers, and add nothing. "Bella, in for Yatra" intro, `@Yatra` bug, true 4K
in 16:9 and 9:16. Result: 14 beats, 2:49.4, eight new `Tbl*` scenes.

**Where it resisted, and what was done next.**
- *Over length.* The first audio pass ran 3:13.5 — over the brief and the 3:00 Shorts cap.
  Narration was trimmed twice to reach 2:49.4.
- *Many publishers, one video.* The main risk recorded is the figures reading as one
  dataset. Every figure scene requires a `source`, and `TblTrust` requires a separate
  source for each of its two figures (26% Greenhouse, 66% Pew) so they are never merged.
- *Figures that tempt arithmetic.* `4 in 5` is kept as written, never `80%` (`value` is a
  verbatim string; a separate `bar` drives drawing). The unfilled 74% of the 26% track is
  left unlabelled. Only the +13-point change was published, so `TblInterview` has no
  earlier-figure prop and states why on screen.
- *A statistic about a technique.* The 41% prompt-injection figure is stamped
  self-reported, and B09 shows only generic resume headings — no working injection string.
- *A defect found by reading frames.* B05's table floated as an empty box above the machine
  row, and the machine-to-machine traffic ran below it, so the beat's argument didn't land
  (MAJOR). Table moved onto the machine row so the traffic crosses it.
- *One composition, two beats.* `TblSide` backs B02 and B03; registered at the shorter
  length, because a longer clip gets trimmed and the citation lands at ~88% of the span.
- *Render environment.* The same two failures as the sibling reel (orphaned Chrome after a
  machine sleep; the 30s per-frame timeout), handled with the `ART_TIMEOUT` knob.
- *Toolkit gates.* GATE V false BLOCKERs and missing GATE T handled by substitution and
  logged.

**What Claude contributed, and what was accepted / changed.** Yatra supplied the figures,
their citations and the standoff framing. The build side wrote the beat sheet and scenes,
ran audio/render/compile, did the frame QC, and audited each citation on the frames
rather than trusting the types. The framing is presented as argument; `TblTable` carries it
with no numeric prop. The records don't say who chose what to cut in the two trims.

**Now understood / still open.**
- Understood: re-measure audio before building anything if narration is re-authored.
- Open: the five source publications were not re-checked in this build.
- Open: the count of supplied figures is inconsistent — FACTCHECK.md says seven, then
  tabulates eight (it counts the +13-point change separately), and also says "six numbers".
- Open: README.md says "2:48.9" and "narrated by Yatra"; SHOTLIST.md says 2:49.4 and
  "Bella, in for Yatra". Not reconciled.
