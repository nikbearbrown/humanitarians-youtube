# BUILD-LOG — claude-plugins-official--claude-liam-build-mcp-server

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-build-mcp-server/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic Build MCP Server
Claude Code plugin-dev Skill — a discovery-and-routing skill — already fully
built, no separate SCRIPT.md; source `beats[*].narration_text` served as the
locked script). Built entirely fresh this invocation — only SUBJECT.json
existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill
asks four discovery questions (deployment, users, action count, auth)
before any scaffolding; three deployment paths ranked by preference —
remote HTTP as the default for anything wrapping a cloud API (zero install
friction, one server for all users, working OAuth redirect handling),
MCPB for local distribution when the server must touch the user's machine
(local files, desktop apps, localhost), local stdio via npx/uvx as a
prototype-only stepping stone; a seven-scenario decision matrix; two
tool-design patterns keyed to action count — one tool per action under
about fifteen operations, or search-plus-execute (two tools: search-actions
and execute-action) for large surfaces to keep the context window from
flooding, with a hybrid promoting the three-to-five most-used actions; the
three non-tool primitives (resources, prompts, elicitation); and the
concrete cost of a vague tool description — Claude reads the description,
not the name, to decide which tool to call, so a description that just
restates the tool's name leaves similar tools (create-issue vs.
update-issue) indistinguishable. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "code" → "decide" — the newcomer's wrong guess that the first
step in building an MCP server is writing server code, corrected toward the
actual mechanism: discovery-before-code, four questions decided before any
scaffolding exists). Register re-registered Teardown→Plain: the source's
B05 "gets five things right / where it bites" list (discovery-before-code
structure, remote-HTTP default, search-plus-execute pattern, elicitation
framed as spec-native with a capability-check caveat, the seven-scenario
matrix — versus the elicitation capability check buried mid-paragraph, the
FastMCP jlowin-PyPI-vs-frozen-1.0 version split, tool description guidance
deferred to a references file, the OAuth CIMD/DCR distinction deferred, and
the "load Claude docs first" invariant having no enforcement) was compressed
to the single most teachable, general-audience fact — the description
decides which tool Claude calls — rather than kept as a full
strengths/gaps inventory; the Claude-harness-internals gaps (FastMCP
package split, elicitation capability-check mechanics, OAuth protocol
distinction) were dropped as assuming a technical audience simple/hai-simple
doesn't target, not as a verdict on the skill's quality. BVDT's verdict
facts (the three-path ranking, the two tool patterns, the description
caveat) were merged into the single BCRY carry-out sentence rather than kept
as a separate bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
deployment-anatomy/tool-design + B05 teardown analysis + BVDT verdict +
BHTF your-turn + BOUT outro). This redo kept the same 7-beat shape: B00
carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat; B01→NB01, B02→NB02 kept as one beat each, content carried over
near-verbatim since both were already factual descriptions of the skill's
own stated guidance rather than this reel's design judgment (no Plain
re-registration content change needed); B05's long gaps/strengths list
compressed into NB03 (the one fact a general viewer needs and can act on);
BVDT folded into BCRY; BHTF kept, with the source's already-generic,
already-runnable prompt ("Build an MCP server that wraps the GitHub API —
tools for creating issues, searching repositories, and getting pull
request details") carried over unchanged; BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`BuildMcpServerDeployment` / `BuildMcpServerPatterns` / `BuildMcpServerTell`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with build-mcp-server-specific labels.

**B00 TIMING LAW — clean on the first render, no fix pass needed.** Text
"What do I / code first / for an MCP / server?" (39 chars, shorter than the
`claude-plugins-official--claude-liam-agent-development` sibling's
already-fixed-safe 60-char text) at that sibling's already-tuned-safe
parameters (42ms/char, 4% mistakeRate, 2%/8% hesitation, seed
`hai-build-mcp-server`) rendered to 9.41s audio + 1.0s lead_silence ≈ 10.4s
clip window; actual `media/B00.mp4` measured 9.43s (≥8s floor). Verified by
frame pull: "code" sits doomed in terracotta at t≈2.2s, the corrected word
"decide" is mid-type by t≈4.0s ("...decide first fi|"), and the fully
corrected question "What do I decide first for an MCP server?" is settled
and legible at the clip's last frame.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); NB01–NB03 rendered via `render_scenes.py`; B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (foreground; completed within the first
call). First `type_check.py` pass was **FAIL, 1 defect**, fixed at the
root, not by touching the validator:

