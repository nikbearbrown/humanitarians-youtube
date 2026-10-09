# BUILD-LOG — documenting-the-system-and-making-the-demo-runnable (week 11)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Tenth episode of the Private AI Valuation Agent series (week 1 → 2 → 4 → 5 → 6 → 7 → 8 → 9 →
10 → 11; there is no week 3 episode). Seventh episode shipped in both orientations.

**The series' last build week, and the only one whose subject is the author being wrong about
his own work.** The code was finished; the week is an audit, and what the audit found is the
episode.

---

## Where the inputs came from

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | Already here | input, unmodified |
| `figdata.json` | Already here — generated at build time by querying the live database, reading the generated findings file, and running `git show HEAD` against the working tree | **the source of truth for every on-screen number** |
| `pantry/w12-*.png` + `.svg` | Were in `images/` | **moved to `pantry/`** — `run.sh` uses `images/` for compile OUTPUT and the series keeps reference art in `pantry/` |
| `lock_durations.py`, `make_vertical.py` | Copied from week 10 | unchanged; the two-digit-week regex fix from week 10 means `W11*` patterns resolve correctly |
| `README.md` | **Does not exist for this reel** | see below |

**There is no reel README this week.** Weeks 9 and 10 each shipped one with a figure-to-beat
map, a "three things not to get wrong" section, and a list of known defects in the source
figures. Without it, the editorial judgments below were made from the script and `figdata.json`
directly, and every arithmetic relationship was re-derived rather than taken from a caption.
That is why `CHECKS-REPORT.md` carries more derivation than usual, and why B03 exists.

---

## Every number is injected, and these groups are asserted

```
documents[]: 6 entries, exactly 3 with existed=false, and every absent one has
             lines_before == 0 — an absent file has no "before"
             nothing shrank: lines_now > lines_before for all six
             444 lines written from nothing, 104 added to what was there
prior_art[]: 3 rows, all at before == 0, all with after > 0
             exactly 2 of them in documents that EXISTED          <- FRAMING
             22 citations added, 13 of them in the two published documents
remark:      1,019 unchanged of 4,079 steps == 0.2498, over 5,178 marks
layers[]:    3 layers, mutability exactly [immutable, append-only, rebuildable]
             the layers' tables account for all 15 tables figdata counts
             EACH layer's row total equals the sum of its OWN tables
             raw_holdings 5,806 == match_decisions 5,806, and 5,806 − 5,479 == 327
demo:        5 acts, 5 files scanned, 0 write statements
```

**The framing assertion is `len(PUBLISHED_ZEROES) == 2`.** `w12-priorart.png` tabulates THREE
documents at BEFORE 0, but one of them — `proposal.md` — carries `existed: false`. Its zero is
an absent file, not a document that failed the requirement. The figure's own caption is careful
("in either published document"); its table is not. If that split ever changes, B03's whole
argument changes with it and the build fails rather than shipping the wider claim.

**One assertion exists to stop a figure drifting from its own detail**: each layer's row total
is asserted equal to the sum of that layer's tables, rather than trusted as a separate number.

`python build_beat_sheet.py --check` runs the assertions and writes nothing.

---

## Four values that are NOT in figdata.json

| Constant | Value | Used by |
|---|---|---|
| `PRIOR_ART_NAMES` | Caplight, Gornall & Strebulaev, Agarwal, Chernenko, Kwon | B03 |
| `LOAD_BEARING` | what the Gornall & Strebulaev citation actually changed | B04, B09 |
| the eight-link chain | `data_architecture.md`'s own trace; only the headline figure is in figdata | B06 |
| `LM_SITES` | exactly two places a language model sits, neither touching a number | B08 |

Each is a named constant and **each beat that uses one says so on screen**. `FACTCHECK.md`
rows 6, 10, 17 and 20.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Six script sections → eight body beats.** | B04 and B05 are new (below); the demo and the limits were split so a limits sentence at 2:52 is not heard as sign-off patter. |
| 2 | **B03 narrows the reel's own headline, against the source figure's table.** | Three documents show BEFORE 0; two of those zeroes are findings and one is a missing file. The script's next sentence already says "in either published document" — this puts that precision on the frame instead of only in the voice. |
| 3 | **B02 prints WORDS where an absent file's "before" would go.** | A 0 in that column reads as "a document with no lines", which is weaker than "no document", and it would sit in the same column as 231 and 956. |
| 4 | **B04 is new.** | The script treats the Gornall & Strebulaev citation as the point of its section. This beat shows what makes it different from the other 21 — a four-step chain ending in a rule that CHANGED. |
| 5 | **B05 is new.** | The script calls the architecture document "the one I'd keep" but no figure draws its spine. Fifteen tables in three layers, keyed on mutability, is that spine. |
| 6 | **B08 says the run log has two rows.** | B06's strongest claim is that the chain is datable. The thing that makes it datable is small enough to say out loud. |
| 7 | **Greeting rotated to `Hoi, HAI`.** | Weeks 1–10 used `Ola`, `Hej`, `Ciao`, `Hallo`, `Salut`, `Ahoj`, `Szia`, `Tere`, `Moi`. Dutch short form; the lexicon never repeats a language. |
| 8 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name. Set at authoring time, so GATE L passed on the first run for the ninth episode running. |

---

## Defects found by READING frames, and fixed

