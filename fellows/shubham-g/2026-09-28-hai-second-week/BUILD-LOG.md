# BUILD-LOG — hai-second-week

## 2026-09-28 — first build
- Channel claude-hai (kicker "Irreducibly Human", chip @HumanitariansAI); voice Kokoro af_bella; greeting "Hej, Shubh".
- Library-first: every beat reuses an existing scene (SocialOneToMany, SocialLoop, SocialHumanSplit,
  stock Claude scenes, HandleTitleOutro) through props only — no new components.
- Midjourney is described, never called or imitated (paid tool; the build stays free and local).
- Claims limited to the author's brief + the approved pipeline framing (FACTCHECK.md).
- Review cuts use ART_NO_DRAWTEXT=1; Windows needs PYTHONUTF8=1.

Portrait-only props (vertical/beat_sheet.json): shorter recap lines on B06, reflowed B01 text, shorter chips on
B04 ("simple words", "clear images") and "No real kids' faces" on B05 so portrait type clears GATE T; composer
largeText off; outro scale 0.9. Same meaning as 16:9.

Gate results (final exports)
- 16:9 renders/hai-second-week.mp4 — 3840×2160, 116.0 s; GATE L/F/V/T pass; SHA-256 b2dfd960aa10ed626155bd18863604a80f53e1be0f3623095bfc83dd33f7e05e
- 9:16 renders/hai-second-week-vertical.mp4 — 2160×3840, 116.0 s; GATE L/F/V/T pass; SHA-256 1bfb6751312204c29032841a01ca68ecf052cc80e0e4ff7e8f1667e866e1333f
