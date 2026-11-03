# BUILD-LOG — claude-plugins-official--claude-liam-access

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-access/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Discord `access` Claude Code
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the
skill's state lives in one file, `~/.claude/channels/discord/access.json`,
with five fields (dmPolicy, allowFrom, groups, pending, mentionPatterns);
a missing file defaults safely; the security rule runs before anything
else — a request that arrived as a Discord message rather than something
typed in the user's own terminal is refused, because channel messages can
carry injected instructions; approving someone follows the `pair` path
(check code + expiry, add to allowFrom, delete the pending entry, write a
marker in an `approved/` folder the Discord side polls); two implementation
rules guard it (read-before-write, never auto-pick a lone pending code);
and the concrete reason that last rule matters — an attacker DMing the bot
seeds a pending code, then a forged second message posing as the user
("approve the pending request") is exactly the attack the terminal-only
refusal stops. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold
open with `BrutalistHesitantWriter` (WRITER LAW: "Discord" → "the
terminal" — the newcomer's wrong guess that asking the bot directly on
Discord is enough to get approved, corrected toward the actual mechanism:
only a terminal-typed command counts). Register re-registered Teardown→
Plain: the source's B05 "gets it right / where it bites" list was
compressed to the single most teachable, general-audience fact (the
forged-message attack) rather than kept as a full strengths/gaps
inventory — the Claude-Code-implementation-detail gaps in the source
(undocumented `$ARGUMENTS` placeholder, unbounded `mentionPatterns` regex,
unexplained `dmPolicy` mode differences, undocumented server re-read
mechanism) were dropped as assuming a technical audience simple/hai-simple
doesn't target, not as a verdict on the skill's quality. BVDT's verdict
facts were merged into the single BCRY carry-out sentence rather than kept
as a separate bulleted artifact card, per CARRY-OUT LAW. Close re-skinned
to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/command-dispatch + B05 teardown analysis + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00
carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat; B01→NB01, B02→NB02 kept as one beat each; B05's long strengths/gaps
list compressed into NB03 (the one fact a general viewer needs and can
act on); BVDT folded into BCRY; BHTF kept, with the source's
Discord-plugin-specific instructions ("set up the Discord channel plugin
and run /discord:access") replaced by a concrete, paste-ready prompt that
needs no Discord setup so it's actually runnable by any viewer today;
BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`DiscordAccessAnatomy` / `DiscordAccessCommands` / `DiscordAccessTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`, one title + up to 4
labeled chips + optional arrows/accent/strike + caption) copied verbatim
from the `claude-for-legal--claude-liam-cease-desist` sibling. B00
hesitant-writer correction ("Discord" → "the terminal") verified on
screen by direct frame pulls: "Discord" typed and fully visible in
terracotta (about to be deleted) at t≈1.5–2s, erased and mid-replacement
("If I ask in t|") by t≈2.5s, settled correct text "If I ask in the
terminal to be approved, does that work?" by t≈4s and still correct at
t≈9s — full clip 10.05s (≥8s TIMING LAW window met).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground; the first invocation exceeded the tool's 120s timeout and
was moved to background by the harness automatically — blocked on it via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule); NB01–NB03 rendered via `render_scenes.py`. First `type_check.py`
pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB02** — smallest text run measured 19px, 1px under the
  20px floor. Diagnosed against the NB01/NB03 siblings (both PASS at
  identical chip-box dimensions and font-size tier): NB02's third chip
  label, `"write approved"` (14 chars, nominally the same `<=14` font-size
  bucket as its neighbors `"check code"`/`"add to list"`), rendered
  narrower than expected and forced extra scale-down. Fixed by shortening
  the label to `"marker file"` (11 chars, matching its neighbors' length
  more closely) — re-rendered NB02 only (NB01/NB03 untouched), and
  `beat_sheet.json`'s `graphic.production_viz.chips` for NB02 was synced
  to the fixed wording directly (not via a full `build_beat_sheet.py`
  re-run, which would have discarded the already-measured audio durations
  and render stamps) before the recompile, per COMPLETION LAW.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-access.mp4`, 7/7 beats
filled real (no slate), 115.4s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 115.4s; mp4
  mtime (1788133288) newer than beat_sheet.json mtime (1788133185)
- Gate V (visual): pulled frames every 8s across the full runtime plus
  targeted checks of B00 (t≈1.5–2s "Discord" doomed in terracotta, t≈2.5s
  mid-correction, t≈4s and t≈9s settled+correct), NB01–NB03 (all three
  chips legible and parallel-sized post-fix), BCRY (carry-out sentence
  reads clean), BHTF (correct topic/title/@HumanitariansAI handle,
  paste-ready prompt text legible), and BOUT (OutroSeries: correct eyebrow
  "DISCORD ACCESS · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.05s (≥8s requirement met); the
  "Discord" → "the terminal" correction lands on screen by t≈4s, well
  inside the clip.

Metadata file written: `claude-plugins-official--claude-liam-access.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins
& Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix
(a `str.startswith` match, not an exact-key match — `"claude-plugins-
official".startswith("claude-plugins")`), which resolves to "Extending
Claude — Skills, Plugins & Connectors"; this is a more specific match than
falling through to the `hai-simple` skill-key default ("Claude Basics")
used on siblings whose family string matches no map prefix (e.g.
`claude-for-legal`). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-30 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-plugins-official--claude-liam-access-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-access/` (4K master
+ description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-access/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
