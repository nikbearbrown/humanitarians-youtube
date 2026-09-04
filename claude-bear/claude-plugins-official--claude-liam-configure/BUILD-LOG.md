# BUILD-LOG — claude-plugins-official--claude-liam-configure

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-configure/beat_sheet.json`
(a Teardown walkthrough of the Anthropic Discord plugin's `configure` skill,
already fully built — no SCRIPT.md; source `beats[*].narration_text` and
`PEDAGOGY.md` served as the locked script/facts). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill
dispatches on its one argument (no-args → status, `<token>` → save + chmod
600, `clear` → remove); two state files do the work — `.env` (credential,
read once at session start) and `access.json` (policy, re-read on every
inbound message); the design explicitly pushes toward locking the access
policy to an allowlist, offering the flip proactively once pairing has
captured everyone; the sharp, easy-to-miss asymmetry that a saved token
needs a session restart to take effect while an allowlist change is live on
the next message; and the concrete gap that the skill never validates a
pasted token's format before writing it to disk. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "now" → "after restart" — the newcomer's wrong guess that
saving a new token makes it live immediately, corrected toward the actual
mechanism: the credential file is boot-read only, so nothing changes until
a restart). Register re-registered Teardown→Plain: the source's B05
five-item "gets it right / where it bites" list was compressed to the
single most teachable, general-audience fact (no token-format validation)
rather than kept as a full strengths/gaps inventory — the unspecified
`.env` key schema, the unstated `access.json` schema, the missing restart
command, and Discord's own unexplained gates (shared-server requirement,
Public Bot toggle) were dropped as assuming a technical audience
simple/hai-simple doesn't target, not as a verdict on the skill's quality.
BVDT's verdict facts were merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat (built
directly from the source's own observation that "a user who saves a new
token and doesn't restart will think the configuration worked but be
running the old token"); B01→NB01, B02→NB02 kept as one beat each
(NB02 keeps B02's lockdown-rule and restart-asymmetry material bundled
together, matching how the source itself bundles them); B05's five-item
gaps list compressed into NB03 (the one fact a general viewer needs and
can act on — no token validation); BVDT folded into BCRY; BHTF kept,
re-scoped from the source's five-point checklist down to the two checks
that match what NB01–NB03 actually taught (validation and the proactive
lockdown offer), rather than testing untaught specifics (masked token
display, restart command wording, Developer Portal guidance); BOUT kept.
Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ConfigureAnatomy` / `ConfigureDesign` / `ConfigureTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with configure-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00 measured 11.39s — clears the WRITER LAW's ≥9s window with
room to spare (rates — 42ms/char, 8% hesitateBetween, 4% mistakeRate —
copied directly from the already-tuned agent-development sibling, which
reliably finished a similarly short 3-line text inside its window; no
re-tuning needed this time). REMOTION beats (B00/BCRY/BHTF/BOUT) rendered
via `remotion_scenes.py` — the run exceeded the tool's 120s timeout and was
moved to background by the harness automatically; blocked on it via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule, never treating a backgrounded render as "handled" without waiting on
it. NB01–NB03 rendered via `render_scenes.py` (foreground, completed within
timeout).

First `type_check.py` pass was **FAIL, 2 defects**, both fixed at the root
via direct frame inspection (pulling the checker's own mid-clip sample
frame and cropping the flagged pixel region), not by guessing from the
report text alone:

- **bbox-overlap §8.6b, NB02** — flagged "two labels…overlapping" at
  (814–986, 95–135). Cropping that exact region showed the overlap was
  entirely *inside* the single word "TOWARD" in the title "PUSH TOWARD
  LOCKDOWN" (a connected-component blob-splitting artifact in bold EB
  Garamond at this size/weight, not two distinct labels touching — the
  same class of font-metric false positive documented in the sibling's
  `scenes.py` comments). Fixed by rewording the title to "THE LOCKDOWN
  RULE" (same meaning, avoids the specific letter adjacency) — re-rendered
  NB02 only.
- **min-size §8.1, NB03** — smallest text run 17px < 20px floor, "likely a
  caption/label too small." A connected-component pixel analysis of the
  checker's own mid-clip sample frame isolated the actual culprit: the
  isolated word "no" in the accented chip label "no format check" is built
  entirely from x-height letters (no ascender/descender), so its own
  connected-component bounding box measured only 17–18px even though the
  full label reads clearly to the eye. First fix attempt — "not validated"
  (adds ascender/descender letters) — passed GATE T (21px) but on visual
  Gate V inspection turned out to render with the inter-word space nearly
  invisible in bold Garamond ("notvalidated"), a real legibility defect
  the automated check doesn't catch. Second fix — a single-token label,
  "unvalidated" — resolved both: no inter-word space to collapse, and
  "un-" supplies the ascender/descender height the x-height-only "no" was
  missing. Re-rendered NB03 twice (once per fix), `beat_sheet.json`'s
  `graphic.production_viz` synced directly for both edits (not via a full
  `build_beat_sheet.py` re-run, which would have discarded the
  already-measured audio durations and render stamps) before each
  recompile, per COMPLETION LAW.

`type_check.py` went 2→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-configure.mp4`, 7/7 beats
filled real (no slate), 123.8s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 123.78s; mp4
  mtime (1788151853) newer than beat_sheet.json mtime (1788151749)
- Gate V (visual): pulled frames at 8s intervals across the full runtime
  plus a dedicated BOUT pull (its ~4s window fell between two 8s samples).
  Checked: B00 ("now" doomed in terracotta mid-typing, caret visible,
  correct @HumanitariansAI footer), NB01 ("THREE MODES, TWO FILES" chips
  legible, arrows clean), NB02 ("THE LOCKDOWN RULE" — title clean post-fix,
  no overlap, chips legible), NB03 ("NO VALIDATION" — "unvalidated" chip
  clean post-fix, no collapsed space), BCRY (carry-out sentence + sparkline
  read clean), BHTF (correct topic/segment/@HumanitariansAI handle,
  paste-ready fake-token prompt legible), BOUT (OutroSeries: correct
  eyebrow "CONFIGURE · @HUMANITARIANSAI", correct title restate "Saved
  Isn't Live.", crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.39s (≥8s requirement comfortably
  met); the "now" → "after restart" correction lands on screen and the
  full corrected question ("I saved a new token. It's live after restart,
  right?") finishes typing well within the clip.

Metadata file written: `claude-plugins-official--claude-liam-configure.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors"; consistent with the `claude-plugins-official--
claude-liam-agent-development` sibling built earlier in this same family.
Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-plugins-official--claude-liam-configure-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-configure/` (4K
master + description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-configure/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `223b863a`, pushed clean
(no rebase conflicts).

**Status: DELIVERED.**
