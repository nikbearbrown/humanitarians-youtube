# BUILD-LOG — verifying-private-ai-valuations

Rebuild of the 2026-08-08 cut using **brutalist.art** (`ai-explainer`, channel `claude-hai`).
Free/local throughout: Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

---

## What was rebuilt, and why

The previous cut (archived at `_previous-build/`) was built by the Mycroft repo's own tool:
6 beats, 112.7s — three Remotion title cards and three PNG stills on `"motion": "hold"`.
Under this toolkit that is a build failure, not a style choice (three consecutive held stills
fail THE PPT TEST; the four required Claude bookends were absent). See `PEDAGOGY.md`
§"Why the structure changed".

The rebuild keeps every fact and every number. It changes the structure (6 → 10 beats), the
shots (stills → native animated Remotion), and the narration wording (tightened to the
45–70-word body budget, evidence moved from the voice onto the screen).

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Skill: `ai-explainer`, not `fellows`.** | `fellows` requires the fellow's OWN recorded video to play as-is as a pass-through beat (THE REPORT IS THE CLOCK). The only .mp4 here was the previously machine-built cut, not a recorded report. `fellows` also blocks on GATE N (Professor Bear signs `NOTES.md`), which is not applicable to a self-authored progress update. |
| 2 | **Channel: `claude-hai`.** | The reel lives in `fellows/om-mali/` on the `@HumanitariansAI` channel. The alternative, `claude-liam`, carries IN-FOR-BEAR LAW ("this is Liam, in for Bear") in B00 and the outro, which collides with a first-person report that opens "Hi, I'm Om Mali." |
| 3 | **Voice: `am_onyx`, unchanged.** | `fellows/om-mali/README.md` records am_onyx as the fellow's persistent, already-recorded choice across the report series. A voice change would be a documented re-voice decision for the whole series, never a silent per-episode one. |
| 4 | **Greeting: `Ola, HAI`.** | The ai-explainer word budget allows the HAI persona only the shortest cues (Hi · Ola · Hej · Ciao). Portuguese, per the world-language hello lexicon. The Wagwan mod-10 rule is Bear-only and does not apply. |
| 5 | **Palette deviation, logged.** | Source figures used the Mycroft `brutalist/DESIGN.md` tokens (crimson `#C8102E` series, ochre `#C8860E` annotation). Rebuilt in the Claude fidelity skin — cream/ink/terracotta — because `ai-explainer` is a fidelity brand that may not be retinted. Palette only; no datum, ordering, or label changed. |
| 6 | **B02 shows tag NAMES, not numerals.** | The beat wanted a filing block with a real `<valUSD>` and `<balance>` pair. No such pair is recorded in `FACTCHECK.md` — only the resulting price. Inventing a plausible numerator/denominator would have looked better and been a DOUBLE-CHECK LAW violation, so the operands stay `<valUSD>` ÷ `<balance>` and only the confirmed quotient ($259.14, rows 2 and 5) appears. |
| 7 | **The "100x" headline was dropped.** | The source figure's right-hand panel was titled "And it kept 100x more rows than planned". 606,028 ÷ ~3,000 is ~202x, and no FACTCHECK row asserts either ratio. B05's title now states the measured figure instead (row 14). The only ratio spoken is ~600x — row 15, as corrected and confirmed. |
| 8 | **B06 compresses the four below-floor companies to one muted strip.** | The source figure gave Figure AI / Perplexity / Groq / Scale AI a full row each. The narration names none of them, and ten bars plus a stat block plus a callout in 17s violates one-idea-per-beat. The strip preserves the coverage floor's meaning without cramming. Flagged in `CHECKS-REPORT.md`. |
| 9 | **The three source PNGs stay in `pantry/` as reference only.** | REBUILD LAW: lifted images are placeholders, not visuals. They are never slotted as media. This also matters because, per `FACTCHECK.md`, the PNGs are the only surviving copies of those figures — the SVG sources were lost from the Mycroft working tree. |

---

## Toolkit defects found and fixed during this build

These were pre-existing bugs in `brutalist.art`, not artifacts of this reel. All three fixes are
backward-compatible — every existing beat sheet renders exactly as before.

1. **`runtime/scripts/remotion_scenes.py` could not launch on Windows.**
   The script called bare `npx` via `subprocess.run()`. On Windows the npm launcher is `npx.cmd`,
   so this raised `FileNotFoundError: [WinError 2]` and no Remotion beat could ever render.
   Fixed with `shutil.which("npx")`, which resolves the launcher on every platform.

