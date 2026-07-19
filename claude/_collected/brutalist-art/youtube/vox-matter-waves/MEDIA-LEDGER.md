# MEDIA-LEDGER — vox-matter-waves audience variants

**Source reel:** `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/vox-matter-waves/`
**Compiled:** 2026-07-16
**Variants:** medhavy-vox-matter-waves, hai-vox-matter-waves

---

## 1. HUMAN-PROVIDED MEDIA

These are existing assets in `media/` — treated as human-provided (ambiguous provenance defaults to human-provided per the rule). They are AI-generated stills rendered via FLUX / nano-banana, but were supplied as finished plates and must not be visually altered.

| Beat ID | File | Abs Source Path | Bytes | SHA-256 | Dims | Type |
|---|---|---|---|---|---|---|
| B01 | B01.png | `.../vox-matter-waves/media/B01.png` | 40441 | `3f3dc2506b62eb461f1854fc22e1eb7a190fd448d196abd8a049cd88503dab5f` | 1280×720 | PNG still |
| B04 | B04.png | `.../vox-matter-waves/media/B04.png` | 48030 | `9e9663b88e7a8fc9bb03cd2cfeb27f63766818c386a38b21b959a9d1b66bab0c` | 1280×720 | PNG still |
| B07 | B07.png | `.../vox-matter-waves/media/B07.png` | 32279 | `74f942f9325ed42c1beb3b45cd99e5010f168bf79792fccdbce96ed4c41f1912` | 1280×720 | PNG still |
| B10 | B10.png | `.../vox-matter-waves/media/B10.png` | 61110 | `9a455d0b9eb9afa16a6d73a30c623d8ccc7bc820ecbfe1a4ecd5e4f9c4104c83` | 1280×720 | PNG still |
| B12 | B12.png | `.../vox-matter-waves/media/B12.png` | 51456 | `4a43d5c441719705cc697d2f40252d2c66d295b45c06abe1b5ecb74e2fece8f6` | 1280×720 | PNG still |
| B13 | B13.png | `.../vox-matter-waves/media/B13.png` | 56961 | `0475f711297c6cbb03140e4c4096b374d96ec793c77d1daf2405a92b8e40bc5c` | 1280×720 | PNG still |

**Copy destinations (both variants):**
- `medhavy-vox-matter-waves/media/<beat>.png` — byte-for-byte copy, SHA-256 verified ✓
- `hai-vox-matter-waves/media/<beat>.png` — byte-for-byte copy, SHA-256 verified ✓

**Permitted conformance:** PNGs may be Ken Burns animated by compile.py for the beat's measured narration duration. No cropping, recoloring, or visual alteration.

---

## 2. CLAUDE-GENERATED VISUAL BEATS (Manim)

These beats are programmatically generated from code. They can be reused as-is in the variant (the narration register changes but the visual content is preserved). All are in the source `manim/` folder; variants symlink them.

| Beat ID | File | Source Path | Bytes | SHA-256 | Dims | Duration | Scene |
|---|---|---|---|---|---|---|---|
| B02 | B02.mp4 | `.../vox-matter-waves/manim/B02.mp4` | 150179 | `feb850f950b415faef94d7ca13eea62f8252c7fb266b4f73985f13252a256eef` | 1920×1080 | 9.54s | B02_Title |
| B03 | B03.mp4 | `.../vox-matter-waves/manim/B03.mp4` | 210569 | `54db97bb179d2201346a14142b82764f137d35ee84dbe5740596be1058aeac7f` | 1920×1080 | 8.71s | B03_TheReversal |
| B05 | B05.mp4 | `.../vox-matter-waves/manim/B05.mp4` | 225516 | `e6dba0843b7cbd2fa63c914904b51a339f5a9acce15248f7810877f9b41b0ef8` | 1920×1080 | 9.42s | B05_AccidentPeaks |
| B06 | B06.mp4 | `.../vox-matter-waves/manim/B06.mp4` | 269067 | `0ef59319b42363d96cd2903378f387b5185242aa5f33eb7f9e241201221173a2` | 1920×1080 | 9.92s | B06_NumbersAgree |
| B08 | B08.mp4 | `.../vox-matter-waves/manim/B08.mp4` | 543744 | `57f3d352940777022f74882424dbb98ab9a0d1850c273c27d46b0317d6034091` | 1920×1080 | 8.88s | B08_TheBuildup |
| B09 | B09.mp4 | `.../vox-matter-waves/manim/B09.mp4` | 165491 | `35970bff2cd03e5b87253a19c7ff49a58d40d5caa51f9fee772f69eccea4f832` | 1920×1080 | 8.04s | B09_BothPaths |
| B11 | B11.mp4 | `.../vox-matter-waves/manim/B11.mp4` | 224970 | `72074b1336b1440ef477295a53d753b4ff9785703b0a8b743f27664add33aa1d` | 1920×1080 | 8.00s | B11_ScaleBar |
| T01 | T01.mp4 | `.../vox-matter-waves/manim/T01.mp4` | 393198 | `06dbc1e56329f6075f878703ff41f9a0338928ea7f1c65737ce8ee7d4b41dc0a` | 1920×1080 | 8.29s | T01_EqSentences |
| T02 | T02.mp4 | `.../vox-matter-waves/manim/T02.mp4` | 216526 | `dc51a4ce1d46726a07b8a9b489d7455055c6ae9c5fa652226b8e4955361c6632` | 1920×1080 | 10.00s | T02_EqGlossary |
| T03 | T03.mp4 | `.../vox-matter-waves/manim/T03.mp4` | 371202 | `e0a3aafbf4db24b5b3b0a7759e9e7a6b7edaf921079466a0fdf1d239d1643cb1` | 1920×1080 | 10.00s | T03_EqExample |