- **min-size §8.1, BOUT** — reported "smallest text run 38px < floor 41px."
  Diagnostic (running the checker's own `text_run_bboxes`/`blob_bboxes`
  functions directly against the extracted frame) showed only ONE blob in
  the entire frame passed the word-run width filter (`w >= h*1.5`): an
  accidental 2-letter merge inside "Discovery" (h=38, w=65), while every
  genuinely individual glyph in the frame measured 41–89px tall (raw blobs:
  89, 84, 77, 56, 51, 50... all comfortably above the 41px floor). This is
  the same false-positive class the checker documents elsewhere for
  non-touching serif letters at 4K: real text fails the "is this a word
  run" width test because adjacent letters in this font don't visually
  touch at this size, so the checker's own individual-char fallback path
  (see B00's own PASS note: "individual-char fallback at 2×") normally
  catches this — but here one unlucky touching pair squeaked past the
  filter first and reported its own (misleadingly low) height instead.
  Root cause confirmed pixel-exact (core glyph color `[41,25,12]` vs.
  checker's `INK_HEX` `#3D3929` — Euclidean distance ≈47.6, just under the
  48 tolerance, consistent and not a compression artifact). Fixed by
  retitling the outro card from the working title "Discovery Before Code."
  to **"Decide First."** — shorter, ties directly to B00's wrong-guess
  correction ("decide") and BCRY's sparkline ("Decide first. Code
  second."), and its different glyph layout avoids the accidental
  touching-pair merge. Re-rendered BOUT and BHTF only (BHTF's `segment`
  prop also carries the title) via `remotion_scenes.py --only <beat>
  --force`; `beat_sheet.json` patched directly for both props (not via a
  full `build_beat_sheet.py` re-run, which would have discarded the
  already-measured audio durations and render stamps), per COMPLETION LAW.
  Full diagnostic trail in SCRIPT.md's BOUT footnote. First `remotion_scenes.py
  --only BOUT --force` call ran past the harness's 120s foreground timeout
  and was moved to background automatically; blocked on it via `TaskOutput`
  (exit 0, both BOUT and BHTF confirmed re-rendered) before proceeding, per
  the COMPLETION LAW's foreground-render rule — never treating a
  backgrounded render as "handled" without waiting on it.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-build-mcp-server.mp4`, 7/7
beats filled real (no slate), 182.5s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect, verified
  independently), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 182.5s; mp4
  mtime (1788140188) newer than beat_sheet.json mtime (1788139974)
- Gate V (visual): pulled frames across the full runtime (B00 open, NB01
  three-deployment-paths chips with remote-HTTP accented, NB02
  two-tool-patterns chips with search+execute accented, NB03
  description-decides chips with description accented, BCRY carry-out
  quote + sparkline, BHTF Your Turn card with correct topic/segment/prompt/
  handle, BOUT correct eyebrow + retitled "Decide First." + crimson
  underline). All legible, correct accents, no overlap or truncation. No
  blockers.
- B00 TIMING LAW: `actual_duration_s` 9.43s (≥8s requirement met); "code" →
  "decide" correction lands on screen by t≈4.0s and the full corrected
  question stays legible through the clip's last frame.

Metadata file written: `claude-plugins-official--claude-liam-build-mcp-server.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors"; more specific than falling through to the
`hai-simple` skill-key default ("Claude Basics"), consistent with the
`claude-plugins-official--claude-liam-agent-development` sibling built
earlier in this same family. Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