2. **Frame-keyed bookend scenes were center-cut into frozen frames.**
   `ClaudeComposerAsk` finishes typing, arms the send button and lands its output lines by
   ~frame 115 (~3.8s), then holds — but it is registered at 900 frames (30s). `compile.py`
   center-cuts any clip longer than its beat, so a 30s render conformed to a 14.8s beat starts
   7.6s in: **the typing and the answer lines are chopped off both ends and the beat plays as a
   still.** This silently affects every reel in the toolkit, including the shipped exemplar
   `examples/ai-explainer/claude-debunked` (B00: 11.22s beat, 30s composition).
   Fixed by adding an OPTIONAL `durationInSeconds` prop plus `calculateMetadata` to
   `ClaudeComposerAsk`, `ClaudeVerdictArtifact` and `ClaudeTitleOutro`. Omit the prop and the
   registered default length is used, so nothing existing changes.

3. **EB Garamond was never actually loaded.**
   The Claude token stack asks for `"EB Garamond"` and the toolkit ships it at
   `runtime/fonts/EB_Garamond/`, but no `@font-face` existed anywhere in the Remotion project —
   so every serif in every reel silently fell back to Georgia. Copied the Regular and Medium
   TTFs into `runtime/remotion/public/fonts/` and injected the `@font-face` **inside this reel's
   own component file**, so the fidelity serif renders here without changing any other reel's
   output.

4. **Every non-ASCII character rendered as mojibake.** The worst of the seven.
   `remotion_scenes.py`, `compile.py` and `todo.py` read and wrote beat sheets with bare
   `read_text()` / `write_text()`, which use the ANSI codepage on Windows. The beat sheet is
   UTF-8, so every em dash, ellipsis, arrow and middot was decoded as cp1252 and handed to
   Remotion corrupted: `—` rendered as `â€"`, `…` as `â€¦`, `→` as `â†'`, `·` as `Â·`. It was
   visible in **every beat of the first cut**. The beat-sheet FILE was undamaged — cp1252 decode
   followed by cp1252 encode round-trips the bytes intact — so the corruption was invisible
   except on screen, which is exactly why the VISUAL QC LAW says to look at frames rather than
   trust the probe. Fixed by making every beat-sheet read/write explicitly `encoding="utf-8"`.
   `beat_lint.py` had the same bug and reported a mangled label in its own error message.

5. **`run.sh` handed POSIX paths to a Windows Python.** It built `$ROOT` and `$REEL_DIR` with
   `pwd`, which under Git Bash returns `/d/study_other/…`. Windows python3 cannot open that, so
   the first gate died with `FileNotFoundError`. Fixed with an `abspath()` helper preferring
   `pwd -W` where it exists (a no-op elsewhere).

6. **The review cut could never be assembled on Windows.** `compile.py`'s `--review` timecode
   passes the font path into an ffmpeg filtergraph. ffmpeg parses the graph before the option
   value, so backslashes are eaten as escapes and the drive colon terminates the option.
   Escaping the colon alone is NOT sufficient — verified against ffmpeg 8.1, the value must
   ALSO be single-quoted: `fontfile='E\:/path/f.ttf'`.

7. **GATE V could never pass, on any reel, on any platform.** `final_frame_check.py` preferred
   `*-slate.mp4` — the `--review` cut, which carries burned-in beat-id labels (bottom-left) and
   a running timecode box (top-right), both deliberately OUTSIDE the title-safe inset. So
   `edge-bleed` fired on the toolkit's own debug chrome in **every frame of every reel**: this
   build's first GATE V run reported 20 BLOCKERs on 20 frames, including the untouched
   proven-core outro. That noise is worse than no gate, because it buries real defects.
   Fixed to prefer the clean cut and fall back to the slate cut only when no master exists
   (i.e. the reel still has unfilled slates). After the fix: 0 BLOCKER, 2 MAJOR — and the 2
   MAJOR are a real, correctly-identified finding (see below).

---

## Gates

