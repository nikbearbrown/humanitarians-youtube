# BUILD-LOG

- 2026-10-21 — Brief: 60 s, 12 beats, am_onyx, native 16:9 + 9:16 as separate outputs, fixed opening line, review cut only.
- Branding: "Namaskaram, Likhith"; @HumanitariansAI (claude-hai, Plain); HAI outro (HaiOutro / HaiOutro916) with AI-narration disclosure at B00 and B11.
- Audio: 79.9 s at speed 1.0 → trimmed narration twice + Kokoro `--speed 1.1` → 67.6 s audio / 67.8 s cut. Stopped there rather than drop any of the 7 brief points (duration is an output).
- Evidence: evidence/rate_limit_toy.py reproduces every on-screen outcome (B05 5/5, B06 11/4, B07 10 vs 5, B08 22/1/1 vs 8/8/8).
- New components: runtime/remotion/src/ApiGateway.tsx (7 scenes × 16:9 + 916), registered in Root.tsx, scene-index rebuilt.
- 16:9 QC fixes: B03 counter wrapped → stacked; B04/B07 toy-note collided with packet / "now" label → moved to title row; B05 load bar collapsed (flex-shrink) and gate bar crossed its counter; B06 token circles overlapped.
- 9:16 QC fixes: B01 restacked to 4 lines (fontSize 300); B04 route card overflow; B05 backend text vs note; B06 token count vs burst row; B07 "now" label clipped at right edge; B08 legend vs title, caption vs spark.
- 16:9 review: claude-hai-api-gateways-slate.mp4 — 3840×2160, 67.8 s; GATE V 0 BLOCKER / 0 MAJOR.
- 9:16 review: vertical/claude-hai-api-gateways-vertical-slate.mp4 — 2160×3840, 67.8 s, compiled --height 3840; every beat native <Pattern>916; frames read by hand.
- Not run (review cut only): GATE T / `./art final` masters. FACTCHECK.md awaits Likhith's sign-off.
- 2026-10-21 (rev 2) — Likhith asked for exactly 60 s and a plain "Dictated by an AI voice" note (no model name, no "not Likhith").
  Narration trimmed in B01/B02/B03/B05/B06/B07/B08/B09/B10/B11 (all 7 brief points kept), Kokoro `--speed 1.14`, B11 audio trimmed to 3.99 s (outro hold) so the 24 fps timeline is 1440 frames.
  B00 result line → "dictated by an AI voice"; B11 note → "Dictated by an AI voice."
  16:9 review 3840×2160, video + audio 60.000 s, GATE V 0/0. 9:16 review 2160×3840, video + audio 60.000 s.
- 2026-10-21 (masters) — Toolkit fast-forwarded to upstream main a187fab (no GitHub releases exist; Remotion 4.0.535 / React 19 per the release's package.json). Local tracked edits stashed as "pre-update local edits 2026-10-21 (Likhith HAI reels)" and replayed cleanly; stash kept as backup.
  Greetings: 16:9 "Namaskaram, Likhith", 9:16 "Hey, Likhith". Narration now uses plain "API"/"AI" (spaced "A P I" phonemized as "uh-pee-eye"); B00 text = the requested intro line verbatim; audio re-tuned, B11 tail trimmed to 3.70 s → 1440 frames @24 fps.
  GATE T fixes (checker unmodified): filled pills/chips (INK, INK_SOFT) for small labels and service names; portrait labels ≥ 46–48 px; B07 window as a tinted band; B06 tokens ink, bucket outline GHOST; B05 gate bar drawn above dots; animations finish before mid-clip. GATE V fixes: B05 portrait 429 row inside SAFE; portrait B01 fontSize 375 / lineSpacing 2.25; verdict lines fuller.
  FACTCHECK.md signed off by Likhith (his wording) before the masters.
  Masters: renders/H-APIGatewaysAndRateLimiting_LikhithR.mp4 (3840×2160) and renders/V-APIGatewaysAndRateLimiting_LikhithR.mp4 (2160×3840), both 60.000 s video + audio, GATE T PASS, GATE V 0/0, receipts *.verified.json (status ready, sha256 match).
- Disclosure wording standardised across the series: B00 result line "narrated by an AI voice" and B11 outro note "Narrated by an AI voice." (on-screen text only; narration and audio unchanged). B00 and B11 re-rendered in both aspects and the masters re-exported.
