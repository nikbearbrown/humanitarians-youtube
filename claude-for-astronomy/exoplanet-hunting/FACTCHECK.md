# Ep. 02 — Exoplanet Hunting — Fact-Check

**Status: Verification complete against primary/official sources found via web search on
2026-08-01. Beat numbers below were renumbered 2026-08-01 when a new presenter
self-introduction/executive-summary beat was inserted as B02, pushing every former B02-B19 beat up
by one; no claim's underlying facts changed, only its beat number. Renumbered again 2026-08-01
(second pass) when beats 1 and 2 were swapped so the presenter intro now opens the film, followed
by the cold open — again, only the beat-number column shifted.**

Beat numbers refer to the 20-beat list in `SHOTLIST.md`.

**Beat 1** (`"Hi, I'm Om Mali. This video is about how NASA built an AI system that explains
exactly why it thinks a signal is a real planet, instead of just giving a yes or no answer."`) is a
presenter self-introduction, not a factual claim, and carries no row in the table below — same
treatment as Ep.01's own intro beat.

| Claim (as used in script) | Beat(s) | Verification | Source | Status |
|---|---|---|---|---|
| Kepler's pipeline produced thousands of unconfirmed transit candidates ("threshold-crossing events," TCEs) that sat unvalidated for years | 2, 3 | Confirmed as the general framing of the vetting backlog problem that ExoMiner and its predecessors were built to address. | [Kepler Data Validation I — Architecture, Diagnostic Tests, and Data Products for Vetting Transiting Planet Candidates, arXiv](https://arxiv.org/pdf/1803.04526) | ✅ |
| Transit-like dips can come from (a) eclipsing binaries, (b) stellar variability, (c) instrumental artifacts, in addition to real planets | 4–7 | Confirmed. AstroNet-family vetting classifies TCEs into categories including planet candidate (PC), eclipsing binary (EB), stellar variability (V), and instrumental artifact (IS/junk); most TCEs are in fact caused by instrumental artifacts and stellar variability rather than planets. | ["Identifying Exoplanets with Deep Learning III" (AstroNet-Triage), IOPscience](https://iopscience.iop.org/article/10.3847/1538-3881/ab21d6) | ✅ |
| Eclipsing binaries can mimic a planetary transit dip and are a well-documented false-positive source | 5 | Confirmed — this is one of the two most-cited false-positive classes in the vetting literature. | [Same as above — AstroNet-Triage, IOPscience](https://iopscience.iop.org/article/10.3847/1538-3881/ab21d6) | ✅ |
| Stellar variability (starspots, flares) independently dims stars and is a distinct false-positive source from eclipsing binaries | 6 | Confirmed — listed as its own TCE disposition category ("V") separate from EB and IS in the vetting taxonomy. | [Same as above](https://iopscience.iop.org/article/10.3847/1538-3881/ab21d6) | ✅ |
| Instrumental artifacts (camera/spacecraft-systematics noise) are a distinct false-positive source, and in fact the majority cause of raw TCEs | 7 | Confirmed. | [Same as above](https://iopscience.iop.org/article/10.3847/1538-3881/ab21d6) | ✅ |
| NASA's Ames Research Center built ExoMiner, announced Nov 22, 2021 | 9 | Confirmed. Announcement date per NASA/JPL press release. | [NASA JPL press release](https://www.jpl.nasa.gov/news/new-deep-learning-method-adds-301-planets-to-keplers-total-count/) | ✅ |
| ExoMiner is explicitly designed to be explainable — "mimics how domain experts examine diagnostic tests to vet a transit signal," unlike prior black-box classifiers | 9, 10, 15 | Confirmed, direct paraphrase of the paper's own framing. Ames scientist Jon Jenkins on the design goal: "we can easily explain which features in the data lead ExoMiner to reject or confirm a planet." | [ExoMiner paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ac4399); [arXiv abstract](https://arxiv.org/abs/2111.10009); [NASA JPL press release](https://www.jpl.nasa.gov/news/new-deep-learning-method-adds-301-planets-to-keplers-total-count/) | ✅ |
| ExoMiner's architecture feeds distinct diagnostic tests (full/transit-view flux, full/transit-view centroid motion, secondary-eclipse flux, odd/even flux, a "ghost" optical-contamination diagnostic, and stellar parameters) through **separate convolutional branches**, merged only at the end | 10, 11, 15 | Confirmed — this is the documented architecture, not a simplification. Each diagnostic input (full-orbit flux, transit-view flux, full-orbit centroid, transit-view centroid, odd & even flux, secondary-eclipse flux) is "fed as separate convolutional branches, where each branch is formed of blocks containing convolutional layers plus a max pooling layer." | [ExoMiner paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ac4399); [Kepler Data Validation I, arXiv](https://arxiv.org/pdf/1803.04526) | ✅ |
| One of ExoMiner's diagnostic branches is a **centroid-offset test** — checking whether the light causing the dip is actually centered on the target star or shifted toward a neighboring star (catching background/nearby eclipsing binaries) | 12 | Confirmed. Centroid motion (full-orbit and transit-view) and difference-image (out-of-transit) centroid offsets are explicit named inputs. | [ExoMiner paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ac4399) | ✅ |
| Another branch is an **odd/even transit-depth test** — comparing odd- and even-numbered transits, since a real planet's transits are identical while some eclipsing binaries alternate in depth | 13 | Confirmed. "Transit-view phase-folded odd & even flux" is an explicit named diagnostic input, matching the standard odd/even vetting test used across the Kepler/TESS pipeline literature. | [ExoMiner paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ac4399); [Kepler Data Validation I, arXiv](https://arxiv.org/pdf/1803.04526) | ✅ |
| A third branch is a **secondary-eclipse test** — looking for a second, shallower dip elsewhere in the orbit, which indicates a stellar (not planetary) companion | 14 | Confirmed. "Transit-view phase-folded secondary eclipsing flux" is an explicit named diagnostic input. | [ExoMiner paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ac4399) | ✅ |
| At 99% precision, ExoMiner recovers 93.6% of real planets (recall), versus 76.3% recall at the same precision for the best prior classifier | 16 | Confirmed, direct figures from the paper. | [ExoMiner paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ac4399); [arXiv abstract](https://arxiv.org/abs/2111.10009) | ✅ |
| ExoMiner validated 301 new exoplanets from the Kepler archive in one batch, published in the Astrophysical Journal, Feb 17, 2022 (vol. 926, no. 2) | 17 | Confirmed. None of the 301 are believed to be Earth-like or habitable — this episode does not claim otherwise. | [NASA JPL press release](https://www.jpl.nasa.gov/news/new-deep-learning-method-adds-301-planets-to-keplers-total-count/); [ExoMiner paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ac4399) | ✅ |
| By 2026, ExoMiner's design was extended as "ExoMiner++" to screen TESS 2-minute-cadence data, published in the Astronomical Journal (vol. 170, no. 5), Jan 22, 2026 | 18 | Confirmed. | [ExoMiner++ paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-3881/ae03a4); [arXiv](https://arxiv.org/abs/2502.09790); [phys.org coverage](https://phys.org/news/2026-01-ai-exoplanets-tess.html) | ✅ |
| ExoMiner++ flagged 7,330 planet candidates among 147,568 unlabeled TESS TCEs on its initial run | 19 | Confirmed exact figures from the paper. | [ExoMiner++ paper, IOPscience](https://iopscience.iop.org/article/10.3847/1538-3881/ae03a4); [phys.org coverage](https://phys.org/news/2026-01-ai-exoplanets-tess.html) | ✅ |
| The original ExoMiner's cumulative validated-planet total reached roughly 370 by the time of the ExoMiner++ coverage | *(background only, not a scripted line)* | Confirmed per the phys.org piece; **not used as a beat claim** because the 301-planet 2021/2022 batch is the cleaner, single-dated number for the script. Left here for the audit trail only. | [phys.org coverage](https://phys.org/news/2026-01-ai-exoplanets-tess.html) | ✅ — not scripted |

## Resolved decisions

1. **No photo of ExoMiner's project scientists (beat 9).** Following the same policy Ep.01 used for
   Shallue/Vanderburg (see Ep.01's `FACTCHECK.md` "Resolved decisions" #3): I did not attempt to
   verify usable image rights for named individuals (e.g., Hamed Valizadegan, Jon Jenkins). Beat 9
   is a text-only name/org card by design, not a placeholder waiting on a photo.
2. **No real-archive stills or footage this episode, by design — not an oversight.** Unlike Ep.01
   (which used three real, credited NASA/NOIRLab assets), this episode is built entirely from
   original Manim diagrams and Remotion cards. This was a deliberate choice, not a limitation: none
   of the 301 batch-validated planets is individually notable enough to justify sourcing a specific
   press image, and the episode's actual subject — a neural-network architecture and its diagnostic
   tests — has no meaningful "photo" to show in the first place. Zero paid generation either; see
   `PROMPTS.md`.
3. **"Human vetter" framing (beat 10).** The script says ExoMiner "runs the same diagnostic tests a
   human vetter would." This is the paper's own framing (it explicitly models the Kepler Data
   Validation report's human-designed diagnostic tests), not an embellishment — see the Kepler Data
   Validation I citation above for the underlying human-designed test suite ExoMiner mirrors.
4. **Precision/recall numbers (beat 16) are from the original 2021 Kepler-focused ExoMiner, not
   ExoMiner++.** The script's ordering (ExoMiner's accuracy and the 301-planet Kepler batch, *then*
   the 2026 ExoMiner++/TESS extension) keeps those two number sets attached to the correct system
   and correct dataset — this was checked specifically to avoid conflating Kepler-era and
   TESS-era statistics.
5. **Punctuation-clarity narration rewrite pass (2026-08-01, pre-dates the beat-2 insertion).**
   Rewrote `narration_text` for 12 beats (then-numbered B02, B03, B04, B05, B06, B08, B09, B11,
   B12, B13, B15, B17; now B03, B04, B05, B06, B07, B09, B10, B12, B13, B14, B16, B18 after the
   beat-2 insertion below) to remove hyphens/dashes/colons joining clauses, which the human
   reviewer found hard to follow by ear, and to make the eclipsing-binary and stellar-variability
   beats actually define the terms they name instead of only labeling them. No new facts were
   introduced — every claim in the reworded beats was already sourced above: eclipsing binary =
   two stars orbiting/eclipsing each other (row 3, beat 5 above); stellar variability =
   starspots/flares causing a star to dim independently of any companion (row 4, beat 6 above).
   This is a phrasing-only pass; on-screen Remotion card `headline` props were left untouched by
   explicit scope, since the human's request was "narration," not visual card copy.
6. **New beat 2 inserted 2026-08-01 (presenter self-introduction, not a factual claim).** A new
   Remotion `SlateCard` beat, `narration_text` = "Hi, I'm Om Mali. This video is about how NASA
   built an AI system that explains exactly why it thinks a signal is a real planet, instead of
   just giving a yes or no answer.", was inserted directly after the B01 cold open, pushing every
   former B02-B19 beat up by one to B03-B20 (see `SHOTLIST.md` and `STATUS.md`). This mirrors the
   identical insertion already made to Ep.01 (`ai-vs-the-data-deluge`) for series consistency (same
   "WELCOME" eyebrow, same "Hi, I'm Om Mali." headline pattern). The beat makes no factual
   assertion about ExoMiner, Kepler, or TESS — it is a presenter/host introduction and executive
   summary of the video's own subject, and requires no source citation. Every beat-number
   cross-reference elsewhere in this file, in `SHOTLIST.md`, and in `beat_sheet.json` was updated
   to match; no claim's substance changed.

**Money status:** zero paid-generation spend planned or used — see `PROMPTS.md`.
