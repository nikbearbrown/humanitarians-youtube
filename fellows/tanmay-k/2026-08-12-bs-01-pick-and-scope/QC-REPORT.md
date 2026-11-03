# QC REPORT — build log

Append-only, dated. Every defect below was found by looking at frames or by measuring the
output — not by reading the code and assuming.

**Film:** *Your Job Description Is Too Generic for AI — Four Questions That Fix It*
**Built:** 2026-08-18 · Brutalist toolkit (Kokoro + Remotion) · `deep-explainer`
**Output:** 3840×2160, 17 beats, narration `am_onyx`, presenter Tanmay Kulkarni

---

## Gate summary

| Gate | Result |
|---|---|
| **Gate P** — premise | ✅ PASS (author, 2026-08-18) |
| **Gate P** — narration | ✅ PASS (author read-aloud, 3 revisions applied first) |
| **Gate L** — beat-mix lint | ✅ clean |
| **Gate F** — paperwork | ⚠️ bypassed by construction (see §2), satisfied manually |
| **Gate V** — visual QC | see §7 — final numbers pending last render |
| Silence sweep (§6) | ✅ clean, 0 gaps >0.55s across all 17 beats |
| Resolution / clock | ✅ 3840×2160, duration == measured audio |
| PROOF `/show` on frames | ✅ run — 2 defects found and fixed (§5) |

---

## 1. Setup — two toolkit blockers

**macOS bash is 3.2.** `./setup` uses `declare -A`, which needs bash 4+, so the doctor half
crashed at `ffmpeg: unbound variable` **while still exiting 0** — an install that reports
success and silently skips its own verification. Run the doctor under Homebrew bash 5:

```bash
PATH="$PWD/.venv/bin:$PATH" /opt/homebrew/bin/bash ./setup
```

**System `python3` is 3.9.6 against a 3.10+ requirement**, and `setup --install` passes
`--break-system-packages`. Installed into an isolated `.venv` on python3.12 instead; nothing
touched the OS Python.

Readiness after that: audio, captions, Manim, Remotion, slates/compile all ✅. Only *Manim
equation beats* blocked (no LaTeX/`dvisvgm`) — irrelevant here, this film has no equations.

## 2. A phantom Manim scene, created by a comment

`run.sh` finds Manim scenes by **regex over raw source text** — it never imports or parses
Python. The first `scenes.py` spelled the example out literally as `class B05_Split(Scene)`
**inside a docstring**, and the scan duly registered a `B05_Split` scene that does not exist.

Had it rendered, it would have produced a blank Manim clip and slotted it **over the B05
Remotion comparator** — the film's central side-by-side. The example is now written
`(manim.Scene)`, which is valid Python and cannot match, with a warning to keep it that way.

**Consequence:** with the phantom gone, `$PENDING` is empty and **GATE F never fires** — it
only gates when there is something to render. The paperwork requirement is therefore bypassed
by construction, not satisfied. `FACTCHECK.md` was written anyway, per PLAYBOOK §1.

## 3. Branding — caught by lint, and I had reasoned it out wrongly

`beat_lint` rule 7 rejected `brand: claude-liam` + `folderLabel: @HumanitariansAI`. I had
earlier decided `claude-liam` was a harmless legacy *directory* name; the toolkit treats it as
a live brand key binding kicker, chip and persona together.

Switched to **`claude-hai`** — chip `@HumanitariansAI`, voice `am_onyx`, Pragmatist register,
all already matching this film. Deciding factor was narrative: the film says "Humanitarians
AI" aloud in B00/B01/B13, so a `@NikBearBrown` chip would contradict its own audio.

Also: **`topic` is not a per-video description.** Rule 7 requires it to *equal* the fixed
per-channel series kicker (`Irreducibly Human`). The descriptive line moved to `subject_line`.

## 4. Underfill — three attempts, and the middle one was a regression

Gate V rejects content covering under 55% of the title-safe area.

