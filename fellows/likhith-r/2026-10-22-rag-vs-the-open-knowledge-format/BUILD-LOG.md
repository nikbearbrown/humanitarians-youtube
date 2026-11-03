# BUILD-LOG

- 2026-10-22 — Brief: 60 s, 12 beats, 8 points, Kokoro am_onyx, native 16:9 (3840×2160) + 9:16 (2160×3840) as separate outputs, fixed opening line, review cut only.
- Branding: 16:9 "Namaskaram, Likhith" / 9:16 "Hey, Likhith"; @HumanitariansAI (claude-hai, kicker "Irreducibly Human", Plain); HaiOutro; AI narration disclosed on screen at B00 ("narrated by an AI voice") and B11 ("Narrated by an AI voice.").
- Fact-check: OKF confirmed against the Google Cloud blog (June 12, 2026) and SPEC.md v0.2. Brief point 6 corrected: agents as well as people can write OKF pages; the cost is curation + review (see SOURCES.md).
- GATE L: RagPipeline.tsx (one RAG step per scene) and GitHubCodeDiff were leads, not fits → new runtime/remotion/src/RagOkf.tsx (7 scenes × 16:9 + 916), registered in Root.tsx, `./art scene-index` rerun. Google logo copied to runtime/remotion/public/logos/google/ (LOGO LAW, B02).
- Executable evidence: evidence/okf_bundle/ (real 5-file bundle), evidence/rag_vs_okf_toy.py (B03 top-3 0.50/0.41/0.32; B06 walk 4 of 5 files, 0 vectors), evidence/okf_git_demo.sh (B06 git log/diff, reproducible hashes 60e6d0d / f49c815).
- Duration: draft 75.9 s → narration trimmed twice (all 8 points kept) + Kokoro `--speed 1.2` → B11 tail trimmed to 3.82 s → 1440 frames @24 fps. Both cuts probe 60.000 s video + audio.
- 16:9 QC fixes: B01 bled past the bottom at fontSize 200, underfilled (GATE V 51%) at 165 → 180 / lineSpacing 1.75; B04 callout pills wrapped and file panel clipped → narrower file panel, auto height; B06 last diff line overflowed → truncated with "…".
- 9:16 QC fixes (portrait branches): B03 title wrapped under the docs → "RAG: search on demand" (both aspects); B04 struck-chips collided with the tree and the file panel ran into the spark → chips stacked right of the tree, file panel moved up at 28 px, "reads directly" pill landscape-only; B01 4 lines at 300 / 2.25; B09 verdict underfill (55%) → fuller verdict lines (both aspects).
- 16:9 review: claude-hai-rag-vs-okf-slate.mp4 — 3840×2160, 60.000 s; GATE V 0 BLOCKER / 0 MAJOR.
- 9:16 review: vertical/claude-hai-rag-vs-okf-vertical-slate.mp4 — 2160×3840, 60.000 s; every beat native <Pattern>916. The compiled file's 24 GATE V BLOCKERs are all edge-bleed from the burned-in review label; the label-free join of vertical/media/*.mp4 gates 0/0, and a 1 fps sweep of it was read by hand.
- Not run (review cut only): GATE T / `./art final` masters. Remotion is 4.0.535 (4.0.537 available); not upgraded, because that affects every reel. FACTCHECK.md awaits Likhith's sign-off.
- 2026-10-22 (masters) — Built on the latest weekly release: upstream main a187fab (fetched; no newer commits or releases), the same commit as this checkout.
  Intro line set to "Hi, I am Likhith, and this video is about RAG vs. Open Knowledge Format." (narration_text, both sheets). Kokoro reads "vs." as "vee-ess" plus a sentence break, so B00 audio was generated from `spoken_as` ("… RAG versus Open Knowledge Format."). Whisper transcript of both masters: "Hi, I am Likith, and this video is about RAG vs. Open Knowledge format."; "Likith" is Whisper's spelling. B00 4.86 s; B11 tail re-trimmed to 3.90 s → 1440 frames.
  Greetings: 16:9 "Namaskaram, Likhith", 9:16 "Hey, Likhith" (checked on master frames).
  GATE T fixes (checker unmodified, 9:16): B02 serif title 80→96 + auto-height card; B03 chunk bars were read as sub-floor text → solid INK_SOFT bars, taller pile (also fixes GATE V low-contrast; 16:9 bars restyled to match); B05 portrait column heads 64→88.
  GATE T PASS (16:9 and 9:16); GATE V 0/0 (16:9 cut; 9:16 label-free join).
  Masters: renders/H-RAGVsOpenKnowledgeFormat_LikhithR.mp4 (3840×2160) and renders/V-RAGVsOpenKnowledgeFormat_LikhithR.mp4 (2160×3840), both 60.000 s video + audio, receipts *.verified.json (status ready, sha256 match, renamed_from recorded).
  FACTCHECK.md still unsigned — masters exported on Likhith's explicit request.
- FACTCHECK.md signed off by Likhith (16:9 and 9:16 watched, every claim checked against the sources); row 9, the viewer handoff prompt, marked EXEMPT rather than "n/a" so GATE F passes. vertical/FACTCHECK.md synced.
