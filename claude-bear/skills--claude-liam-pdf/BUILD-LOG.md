# BUILD-LOG — skills--claude-liam-pdf

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of `anthropics/skills/youtube/claude-liam-pdf/beat_sheet.json`
— a fully-built, Teardown-register skill explainer (7 beats: B00, B01, B02, B05, BVDT,
BHTF, BOUT; `claude-liam` / @NikBearBrown, no SCRIPT.md on the source). Its
`beats[*].narration_text` served as the locked narration per the redo contract. Never
touched the source reel's folder. Only `SUBJECT.json` was present on pickup; everything
else was built fresh this invocation.

**Facts kept unchanged:** the `pdf` skill routes to three Python libraries — `pypdf`
(manipulation: merge/split/rotate/watermark/encrypt/decrypt/metadata), `pdfplumber`
(extraction: text with layout, tables → pandas), `reportlab` (creation: Canvas or
Platypus); CLI tools `pdftotext`/`qpdf`/`pdftk`; OCR is a two-step pipeline
(`pdf2image` → `pytesseract`, never one step); the reportlab gotcha (never Unicode
subscripts — solid black boxes in the built-in fonts, use XML `<sub>`/`<super>` tags in
Paragraph objects); `FORMS.md` and `REFERENCE.md` are separate specialist files for
form filling and advanced pypdfium2/pdf-lib use; the skill doesn't cover PDF
accessibility, tagging, or digital signatures.

