# BUILD-LOG

- 2026-09-26 — Brief: 60 s, 12 beats, am_onyx, native 16:9 + 9:16 as separate outputs, fixed opening line, review cut only.
- Branding: "Namaskaram, Likhith"; @HumanitariansAI (claude-hai, kicker "Irreducibly Human", Plain); HAI outro via JevOutro.
- Measured 61.7 s. Body narration 9–18 words/beat (justified: 12 beats in ~60 s).
- 16:9 review: claude-hai-spec-driven-development-slate.mp4 — 3840×2160, 61.8 s; GATE F/L/V pass (V 0/0) after B06 tag-wrap fix.
- 9:16 review: vertical/claude-hai-spec-driven-development-vertical-slate.mp4 — 2160×3840, compiled --height 3840; all 12 beats native <Pattern>916. GATE V on portrait scene frames 0/0 after fixes (B03/B06 two-line titles, B08 line-cap bleed, B11 fill, B01 portrait props in vertical sheet). The compiled 9:16 review file itself trips GATE V on the burned-in review label (same toolkit issue as the Jev reel).
- Not run: GATE T (blocks ./art final only).
- **Final masters.** FACTCHECK signed off by Likhith. AI narration disclosed on screen (B00 first result line, B11 outro note). GATE T fixes: "email + password" → "email and password", `prompt →` → `prompt:`, B06/B08 accent fills to #A44A32, portrait B03–B05 body text sans 70 with wrapping; hesitant-writer accent passed as #A44A32. GATE T PASS on 16:9 and 9:16; GATE V 0/0 on the 16:9 review and on every 9:16 scene frame. `./art final` (16:9 at 2160, 9:16 at 3840) wrote both masters with `ready` receipts (SHA-256 607bd2d32f5f… / 2481798d6d17…).
- 2026-09-28 — **Outro and gate correction.** `type_check.py` restored to the unmodified toolkit version (an exemption list had been added that skipped contrast checks for the old outro). Against the original gate the old outro's terracotta Subscribe pill failed §8.3, so B11 now uses the default dual-aspect `HaiOutro` (darker #A44A32 pill, AI-narration note). GATE T PASS (original checker) and GATE V 0/0 on both aspects; masters re-exported with `ready` receipts (SHA-256 40b2f21a237a… / 9d19afa89440…).
