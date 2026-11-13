# PEDAGOGY — "The STAR Method Banking Panels Actually Score" (deep-explainer)

**Prepared by:** Claude (agent) · **Date:** 2026-08-10
**Skill:** `deep-explainer` (`skills/make/deep-explainer/SKILL.md`)

This is **GATE P** — the quality gate `generate_audio_kokoro.py` checks before narration is
generated. Per P1, an agent never signs its own gate. `VERDICT` stays `PENDING` until you sign it.

## Register check (Pragmatist)

Narration throughout is dry and practical — states the framework, states what changed for banking,
walks the worked examples, states the lesson. No persona name is used anywhere (compliance
requirement); `af_bella`'s usual "Pragmatist" register is kept as a narration *style* only,
independent of the "hai"/"Humanitarians AI" identity that register is normally paired with.
**CHECK: satisfied.**

## Spine check (deep-explainer)

Required spine: `B00` cold open → ACT I-IV documentary body → `VERDICT` recap → `YOUR TURN` handoff
→ `OUTRO`. **CHECK: satisfied** — see `beat_sheet.json`, 22 beats, exact spine present.

- **Beat-mix contract**: MANIM 38.9% (7/18 body beats), REMOTION 38.9% (7/18), CARD 22.2% (4/18),
  VOX 0% — within the MANIM 25-40% / REMOTION 30-45% bands. **CHECK: satisfied** (see Deviation
  logged below for VOX).
- **Max 2 consecutive same-lane beats**: verified against the full sequence in `SHOTLIST.md`'s
  Rhythm check — no run exceeds 2. **CHECK: satisfied.**
- **HANDOFF LAW**: `B_YOURTURN`'s narration reads the suggested prompt's intent aloud ("draft one
  STAR story... don't stop at 'and I fixed it'... name exactly who you told") rather than only
  displaying it. **CHECK: satisfied.**
- **SHOW-DON'T-TELL LAW**: every beat carries a `shot.show[]` array in `beat_sheet.json` naming
  what happens on screen and when. **CHECK: satisfied.**
- **Gate D1** (first compile is always a full-length slate previz): this is `run.sh`'s existing
  `-slate.mp4` step, no special action needed. **N/A until render gate.**
- **Gate D2** (`SHOPPING.md` post-audio-lock): not applicable — VOX is 0%, no pantry assets to shop
  for. **N/A.**

## Content fidelity

All 14 claims in `FACTCHECK.md`'s claim trace are CONFIRMED against the book's own text. Nothing
was invented — every quote, score, and worked example in this video is drawn directly from Chapters
12 and 14 (see `FACTCHECK.md`'s "What was NOT invented" section). The book's own hedge — that the
banking-specific competency layer is its own pedagogical synthesis, not a published rubric — is
preserved in the narration (B05), not flattened into an attributed-standard claim.

## Deviation logged

**VOX = 0%**, disclosed in `VISUAL-PLAN.md`'s "Lane-mix decision" section — a framework/mock-
interview topic has no archival-photo referent, identical justification to the reference project's
own VOX=0% deviation on a similarly conceptual topic.

**Palette split** (claude bookends / humanitarians body), disclosed in `VISUAL-PLAN.md`'s
"Component note" section — a structural property of the shared Remotion components used, not
persona branding; the human explicitly reviewed and accepted this trade-off before `beat_sheet.json`
was written (see session record: "Accept it (Recommended)" chosen over building custom Manim
replacements for the three affected components).

## Outstanding for human review

- [x] Read all 22 narration blocks in `NARRATION-SCRIPT.md` and confirm the Pragmatist register
      reads right to you.
- [x] Confirm the VOX=0% and palette-split deviations (both disclosed above) are acceptable as
      documented, not something you want re-litigated at this gate.
- [x] Confirm the 11 Manim scenes (already smoke-tested and visually verified — see build notes)
      match your expectations for the STAR framework, competencies, worked example, and Daniel's
      mock-loop visuals.
- [x] Confirm the 4K (3840×2160) render target is acceptable given the render time it implies.

## VERDICT: PASS

Signed: Supriya Kushwaha (human, author)
Date: 2026-08-10
Evidence: Reviewed PLAN.md, beat_sheet.json, scenes.py, and this paperwork set in-session;
approved narration, the STAR-framework/competency/worked-example/mock-loop visuals, the VOX=0%
and palette-split deviations, and the 4K render target as-is. Verdict communicated directly to the
agent in-session ("Approved, proceed to the render gate"); transcribed here per that instruction.
