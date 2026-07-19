# BUILD-LOG — Kokoro: The 9 Romance-Language Voices

## HUMAN FEEDBACK — 2026-07-13

Build following the same pattern as the other language rosters (Mandarin, Japanese, Hindi):
each language + English subtitle on screen on every roster card.
Noted: Japanese voices at C+/C/C- mixed Chinese phonology — documented in Japanese BUILD-LOG.
Moving on to Romance.

## BUILD LOG — 2026-07-13

### Phase A — prereq check + FACTCHECK

kokoro-onnx 0.4.7, model files already present.
`--list-voices` confirms all 9 Romance voices:
  ef_dora, em_alex, em_santa (Spanish)
  pf_dora, pm_alex, pm_santa (Portuguese BR)
  if_sara, im_nicola (Italian)
  ff_siwis (French)

Grades per hexgrad/Kokoro-82M VOICES.md 2026-07-13:
  Spanish ef/em voices: ungraded (—) — pack does not score them
  Portuguese pf/pm voices: ungraded (—) — pack does not score them
  if_sara: C · im_nicola: C · ff_siwis: B- (best non-English grade in the pack)

lang_for() routing per prefix: e→es, p→pt-br, i→it, f→fr-fr ✓

Localized lines machine-authored (not a native speaker). Verified at build:
- Spanish: "Soy Dora/Alex/Santa, voz española." ✓
  "La máquina pone las manos; el gusto lo pones tú." ✓
- Portuguese: "Eu sou Dora/Alex/Santa, voz brasileira." ✓
  "A máquina traz as mãos — o gosto é seu." ✓
- Italian: "Sono Sara/Nicola, voce italiana." ✓
  "La macchina porta le mani — il gusto lo porti tu." ✓
- French: "Je suis Siwis, voix française." ✓
  "La machine apporte les mains — le goût, c'est vous." ✓

KokoroRosterCard nativeFont() updated: CJK detection added before Chinese fallback,
Latin script now falls through to FONT.display (was incorrectly using FONT_ZH before).

### Phase B — audio

- B00 (ElevenLabs): 31.9s — "My clone, in English — the Romance languages belong to the cast..."
- B01 ef_dora: 4.29s · B02 em_alex: 4.29s · B03 em_santa: 4.31s (Spanish)
- B04 pf_dora: 4.07s · B05 pm_alex: 4.16s · B06 pm_santa: 4.16s (Portuguese BR)
- B07 if_sara: 4.33s · B08 im_nicola: 4.93s (Italian)
- B09 ff_siwis: 3.99s (French) · B99 ff_siwis: 3.99s
- Total actual duration: 74.4s

### Phase C — Remotion render + compile

- remotion_scenes.py (foreground): 11/11 beats rendered
- Latin script font fix working: subtitles render in FONT.display not FONT_ZH ✓
- Grade chips: ungraded (—) = crimson · C = slate · B- = teal ✓
- QC sheet verified: all 9 names/codes/groups/grades correct, bilingual subtitle on every
  roster card ✓
- B00 terminal checklist ✓ · B99 comment CTA ✓
- hold:9 warning expected (roster format — all cards hold)
- Review cut: kokoro-romance-voices-review.mp4 (74.4s)

## HUMAN FEEDBACK — 2026-07-13 (gender agreement)

Male voices used feminine adjective agreeing with "voz/voce" noun rather than the speaker.
"voz brasileira" for a male is wrong — a male says "brasileiro."
Fix: restructure all male Romance name lines to use masculine nouns:
  Spanish males:    "voz española"  → "narrador español"
  Portuguese males: "voz brasileira" → "locutor brasileiro"
  Italian male:     "voce italiana"  → "narratore italiano"
Asian language builds (Mandarin 男声, Japanese 男性の声, Hindi पुरुष स्वर) already used
explicit gender nouns — no fix needed there.
Audio regenerated for B02, B03, B05, B06, B08; Remotion re-rendered; recompiled.

→ GATE: human approved.

### Phase D — publish

16:9: https://youtu.be/p2ZZlYHUPXA — "Brutalist — Claude for Video Production" playlist (unlisted)
CC: kokoro-romance-voices.srt uploaded (11 cues, 74.1s) ✓

9:16 Short: https://youtu.be/EwCLrA3QLCc — Shorts playlist (unlisted)

HUMAN ACTIONS (Studio):
  1. Flip both to public when ready.
  2. Verify caption timing on 16:9.
  3. Drag ch6f to correct position in "Brutalist" playlist.
