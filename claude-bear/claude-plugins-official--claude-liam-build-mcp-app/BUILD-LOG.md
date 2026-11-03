# BUILD-LOG — claude-plugins-official--claude-liam-build-mcp-app

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-build-mcp-app/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `build-mcp-app`
Claude plugin-dev Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: an MCP
app is a standard MCP server that also serves UI resources rendered
inline as iframes; the two-part registration pattern splits a tool
(declares `_meta.ui.resourceUri`, handler returns plain data, not the
HTML) from a resource (registered separately, serves the widget's HTML
with the exact MIME type `text/html;profile=mcp-app`); the host fetches
the resource on tool call and pipes the tool's return value into the
iframe via `ontoolresult`; the App class inside the iframe bridges with
`sendMessage`, `updateModelContext`, `callServerTool`, `openLink`; the
iframe's CSP blocks CDN fetches so the ext-apps bundle must be inlined at
startup; route before building — elicitation covers yes/no, enum picks,
flat forms, a widget is only for searchable lists, visual previews,
charts/maps, live progress, otherwise plain text is faster; five design
rules (one widget per tool, description must mention the widget, graceful
degradation is automatic, don't block on widget results, follow host
theme); and the concrete shared failure mode — a wrong MIME type and an
un-inlined bundle both produce the exact same blank rectangle with no
console error. B00 replaced the source's `ClaudeComposerAsk` typed-ask
cold open with `BrutalistHesitantWriter` (WRITER LAW: "tool" → "resource"
— the newcomer's wrong guess that the tool itself sends back the widget's
HTML, corrected toward the actual mechanism: a separately-registered
resource serves it). Register re-registered Teardown→Plain: the source's
B05 "gets it right / where it bites" list (routing table, working
TypeScript, bundle-inlining snippet, eight-method App class API, design
rules — versus the Desktop cache-flush gotcha, CSP-blank documented in a
reference file, the frameDomains footnote, the silent wrong-MIME failure,
sendMessage/updateModelContext placement) was compressed to the single
most teachable, general-audience fact (the two causes of the identical
blank-rectangle failure) rather than kept as a full strengths/gaps
inventory — the tooling-internals gaps (Desktop cache-flush requirement,
frameDomains restriction, method-list placement complaint) were dropped
as assuming a technical audience simple/hai-simple doesn't target, not as
a verdict on the skill's documentation quality. BVDT's verdict facts were
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on); BVDT
folded into BCRY; BHTF kept, with the source's already-generic,
already-runnable prompt ("Build an MCP app with a file picker widget that
lets users select a file from a list returned by a directory scan tool")
carried over near-verbatim with all four of its watch points; BOUT kept.
Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`BuildMcpAppAnatomy` / `BuildMcpAppDecision` / `BuildMcpAppTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with build-mcp-app-specific labels.

**B00 TIMING LAW** — text kept short from the start (44 forward-typed
chars, 3 lines: "How do I make / my tool serve / the widget's HTML?",
trigger "tool" → "resource") and rendered at the safe-margin params
already established on the `agent-development`/`access` siblings'
post-fix attempts (42ms/char, 4% mistakeRate, 2% hesitateWithin, 8%
hesitateBetween) — no TIMING LAW overrun this time. `actual_duration_s`
10.05s (≥8s floor met). Frame-pull verification: "tool" doomed in
terracotta by t≈2.2s, the correction ("my resource serve") visible by
t≈4.5s, the full corrected question "How do I make my resource serve the
widget's HTML?" settled and legible by t≈9.5s, held to the end of the
10.1s clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(exceeded the tool's 120s foreground timeout and was moved to background
by the harness — blocked on it via `TaskOutput` before proceeding, per
the COMPLETION LAW's foreground-render rule); NB01–NB03 rendered via
`render_scenes.py`. First `type_check.py` pass was **FAIL, 2 defects**:

- **min-size §8.1, NB01 (17px) and NB03 (18px)**, both < the 20px floor —
  root-caused against the passing `agent-development` sibling: every
  chip label that PASSED there was ≤14 characters (the safe font-size
  tier); my initial NB01 chip "resource -> HTML" (16 chars) and NB03 chip
  "bundle not inlined" (18 chars) fell into the next tier down (fs=22),
  which then over-scaled to fit the fixed chip width and dropped under
  the floor. Fixed by shortening every long chip label to ≤14 characters
  (NB01: "resource -> HTML" → "resource: HTML"; NB03: "bundle not
  inlined" → "no bundle", "blank, no error" → "silently blank"), synced
  in both `scenes.py`'s `BEAT_CONTENT` and `beat_sheet.json`'s
  `graphic.production_viz.chips`/`caption` directly (not a full
  `build_beat_sheet.py` re-run, which would have discarded the measured
  audio/render stamps) — re-rendered NB01 and NB03 only (NB02 untouched,
  its own labels never failed).

`type_check.py` went 2→**PASS, 0 FAILs**. First `compile.py` invocation
was wrapped in a shell `timeout 115` (to dodge the tool's 120s
auto-background) — **this produced a silently truncated master**: the
4K `slow`/`crf16` x264 encode of ~176s of footage takes longer than
115s, so `timeout` sent SIGTERM mid-encode; ffmpeg finalized the mp4
gracefully at the point of interruption, writing a fully valid,
playable, correctly-headered **134.2s** file with no error surfaced
anywhere (ffprobe, GATE T, and a first duration check all looked clean).
Caught only by cross-checking the compiled duration against the sum of
the beats' own measured `actual_duration_s` (~176s expected vs. 134s
delivered) and confirming via `ffmpeg -f null -` frame-count decode
(3218 of an expected 4233 frames). **Root cause and fix:** never wrap
`compile.py`'s real (non-`--review`) encode in a shell `timeout` short
enough to interrupt a slow-preset 4K pass — let the harness's own
120s-then-background behavior apply instead, and block on the
backgrounded task via `TaskOutput` with a generous timeout, exactly as
the COMPLETION LAW already prescribes for renders. Recompiled without
the shell timeout (auto-backgrounded at 120s, blocked via `TaskOutput`
at 480s ceiling): full 176.25s, 4230/4233 frames decoding cleanly
end-to-end via a second independent `ffmpeg -f null -` pass.

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-build-mcp-app.mp4`, 7/7
beats filled real (no slate), 176.25s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

A post-compile beat_sheet.json edit (reverting NB02's `chips` metadata
back to match its already-rendered, never-failing labels, after an
earlier edit had drifted the metadata out of sync with the actual video)
triggered one more recompile per the COMPLETION LAW's "never leave
beat_sheet.json touched after the final compile" rule — final numbers
unchanged (176.25s / 4230 frames / GATE T PASS / GATE AUDIO −24.0 dB),
confirmed by re-running every check below against this last master.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.5 dB
- ffprobe + independent `ffmpeg -f null -` decode: video 3840×2160 h264,
  audio (aac) present, duration 176.25s, 4230 frames decoded end-to-end
  (matches the beats' summed audio-measured duration); mp4 mtime
  (1788137711) newer than beat_sheet.json mtime (1788137575)
- Gate V (visual): pulled frames across the full runtime (B00 at
  t≈2.2/4.5/9.5s for the WRITER LAW correction; NB01 mid-beat showing
  the "tool: data → resource: HTML → bundle inlined" chip row with the
  correct beat accented; NB02 mid-beat "elicitation first → widget if
  needed → else: text"; NB03 "wrong MIME → no bundle → silently blank";
  BCRY carry-out quote + sparkline; BHTF paste-ready prompt with correct
  topic/title/@HumanitariansAI handle; BOUT title-restate outro). All
  legible, correct palette, no overlap, no truncation. No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.05s (≥8s requirement met); the
  "tool" → "resource" correction lands on screen by t≈4.5s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-build-mcp-app.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix
(`"claude-plugins-official".startswith("claude-plugins")`), consistent
with the `access` and `agent-development` siblings built in this same
family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-30 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-plugins-official--claude-liam-build-mcp-app-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-build-mcp-app/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-build-mcp-app/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`297f1b32`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