| Pass | BLOCKER | MAJOR | What happened |
|---|---:|---:|---|
| 1 | 0 | **26** | Every beat under 55%. My components capped at `width*0.84`/`0.88` with hard pixel caps. |
| 2 | **16** | 10 | I raised width to `0.94` **and kept 3% parent padding** — two competing width systems. Content crossed title-safe → `edge-bleed`. **Strictly worse: I turned 26 MAJORs into 16 BLOCKERs.** |
| 3 | 0 | 8 | One width system: parent 6% padding defines the box, child fills at 100%, `boxSizing: border-box`. |
| 4 | 0 | *pending* | Remaining 8 addressed via `ClaudeArtifactCardFull` (§8). |

**Pass 2 was predicted and shipped anyway.** I wrote before rendering that bigger type in
fixed boxes risked clipping, then committed a full 4K render without checking geometry. The
fix was a 20-second still.

**Method that worked:** render an isolated `remotion still`, measure the content bbox against
title-safe with PIL, then look at the PNG. The outro went 15% → 33% → 78% across three
iterations in under two minutes total.

## 5. PROOF `/show` pass on frames — two defects invisible to Gate V

Gate V passed these frames at 0 blockers. Both defects below required *looking*.

**5a. The on-screen handle contradicted the audio.** All four `ClaudeComposerAsk` beats
(B00, B01, B09, B12) rendered the component's default `folderLabel` — **`@NikBearBrown`** —
while the narration says "Humanitarians AI". `folderLabel` is a per-beat prop; I set the brand
in metadata and never passed it through. Precisely the contradiction I chose `claude-hai` to
avoid. **Fixed:** `@HumanitariansAI` on all four.

**5b. Card copy contradicted the narration.** The plain-language pass touched only
`narration_text`. Every card still read *"Does it exclude, or only describe?"*, *"Who is your
nearest neighbour?"*, *"the load-bearing phrase"*, *"Verdict flipped"* — while the voice said
"rule anyone out", "closest job to yours", "the words doing the work", "pass-or-fail". A
viewer would have heard one thing and read another **for the film's entire framework**.

PLAYBOOK §1 warns about exactly this: *"Check on-screen card text for the same issues as
spoken narration — a pass that only scans `narration_text` can miss a bad claim sitting in a
visual-card prop."* **Fixed:** 12 beats' props rewritten to match the spoken words.

**What the pass confirmed as sound:** B04B's AGS/HIGN attribution legible with its "wrong"
chip; B06 and B07 carry `PREPRINT` labels in-frame *with* their numbers; B07's limitations
footer present; B08's dimmed column still readable at the 0.45 floor; B10B pairs 42%/17%
against 17%/8% with the bound beneath it; B11 shows keep/correct together.

**One factcheck catch on the frame:** B06's card said "persona" in our labels while narration
said "personality". Aligned lines 1/2/3/5 but **left line 4 verbatim** — *"Longer persona
prompts damage more"* is a direct quote in quotation marks. Rewording a quote to match house
vocabulary would be a factcheck violation.

## 6. Silence sweep — PLAYBOOK §1d

Six beats use deliberate hard stops for rhythm, which is the pattern §1d warns can read as a
dropped word. Swept all 17 beats at `silencedetect=n=-40dB:d=0.55`:

**Zero gaps over threshold.** B02's *"healthcare professional. Software engineer. Financial
analyst."* and B04B's *"She could write those words. She probably has."* read as rhythm, not
holes. Measured, not assumed.

## 7. Audio as the clock — 14 stale clips

The narration was rewritten twice (plain-language pass, then three author revisions). Total
runtime barely moved, but **per-beat durations moved a lot** — B10 25.4s → 38.9s, B07 30.6s →
25.0s. Comparing each rendered clip against its audio found **14 of 17 stale**, only B04, B08
and B12 within 0.25s.

Reusing a clip whose length no longer matches its narration would desync the film. Checked by
measurement rather than by tracking which beats I had edited.

## 8. Components built for this film

All additive. No shared component was modified — they are referenced by other reels, and the
underlying issue is a toolkit-level one (§9).

