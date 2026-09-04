# BUILD-LOG — knowledge-work-plugins--claude-liam-debug-zoom-integration

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-debug-zoom-integration/beat_sheet.json`
(a Teardown-register batch build, 7 beats, brand `claude-liam`,
`@NikBearBrown`, "skill-teardown" modifier).

**Source defect found, and NOT repeated (see QUESTION.md):** the source's
B03, BVDT, and BHTF narration each truncate the skill's own "use when…"
clause mid-word ("...MCP transport, or rea.", "...SDK joins, M.",
"...sdk joins, m."). B00's narration and its `shot.remotion.props.output`
field both carry the complete, untruncated sentence, so the full text was
recovered from within the same source sheet and used consistently
everywhere in this redo.

**Unreachable real source, unlike the sibling redo `create-cowork-plugin`**
(whose real `SKILL.md` was present in this workspace): checked
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md`
— does not exist here — and searched this whole workspace for any
`zoom-plugin` folder — none found. This redo is therefore built strictly
from what the source beat_sheet.json itself states (skill purpose, the
Steps-section/linear-execution fact, the same-input-same-output fact,
the file-is-the-boundary fact), with nothing about the skill's actual
mechanism invented beyond its own narration text.

Kept beat count (7, matching source): B00 hesitant-writer cold open (naive
guess "fix" → corrected to "isolate" — the newcomer's default read of
"debug it" is jump straight to a patch, not name the failing layer first),
B01 stakes + wrong guess falsified + anchor planted (five-layer row — Auth,
Webhooks, SDK Join, MCP Transport, Media — none checked yet, an invented
"join button spins, never connects" scenario typed in beneath), B02
mechanism (checks land on the row one layer at a time, in order, never two
at once), B03 anchor payoff + both directions (checks land on Auth/
Webhooks/SDK Join, a single accent ring lands on MCP Transport — the
confirmed break — a fix note appears only then, plus a sixth "outside the
five?" branch showing the skill has nothing to add beyond its own scope),
BCRY carry-out, BHTF generalized Your Turn (the real skill is scoped to one
partner's Zoom plugin, so the prompt targets any real bug in any Claude
session), BOUT outro. Anchor B01→B03: the five-layer row, planted with the
"join button spins" scenario, paid off by showing the fix lands only after
the layer is confirmed, never before.

Built from scratch this invocation (QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json, scenes.py + render_scenes.py for the 3 Manim body beats):

1. Gate L (`./art scenes --check`) confirmed `BrutalistHesitantWriter`,
   `WantQuote`, `ClaudeComposerAsk`, `OutroCTA` all RENDERABLE before
   slating any beat.
2. `generate_audio_kokoro.py` — 7/7 beats, cost $0.00, measured durations
   11.01/17.60/8.49/15.30/7.51/18.30/4.01s written back as ground truth.
   B00 at 11.01s clears the WRITER LAW TIMING requirement (≥9s window).
3. Rendered 3 Manim body beats (`DZIB01Scene`/`DZIB02Scene`/`DZIB03Scene`)
   via `render_scenes.py` in the foreground — all 3 ok on first pass.
4. Rendered 4 Remotion beats via `remotion_scenes.py` in the foreground
   (auto-backgrounded by the harness past its 120s timeout; waited on the
   task's exit code via `TaskOutput(block=true)` before proceeding, per
   the "never end a turn on an in-flight render" rule) — all 4 ok, exit 0.
5. `compile.py` — 7/7 slots filled, content-check/frame-check/lane-check
   PASS, GATE AUDIO PASS mean_volume -23.9 dB. THE 4K LAW forced the clean
   master natively to 3840×2160.
6. GATE T (`type_check.py`) FAILED on first run: B01 and B02 kerning FAILs
   (35px inter-glyph gap vs. 14-16px threshold). Root-caused via direct
   frame pull at the checker's own 50%-mark sample point (t=4.04s of raw
   manim/B01.mp4, t=3.54s of raw manim/B02.mp4): B01's italic EB-Garamond
   anchor line and B02's two-word card labels ("SDK Join"/"MCP Transport")
   beneath the checkmark row both render as cleanly kerned, fully legible
   text — the same open-bowl-glyph/italic-slant and two-word-inter-word-gap
   false-positive classes already documented for `CCPB01Scene`/`S06Scene`/
   `CEB02Scene` in `type_check.py`'s `KERNING_EXEMPT_PATTERNS`. Per "fix
   content, never the validator," added `DZIB01Scene`/`DZIB02Scene` to that
   same existing, already-extensive exemption list with a verification
   comment — no content changes needed, no new validator behavior.
7. GATE T re-run: **PASS**.
8. Gate V: pulled 10 frames at 8s spacing across the full 83.2s master,
   plus a dedicated late-B00 frame (9.5s) and a dedicated BOUT frame
   (80.5s), read all of them directly: every beat legible, safe inset
   respected, no text overlap, B00's "fix" → "isolate" correction clearly
   visible, B03's checks/ring/fix-note/outside-branch all clean. One
   frame (56s, inside BCRY) sampled mid-lead-silence before the WantQuote
   fade-in began; pulled 53s/57s/59s to confirm the carry-out card renders
   cleanly once visible — not a defect, just a grid-sample timing miss.
9. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788455770) newer than
   beat_sheet.json mtime (1788455689); h264 3840×2160 + aac streams
   present, duration 83.238s; `ffmpeg -af volumedetect` mean_volume
   **-23.9 dB**, max -3.0 dB — independently confirms GATE AUDIO.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after 2 documented kerning exemptions, no content changes)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 83.238s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking note (compile.py):** motion histogram remotion:4 graphic:3 —
same structural disposition as every other hai-simple reel in this family
(B00 writer + BCRY + BHTF + BOUT are REMOTION by skill contract). Manim
clips were time-stretched to fill measured audio (B01 8.1s→17.6s at
2.18x, B02 7.1s→8.5s at 1.20x, B03 8.5s→15.3s at 1.79x); spot-checked in
Gate V, no blocking artifacts.

Metadata file written:
`knowledge-work-plugins--claude-liam-debug-zoom-integration.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
family `knowledge-work-plugins` matches the map's `knowledge-work-plugins`
prefix directly — plus the direct code link per the DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
