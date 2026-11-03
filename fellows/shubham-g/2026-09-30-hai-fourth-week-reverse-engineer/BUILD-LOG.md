# BUILD-LOG — hai-fourth-week-reverse-engineer

## 2026-09-30 — first build (Windows 11, Git Bash, native toolchain)

Decisions
- New reel, not a variation: week 4 of the HAI learning series is about the process itself — build one learning
  video, then reverse engineer it (decision log → template → six-step playbook → fix-to-rule) so recruits and
  editors work faster, more efficiently and consistently. New greeting **Jambo** (Namaste/Hola/Hej/Ciao/Bonjour/Olá/Aloha
  already used) and seven new scenes; no earlier body scene reused.
- Channel: claude skin, chip **@Shubh & @HumanitariansAI** on every Claude page — beginning (B00), middle (B05),
  end (B10 verdict, B11 handoff) — and the outro. Voice Kokoro `af_bella`, Plain register. B01 opens
  "Hi, I'm Shubh, and this video is about week four…". The brief's reference link was a bare youtube.com URL, so
  no reference video was used.
- Beat 2 correction: "Every video is built from scratch." → `scratch` → `a playbook` (single-word trigger — the
  component only matches whitespace tokens). `qc.sparse_by_design` declared up front for the typing frames.
- Honesty: every decision and fix on screen is a real one from this series (see FACTCHECK.md); the only chart
  (B08 time paths) is captioned "Illustrative — not measured".
- GATE L: no fitting scenes for build/reverse, decision log, fixed-spine template, playbook, fix→rule, gains or
  limits → built `runtime/remotion/src/scenes/Week4Playbook.tsx` (dual-aspect; `<Name>` and `<Name>916`), reusing
  exported helpers from ContentPerformance.tsx; scene-index re-run.
- Lessons from last week's build applied before the first render: labels ≥ 44 px (landscape) / serif 92, sans 78
  (portrait); accent on bars/underlines/arrows only; no number discs; ≤ 5 verdict lines; portrait hairline borders.

QC fixes
- Preview stills: B02 saved row moved down; B06 checks forced into a column, grid kept off the logo; B07 rows enlarged.
- Portrait previews: B04 slots overflowed → smaller spine blocks, tighter slots; B06 clipped checklist text →
  checkmarks only in portrait; B08 first label hit the spark line → lanes/gains reflowed.
- GATE T (16:9): B04 ink-bordered lit blocks fused with their labels (§8.6b) → hairline borders, lit = card fill;
  B07 thick accent arrows read as accent text (§8.3) → ink arrows, accent bar on each rule card.

Portrait-only props: `python portrait_props.py vertical/beat_sheet.json` (short labels; B01 five-line reflow at 300;
B10 four lines, textScale 2.0; B12 title on four lines, scale 0.8).

Environment notes
- `PYTHONUTF8=1` is required on Windows; review cuts use `ART_NO_DRAWTEXT=1`; portrait review cut `--height 1920`.
- Portrait GATE V: B00 segment title crossed SAFE916 → portrait segment "Reverse Engineer It".

Gate results (final exports)
- 16:9 renders/hai-fourth-week-reverse-engineer.mp4 — 3840×2160, 165.7 s; GATE L/V/T pass; receipt hai-fourth-week-reverse-engineer.verified.json
- 9:16 renders/hai-fourth-week-reverse-engineer-vertical.mp4 — 2160×3840, 165.7 s; GATE L/V/T pass; receipt hai-fourth-week-reverse-engineer-vertical.verified.json
- Frame review by eye: `_qc/beats/sheet*.png` (15/50/90 %) and `vertical/_qc/beats/sheet.png` (50/92 %).
