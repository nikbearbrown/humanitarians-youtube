# BUILD-LOG — How a QR Code Works

**2026-11-10**
- Topic chosen by Tanishaa ("How a QR code works", from four options: Wi-Fi, noise-cancelling, QR codes, a Lyrical Literacy update).
- Demo first (`demo/qr_demo.py` → `demo/qr_output.json`): segno 1.6.6 encodes `https://www.youtube.com/@HumanitariansAI` (40 bytes) at L/M/Q/H; a centred white square grows over each code (finder squares untouched) and OpenCV 5.0.0's QRCodeDetector tries to read it. L (29 × 29) reads up to 6 × 6, fails at 7 × 7. H (37 × 37) reads up to 17 × 17 (21.1% of the area), fails at 18 × 18. (segno and opencv-python-headless were pip-installed into the brutalist env.)
- Script v1 drafted.

**2026-11-11**
- Fact-check (FACTCHECK.md, SOURCES.md). One fix: v1's "most of a QR code isn't your message" is true at H (46 data + 88 recovery codewords) but false at L (55 + 15), so B05 now says it "carries more than your message". Denso Wave's own sites wouldn't load; history from Wikipedia (which cites them). Script v2.

**2026-11-13**
- Script v2 approved in chat ("Approved, build it").
- Demo extended: the real module grids for L and H go into qr_output.json for the scenes, and a round "logo" test on the H code (reads up to a 17-module disc, fails at 19); the video uses 13.
- Audio: Kokoro `af_bella`, speed 0.95, 12 beats, 158.0 s, $0.00. "1994" was phonemized as "nineteen hundred ninety-four", so the narration text spells "nineteen ninety-four". faster-whisper cue forms used: "bottom right", "8 bits", "called Reed". Whisper heard "lowest level in the highest" in B06 (Bella's "and" is soft); no on-screen text depends on it.
- Library-first: no existing scene draws a real QR grid, finder/timing patterns, a reading path, codeword blocks, a damage test or a logo. Wrote `runtime/remotion/src/QrScenes.tsx` (QrHook, QrGrid, QrFinders, QrReadPath, QrRecovery, QrDemo, QrLogo + native 916s), registered in Root.tsx under "HowQrCodesWork". Reused ClaudeComposerAsk, RagWhenToUse, GpsTakeaway, HaiTitleOutro and LbTakeaway916 (vertical B09). No BrutalistHesitantWriter (sync rule).
- Preflight fixes: B03 tilted code poked past the left edge → shrinks while tilted. B04 path covered the whole code and looked like noise → only the first three two-column strips, and it fades when the mask appears. B06 panel shadow stretched wider than the code → wrapper sized to the code. B07 said "with a logo: 37 × 37", but the size comes from the level, not the logo → "same link, highest level". Portrait: B04 link overflowed → split onto two lines; B05 header overlapped the grid → shorter header, 14 columns; B06 panels overlapped the footnote → stacked, smaller.
- GATE T first run: B01 min-size FAIL (QR modules 40 px < 41 px floor at 4K) → bigger code, 1-module border. PASS after.
- GATE V first run: edge-bleed on B11 (the outro title "How QR Codes Work." wrapped to two lines) → outro title "How QR Works." (the composer and takeaway cards keep "How QR Codes Work"). 0 BLOCKER / 0 MAJOR after. Advisory only: B09 narration recites its card (same as GPS).
- Landscape master: `how-qr-codes-work.mp4`, 3840×2160, 158.0 s, 12/12 slots.
- My review: frames 0.5 s before and 0.3 s after "still", "dark", "light", "invented", "three", "dotted", "8", "mask", "extra", "lowest", "highest", "low", "high", "just", "bigger", "smudges", "scammer", "always", "corner", "checks" (`_qc/sync1.png`, `_qc/sync2.png`). Each item is absent before and present on its word.
- Vertical (`./art vertical` → `vertical/`): hand edits B09 → LbTakeaway916 and B10 composer normal text (as in how-gps-works). Re-running `./art vertical` undoes them.
- Vertical GATE T first run: 5 min-size FAILs. Two causes: portrait labels below the phone floor (B05 header, B06 labels/footnote, B07 labels) → raised to serif ≥ 86 / sans ≥ 72 / mono ≥ 76 design px; and the QR module squares themselves read as 37–52 px "text runs" (B01, B04, B07), which can't reach 72 px (37 modules × 36 px won't fit 1080 px) → QrHook916, QrReadPath916, QrLogo916 added to type_check.py's HAND_DRAWN_PATTERNS with a comment (§8.1 only; other checks still run). PASS after.
- Vertical finals: GATE T PASS, GATE V 0 BLOCKER / 0 MAJOR (24 frames), 12/12 slots, 158.0 s, 2160×3840. Checked the same 20 cue words in portrait (`vertical/_qc/vsync1.png`, `vsync2.png`): each item is absent before and present on its word.
- SHA-256: landscape `43841138983292b9ed7f54ed0d4d464fabe7f6ad6d1ee3c1ce4e8aa98a60e683`, vertical `fb746a843dc3e8a0cd808e9b642b7035b76909a2d63940319188120c3dd40784`.
- Open: the README needs Tanishaa's "Human and AI work" notes and the Drive link; no FRICTIONAL.md entry yet (needs her own account of what she tried).
- **B08 fix (Tanishaa's feedback, 2026-11-13):** "too much of a gap" before "It's good at" (~1:56–1:58): the screen sat empty for ~3.5 s because the header was cued to "great at" while Bella asks "So when can you trust it?". The header now appears on "So when" (start of the beat), in both versions. Both finals rebuilt: GATE T PASS, GATE V 0/0, 12/12 slots. SHA-256 now: landscape `217ac6f1f4efadc18b9cb869ac4d1d6f933b81716ec63a8e562e143a9b8f3e38`, vertical `0942a2bd5bc3c4714ddaf257c3386d063a4f2b64f3aa5b0d2883679826ee2842`.
