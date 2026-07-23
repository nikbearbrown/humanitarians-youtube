# BUILD-PROMPT — Kokoro: The 5 Japanese Voices

COMPANION REFERENCE CUT in the Kokoro roster family (siblings: kokoro-free-voices — the
story; kokoro-all-28-english-voices — the English roster; and the other language rosters).
This one is for people who want to hear the Japanese 5 voices before casting. beat_sheet.json
is ALREADY AUTHORED — do not re-author. PEDAGOGY.md carries VERDICT: PASS. No
chapter_number — reference cuts ride outside the chapter order.

Standing rules #1–#4 (EXAMPLES-CAMPAIGN.md) apply. Prereq: kokoro-onnx + model files
(short film's Phase A) and the KokoroRosterCard / KokoroRosterCard916 components (authored
by the all-28 build — if they don't exist yet, author them per that BUILD-PROMPT first).

## Build

1. FACTCHECK (this family's is stricter — non-English is the thin edge of the pack):
   --list-voices must contain every sheet voice; grades came from hexgrad/Kokoro-82M
   VOICES.md 2026-07-13 (ungraded voices show "—" and STAY ungraded — never invent a
   grade); jf_tebukuro's grade needs explicit verification (the doc listing was ambiguous). The in-language name lines and localized house lines were authored by
   the toolkit, not a native speaker: verify each with a fluent source (or a strong
   translation check), fix any that read wrong, and note "localized lines
   machine-authored, verified at build" in FACTCHECK.md and the description.
2. Audio: generate_audio.py --only B00 (the only paid beat), then
   generate_audio_kokoro.py for the rest ($0.00 — lang_for() routes each voice to its
   G2P language; if Mandarin errors on lang "cmn", try "zh" and log the fix). LISTEN to
   every voice — a garbled name gets a spelling fix in that beat's text; a garbled LINE
   gets logged honestly (thin-support evidence, not hidden).
3. Render: KokoroRosterCard per roster beat (props: name, code, group, grade, index,
   topic), B00/B99 house patterns, remotion_scenes.py FOREGROUND (rules #3/#4).
4. ./art run → qc-sheet BY LOOKING (rule #2): every card's name/group/grade/index
   correct. GATE: review cut + listening notes; WAIT for human approval.
5. After approval: ./art final (master staged AFTER final), <slug>.srt, publish unlisted
   to the Brutalist playlist (no chapter slot). Description: per-voice YouTube chapter
   markers (timestamp + name + grade), the machine-translation note, and cross-links to
   the whole Kokoro family (short film + all-28 + the other language rosters as they
   publish). Append to PUBLISH-LOG.md; findings to CAMPAIGN-FEEDBACK.md.
