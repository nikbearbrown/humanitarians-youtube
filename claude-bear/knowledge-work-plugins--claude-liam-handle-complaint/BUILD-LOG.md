# BUILD-LOG — knowledge-work-plugins--claude-liam-handle-complaint

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-handle-complaint/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `handle-complaint`
Skill — pulls context on an incoming customer complaint, drafts a
response, and suggests an operational fix, with an optional email or
ticket ID argument — already fully built; no SCRIPT.md existed on the
source, so source `beats[*].narration_text` served as the locked script;
the source's own `source_skill` path pointed at a different machine's
CoWork tree and was not readable locally, so no direct SKILL.md read was
possible or needed — the source beat_sheet.json's own narration_text and
quoted job description carried every fact used). Followed the
`knowledge-work-plugins--claude-liam-accessibility-review` sibling as the
structural precedent: identical source shape (7 beats: composer-ask cold
open + anatomy/pipeline + design-tell + verdict + your-turn + outro),
identical redo pattern (BrutalistHesitantWriter cold open, merged
design-tell+verdict beat, OutroSeries close), same Manim chip-row
scenes.py template copied verbatim for the GRAPHIC beats.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works (this one, handle-complaint, is a
single SKILL.md file, about two kilobytes); the SKILL.md is a
plain-language instruction set with no hidden logic underneath it, and
Claude reads the file then acts on what it says; the skill's job, quoted
from its own description field: pulls context on the complaint, drafts a
response, and suggests an operational fix, with an optional email or
ticket ID as input; once triggered, Claude executes the Steps section in
order, linear, no branching unless a step says so; and the concrete
distinction that follows from the job description's own verbs — pulls,
drafts, suggests, never sends or implements — same complaint, same kind of
draft and fix, every time, but the skill never sends the reply or makes
the fix itself, and anything outside the SKILL.md's spec is outside what
it does.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "send" → "draft" — the newcomer's
wrong guess that asking Claude to "handle" an incoming complaint means
Claude will send the reply itself, corrected toward the actual mechanism:
the skill's own job description says it drafts a response and suggests a
fix, never that it sends or implements anything). Register re-registered
Teardown→Plain: the source's B03 "here is the Teardown moment... what it
gets right / what it bites" framing and BVDT's four-line verdict artifact
were merged into a single NB03 beat and stripped of judgment language,
kept as the one fact a general audience needs and can act on
(repeatable draft-and-suggest / spec-only limit), per the NO JUDGMENT
register check. BVDT's separate bulleted artifact card was not kept as its
own beat, per CARRY-OUT LAW — its facts live in the single BCRY sentence
instead. NB02 additionally folded in the job-spec clause the source had
only quoted inline at B00 (now replaced), since B00 is no longer the
composer-ask beat that carried it. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03+BVDT compressed into the single NB03; BHTF
kept, with the source's garbled truncation artifact ("I want to handles an
incoming customer complaint end-to-end — pulls context, drafts a resp…")
rewritten to clean grammar ("I want to handle an incoming customer
complaint"), since the source text was a template-substitution artifact
cut off mid-sentence with a grammatical error, not a deliberately authored
prompt; BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-accessibility-review` sibling,
adapted with handle-complaint-specific labels. Learned from that sibling's
own BUILD-LOG note (a prior GATE T min-size FAIL from a too-long
multi-word chip label forced into a smaller font tier) and pre-emptively
kept every chip label at or under 14 characters where possible — except
NB02's original "drafts-and-suggests" (19 chars, fs=22 tier), which still
tripped GATE T on first pass (see below).

**B00 TIMING LAW.** Text: "How do I get Claude / to send a reply / to an
angry customer?" (57 chars, 3 lines) — under the family's established-safe
60-char config — rendered at the same known-good parameters (charMs=42,
mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%, jitter=26,
lead_silence_s=0.8). Narration measured 11.26s + 0.8s lead ≈ 12s window
(≥9s floor, comfortably). Verified by frame pull at 2fps: "send" sits
doomed in terracotta at t≈3s, replaced by "draft" in ink by t≈3.5s, and the
corrected question "How do I get Claude to draft a reply to an angry
customer?" is fully settled and legible from t≈9s through the clip's end
(actual_duration_s 11.27s, ≥8s requirement met).

**One real GRAPHIC-beat defect caught by GATE T, fixed before Gate V.**
First `type_check.py` pass on the compiled master was **FAIL, 1 defect**:
NB02's "drafts-and-suggests" chip (19 chars) fell into the `_chip()`
helper's fs=22 font tier, then triggered the width-constrained scale-down
path (`txt.width > w * 0.82`), landing its rendered text-run height at
18px — under the §8.1 floor of 20px (1.9% of 1080px logical) — where the
sibling reel's shorter chip labels (all ≤14 chars, fs=26 tier) had passed
clean. Root-caused to the longer label's width forcing a secondary
shrink past what the 22px tier alone would produce. Fixed by shortening
the label to "draft-suggest" (13 chars, fits the ≤14-char / fs=26 tier
with no scale-down needed) in both `scenes.py`'s `BEAT_CONTENT` and
`beat_sheet.json`'s NB02 `graphic.production_viz.chips`; deleted the stale
`manim/NB02.mp4` and re-rendered that beat alone via `render_scenes.py`
(skip-if-exists logic left NB01/NB03 untouched); recompiled
(`compile.py --force`); re-ran `type_check.py` on the full reel: **PASS, 0
FAILs** (NB02's smallest text-run now measures 21px, ≥ the 20px floor).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no re-generation needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, one pass for NB01/NB03, one targeted
re-render for NB02 per the fix above); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` — the first invocation was killed by the Bash tool's
own 120s default timeout partway through (B00 and BHTF not yet rendered,
BCRY/BOUT already completed in that window) rather than the harness
backgrounding anything; re-run to completion in the foreground with an
explicit 590s tool timeout, per the COMPLETION LAW's foreground-render
rule, confirming all 4 REMOTION beats present via ffprobe before
proceeding. Compiled twice (first cut, then the NB02 fix + recompile):

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-handle-complaint.mp4`, 7/7
beats filled real (no slate), 89.7s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: FAIL→PASS, 0 FAILs after the NB02 chip-label fix (see defect +
  fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 89.681s;
  mp4 mtime (1788492129) newer than beat_sheet.json mtime (1788492010)
- Gate V (visual): pulled frames every 8s across the full 89.7s runtime
  plus targeted checks of B00 (t≈3s "send" doomed in terracotta, t≈3.5s
  corrected to "draft", t≈9s+ fully settled and correct through the clip's
  end), NB01–NB03 (all chips legible, correctly spaced, single terracotta
  accent per beat, no collapsed-space defect), BCRY (carry-out sentence +
  sparkline "It drafts. You send." read clean), BHTF (correct topic/title/
  @HumanitariansAI handle, full paste-ready prompt legible; two-line topic
  wrap sits close to but does not overlap the title, consistent with the
  component's dynamic kicker-line spacing and GATE T's bbox-overlap PASS),
  and BOUT (single-line eyebrow "COMPLAINT · @HumanitariansAI" reads
  clean, correct title restate, crimson underline, no truncation). No
  blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 11.27s (≥8s requirement met); the
  "send" → "draft" correction lands on screen by t≈3.5s and the full
  corrected question stays legible from t≈9s through the remainder of the
  clip.

Metadata file written: `knowledge-work-plugins--claude-liam-handle-complaint.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly
to "Extending Claude — Skills, Plugins & Connectors" — consistent with the
`accessibility-review` sibling built in the same family. Direct code link
per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
