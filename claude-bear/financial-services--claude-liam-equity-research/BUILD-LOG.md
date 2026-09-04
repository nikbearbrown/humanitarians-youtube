# BUILD-LOG — financial-services--claude-liam-equity-research

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown skill-teardown
sheet (`anthropics/financial-services/youtube/claude-liam-equity-research/beat_sheet.json`,
7 beats, the `equity-research` Anthropic Skill — a partner-built LSEG
financial-services skill — brand `claude-liam`, audience `Claude`,
`@NikBearBrown`). SUBJECT.json's `source_sheet`/`source_dir` pointed at the
correct local path this time (unlike the plugin-structure redo, no
nonexistent `/Users/bear/...` path to chase); read it plus its
PEDAGOGY.md/LENS-AUDIT.md/TYPECHECK.md in full. The metadata's
`source_skill` field, however, points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/lseg/skills/equity-research/SKILL.md`
— Bear's machine, not reachable here — and no equivalent local copy of the
full SKILL.md was found anywhere under this repo. The source reel's own
narration is consequently generic/templated (this `claude-liam-<skill>`
family spans ~50 financial-services skill teardowns from the same
template): a one-paragraph stated purpose, a one-file anatomy, a linear
read-then-execute pipeline, and a repeatable-but-bounded reliability claim
— no deeper walkthrough of the skill's actual internal steps was available
to carry forward. Built strictly from what the source narration itself
states; did not invent additional domain mechanism (no fabricated
tickers, formulas, or specific figures).

Kept beat count (7) and every fact the source narration actually asserts:
`equity-research` is a Claude Skill — a folder Claude reads before it
works, one file (`SKILL.md`), plain language, no hidden logic; its stated
purpose is to combine analyst consensus estimates, company fundamentals,
historical prices, and macroeconomic context into a research snapshot, for
researching stocks / comparing estimates to actuals / analyzing financials
/ assessing valuations / building investment cases; execution is linear —
read the file, execute each step in order, return the result; same input
produces the same output every run; the skill only does what the file
specifies. Remapped the source's B03 "gets right / bites" Teardown framing
into B03's both-directions beat (a question the file's steps don't cover
goes unanswered — not refusal, just nothing written for it; a clean
snapshot doesn't prove the numbers were checked or judged — same facts, no
verdict), and its BVDT verdict recap into a single BCRY carry-out sentence
per CARRY-OUT LAW. Anchor B02→B03: ask Claude to research one company (the
file opens, runs its four steps, assembles one snapshot) → ask the same
skill a question its steps don't cover, like whether to buy the stock (no
step lights up, nothing written for it).

B00 WRITER LAW: naive guess "a trained analyst inside it" → corrected to "a
written file" (the newcomer's default assumption that Claude's equity
research draws on specialized, separately trained financial judgment,
rather than a plain-language instruction file it reads before acting);
34-word narration + `lead_silence_s: 0.8`, measured 10.65s raw / 10.7s
compiled (clears the TIMING LAW ≥9s window); verified on a frame pull at
9.5s that the writer's text reads "is that a written" mid-typing "file" —
correction confirmed on screen well before the beat ends.

Built entirely fresh this invocation (only SUBJECT.json present on
pickup):

1. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (7 beats),
   scenes.py (3 Manim GRAPHIC scenes: `EQRB01Scene`/`EQRB02Scene`/`EQRB03Scene`,
   humanitarians palette #F3EBDD/#2F2A26/#E4572E/#1F4E5F), render_scenes.py.
2. Rendered B01–B03 via `manim -qh` (foreground) — clean on first pass;
   spot-checked mid/late frames of each before locking narration.
3. `generate_audio_kokoro.py` — 7/7 beats, `am_onyx`, measured durations
   written back (B00 10.65s, B01 18.58s, B02 18.22s, B03 17.37s, BCRY
   7.79s, BHTF 21.08s, BOUT 3.29s). Cost $0.00.
4. `remotion_scenes.py` (foreground; the harness auto-backgrounded the
   first invocation past its 120s output-timeout — waited on it via
   `TaskOutput(block=true)` rather than treating the backgrounding as
   permission to move on, per the COMPLETION LAW against orphaned
   renders) — B00/BCRY/BHTF/BOUT all `ok`, B00 extended to 10.7s.
5. `compile.py` — 7/7 slots filled (B00/BCRY/BHTF/BOUT VIDEO, B01/B02/B03
   MANIM), content-check/frame-check/lane-check PASS, THE 4K LAW forced
   the master to 3840×2160 natively (no `--review`), GATE AUDIO PASS
   mean_volume -24.0 dB.
6. GATE T (`type_check.py`) — **first pass FAIL**: B02's four step-card
   labels (font_size 16) fell under the §8.1 min-size floor (15px < 20px
   at 1080p). Fixed by enlarging to font_size 21 and widening the cards
   slightly. Second pass introduced a **new FAIL**: §8.4 kerning-sanity
   flagged a 169px "inter-glyph gap" (9.2× expected) in B02 — not a real
   Pango-fallback bug (font was named throughout) but a false positive:
   with all four step cards row-aligned, their four short text labels
   collapsed into single unbroken ink runs per word, and the checker's
   peak-ink-row scan read the wide whitespace *between* the four separate
   cards as huge inter-letter kerning gaps within one text run. Root-cause
   fixed in scenes.py — not the validator — by staggering cards at odd
   indices down 0.22 units so no single horizontal band spans all four
   labels' baselines at once; re-rendered B02, recompiled. **GATE T:
   PASS**, third pass, 0 FAILs.
7. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime newer than beat_sheet.json mtime
   at every recompile; h264 3840×2160 + aac streams present, duration
   97.96s; `ffmpeg -af volumedetect` mean_volume **-24.0 dB**, max -2.8 dB
   — independently confirms GATE AUDIO.
8. Gate V: pulled 13 frames spaced across the full 98s runtime (including
   mid-animation transition frames, not just settled end-states) and read
   all of them directly. Found one real defect: at BHTF (~72–94s), the
   `ClaudeComposerAsk` eyebrow prop `"EQUITY-RESEARCH · ANTHROPIC SKILL ·
   YOUR TURN"` wrapped to two lines and its second line visually
   overlapped the "Your Turn" segment heading beneath it — carried over
   verbatim from the source sheet's BHTF topic string, which never had to
   coexist with this component's two-line "Your Turn" treatment before.
   Fixed by shortening the topic prop to `"EQUITY-RESEARCH · ANTHROPIC
   SKILL"` (dropping the redundant "· YOUR TURN" suffix, since `segment`
   already reads "Your Turn") — matches the shorter form already used at
   B00 and in the plugin-structure precedent. Re-rendered BHTF only,
   recompiled, re-ran GATE T (still PASS), re-pulled the frame — overlap
   gone, eyebrow reads cleanly on one line. No other defects found across
   B00/B01/B02/B03/BCRY/BOUT — legible, safe inset respected, no other
   text overlap, humanitarians palette consistent, exactly one terracotta
   accent moment per beat.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, third pass — two content fixes, validator untouched)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: duration 97.96s; mp4 mtime newer than beat_sheet.json mtime at final compile

**Non-blocking note (compile.py):** motion histogram remotion:4 graphic:3 —
same structural split as every other 7-beat hai-simple reel in this family
(B00/BCRY/BHTF/BOUT REMOTION by skill contract, 3 GRAPHIC body beats).
Three Manim clips were time-stretched by compile.py to fill their measured
audio durations (B01 9.0s→18.6s at 2.05x, B02 10.7s→18.2s at 1.70x, B03
11.0s→17.4s at 1.58x); spot-checked in the Gate V frame pull, no visible
artifacting (static-camera Manim compositions).

Metadata file written:
`financial-services--claude-liam-equity-research.md` (channel
@HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's family
`financial-services` matches no prefix in the map, so per the resolution
order ("match SUBJECT.json's family, or the hai-simple prefix, against the
map's prefixes in order") fell through to the `hai-simple` skill-name key,
which maps to `Claude Basics` — plus the direct code link per the DELIVERY
CONTRACT format.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