**Symlink destinations (both variants):**
- `medhavy-vox-matter-waves/manim/<beat>.mp4` → symlink to source
- `hai-vox-matter-waves/manim/<beat>.mp4` → symlink to source

---

## 3. REMOTION-GENERATED BEATS (source — replaced in variants)

These are Remotion renders from the source reel. They carry NikBearBrown / Liam branding and must be regenerated in the variant with the correct brand props and new narration.

| Beat ID | File | Source Path | Bytes | SHA-256 | Duration | Pattern | Action in Variant |
|---|---|---|---|---|---|---|---|
| B00 | B00.mp4 | `.../vox-matter-waves/media/B00.mp4` | 878231 | `46faeb19d09c7eaa5b37f42e589c8d9c9f9cc5e1b804c091a71f7f47d502eba7` | 15.06s | ClaudeComposerAsk | REPLACED — new variant open rendered |
| B14 | B14.mp4 | `.../vox-matter-waves/media/B14.mp4` | 851430 | `bf26c1b95d7e729090bed4cae52ad2ca8a0634cdffbc5d5dbae75737d0e3b754` | 15.06s | ClaudeComposerAsk | REPLACED — Medhavy/HAI handoff beat or CLI exercise |
| B15 | B15.mp4 | `.../vox-matter-waves/media/B15.mp4` | 340291 | `c710be4e1acf57a716754e112e35666092912c97d47baff4651ed24bee353b15` | 6.06s | ClaudeTitleOutro | REPLACED — Medhavy/HAI outro |

---

## 4. HUMAN-PROVIDED MEDIA NARRATION CONFORMANCE TABLE

Source narration durations (from source beat_sheet.json `actual_duration_s`) vs new Kokoro MP3 durations to be measured after generation. Trim/retime factor computed after audio generation.

| Beat ID | Source Duration | MP3 Duration (to measure) | Factor | Action |
|---|---|---|---|---|
| B01 | 9.87s | TBD | TBD | Ken Burns hold or retime |
| B04 | 9.93s | TBD | TBD | Ken Burns hold or retime |
| B07 | 9.38s | TBD | TBD | Ken Burns hold or retime |
| B10 | 8.36s | TBD | TBD | Ken Burns hold or retime |
| B12 | 11.36s | TBD | TBD | Ken Burns hold or retime |
| B13 | 9.61s | TBD | TBD | Ken Burns hold or retime |

compile.py handles conformance automatically: stills are held for the measured MP3 duration. No manual intervention needed.

---

## 5. SHA-256 VERIFICATION STATUS

All human-provided media copied to both variant directories:

| File | Source SHA-256 | Medhavy copy verified | HAI copy verified |
|---|---|---|---|
| B01.png | `3f3dc2506b62eb461f1854fc22e1eb7a190fd448d196abd8a049cd88503dab5f` | ✓ | ✓ |
| B04.png | `9e9663b88e7a8fc9bb03cd2cfeb27f63766818c386a38b21b959a9d1b66bab0c` | ✓ | ✓ |
| B07.png | `74f942f9325ed42c1beb3b45cd99e5010f168bf79792fccdbce96ed4c41f1912` | ✓ | ✓ |
| B10.png | `9a455d0b9eb9afa16a6d73a30c623d8ccc7bc820ecbfe1a4ecd5e4f9c4104c83` | ✓ | ✓ |
| B12.png | `4a43d5c441719705cc697d2f40252d2c66d295b45c06abe1b5ecb74e2fece8f6` | ✓ | ✓ |
| B13.png | `0475f711297c6cbb03140e4c4096b374d96ec793c77d1daf2405a92b8e40bc5c` | ✓ | ✓ |
