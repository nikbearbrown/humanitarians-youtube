# BUILD-LOG — entity-resolution-and-the-golden-set (week 4)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Third episode of the Private AI Valuation Agent series. **There is no week 3 video** — the
series goes week 1 → week 2 → week 4.

---

## Where the inputs came from

The requested script path — `mycroft/data/raw/.../docs/video_script_week4.md` — **does not
exist.** The worklog explains why: *"Narration script moved out of the repo into the video
working folder, with a README mapping each figure to its beat."* It had already been moved into
this reel folder as `narration_script.md`, together with `README.md` and `figdata_week4.json`.
Nothing was missing; the path in the request was just stale.

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | Already here (moved out of the Mycroft repo) | input, unmodified |
| `README.md` | Already here — the figure-to-beat map and the "three things the script is careful about" | input, appended with a pointer to the built reel |
| `figdata_week4.json` | Already here | **the source of truth for every on-screen number** |
| `pantry/w4-*.png` + `.svg` | Were in this folder's `images/` | **moved to `pantry/`** — see below |

**Why the figures moved out of `images/`.** `run.sh` uses `images/` as a compile OUTPUT
directory (`cp media/*.png images/`), so leaving the four source figures there would have mixed
them with rendered stills and made it impossible to tell input from output. They now sit in
`pantry/` with the rest of the series' reference art. The copies in the Mycroft repo were left
alone — this request did not ask for a move, unlike week 2.

---

## Every number is injected, and two are asserted

The reel plots `figdata_week4.json` directly; no figure number is typed into a scene or a beat
sheet by hand. Two assertions run at injection time and fail the build if violated:

```
assert len(universe_rows) == 7      # not "top 7 by spelling count"
assert sum(names) == 128            # 51+28+23+11+10+3+2
assert watchlisted_total == 24      # xAI 19 + Perplexity 3 + Groq 2
```

