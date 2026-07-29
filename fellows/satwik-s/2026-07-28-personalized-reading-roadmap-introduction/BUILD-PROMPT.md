# BUILD-PROMPT — Personalized, Project-Driven Reading Roadmaps for CaNCURE Trainees

AI-explainer reel · channel `claude-hai` (Humanitarians AI) · Kokoro **Bella** (`af_bella`) · free, local, **zero API keys**.

**Do not run this until `PEDAGOGY.md` reads `VERDICT: PASS` with a human signature and `NARRATION-GATE-P.md` is approved.** GATE P binds — narration is signed off on the animated slate *before* any audio is generated. (The build has been paused here by request so the paperwork can be reviewed first.)

Paste into Claude Code, run from the toolkit root `brutalist.art/` (free pipeline; `--dangerously-skip-permissions` is appropriate here — git-tracked, regenerable outputs, GATE P still gates spend):

```
Build the claude-hai ai-explainer reel "Personalized, Project-Driven Reading Roadmaps for CaNCURE Trainees" — free Kokoro pipeline, Bella voice. Reel lives OUTSIDE this toolkit; treat REEL as:
REEL=../weekly-videos/week-01-paper-introduction/output/personalized-reading-roadmap-introduction

Ground truth, read first (build ONLY from these — no external facts):
1. $REEL/beat_sheet.json — the master. Metadata: brand=claude-hai, engine=kokoro, voice_kokoro=af_bella, palette=claude (UI beats), body_palette=humanitarians (B01–B06), channel_title=@HumanitariansAI, greeting "Hello, Satwik".
2. $REEL/PEDAGOGY.md + $REEL/NARRATION-GATE-P.md — the gates. CONFIRM both read PASS/approved before touching audio. If PENDING, STOP and report.
3. $REEL/SOURCES.md — the single source (sources/manuscript.pdf) and the CLAIM GUARDRAIL LEDGER. These guardrails are hard constraints on every on-screen word and mark.
4. $REEL/VISUAL-PLAN.md — the two-skin palette contract, the six net-new components, and each beat's show design.
5. skills/make/ai-explainer/SKILL.md + CLAUDE-BRAND.md + skills/make/hai/SKILL.md + brands/hai.md — the laws (ILLUSTRATE, ASK→RESULT, SHOW-DON'T-TELL, HANDOFF, OUTRO, LOGO, REBUILD, DOUBLE-CHECK, VISUAL QC).

Guardrails (from SOURCES.md — never violate, in voice OR on screen):
- NO improved-learning-outcomes claim. NO "all prerequisites approved" (B04 must show model-proposed, UNDER-REVIEW edges). NO adaptive/real-time-progress as shipped (B06 future panel = greyed, "DEFERRED"). NO Hattie effect sizes. NO textbook title/authors. NO invented numbers — only "38 chapters" and "4 stages" are spoken.

Steps:
1. Build the six body components in $REEL/remotion-src/ (humanitarians tokens; pure fn of useP(); one accent; no CSS transitions/timers/random): RoadmapProblemFanout (B01), RetrieveVsReorder (B02 — rhetorical, add an anim.json entry + present the pattern table before building), RoadmapPipeline (B03), DependencyGraphReview (B04), WeeklyRoadmap (B05), LimitsAndFuture (B06). UI beats use the shipping claude scenes: ClaudeComposerAsk (B00, B08), ClaudeVerdictArtifact (B07), ClaudeTitleOutro (B09). Register all in the reel composition. Anything not yet built renders as a labeled slate on the first compile — that is expected (fill-in-first).
2. Audio = the clock: python3 runtime/scripts/generate_audio_kokoro.py $REEL   (Kokoro af_bella "Bella"). ffprobe each mp3 → write actual_duration_s back into beat_sheet.json; conform frames = ceil((mp3 + tail) * 30). Captions via the faster-whisper pipeline.
3. Compile the review cut: ./art run $REEL   → then ./art todo $REEL to see which slots still need real components. Fill remaining slots in remotion-src/, rerun; only changed slots recompile.
4. Render/assemble ONLY via python3 runtime/scripts/compile.py $REEL --height 1080  (foreground; never hand-roll npx remotion render). Master stays as $REEL/media/…; final clean cut via ./art final $REEL.
5. VISUAL QC LAW (mandatory — the mp4 probe is NOT QC): sample frames (ffmpeg -i cut.mp4 -vf fps=2 _qc/frames/%05d.png, plus each beat ~15/50/85%), actually READ the PNGs, audit the 9-point rubric. Two-skin check: B00/B07/B08/B09 read as the claude cream/terracotta UI; B01–B06 read as humanitarians editorial; exactly ONE accent per beat; HAI corner bug lower-right every beat, full-size on the outro; @HumanitariansAI centered-bottom on B00 only. Verify B04 shows under-review edges and B06 shows the DEFERRED panel. Log defects+fixes to _qc/REPORT.md; fix root causes in scene source; re-render until zero BLOCKER/MAJOR.
6. Report the beat-by-beat status table, the measured runtime (target 2–3 min; if >3:00 trim B06 then B07 and REGENERATE audio — never hand-edit timing), and any slates still standing. Then STOP. NEVER publish — the master stays in the reel folder.
```

## Notes

- **Money:** none. Kokoro (Bella) ships in the toolkit; no key, no `.env`. If any step asks for a credential, that's a bug — stop.
- **Never modify** `sources/manuscript.pdf` or files outside `$REEL`.
- **Two-skin reminder:** the Claude UI is a *fidelity* brand — do **not** retint the UI beats. The humanitarians palette applies only to the body illustration beats (B01–B06), per the ai-explainer ASK→RESULT LAW.
- **Voice discrepancy:** `CLAUDE-BRAND.md`'s channel table lists `am_onyx` for `claude-hai`; the authoritative spec (HOW-TO.md / CLAUDE.md / brands/hai.md) and the user request both say `af_bella`. Build with **Bella (`af_bella`)**.
- **Duration is an output**, confirmed only after audio. Do not pad or trim to hit a number in the beat sheet.