| Beat | Defect | Fix |
|---|---|---|
| B02 | **The bar column inverted the beat's own claim.** Scaled to total lines, `entity_resolution.md` — which grew 60 lines of 1,016 — had the LONGEST bar on a frame whose argument is that three documents were written from nothing, and those three had the SHORTEST. | Stacked: a pale segment for what was already there, a solid accent segment for what this week added. `proposal.md` is now accent end to end; `entity_resolution.md` is a long pale bar with a sliver. The frame says which is which, once, under the table. |
| B06 | `filings -> data/<qtr>_nport.zip` used an ASCII arrow in a mono chain. | `→`. Typography only; the weeks 9–10 defect. |
| B11 | The outro wrapped "Re-runnable" at its own hyphen, leaving a line ending "Re-" above a line reading "runnable". | Non-breaking hyphen (U+2011) in `SEGMENT`. |

**B09 and B11 were correct on the first render this week.** Week 10 shipped both with another
project's placeholder copy because the props were misnamed; the lint added to
`remotion_scenes.py` stayed silent through this entire run, which is the confirmation it is
wired correctly rather than merely present.

---

## What the visual gate could not have caught, in this episode

Ten episodes of evidence. The gate cannot see overlap (weeks 1, 4, 6, 7, 8), cannot tell
whether a number on screen is the RIGHT number (weeks 5, 7, 8, 9), cannot tell whether a source
line cites a file containing the claim (week 6), cannot tell whether a caption describes the
chart beneath it (week 8), cannot tell an empty element from an intentional one (week 9), and
cannot tell whose words are on the frame (week 10). This week adds:

**It cannot tell whether a bar is measuring the thing the beat is about.** B02's bars were
correctly sized, correctly coloured, correctly spaced and inside the safe area. They were
measuring total document length on a frame whose entire argument is about new work, and they
gave the accent rows the smallest bars.

---

## Source-figure defects NOT inherited

`w12-demo.png` has an edge-bleed defect of its own: its layer-summary line runs off the right
edge, ending "resolved 3 (rebuil". The rebuild does not inherit it — B05 carries the layer
summary as three cards instead.

`w12-priorart.png`'s table shows three documents at BEFORE 0 where its own caption says "either
published document". B03 draws the caption's narrower claim.

---

## GATE V blocked the 9:16 cut, and the fix was in the toolkit

**2 BLOCKERs, `edge-bleed` on B11, both frames.** The third time in this series the gate has
stopped a real defect rather than it being found by reading frames.

The cause was NOT this reel's props. `ClaudeTitleOutro916` sized the title at a fixed
`height * 0.072` (~138px) with no regard for the longest word in it. A word cannot wrap inside
itself, so any title containing an 11-character word overflows the 936px content box and
crosses the title-safe right edge. Weeks 1–10 never hit it because none of their titles had a
word that long; "Documenting" is the first.

**Fixed with a longest-word guard** in `ClaudeTitleOutro916.tsx`: the title font shrinks only
when the longest word does not fit, so every title that already fitted renders byte-identically
and the earlier signed masters are unaffected.

It took two passes. The first guard estimated 0.62 em per character and **still bled** —
measured against the render, this serif at weight 700 is about 0.71, so "Documenting" was
~1068px against a 936px box. An estimate that is too small does not fail safe here; it fails as
an edge bleed. Set to 0.72 with a 0.5 floor.

### A misdiagnosis of my own, recorded

Before the gate ran I had "fixed" the landscape outro wrapping "Re-runnable" at its own hyphen
by making the hyphen non-breaking (U+2011). That was a cosmetic nit, and the fix made the word
unbreakable, which is the opposite of what a narrow frame needs. I then reported the bleed as
having been *caused* by that change. Both readings were wrong: the portrait outro would have
bled with the original plain hyphen too, because the problem was always "Documenting". The
hyphen is back to a plain one — a hyphen break is legitimate typesetting, and with the font
guard in place the line no longer breaks there anyway.

## The recurring toolkit footgun, again

`remotion_scenes.py` loads the beat sheet at the START of a run and rewrites it at the END, so
any edit made during a long render is silently lost. It has cost an edit in every episode since
week 5. Edits made during this build's landscape render were re-applied afterwards by re-running
`build_beat_sheet.py` and `lock_durations.py`, both of which are idempotent.

---

## What shipped

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_09_10_2026.mp4` | 3840×2160, 24fps, 212.17s — the clean 16:9 master |
| `vertical/documenting-the-system-and-making-the-demo-runnable-916.mp4` | 2160×3840, 24fps, 212.17s |
| `*-slate.mp4` (both) | review cuts, beat IDs + running timecode |
| `mp4/` | all four, md5-verified identical to the delivered masters |

**GATE L clean. GATE V clean on BOTH cuts** after the toolkit fix — 24 frames sampled each,
0 BLOCKER, 0 MAJOR, re-run explicitly with `--mp4` against the exact delivered files. GATE F
never triggered: there are no Manim beats. **GATE P is signed** — `PEDAGOGY.md` carries
`VERDICT: PASS`, signed by the author (Om Mali) on 2026-10-09, and the Kokoro gate was re-run
without `--no-gate` afterwards to confirm it passes on its own. The audio was not regenerated
after signing, so the masters are the same cut GATE V cleared.

**One compile was killed mid-write** when the system ran low on memory, leaving a truncated
9:16 master (`moov atom not found`). Recompiled from the same beats; nothing upstream was lost,
because the per-beat mp4s and the locked durations are the durable state.

## Cost

`$0.00`. Kokoro TTS runs locally from a downloaded model; Remotion and ffmpeg are local. No API
key was used at any point, and no step asked for one.
