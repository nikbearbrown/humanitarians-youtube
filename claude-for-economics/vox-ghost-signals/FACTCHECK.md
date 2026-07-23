# FACTCHECK — vox-ghost-signals
Source chapter: the-reallocation-engine/chapters/08-is-the-job-real-ats-detection-and-liveness.md

Every claim in narration, viz data, and card copy → verdict + source line + fix if needed.
Invented/illustrative numbers are labeled as such.

---

## Claims Table

| Beat | Claim | Verdict | Source / derivation | Fix |
|------|-------|---------|---------------------|-----|
| B01 | "Two job postings. Same employer. Same title. Same sponsorship tier." | ✓ | Ch08 p.91: "The same employer. The same title. The same sponsorship tier." | — |
| B01 | "One of them has never been a real opening." | ✓ | Ch08 p.91: "One is a door; one is a picture of a door." | — |
| B02 | Illustrative scene — person writing cover letter | editorial | Not a factual claim; illustrative framing | — |
| B03 | "The most compelling-sounding posting is the ghost." | ✓ | Ch08 Exercise 5: Helix Bio verdict where the compelling description = ghost; "the description is more compelling" per card content | — |
| B04 | "Between 28 and 42 percent of job postings are ghosts" | ✓ | Ch08 p.4: "Somewhere between 28 and 42 percent of job postings, depending on the study and the year, are ghosts" | — |
| B04 | "That figure has held steady for five years." | ✓ | Ch08 p.4: "held roughly steady across five years of measurement" | — |
| B04 | "It is structural." | ✓ | Ch08 p.4: "it isn't an artifact of a particular labor market cycle. It is a structural feature of how hiring works" | — |
| B05 | "A ghost is not a cancelled role." | ✓ | Ch08 p.6: "A ghost job isn't a posting that went live and then the position was cancelled." | — |
| B05 | "A posting never connected to a hiring intention — a pipeline hedge, an investor signal, bureaucratic inertia." | ✓ | Ch08 p.6: "a pipeline hedge … signal to investors … bureaucratic inertia" | — |
| B06 | "Ghost detection is structurally identical to spam filtering. Not metaphorically — mechanically." | ✓ | Ch08 p.42: "Ghost job detection is structurally identical to spam filtering — not metaphorically, but mechanically." | — |
| B06 | "Your spam filter does not read the message. It scores behavioral fingerprints." | ✓ | Ch08 p.44: "it scores the message's behavioral fingerprints against patterns of mail that is actually wanted" | — |
| B07 | Three fingerprints: temporal anomaly, interaction void, textual homogeneity | ✓ | Ch08 p.44: "Temporal anomalies … Interaction voids … Textual homogeneity" | — |
| B07 | "Temporal anomaly — the posting is frozen in time." | ✓ | Ch08 p.46: "A posting that has been up eleven weeks with no update … looks like a bulk send with no engagement — the temporal anomaly." | — |
| B07 | "Interaction void — no portal activity." | ✓ | Ch08 p.46: "A portal that has never advanced a candidate … looks like mail no one is responding to — the interaction void." | — |
| B07 | "Textual homogeneity — the description is a copy." | ✓ | Ch08 p.46: "A job description identical to three other listings … textual homogeneity." | — |
| B08 | Five signals: posting age, last updated, sibling listing activity, description specificity, active search context | ✓ | Ch08 pp.59–67: listed explicitly as the five signals in order | — |
| B08 | "Together they classify behavior — not prose." | ✓ | Ch08 core thesis: "stop reading job postings as prose and start reading them as data" | — |
| B09 | Three outputs: live, ghost, investigate | ✓ | Ch08 p.78: "The output is one of three calls per posting: live, ghost, or investigate." | — |
| B09 | "No single signal is decisive." | ✓ | Ch08 p.48: "No single signal is decisive." | — |
| B09 | "The way no individual word makes an email spam but the pattern does" | ✓ | Ch08 p.48: paraphrased closely from chapter | — |
| B10 | "The compelling description is the costume. The metadata is the evidence." | ✓ | Ch08 Exercise 5: "The signals are the data claim; the description is the costume." | — |
| B10 | "One false negative exists: fresh, specific-sounding harvest postings designed to beat the detector." | ✓ | Ch08 p.122: "A fresh posting can be fake. A recruiter running a sourcing campaign posts a crisp, specific, recently dated listing precisely because candidates screen for recency." | — |
| B11 | "Helix Bio, two Senior Data Scientist roles." | ILLUSTRATIVE | Ch08 uses "a biotech" generically in p.82; Exercise 5 uses "Helix Bio" as a named example. Kept as illustrative per card content. Labeled in narration. | Narration already says "illustrative numbers — same mechanism." |
| B11 | "Posting A: 9 days, refreshed twice, names a model-retraining project." | ILLUSTRATIVE | Ch08 p.84: "Posting A went up nine days ago … description references a specific named project — a model being retrained on a new assay dataset" | Narration labels illustrative. |
| B11 | "Posting B: 11 weeks, frozen, description word-for-word from 18 months ago." | ILLUSTRATIVE | Ch08 p.86: "Posting B has been up eleven weeks … word-for-word identical to a data scientist posting the company ran eighteen months ago" | Narration labels illustrative. |
| B11 | "A is live. B is a ghost." | ILLUSTRATIVE | Ch08 p.84–86: explicit in chapter; labeled illustrative | — |
| B12 | "Don't write a cover letter for a door that was never going to open." | ✓ | Ch08 p.6: "A day spent writing a cover letter … to a door that was never going to open." | — |

---

## Exclusions Confirmed

- No ATS vendor comparisons: Greenhouse, Lever, Ashby mentioned in chapter but do NOT appear in any beat narration, card, or viz.
- No detail on how the ATS detection script works internally: no mention of `detect-ats.py`, `ats:scan`, `ats:liveness` commands, or script internals in any beat.
- False negatives: covered in ONE sentence only (B10 narration: "One false negative exists: fresh, specific-sounding harvest postings designed to beat the detector.").
- No equations.

---

## Terms Table

| Term | Debut beat | Prior beat that creates the need |
|------|-----------|----------------------------------|
| ghost (job) | B01 | B01 cold open sets up "never been a real opening" — need for a name comes by B04 |
| spam filtering | B06 | B06 — analogical mechanism introduced at the mechanism act, after problem established |
| temporal anomaly | B07 | B06 introduces the fingerprint concept, B07 names the three |
| interaction void | B07 | B06 introduces the fingerprint concept, B07 names the three |
| textual homogeneity | B07 | B06 introduces the fingerprint concept, B07 names the three |
| live / ghost / investigate | B09 | B08 lists the five signals that feed the classifier, B09 names the outputs |