| Gate | State |
|---|---|
| **FACTCHECK** | PASS — all 20 rows CONFIRMED by the author 2026-08-08. The rebuild changed no figure, so those confirmations carry over. Two source-figure claims were *dropped* rather than carried (decisions 6 and 7). |
| **PROOF GATE / CHECKS-REPORT** | PASS — 6 SHOW / 4 justified-HOLD / 0 PUNT. Teaching arc 6/6. Written before the first compile. |
| **GATE P (pedagogy)** | **PASS — signed by the author (Om Mali), 2026-08-10**, after reviewing the slate cut. Covers the 6→10 restructure, the re-worded narration, the new B08 handoff prompt, and the palette deviation. Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than passed silently; the gate was re-run WITHOUT the override after signing and passes on its own. The narration is unchanged between the review cut and the master, so no audio was regenerated. |
| **GATE L** (beat-mix lint) | PASS — after one real catch. The sheet's `topic` was `MYCROFT · PRIVATE AI VALUATION`, exactly the "per-video guess" rule 7 exists to stop: `claude-hai` has a FIXED slot-1 kicker, `Irreducibly Human` (`runtime/qc/brand_labels.json`). Corrected in metadata and in both composer beats' props; B00/B08 re-rendered. The fit is real rather than merely compliant — the episode is a human hand-checking numbers a pipeline would have gotten wrong. |
| **GATE V** (frame-level visual QC) | PASS — 20 frames, 0 BLOCKER, 0 MAJOR → `_qc/REPORT.md`. |
| **GATE F** | not triggered — no Manim beats in this reel, so `SHOTLIST.md`/`PROMPTS.md` are not required. |

---

## Visual QC — what LOOKING at the frames caught that no gate did

The mp4 probe was green from the first compile. Every defect below came from reading PNGs.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| all 10 | Mojibake in every non-ASCII glyph (`—` → `â€"`, `…` → `â€¦`, `→` → `â†'`, `·` → `Â·`) | BLOCKER | Toolkit defect 4. All ten beats re-rendered. |
| B03 | The baseline rule ran straight through the second row of low labels ("T. Rowe Price", "ARK") | BLOCKER | Removed the heavy baseline (the two tier gridlines already anchor the chart) and dropped Y_LOW to 700. |
| B03 | The dashed repricing segment passed through the "2.27x — a new round" annotation, and would have crossed the high-tier labels | MAJOR | Moved high labels ABOVE the high line and the $589.0095 value clear to the right of where the dashes land, so no label can sit on the segment. |
| B03 | Annotation wrapped and orphaned the word "in" onto its own line | MINOR | Widened the note 430 → 540. |
| B09 | Outro filled only 11% of the safe area | MAJOR | `ClaudeTitleOutro` was a hardcoded 72/38/22px block marooned in a 1920×1080 frame. Now derived from composition height and distributed down the abundant axis. Prop contract unchanged. |
| B07 | Verdict card came out ~545px tall — `underfill` at 46% of safe (floor 55%) | MAJOR | `ClaudeVerdictArtifact` had its width fixed by an earlier pass but everything else stayed hardcoded in px. Type and padding now derive from composition height (~61%), which also makes the recap legible from across a room. Prop contract unchanged. B07 re-rendered before the master. |

Frames re-read after each fix; the final pass is clean at 0 BLOCKER / 0 MAJOR on the 4K master.

**Staleness check before the master.** `PrivateAiValuations.tsx` has an mtime newer than the
B01/B02/B04/B05/B06 renders, but the only edit after those renders was the B03 annotation width,
scoped entirely to `PavConvergence` — and B03 was re-rendered after it. B07 was the one genuinely
stale beat (its scene changed after its render) and was re-rendered. Nothing else needed rebuilding.

## Build facts

- **10 beats**, all filled by Remotion. Zero slates.
- **Audio**: Kokoro `am_onyx`, 155.50s total (2:35.5). Measured durations are the master clock
  and are written into each scene's `durationInSeconds` prop, so every animation RE-TIMES to its
  real narration rather than being truncated or freeze-padded.
- **Six reel-local scenes** in `runtime/remotion/src/PrivateAiValuations.tsx`, registered under
  the `PrivateAiValuations` folder in `Root.tsx`. Six deliberately different visual schemes —
  no two consecutive body beats share one (ILLUSTRATE LAW).
- **Deliverables**: `verifying-private-ai-valuations.mp4` — clean master, **3840×2160, 24fps,
  155.5s**; `verifying-private-ai-valuations-slate.mp4` — 1080p review cut with beat IDs and
  running timecode. Both also copied into `mp4/`.
- **Never published.** The master stays in this folder. Publishing is a separate, explicitly
  human-authorized step that this toolkit does not perform.