| Component | Purpose | Fill achieved |
|---|---|---:|
| `ClaudeFourQuestionBoard` | framework as a structure; `activeIndex` lights one row | 66% |
| `ClaudeSplitComparator` | side-by-side; **both columns on one shared spring** so neither can land late and fail the ≥2s gate | 94% |
| `ClaudeArtifactCardFull` | numbered artifact card, `chrome: window \| artifact` — one component covering both looks | 95% |
| `ClaudeTitleOutroFull` | resolution-scaling outro | 78% |

## 9. Toolkit issue to raise upstream

**Three shared components size in absolute pixels and therefore do not scale to 2160p.**

| Component | Evidence | Fill at 4K |
|---|---|---:|
| `ClaudeWindow` | hardcodes `width: 1100` — 57% of a 1920 frame, **29% of a 3840 one** | 18–20% |
| `ClaudeVerdictArtifact` | `fontSize` 30 / 46 / 28 | 53% |
| `ClaudeTitleOutro` | `fontSize: 72`, `maxWidth: 1080`, `marginTop: 28` | 15% |

**They are correct at 1080p and fail only at 4K.** That is the precise framing: not "badly
sized" but "does not scale". The fix is mechanical — convert absolute pixels to fractions of
`height`, and let parent padding be the only width system. Proven on four components here.

Any reel rendering these at 2160p will fail Gate V on underfill. Worth fixing once upstream
rather than per-film.

## 10. Process lessons

1. **Render a still before a full pass.** Two stills caught geometry problems in seconds; the
   alternative cost a 15-minute 4K render and a regression.
2. **Never touch a reel's files while a run is live.** I deleted `media/B13.mp4` mid-compile
   after confirming Remotion's node processes had exited — but `compile.py` was still reading
   clips. It **truncated the clean master by 9.66s**, exactly B13's length. Checking one
   process and generalising to the pipeline is unsound.
3. **Documentation is not the artifact.** Every significant error this build came from
   trusting a description over the thing itself: the README's `State` column instead of the
   disk (reported 968 open topics; the real number was 136), the voices `.bin` instead of the
   generator's allowlist (`af_kore` is present but rejected), a remembered legibility comment
   instead of a rendered frame.
4. **A model agreeing with you is not a source.** Sonnet 5 asserted the Beers Criteria
   licensure framing in our own trial data; it was plausible and it was drafted as fact. It is
   false. See `FACTCHECK.md` §2.

---

## Final verification — 2026-08-18

- [x] **Gate V: 0 BLOCKER, 0 MAJOR** · `run.sh` exit 0
- [x] **`ffprobe`: 3840×2160** — verified on the file, not inferred from the `--height` flag (PLAYBOOK §6 records it silently producing 720p once)
- [x] **Duration 505.8s == sum of `mp3/timings.json` (505.8s)** — audio is the clock and the clock holds
- [x] **Contact sheet reviewed end to end** — all 17 beats
- [x] **`@HumanitariansAI` on all four composer beats** (B00, B01, B09, B12) — confirmed on frames
- [x] **No card text contradicting the narration** — verified case-insensitively across every
      displayed string on every beat, and confirmed on the B10B frame at 15%. One licensed
      exception: B06 line 4 keeps "persona" because it is a verbatim quote in quotation marks.
- [x] **Moment-of-assertion legibility** — 12 extra frames at 15%/30% of the six contract
      beats. B06 at 4.7s of 34.7s already carries all three numbers, the quote, the caveat and
      the `PREPRINT` chip; B10B at 5.4s carries both columns, both chips and the bound.

**Gate ledger: Gate P ✅ (premise + narration) · Gate L ✅ · Gate V ✅ 0/0 · silence sweep ✅ ·
PROOF Phase 3 ✅ clear-for-public, teaching 12/12, production gate PASS.**

Outstanding, carried forward rather than fixed: **motion monoculture — 16/17 beats Remotion
(94%) against a ~40% cap.** Tagged `[RESHOOT/NEW SOURCE]`; the only punch-list item that
cannot be fixed with a prop edit. Not a gate failure. Standing item for bs-02 and bs-03.