**Register: Teardown -> Plain.** The source's B05 (`PdfTell` — a hardcoded two-column
"WHAT IT GETS RIGHT" / "WHERE IT BITES" judgment card) and BVDT ("Verdict",
`ClaudeVerdictArtifact`) explicitly rank the design's trade-offs. Plain states the
identical delegation and gap as fact (this reel's B03: "never one library for every
job... read those before attempting either... accessibility, tagging, and digital
signatures [are not] in this skill at all") and lands it as the carry-out (BCRY)
instead of a verdict artifact or gets-right/bites card — same facts, judgment removed.

**B00 WRITER LAW:** the natural newcomer misreading of "hand Claude a PDF task" is
that one all-purpose library should handle it — the exact assumption the source's own
handoff beat (BHTF) already tested for ("if Claude uses pypdf's extract_text on a
scanned PDF... it missed the OCR path" only matters if you assumed one tool does
everything). Typed text: "There's one PDF library / for every job. / Wait — how does /
the pdf skill actually decide?", trigger "one" -> replacement "no one". B00 audio
measured 11.84s + `lead_silence_s` 0.8 = 12.64s window (TIMING LAW's >=9s floor cleared
with margin), narration 35 words. Verified across four frames (t=2s, 5s, 8s, 10.5s): at
t=2s the writer is still mid-typing the wrong word ("There's one|"); by t=5s the
correction has fully resolved ("There's no one PDF library for every job. / Wait —
how|"); by t=10.5s the writer is mid-way through the final corrected question ("...the
pdf skill actually|") with the beat not yet over — correction and framing both land
inside the beat with margin.

**B05 (`PdfTell`) + BVDT (`ClaudeVerdictArtifact`) -> B03 (`SkillTeardownMechanism`) +
BCRY (`WantQuote`):** the source's two judgment-carrying beats collapse into one
factual mechanism beat (the routing rule + what's delegated + what's absent) and the
bare carry-out sentence, matching `simple`'s law that the verdict-recap position
becomes the carry-out line in Plain register. `PdfTell` was NOT reused for B03 even
though it renders (`./art scenes --check` confirmed RENDERABLE) because its
"gets right"/"bites" columns are hardcoded into the component's pixels — reusing it
would keep a Teardown-judgment visual on screen no matter how the narration was
rewritten, so `SkillTeardownMechanism` (a generic, judgment-free heading+body card
already in the library) was used instead. Same beat count (7 -> 7), renumbered
sequentially (B00, B01, B02, B03, BCRY, BHTF, BOUT vs. source's B00, B01, B02, B05,
BVDT, BHTF, BOUT).

**B01/B02 reused as-is:** `PdfAnatomy` and `PdfOperations` render the library/task/tool
tables and the reportlab gotcha with no baked-in judgment — pure fact, so they carry
over from the source unchanged (props: `sparkLine` only; content is fixed in the
component). Confirmed renderable via `./art scenes --check` before use (GATE L).

**BHTF:** kept the source's scanned-invoice OCR+tables prompt near-verbatim — already
a real, paste-ready Claude prompt a general viewer can run today, and it drills the
exact wrong guess (one tool does everything) B00 opened with. Dropped only the
explicit "Use the PDF skill" instruction, since a general first-time viewer is being
handed a task, not told to invoke a specific skill by name.

**Close:** BOUT's `ClaudeTitleOutro` (`@NikBearBrown`) -> `OutroCTA` (Humanitarians AI
skin, `@HumanitariansAI`), per hai-simple's channel-skin law. Voice/persona unchanged
— Liam, Kokoro `am_onyx`, "in for Bear."

**No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source beat
was already a registered Remotion component. No NO-GENAI/NO-PANTRY substitution was
needed beyond B00 (mandatory writer-open swap), B03 (mandatory judgment-card swap),
and BOUT (mandatory HAI-skin swap).

## Build

- GATE T (`type_check.py`): initial FAIL — B03's `body` prop (14 words) exceeded the
  12-word pull-quote limit (§8.5 no-wordy-card). Fixed by shortening to a 9-word label
  ("Forms, advanced use: own files. Not here: accessibility, signatures."). Re-run:
  PASS, 7/7 beats.
- Audio: `generate_audio_kokoro.py` — 7/7 beats, $0.00, Kokoro `am_onyx`.
- Remotion: `remotion_scenes.py` timed out at both the 2-minute and 10-minute Bash
  limits while rendering the full reel in one pass (each beat individually renders
  fine; the combined wall-clock for all 7 exceeds both timeouts). Worked around by
  rendering beat-by-beat with `--only <BEAT_ID>` — no orphaned background renders, each
  invocation run to completion in the foreground before starting the next.
- One corrupted output found and fixed: the first (2-minute, killed-mid-write) attempt
  left a truncated `media/B00.mp4` ("moov atom not found" — confirmed via `ffprobe`).
  The later `--only B00` run had skipped it as "already rendered." Forced a rebuild with
  `--only B00 --force`; re-verified via `ffprobe` before compiling.
- Compile: `compile.py` — 7/7 filled, GATE AUDIO PASS (mean_volume -23.9 dB, max -3.0
  dB), content-check PASS, frame-check PASS, lane-check PASS. Output:
  `skills--claude-liam-pdf.mp4`, 150.56s, 3840x2160 (4K master — `compile.py` forces
  4K by default; no separate `--height 1080` review cut was needed since the 4K master
  itself passed every gate).
- Gate V (frame pulls + read): B00 at t=2s/5s/8s/10.5s confirms the correction lands by
  t=5s, well inside the beat. Mid-beat pulls at t=30s (B01), t=75s (B02), t=110s (B03),
  t=124s (BCRY), t=138s (BHTF), t=149s (BOUT) all show clean, legible, non-overlapping
  type inside safe insets; B03 confirmed judgment-free (heading + short body, no
  gets-right/bites framing); BOUT confirmed HAI skin (@HumanitariansAI, no
  @NikBearBrown).
- Audio presence: `ffmpeg -af volumedetect` on the compiled master — mean_volume
  -23.9 dB, well above the -40 dB floor.
- mtimes: `skills--claude-liam-pdf.mp4` (2026-09-04T15:06) newer than `beat_sheet.json`
  (2026-09-04T14:44, unedited since compile) — cut is current, not stale.

**Result: review cut PASSES every gate.** `skills--claude-liam-pdf.mp4` exists, is
newer than `beat_sheet.json`, carries audible narration audio, and is a 4K master
(3840x2160) — not a 1080p slate. Playlist: "Extending Claude — Skills, Plugins &
Connectors" — family `skills` has no literal `playlists.json` prefix match (shorter
than the `claude-skills`/`claude-agent-skills` keys); resolved by direct content match
on the reel's actual subject (an Anthropic Agent Skill's anatomy and routing rule)
rather than falling to the `hai-simple`->"Claude Basics" fallback, matching the
override already established today by every other `skills--claude-liam-*` sibling in
this batch (`brand-guidelines`, `canvas-design`, `doc-coauthoring`, `docx`,
`internal-comms`) per `HAILOOP-LOG.md`. `metadata.playlist` was corrected and the
reel recompiled (metadata-only sheet edit, `compile.py` re-run per the COMPLETION LAW
to avoid leaving the cut stale) — same GATE AUDIO PASS (-23.9 dB), same 7/7 fill,
mtime re-verified newer than `beat_sheet.json` after the recompile.
