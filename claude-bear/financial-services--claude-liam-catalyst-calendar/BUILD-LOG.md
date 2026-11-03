# BUILD-LOG — financial-services--claude-liam-catalyst-calendar

## 2026-09-01 — hai-simple redo, review cut + delivery

**Mode:** `redo`. Source: `/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-catalyst-calendar/beat_sheet.json`
— a Teardown-register skill showcase of the Anthropic-style `catalyst-calendar` Skill
(builds and maintains a calendar of upcoming catalysts across a coverage universe:
earnings dates, conferences, product launches, regulatory decisions, and macro events;
helps prioritize attention and position ahead of events). 7 beats in the source; 7
beats in this redo (B00, B01, B02, B03, BCRY [was BVDT], BHTF, BOUT).

**State at pickup:** the reel dir held only `SUBJECT.json`. A prior filmloop worker had
marked this reel `"status": "building"` in the loop's `queue.json` but left no output
(0-byte `.filmloop/financial-services--claude-liam-catalyst-calendar.w44071.out`, no
other files) — treated as an abandoned attempt and built fresh, per COMPLETION LAW.

**What changed from source (all facts kept, register/skin only):**
- B00: `ClaudeComposerAsk` → `BrutalistHesitantWriter` (WRITER LAW). Wrong word "app"
  corrected to "skill" on screen, tied to the reel's actual mechanism (a Skill isn't an
  autonomous app that watches the market on its own — it's a folder of instructions
  Claude follows). Narration 34 words + `lead_silence_s: 0.8`; rendered `B00.mp4` =
  11.33s (≥ the 8s / 9s-window floor).
- B03 ("design tell" in the source, with Teardown verdict language — "what it gets
  right" / "what it bites"): rewritten as a plain mechanism + scope statement, no
  trade-off verdict. Facts (the skill's stated job, verbatim from the source narration)
  unchanged.
- BVDT (verdict artifact) → BCRY (carry-out, `WantQuote`): "A Skill doesn't make Claude
  smarter — it makes Claude follow your steps, in order, every time." Written first,
  ties back to B00's wrong guess. (Same carry-out sentence as the
  `financial-services--claude-liam-buyer-list` sibling — the underlying argument this
  skill-teardown format makes is generic to how a Skill executes, illustrated via the
  specific skill; both reels land the identical distinction.)
- BHTF: kept `ClaudeComposerAsk` (composer only appears at the Your Turn handoff, per
  WRITER LAW) but replaced the source's proprietary-skill prompt with a generically
  runnable one (explain a Claude Skill + walk through a 3-step coffee SKILL.md) since
  viewers don't have the catalyst-calendar SKILL.md file.
- BOUT: `ClaudeTitleOutro` (locked to @NikBearBrown) → `OutroSeries` with the
  Humanitarians AI skin, same title-restate narration as source.
- No AI-VIDEO, pantry, or human-drop beats existed in the source (it was already
  all-REMOTION), so NO-GENAI/NO-PANTRY LAW required no beat substitution beyond the
  B00 WRITER LAW swap.

**GATE T:** PASS on first run, 0 FAILs, 7/7 beats checked (B03's on-screen body prop
was written short — "Build and maintain a catalyst calendar." — from the start, so no
rework was needed here, unlike the buyer-list sibling which needed a post-hoc trim).

**Build:**
- Audio: `generate_audio_kokoro.py`, 7/7 beats, am_onyx, $0.00.
- Render: `remotion_scenes.py`, 7/7 REMOTION beats, foreground, waited on exit code
  (ran long enough to trip the shell tool's default background-move at 120s; blocked on
  `TaskOutput` for the same task id until it reported `exit_code=0` rather than treating
  the move-to-background as completion — no render step was left unsupervised).
- Compile: `compile.py` → forced 4K master directly (720p→2160p, no slates) —
  `financial-services--claude-liam-catalyst-calendar.mp4`, 76.6s, 3840×2160.
- GATE AUDIO: PASS, mean_volume −24.0 dB (compile.py) / independently reconfirmed via
  `ffmpeg -af volumedetect`: mean −24.0 dB, max −2.8 dB — both far above the −40 dB
  floor.
- Independently reconfirmed via ffprobe: master carries both video (h264, 3840×2160)
  and audio (aac) streams, duration 76.560s, mtime newer than `beat_sheet.json`.
- Gate V: pulled 19 frames at 4s stride across the full runtime plus a direct late-frame
  pull from `media/B00.mp4` (t=10.5s) and read all of them directly. B00's correction
  ("app" → "skill") is visible and settled ("How does the catalyst-calendar skill /
  track eve|"). B01, B02, B03, BHTF, BOUT are legible, correctly composed, no overlap,
  no overflow. Known, previously-logged palette limitation persists (see below) — not a
  new defect.

**Known template limitation (logged, not a blocker — same as the buyer-list sibling):**
`OutroSeries`/`OutroCTA` import `tokens/vox` (white/near-black/crimson), not
`tokens/humanitarians.ts` — no registered scene imports the true humanitarians hex set.
`SkillTeardownAnatomy`/`Pipeline`/`Mechanism` and `WantQuote` likewise hardcode the
Claude palette with no override props. `BrutalistHesitantWriter` (B00) DOES expose
`ink`/`accent`/`bg` and was built with the true humanitarians hex values (`#2F2A26` /
`#E4572E` / `#F3EBDD`). Componentry gap in the shared scene library, not a defect in
this reel's sheet; editing shared Remotion scene source was out of scope for a
single-reel build.

## Result

`financial-services--claude-liam-catalyst-calendar.mp4` — 76.6s, 3840×2160, audible
audio (mean −24.0 dB), newer than `beat_sheet.json`. Review cut DONE.
`beat_sheet.json` not touched after this compile, per COMPLETION LAW.

## Phase 4 (delivery)

Master was already born native 3840×2160 (compile.py's 4K LAW), so
`financial-services--claude-liam-catalyst-calendar-4k.mp4` was produced as a direct
copy of the master (verified 3840×2160 via ffprobe before copying) — no separate
upscale render needed. Ran:

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

- Drive outbox: `DELIVERY/financial-services--claude-liam-catalyst-calendar/` —
  `financial-services--claude-liam-catalyst-calendar-4k.mp4` +
  `financial-services--claude-liam-catalyst-calendar-description.md`.
- Repo: `humanitarians-youtube/claude-bear/financial-services--claude-liam-catalyst-calendar/`
  — README.md (= description), beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md.
  No mp3/mp4 in the repo copy.

**Status: DONE.** Review cut passes every gate; 4K delivered to both targets.
