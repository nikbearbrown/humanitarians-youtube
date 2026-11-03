# BUILD-LOG — hai-first-week

## 2026-09-27 — first build
- Channel claude-hai (kicker "Irreducibly Human", chip @HumanitariansAI); voice Kokoro af_bella; greeting "Hola, Shubh".
- Library-first: reused SocialOneToMany, SocialLoop, SocialHumanSplit (props only; added optional
  `cols` and `signalsLabel`, defaults unchanged) and the stock Claude scenes. Genuine miss: a
  partnership diagram → new `PartnerBridge` / `PartnerBridge916` (runtime/remotion/src/scenes/PartnerBridge.tsx).
- Outro: HandleTitleOutro with @HumanitariansAI (ClaudeTitleOutro is locked to @NikBearBrown).
- Claims limited to the author's brief (FACTCHECK.md). Reference link omitted at the author's request.
- Review cuts use ART_NO_DRAWTEXT=1; Windows needs PYTHONUTF8=1.

Toolkit changes this build (defaults unchanged for other reels)
- SocialOneToMany `cols`, SocialLoop `signalsLabel`, HandleTitleOutro `scale` + `\n` line breaks.
- ClaudeVerdictArtifact (16:9) optional `largeText`; ClaudeVerdictArtifact916 optional `textScale`
  (chip moves above the card when set, clear of the Shorts UI band).
- Active loop stage highlighted with a warm-grey border (an ink outline read as a text run in GATE T).
- BrutalistHesitantWriter matches single-word triggers only; B01 uses technology→people, subject→door.

Portrait-only props (vertical/beat_sheet.json): shorter recap lines on B07, reflowed B01 text, largeText off
on composer pages, outro scale 0.9. Same meaning as 16:9, fewer words per frame.

Gate results (final exports)
- 16:9 renders/hai-first-week.mp4 — 3840×2160, 114.4 s; GATE L/F/V/T pass; hai-first-week.verified.json.
- 9:16 renders/hai-first-week-vertical.mp4 — 2160×3840, 114.4 s; GATE L/F/V/T pass; hai-first-week-vertical.verified.json.
