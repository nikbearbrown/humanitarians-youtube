# BUILD-LOG — claude-plugins-official--claude-liam-mcp-integration

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-mcp-integration/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `mcp-integration`
Claude Code plugin-dev Skill, already fully built — no SCRIPT.md; the
source's own `source_skill` path
(`../anthropics/claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`)
does not exist on this machine, same defect class as several
`claude-plugins-official` siblings, so the source's already-narrated
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: MCP
connects Claude Code plugins to external services over four transport
types — stdio (spawns a local child process, Claude Code manages its
lifecycle over stdin/stdout, for custom servers and local tools), SSE
(hosted, Server-Sent Events, OAuth handled automatically after one
browser login, for official hosted services like GitHub/Asana/Linear),
HTTP (REST API, token in request headers, stateless), WebSocket
(persistent bidirectional, real-time/low-latency); every server loads
lazily (first tool use triggers the connection) and a config change needs
a Claude Code restart (no live reload); design patterns that keep a
multi-server plugin working — a separate `.mcp.json` instead of inline
`mcpServers` in `plugin.json`, the `CLAUDE_PLUGIN_ROOT` variable for every
path instead of a hardcoded one, and pre-allowing the exact tool name
(`mcp__<plugin>_<server>__<tool>`, discovered via `/mcp`) instead of a
wildcard; and the concrete cost of that exactness — a one-character
mismatch in the pre-allow list makes the tool invisible with no error, and
stdio/HTTP env-var credentials aren't validated until the first real call,
so a broken setup can look healthy until then. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "key" → "transport" — the newcomer's wrong guess that the
important decision is which API key/credential to use, corrected toward
the actual mechanism: the transport type is what has to match where the
service lives; SSE's automatic OAuth is itself evidence against "you
manage a key yourself" being the universal case). Register re-registered
Teardown→Plain: the source's B05 "gets it right / where it bites" list
(five strengths + five gaps) was compressed to the single most teachable,
general-audience fact (the exact-match tool name with no error on
mismatch, plus the unvalidated env var) rather than kept as a full
strengths/gaps inventory — the no-live-reload gap and the full strengths
enumeration were dropped as assuming a technical audience simple/hai-simple
doesn't target, not as a verdict on the skill's quality. BVDT's verdict
facts were merged into the single BCRY carry-out sentence pair rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01
(four transport types), B02→NB02 (`.mcp.json`/`CLAUDE_PLUGIN_ROOT`/exact
tool names) kept as one beat each; B05's long strengths/gaps list
compressed into NB03 (the one fact a general viewer needs and can act on —
exact-match tool names, no error on mismatch, unvalidated env vars); BVDT
folded into BCRY; BHTF kept, with the source's already-generic,
already-runnable prompt ("Add GitHub SSE MCP server and a local custom
stdio server to my plugin") carried over unchanged; BOUT kept. Full audit
in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`McpIntegrationAnatomy` / `McpIntegrationDesign` / `McpIntegrationTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with mcp-integration-specific labels.

B00 params (text "What kind of / key does my plugin / need for / a
service?", trigger "key"→"transport", 42ms/char, 4% mistakeRate, 2%
hesitateWithin, 8% hesitateBetween, jitter 26, `lead_silence_s: 1.0`)
copied verbatim from the agent-development sibling's proven-safe,
post-fix values rather than the component's higher-friction defaults — no
timing overrun on the first render. Audio 10.67s clears the ≥9s TIMING LAW
window comfortably (shorter forward-typed character count than the
sibling's own fixed text, ~49 vs. ~60 chars). Frame-pull verification:
"key" sits doomed in terracotta at t≈1.8s, deletes, "transport" is
retyped and settled by t≈3.0s, and the full corrected question — "What
kind of transport does my plugin need for a service?" — is complete and
legible at t≈4.0s, holding to the end of the 10.7s clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); NB01–NB03 rendered via `render_scenes.py` (Manim, all 3 clean
on first pass); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground; exceeded the tool's 120s timeout and was moved to background
by the harness automatically — blocked on it via `TaskOutput` before
proceeding, per the COMPLETION LAW's foreground-render rule, never
treating a backgrounded render as "handled" without waiting on its exit
code, which was 0). `type_check.py` (GATE T) ran clean on the first pass:
**PASS, 0 FAILs**, no exemptions needed. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-mcp-integration.mp4`, 7/7
beats filled real (no slate), 149.1s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (first pass, no fixes needed)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.5 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 149.125s;
  mp4 mtime (1788163390) newer than beat_sheet.json mtime (1788163201)
- Gate V (visual): pulled frames every ~12s across the full runtime plus
  targeted checks of B00 (t≈1.8s "key" doomed in terracotta, t≈3.0s
  corrected to "transport", t≈4.0s full question settled, held to the
  10.7s end), NB01 (four transport chips legible, SSE correctly accented),
  NB02 (`.mcp.json`→`CLAUDE_PLUGIN_ROOT`→exact tool names chain with
  arrows, correct accent), NB03 (exact match/one typo/no error chips, "no
  error" accented, caption legible), BCRY (carry-out sentence + sparkline
  read clean, italic serif rendering with no glyph-detachment artifacts),
  BHTF (correct topic/title/@HumanitariansAI handle, paste-ready prompt
  text legible, no card overflow), and BOUT (OutroSeries: correct eyebrow
  "MCP INTEGRATION · @HUMANITARIANSAI", correct title restate, crimson
  underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.7s (≥8s requirement met, ≥9s
  audio-window requirement also met at 10.67s including lead_silence); the
  "key" → "transport" correction lands on screen by t≈3.0s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-mcp-integration.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match — `"claude-plugins-official".startswith("claude-
plugins")`), which resolves to "Extending Claude — Skills, Plugins &
Connectors"; this is a more specific match than falling through to the
`hai-simple` skill-key default ("Claude Basics"), consistent with every
other `claude-plugins-official` sibling built to date. Direct code link
per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
