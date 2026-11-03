# BUILD-LOG — knowledge-work-plugins--claude-liam-content-strategy

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-content-strategy/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`content-strategy` Anthropic skill — the `small-business` plugin's
sales-to-content-plan tool). Only `SUBJECT.json` existed on pickup.

**Source-material defect found and worked around:** the source sheet's own
narration had unfilled `>` template gaps in B00, B03, BVDT, and BHTF — a
batch-build defect from the original 2026-07-25 run (visible in the source
`beat_sheet.json`: `"Claude's job: >. What it gets right..."`,
`"I want to >. Read the content-strategy skill..."`). Its
`source_skill` path (`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/...`)
also does not exist anywhere in this local tree — this book's local copy
only contains the rendered `youtube/` output, not the plugin source. Per
the REDO LAW ("keep its question, its facts, its body argument"), the
missing facts could not simply be invented. Resolved by fetching the real,
public source directly: `github.com/anthropics/knowledge-work-plugins`,
`small-business/skills/content-strategy/SKILL.md` (confirmed via
`WebSearch` to be a genuine public Anthropic repo, then read via
`curl`/raw.githubusercontent.com this invocation). All facts in this reel
are sourced from that real file, not from the source sheet's broken
template text.

**Register re-registered Teardown -> Plain**: the source graded the skill
("what it gets right… what it bites") and framed a "Verdict" card; this
redo states the six-section brief boundary as fact (no grading language)
and folds the verdict into a `WantQuote` carry-out beat. B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "write"->"rank", "posts"->"sellers" — the newcomer assumption
that this skill writes your social posts, corrected to: it ranks what your
sales data says is working). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. BHTF's prompt was rewritten
clean — the source's handoff string was a broken template referencing a
skill file and connected accounting accounts (QuickBooks/PayPal) the
general viewer won't have; this version asks the viewer to paste a short
made-up sales list and ask Claude to rank it and stop there, which doubles
as a live test of the reel's own claim.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so the law required no substitution beyond the WRITER
LAW and channel-skin row it already mandates.

## Built end to end this invocation

1. Read `SKILL.md` (hai-simple), `SKILL.md` (simple, parent), the source
   `beat_sheet.json` + `PEDAGOGY.md`, and the structure-template sheet
   (`claude-liam-simple-delve`). Discovered the source's `>` template gaps
   and missing local `source_skill` path; re-sourced real facts from the
   public `anthropics/knowledge-work-plugins` GitHub repo (WebSearch to
   confirm it's genuine, then fetched the raw SKILL.md via curl).
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Plain
   register: carry-out written first, then the reel reverse-engineered to
   land it). Wrong guess: "content strategy" means Claude hands you
   finished posts or a calendar. Correction: it ranks real sales data into
   push/hold/reposition and stops at a six-section brief, pending owner
   approval.
3. Wrote `SCRIPT.md` (7-beat table, redo audit, register audit, deliberately
   -not-claimed section) and `beat_sheet.json`, matching the source's exact
   7-beat count (B00, B01, B02, B03, BVDT->BCRY, BHTF, BOUT). GATE L
   checked all four reused Remotion components before slating —
   `BrutalistHesitantWriter`, `ClaudeComposerAsk`, `WantQuote`, `OutroCTA`
   all RENDERABLE with matching props (`./art scenes --check`).
4. Generated audio: `generate_audio_kokoro.py`, free, `am_onyx`, cost
   $0.00. Measured durations: B00 12.33s, B01 16.51s, B02 12.86s, B03
   16.51s, BCRY 11.43s, BHTF 15.45s, BOUT 4.31s.
5. Wrote `scenes.py` / `render_scenes.py` for the three GRAPHIC beats
   (B01 anatomy — folder + SKILL.md/reference contents; B02 pipeline —
   pull data -> rank + weigh season -> return brief; B03 constraint — six
   brief sections + "no calendar. no assets." boundary), Manim,
   humanitarians palette, durations matched to measured audio. Rendered
   all three in the foreground — clean on first pass.
6. Rendered the four REMOTION beats via `remotion_scenes.py` (foreground).
   The render exceeded the tool's 120s inline timeout and the harness
   moved it to a tracked background task; per the COMPLETION LAW (never end
   a turn on an unsupervised render), blocked on it directly via
   `TaskOutput(block=true)` until the task-completion notification
   confirmed exit code 0 — 4/4 beats rendered clean (B00, BCRY, BHTF,
   BOUT). Verified `media/B00.mp4` directly: `ffprobe` confirms 12.33s with
   audio+video tracks, clearing the >=8s TIMING LAW floor; a frame pull at
   t=10s shows both corrections complete and legible — "Can Claude rank my
   sellers this week?".
7. First `compile.py` pass -> 7/7 real (no slate), native 4K master, 90.4s,
   mean_volume -24.0 dB.
8. GATE T (`type_check.py`): PASS on first run, 0 FAILs.
9. Gate V: pulled a frame from all 7 beats and read each directly. Found
   **one real defect**: B01's folder box (width 2.9) was too narrow for
   the `reference/gotchas.md` / `reference/examples/` rows (font_size 20),
   so those two rows overflowed the box on both sides and the leading "r"
   of "reference" was visually clipped by the folder's left stroke line.
   **Fix:** widened `folder_body`/`folder_top` (2.9 -> 3.9 units) and
   trimmed the reference-row font size (20 -> 18) in `scenes.py`,
   re-rendered B01 only, recompiled. Re-ran `type_check.py`: **GATE T
   PASS**, §8.1 min-size still clears the floor at font_size 18
   (min text-run height 41px >= floor 20px per TYPECHECK.md). Re-pulled
   frames across all 7 beats on the recompiled master: B01 now clean, no
   clipping; all others unchanged and clean. (BOUT/`OutroCTA` renders on
   flat white, not the humanitarians cream ground — a known shared-
   component note already logged unfixed on multiple siblings in this
   factory, e.g. `knowledge-work-plugins--claude-liam-content-creation`;
   not a new defect, not blocking.)
10. Final master verified directly: 3840x2160 (born natively via
    compile.py's 4K LAW), 90.4s, mean_volume -24.0 dB (max -2.9 dB), mtime
    newer than `beat_sheet.json` — the COMPLETION LAW conditions are all
    met.

## Gates

- **TIMING LAW (B00):** narration 35 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **12.33s**, clears the >=8s floor. Both
  corrections ("write"->"rank", "posts"->"sellers") visible and settled
  on-screen by t=10s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS, 0 FAILs (checked once after the B01
  fix — see defect #9 above; no separate pre-fix run was needed since the
  clipping was caught first at Gate V).
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly, B01
  re-checked after its fix. One real defect found and fixed; clean on
  final pass.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was
needed — copied directly to
`knowledge-work-plugins--claude-liam-content-strategy-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-content-strategy/` (4K
master + description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-content-strategy/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`, clean,
no conflicts. `HAILOOP-LOG.md` updated with the matching entry.
