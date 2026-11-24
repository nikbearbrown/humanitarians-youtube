# Frictional Log — the-cell-dies-rich (Week 32 topic video, long and Short)

**Record provenance:** drafted 2026-11-23 with Claude from this folder's records and the session's own measurements, after the work was done rather than while it happened. **Reviewed by Tanmay.** Every entry points at the record it comes from.

## 2026-11-23 — A "no hits" that meant nothing
- **Work and expectation:** confirm that no fellow's files on the 30 branches that had moved since the last sweep mention brownout, coin cells or internal resistance.
- **Where it resisted:** the first content scan fetched each file's raw link without following GitHub's redirect, so every body came back empty and "no hits" was an artefact. It was caught before it was written down as a result.
- **What was done:** the scan was rerun over all 4,140 files with redirects followed (0 failed): no hits (`TOPIC-DECISION.md`).

## 2026-11-23 — The library film's number was not the datasheet's
- **Work and expectation:** build the simulation on the library film's cell (3 V, 1000 ohm, an 8 mA burst).
- **Where it resisted:** Energizer's handbook gives about 10 ohm for a fresh coin cell, so a fresh cell cannot reset at 8 mA at all; a 2 V line needs 125 ohm for that, which the cell never reaches in the plotted run. The thesis I had written ("most of the charge is stranded") held only for large bursts.
- **What was done:** the thesis became a measured shape (8 mA strands nothing, 30 mA a sixth, 60 mA nearly half, 100 mA everything), and Tanmay chose to keep the title and have the film state the dependence (`MEASUREMENTS.md`, `ANGLE.md`).

## 2026-11-23 — Two datasheet links that were web pages
- **Where it resisted:** the first two downloads (Energizer's older link, Duracell's old address) returned HTML, not PDFs. The current Energizer manual was a real PDF; Duracell's current file was found on its technical library page.
- **What was done:** the values were read, the graph values recorded as "about", and the downloaded files deleted after use, as Tanmay asked (`FACTCHECK.md`).

## 2026-11-23 — A PROOF review of my own script
- **Where it resisted:** the opening line said "it was not the charge", which the film's own B05 contradicts (for a small burst the charge is exactly what runs out); the viewer task said "find your device's biggest burst" with no way to do it; a line claimed a capacitor "can help", with no source.
- **What was done:** reworded, a worked check and the two numbers to look up were added, the capacitor claim removed (`PROOF-REVIEW.md`).

## 2026-11-23 — Pace measured on the previews: 23 stretches over 3 s
- **Where it resisted:** the first motion pass of the Short had 23 stretches without a visible change longer than 3 s (the longest 6.9 s), and the long film had a stretch of 11.2 s. A nested picture layer that was switched back on by an inner layer also left the closing text over the RESET box on the Short's last frame, so the loop did not close (difference 1.9 grey levels).
- **What was done:** the plan went from about 60 timed items to 91 for the Short, each tied to a spoken word; the layer fault was fixed (loop difference 0.208, later 0.03) (`PROOF-REVIEW.md`).

## 2026-11-23 — What the voice would have said
- **Where it resisted:** Kokoro's own tokenizer reads past-tense "read" as "reed" ("graphs I read", twice) and the verb "use" as "yoos" ("Use a resistance curve"). Separately, a reveal began at the spoken cue and then faded in over 0.35 s, so figures reached full strength after the word; and "which raises resistance" about cold was not in our sources.
- **What was done:** the voice-only respellings (page text unchanged), pictures now lead their words by 0.25 s, and B10 was reworded and re-signed (`PEDAGOGY.md`).

## 2026-11-23 — The voice is faster than the plan
- **Where it resisted:** Kokoro read at 3.4 to 3.6 words a second against a planned 2.7 and 2.4, so the long film came to 4:23 (planned 5:46) and the Short to 1:56 (planned 2:48). Re-timing found that a cue at the very start of the Short had landed 0.17 s in, so frame 0 lacked the RESET device and the loop failed.
- **What was done:** every reveal was re-bound to Whisper word times, cues in the first 0.6 s sit on frame 0, and Tanmay approved the pace after listening (`PEDAGOGY.md`).

## 2026-11-23 — Spacing the eye missed
- **Where it resisted:** after Tanmay asked for a check of boxes close to text and text cutting lines, a geometry audit of every half-second of both films found 30 spots and, at a stricter threshold, 18 more (labels 5 px from chart edges, labels sitting on curves, a highlight box crossing tick labels) that contact sheets had not shown.
- **What was done:** all fixed; the audit reads zero issues over 778 frames (`PROOF-REVIEW.md`).

## 2026-11-23 — Three things only the compiled files showed
- **Where it resisted:** (1) the Short's pictures were cut at each line boundary instead of fading, a luma step of 7.4; (2) the Short ended with 1.04 s of silence, over its 1.0 s limit; (3) the final review found the video was converted to YUV with the BT.601 matrix and played back as BT.709, which shifts the accent colours (teal off by 15 levels, red by 13, amber by 8). The measured gates cannot see this.
- **What was done:** pictures now fade over 0.35 s, the loop tail is 0.80 s, and both films were re-rendered with an explicit BT.709 conversion and tags; a colour round trip now returns every palette colour within 1 level (`PROOF-REVIEW.md`).