These exist because the worklog records the source figure getting exactly this wrong: a chart
captioned "seven companies" was taking the top seven by count, which **silently swapped Cerebras
and Figure AI out for xAI and Perplexity — both watchlisted, marks not published.** The
assertion makes that class of error impossible on this side of the boundary.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Four script sections → eight body beats.** | Three sections each carried two ideas: the spelling problem AND the ground-truth set (0:18); the scoreboard AND the dot that explains it (0:42 — the script's own shot note asks for two shots); the retraction AND the threshold question (1:38, with `w4-tie` mapped there in the README). Split at those seams. |
| 2 | **~130 words of connective narration added.** | Eight body beats at the 45–70 word budget need ~400 words; the script's body is ~240. Every added sentence is connective or judgment. No added claim, and every added figure is injected from `figdata_week4.json`. |
| 3 | **"Last month's simple name patterns" → "the patterns I started with".** | DOUBLE-CHECK LAW: strip what dates the video. Weeks 1–2 shipped the same month, so "last month" is both datable and slightly wrong. Same referent (`A_like_patterns`). |
| 4 | **The ground-truth line was rephrased.** | The script's "a ground truth set — three hundred and twenty-two of these strings" risks implying the labels are hand-made. Only **8 of 322** are. The line now says each string is "labelled with the company it actually means" — true, without implying who did it — and B09 states the 8 out loud. |
| 5 | **B08's holding names shortened at the exposure clause.** | The real strings are up to 138 characters (`DXYZ SPACEX I LLC (ECONOMIC EXPOSURE TO SPACE EXPLORATION TECHNOLOGIES CORP., 99% CLASS A COMMON STOCK AND 1% SERIES J PREFERRED STOCK)`). Rendered in full they crossed the right title-safe edge AND collided with the note lines. The source figure shortened them too; the truncation is disclosed in the on-screen source line. |
| 6 | **The trailing-space duplicate is surfaced, not hidden.** | Tie rows 3 and 4 are the same 137-character string differing **only by a trailing space** (137 vs 138 chars). Truncated they look like a duplicate row, which reads as a bug. The narration now says "two of those three are the same string, differing only by a trailing space" and the row carries that note. It is a real entity-resolution detail and it earns its place. |
| 7 | **"three genuine SpaceX vehicles" → "three entries that really are SpaceX".** | Follows from decision 6: there are three correct golden-set ENTRIES but only two distinct vehicles. The original phrasing would have overstated it. |
| 8 | **Greeting rotated to `Ciao, HAI`.** | Week 1 `Ola`, week 2 `Hej`. The lexicon rotates so the series never repeats a language; HAI takes only the short forms. |
| 9 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name. Set at authoring time, so GATE L passed on the first run for the second episode running. |
| 10 | **`EntityResolutionGoldenSet.tsx` is self-contained.** | Same reasoning as week 2: reel-local files duplicate the chrome helpers so the earlier signed masters stay re-renderable byte-identically. |

---

## Toolkit state

No new toolkit defects surfaced. All seven Windows/portability fixes from week 1 were exercised
again and held. Added for this reel: `runtime/remotion/src/EntityResolutionGoldenSet.tsx` (eight
components) and its folder in `Root.tsx`. Nothing else in the toolkit was modified.

---

## Visual QC — what LOOKING at the frames caught

GATE V's first pass reported 2 BLOCKER. Reading the PNGs found one more that the gate could not
see, and it was the worse of the two.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B08 | Full 138-char holding names crossed the right title-safe edge, wrapped, and overprinted the note lines beneath | BLOCKER (gate) | Names shortened at the exposure clause; truncation disclosed in the source line. The trailing-space distinction that the truncation would have hidden is now stated in the narration (decisions 5–7). |
| B02 | The "128 spellings in total" block sat directly on top of the 3,204,853 haystack line — **two elements overprinting each other** | MAJOR, **missed by GATE V** | Both elements were individually inside the safe area, so `edge-bleed` and `underfill` both passed and the collision was invisible to the gate. Total block moved to the right column under the samples panel; bar pitch tightened 74 → 70. |

Frames re-read after each fix. Final pass: **24 frames, 0 BLOCKER, 0 MAJOR.**

**Note on GATE V's blind spot.** This is the second time in the series that reading frames has
caught a text-on-text collision the gate missed (week 1: B03's baseline rule through the manager
labels). The gate checks edge bleed, canvas fill and contrast — not overlap. Worth knowing when
deciding how much to trust a clean report.

---

## Gates

| Gate | State |
|---|---|
| **FACTCHECK** | 20 rows, all traced. **Rows 2, 12 and 16 flagged** — the universe-v1 filter, the hardest-cases precision LOSS, and the corrected "not LEI-confirmed" wording. |
| **PROOF GATE / CHECKS-REPORT** | PASS — 8 SHOW / 4 justified-HOLD / 0 PUNT. Teaching arc 6/6. Written before the first compile. |
| **GATE P (pedagogy)** | **PASS — signed by the author (Om Mali), 2026-08-23**, after reviewing the slate cut. Covers the three script splits and the added narration, the three wording changes, FACTCHECK rows 2/12/16, the B10 handoff prompt and the palette deviation. Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than passed silently; the gate was re-run WITHOUT the override after signing and passes on its own. |
| **GATE L** (beat-mix lint) | PASS on the first run. |
| **GATE V** (frame-level visual QC) | PASS — 24 frames, 0 BLOCKER, 0 MAJOR → `_qc/REPORT.md`. |
| **GATE F** | Not triggered — no Manim beats. |

---

## Build facts

- **12 beats**, all filled by Remotion. Zero slates.
- **Audio**: Kokoro `am_onyx` (the fellow's persistent voice, unchanged since week 1),
  **201.75s (3:21.8)**. B08 was re-voiced once after decision 6 changed its narration.
- **Eight reel-local scenes**, eight different visual schemes. No two consecutive body beats
  share one (ILLUSTRATE LAW).
- **The episode argues against its own author in three places** — B04 (precision loss), B06/B07
  (an approved label overturned, both scores published), B08 (a limit no threshold fixes). The
  cut is built to keep those rather than soften them; see `PEDAGOGY.md` §Honesty check.
- **Deliverables**: `entity-resolution-and-the-golden-set.mp4` — clean master,
  **3840×2160, 24fps, 201.75s**; `-slate.mp4` — 1080p review cut with beat IDs and running
  timecode. Both mirrored into `mp4/`.
- **Never published.** The master stays in this folder. Publishing is a separate, explicitly
  human-authorized step that this toolkit does not perform.

## Finalization (2026-08-23)

GATE P signed. Three things done before and after the master render:

1. **Staleness verified per COMPONENT, not per file.** `EntityResolutionGoldenSet.tsx` has an
   mtime (01:25) newer than seven of the twelve renders, so a file-level check would have
   demanded a full re-render. The 01:25 edit was the B02 collision fix, and all three of its
   changes were confirmed by script to fall inside the `W4Spellings` component span — B02 was
   re-rendered at 01:26, after them. Nothing else needed rebuilding.
2. **Two corrections to this reel's own signed PEDAGOGY.** The length-law block still carried
   pre-QC word counts: B08 was listed at 57w when the trailing-space rewrite had taken it to
   67w, and the text claimed all eight body beats sat inside the 45–70 band when B02 (43w) and
   B06 (71w) sit just outside. Both are deliberate and are now stated as such rather than
   denied. Measured runtime added.
3. **`mp4/` refreshed by hand.** `./art final` writes only the master, so the mirrored copies
   were stale again — the same step weeks 1 and 2 needed.

GATE V was re-run against the 4K master itself, not the 1080 cut: **24 frames, 0 BLOCKER,
0 MAJOR.**
