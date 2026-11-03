# BUILD-LOG — financial-services--claude-liam-deal-screening

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-deal-screening/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `deal-screening`
skill for triaging inbound private-equity deal flow, already fully
built — no SCRIPT.md; source `beats[*].narration_text` served as the
locked script). Built entirely fresh this invocation — only SUBJECT.json
existed on pickup.

Question, facts, and full body argument carried over unchanged:
deal-screening quickly screens inbound deal flow — CIMs, teasers, and
broker materials — against a fund's investment criteria; it extracts key
deal metrics, runs a pass/fail framework, and outputs a one-page screening
memo; a skill is a folder Claude reads before it works, and the SKILL.md
inside is the full instruction set, in plain language, with no hidden
logic; the instructions live in a Steps section that Claude executes
linearly, in order, with no branching unless a step says so; and the
skill's limit is that it only does what those steps specify — same input,
same output, every run. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/private-equity/skills/deal-screening/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source beat_sheet.json's own narration already stated the skill's
scope in enough detail to redo faithfully; no reconstruction was needed
(see QUESTION.md).

**The call:** register re-registered Teardown → Plain. Source's B03 framed
the skill's scope as a "design tell" verdict ("what it gets right" / "what
it bites") — Teardown judgment language — removed; NB03 states only the
mechanism (a fixed spec, executed the same way every run) and its plain
consequence (nothing outside the spec is in scope, including the decision
itself), never a verdict on the skill's design. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER
LAW: "decide" → "screen" — the newcomer's wrong guess that the skill
decides whether the fund should pursue the deal, corrected toward the
actual mechanism: it screens the deal against stated criteria and hands
back a memo; a person still decides.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design-tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat — the source's Teardown shape carries no
separate wrong-guess or anchor beat to redistribute, and stays on one
running example throughout, so no separate anchor beat was invented
either — same resolution as the `financial-services--claude-liam-cim-builder`
and `claude-plugins-official--claude-liam-agent-development` siblings,
both of which had the identical thin-Teardown shape); B01→NB01, B02→NB02
kept as one beat each; B03's design-tell framing compressed into NB03 as a
plain mechanism-and-scope statement; BVDT's verdict facts folded into the
single BCRY carry-out sentence per CARRY-OUT LAW rather than kept as a
separate bulleted artifact card; BHTF kept, with the source's prompt
carried over (lightly de-truncated — the source narration cut the phrase
to "against the fund's investme," restored here to "against my fund's
investment criteria," same prompt, not a new one); BOUT kept, re-skinned
to the Humanitarians AI outro (`OutroSeries`). Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact` / `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`), copied verbatim from the
`financial-services--claude-liam-cim-builder` sibling, adapted with
deal-screening-specific labels and chip content.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, local, `am_onyx`. Clean on
   the first pass, no regeneration needed. Durations: B00 9.86s, NB01
   13.08s, NB02 8.38s, NB03 13.89s, BCRY 10.30s, BHTF 18.71s, BOUT 3.93s
   (+1.0s tail).
2. `render_scenes.py` — all 3 Manim scenes rendered clean on the first
   pass.
3. `remotion_scenes.py` — the call exceeded the tool's 120s timeout and
   was moved to background by the harness automatically; blocked on it via
   `TaskOutput` before proceeding, per the COMPLETION LAW's
   foreground-render rule — never treated the backgrounded render as
   "handled" without waiting on its exit code. All 4 Remotion beats
   (B00/BCRY/BHTF/BOUT) rendered clean on the first pass, exit code 0.
4. **B00 TIMING LAW verified by frame pull, not just duration**:
   media/B00.mp4 is 9.86s (clears the ≥8s floor). Pulled frames at
   t=3.0s/3.5s — "decide" types out fully in terracotta — and at
   t=4.5s/9.0s — the mistake is deleted mid-word ("scr|") and rebuilt into
   the full corrected question "Does the deal-screening skill screen this
   deal for me?", settled and legible with real margin before the clip
   ends. No timing defect; no B00 re-render needed.
5. `compile.py --force` → 7/7 beats filled real (no slate), 79.2s,
   3840×2160 (native 4K, THE 4K LAW). GATE AUDIO reported PASS inline:
   mean_volume -24.1 dB.
6. `type_check.py` (GATE T) → **PASS, 0 FAILs, first pass** — no defect to
   fix.
7. Gate V (visual, manual): pulled 10 frames every ~8s across the full
   79.2s runtime plus 4 targeted B00 timing-check frames (t=3.0/3.5/4.5/9.0s),
   and read every one directly. B00's mistake-then-correction reads clean
   with margin; NB01–NB03's chip rows are all legible, correctly labeled,
   one accent moment each (SKILL.md → plain language → **the program**;
   Steps section → in order → **linear**; deal metrics → pass/fail →
   **one memo**); BCRY's carry-out quote and sparkline read clean; BHTF's
   composer card shows the correct topic/title/@HumanitariansAI handle and
   the full paste-ready prompt; BOUT's title restate is legible. No
   blockers found.
8. Audio presence: `ffmpeg -af volumedetect` on the final master → mean
   volume **-24.1 dB**, max -3.0 dB. `ffprobe` confirms h264 3840×2160
   video + aac audio present. Master mtime (1788286377) is newer than
   beat_sheet.json mtime (1788286306).

**Noted, not a defect introduced here:** `OutroSeries` renders on flat
white rather than the humanitarians cream ground in BOUT — same
shared-component behavior already logged unremarked for `OutroSeries` /
`OutroCTA` in the `financial-services--claude-liam-cim-builder` and
`financial-services--claude-liam-bond-relative-value` siblings. Not fixed
here, per the same precedent.

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs, first pass
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 79.2s; mp4
  mtime newer than beat_sheet.json mtime
- B00 TIMING LAW: `actual_duration_s` 9.86s (≥8s requirement met); the
  "decide" → "screen" correction lands on screen by t≈9.0s with margin

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to the `hai-simple` skill-key literal match,
resolving to **Claude Basics** — same resolution as every other
`financial-services--*` sibling in this family.

Metadata file written: `financial-services--claude-liam-deal-screening.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4, DELIVERED

Master is already native 3840×2160 (compile.py's 4K LAW forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-deal-screening.mp4 \
   financial-services--claude-liam-deal-screening-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-deal-screening/`
(4K mp4 + description.md) for the Drive sync. Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-deal-screening/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `155b68b6`, pushed clean.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
