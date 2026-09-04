# BUILD-LOG — claude-tag-plugins--claude-liam-pagerduty-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-pagerduty-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel, 7 beats: B00
`ClaudeComposerAsk` typed ask; B01 `PagerdutyApiAnatomy` — two-API/two-host
split + data model chain; B02 `PagerdutyApiDesign` — sanity check, trace
routing, log entries, `From:` header, gotchas; B05 `PagerdutyApiTell` — a
"gets it right / where it bites" teardown of the skill's own documentation;
`BVDT` `ClaudeVerdictArtifact` recap; `BHTF` your-turn; `BOUT`
`ClaudeTitleOutro`). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: PagerDuty
splits into two separate APIs on two hosts with two unrelated auth schemes —
REST at `api.pagerduty.com` (`Authorization: Token token=<key>`, not Bearer,
not Basic) for reading/managing everything (schedules, services, escalation
policies, incidents, users); Events v2 at `events.pagerduty.com`
(`routing_key` in the JSON body, no Authorization header) for
trigger/acknowledge/resolve; the data model is a chain (alert fires on a
service, routes through an escalation policy to schedules/users, opens an
incident; log entries are the authoritative "who got paged and why" record);
sanity check first (`GET /v1/users/me`, 401 = empty body, must print HTTP
status explicitly); `From:` header required on every mutation or 400; raw
curl bracket-filter params need `-g`/`--globoff` (the bundled `pd_oncall.sh`
already handles this); reference objects need both `id` and `type` or a 400;
Events v2 errors are plain text, not JSON; rate limits differ (REST 960/min
with headers, Events v2 ~120/min with none).

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "TOKEN" → "ROUTING KEY" — the
newcomer's actual wrong guess that one credential covers triggering an
alert, corrected toward the real Events-v2 routing-key auth). Register
re-registered Teardown-shaped→Plain: the source's B05 "gets it right /
where it bites" list is a documentation-quality verdict — Teardown judgment
on the skill's own writing, not on Claude's behavior. Plain register keeps
every fact in that list (folded into NB03) but drops the verdict framing
entirely. `BVDT`'s verdict facts were merged into the single `BCRY`
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW. Close re-skinned to `@HumanitariansAI` (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape, matching the
`notion-api`/`linear-api`/`jira-api` siblings built earlier the same day:
B00 carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat; B01→NB01 (two APIs + data model), B02→NB02 (the two most consequential
design points: sanity check and the `From:` header); B05's "gets
right/bites" list plus B02's remaining gotchas (bracket URL encoding,
reference `type` field, plain-text Events v2 errors, rate limits) folded
into NB03's neutral "worth knowing" facts, dropping only the verdict
framing; BVDT folded into BCRY; BHTF kept, with the source's five-point
Claude-Code-session watch-list replaced by one paste-ready prompt that tests
the same REST-vs-Events-v2 reasoning without requiring a live PagerDuty
account; BOUT kept.

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` for
B00/BHTF, `PagerdutyApiAnatomy`/`PagerdutyApiDesign`/`PagerdutyApiTell` for
the body, `ClaudeVerdictArtifact` for BVDT, `ClaudeTitleOutro` for BOUT), so
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's mandated
cold-open swap. None of the source's custom body components were reused for
NB01–NB03 even though they are REMOTION: `PagerdutyApiTell`'s on-screen text
bakes in a "gets right / bites" rubric, the same defect class the
`notion-api`/`confluence-api` siblings documented. NB01–NB03 instead reuse
the generic "chip row" Manim template (copied verbatim, mechanism and GATE T
exemption notes included, from the `claude-tag-plugins--claude-liam-notion-api`
sibling), parametrized entirely from neutral title/chip/caption strings.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground,
completed within the tool's timeout this run — all 4 beats came back `ok`,
B00 extended to 13.1s); NB01–NB03 rendered via `render_scenes.py` (manim,
foreground).

**One real legibility defect found and fixed before the first GATE T pass
completed clean, via direct bbox inspection (not just frame-reading):**
GATE T's first run flagged NB01 and NB03 at a 17px text-run height (floor
20px). Bumping the shared `_chip()` font-size tiers 26/22/18→30/26/20 (the
proven fix from the `linear-api` sibling) resolved NB03 and NB02 immediately
but left NB01 unchanged at exactly 17px — because NB01's failing run was not
the chip text itself but the `=` glyph inside the long, width-constrained
"EventsV2=routing_key" label: the shared `_chip()` auto-scale-to-fit logic
compresses text back down to the fixed chip width regardless of the
font-size tier once a label already overflows, so a larger requested
font-size on an already-overflowing label nets an *identical* rendered size
(confirmed by calling `type_check.py`'s own `visible_text_mask` /
`labeled_blobs` / `text_run_bboxes` functions directly and diffing bboxes
before and after the font bump, rather than guessing from re-rendered
frames — the same direct-inspection technique documented on the
`linear-api` sibling). The `=` sign renders as two separate thin horizontal
bars in EB Garamond, which shrink under the floor once the surrounding label
is long enough to force scale-down; the shorter `REST=Token` chip uses the
same glyph at full, unscaled size and was never flagged. Fixed at the
content level (not the shared renderer) by shortening the label to
`EventsV2=key` — the full "routing_key in the body" fact is already carried
in NB01's narration, so the chip only needs to name the concept, not repeat
the field name. Re-verified via the same direct bbox dump (smallest run
24px, clear of the floor) before re-rendering and recompiling. Synced
`beat_sheet.json`'s `graphic.production_viz.chips` field to `scenes.py`
before recompiling, per COMPLETION LAW.

`type_check.py` (GATE T): first pass FAIL 2 (NB01, NB03 min-size §8.1);
PASS 0 FAILs after the font-tier bump + NB01 content fix above.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-tag-plugins--claude-liam-pagerduty-api.mp4`, 7/7 beats
filled real (no slate), 158.6s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (compile.py's own check)
- ffprobe (self-verified, not just trusted from compile.py's log): video
  3840×2160 h264, audio (aac) present, duration 158.6s; independently
  re-ran `ffmpeg -af volumedetect` — mean -23.8 dB, max -2.8 dB; mp4 mtime
  (1788222050) newer than beat_sheet.json mtime (1788221907)
- Gate V (visual): pulled 23 frames across the full 158.6s runtime
  (roughly every 7s) plus targeted crops of the NB01 accented chip (to
  confirm the `=`-glyph fix held and no strikethrough-like artifact
  remained on any accented chip), B00 (t=2s "Can Claude trigger a" typing,
  t=10s full corrected question "my API ROUTING KEY?" typed and settled,
  held to the clip's end), all three GRAPHIC beats' chip rows (titles,
  chips, captions all legible, accent underline never crosses a glyph
  descender), BCRY (carry-out sentence and sparkLine footer read clean),
  BHTF (correct topic/title/`@HumanitariansAI` handle, prompt text legible,
  no clipping), and BOUT (`OutroSeries`: correct eyebrow "PAGERDUTY API ·
  @HUMANITARIANSAI", correct title restate "The Routing Key, Not the
  Token.", crimson underline, no truncation). No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 13.07s (≥8s requirement met, ≥9s
  window from `lead_silence_s: 0.8` + 35-word narration); frame pulls
  confirm the correction ("TOKEN" → "ROUTING KEY") fully typed and settled
  by t≈9s, held with the full corrected question legible to the clip's end.

Metadata file written: `claude-tag-plugins--claude-liam-pagerduty-api.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`claude-tag-plugins`) does not
match any map prefix by `str.startswith` (same as the `notion-api`/
`linear-api`/`jira-api` siblings), so resolution fell through to the
`hai-simple` skill-key entry, which resolves to "Claude Basics". Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-tag-plugins--claude-liam-pagerduty-api-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-tag-plugins--claude-liam-pagerduty-api/` (4K master +
description) for the Drive sync. Committed and pushed to
`claude-bear/claude-tag-plugins--claude-liam-pagerduty-api/` in
humanitarians-youtube (commit `c0544ad0`: README.md = description,
beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md, QUESTION.md,
BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
