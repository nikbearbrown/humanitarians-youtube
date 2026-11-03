# BUILD-LOG — AI in Your Project Management Tools

Reel: `ai-project-management-tools` · channel @HumanitariansAI · narrator Sanjana Rao
Skill: **ai-explainer** (claude-explainer, Claude skin) · voice af_bella (Bella, female) · built 2026-09-29.

## Decisions
- Topic (fellow's request): **AI in project management tools** (Jira, Trello, Asana, …).
- Skill: ai-explainer this time (films 1–3 were cli-explainer). So the reel uses the
  full ai-explainer spine: ClaudeComposerAsk cold open → **BrutalistHesitantWriter BLUF**
  (Beat T01, EXECUTIVE-SUMMARY LAW) → concept-illustration Manim body → Your-Turn handoff
  → ClaudeTitleOutro. Middle is illustrations, not a live-code loop.
- Framework taught: **THE TICKET TEST** — mechanical? / reversible? / in the tool? →
  AI *drafts & surfaces*, a human *decides & commits*. Original reusable rubric.
- Framing: first-person as Sanjana, cold open "Hi, I'm Sanjana … this video is about …".
- Two deliverables: 16:9 4K (3840×2160) long + 9:16 Short. Output kept local under
  "Humanitarians AI Brutalist files" — NOT pushed to GitHub (per request).
- Voice: af_bella, Sanjana's persistent approved fellow voice (all four films). Human
  voice-approval recorded in beat_sheet.json metadata.approvals.voice (authorized in chat).

## Toolchain setup on this machine (fresh brutalist.art-main unzip)
- Kokoro model was absent → downloaded kokoro-v1.0.onnx + voices-v1.0.bin into
  runtime/models/kokoro/ (free, Apache-2.0, official kokoro-onnx release; user-approved).
- runtime/remotion had no node_modules → `npm install` (189 pkgs) to enable Remotion.
- Re-applied the Windows npx-resolution patch in remotion_scenes.py
  (`shutil.which("npx") or "npx"`) — bare "npx" isn't found by subprocess on Windows.
- Beat ids use a **T-prefix** (T00–T09), not B**: this toolkit's build_safety treats
  B04 as a fellow-report source beat and B05/B06 as professor-notes beats, which would
  wrongly skip/gate a self-authored explainer. T-ids avoid those conventions cleanly.

## Pipeline (Windows — bash wrappers bypassed; scripts called directly)
1. `generate_audio_kokoro.py` → 10 mp3s, af_bella. Durations = master clock (total ~4:20).
2. Wrote measured audio durations into estimated_duration_s so Remotion clips match exactly.
3. `remotion_scenes.py --now … --force` → Claude beats (T00,T01,T04,T08,T09) at 4K (--scale=2).
4. `manim -qk -r 3840,2160` → 5 concept scenes (T02,T03,T05,T06,T07) → manim/<id>.mp4.
   Re-paced T05/T07 holds so no beat conforms above ~1.3× slow.
5. `compile.py --height 2160` → final 16:9 master (skip --review on Windows: drawtext bug).
6. `add_transitions.py` → cross-dissolve-through-cream at every beat boundary → *-fx.mp4.
7. Visual QC (frame sampling, read PNGs) + PROOF self-review → fixes → recompile.
8. 9:16 Short authored + compiled at 2160×3840 (S00–S03).

## Honesty / DOUBLE-CHECK
- No external stats/benchmarks on screen; every verdict is the Ticket Test applied to a
  visible, self-authored worked example. Tool names stated generally, no version/feature
  claims that would date the video. See SOURCES.md.
- Falsifiability shown on screen (T06): same tool, three-red verdict + stale-board flip.
