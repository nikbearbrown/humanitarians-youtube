# Beat Sheet (APPROVED — Gate P, 2026-08-31): "Embeddings: How AI Tells Similar From Different (When Keyword Matching Can't)"

**Creator:** Sai Pranavi Jeedigunta | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly work report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as
`2026-08-30-what-prompt-injection-actually-looks-like/`, which scored 11/12 against `PROOF.md`)
**Phase:** 2 — approved for narration lock / audio generation. Both FACTCHECK items resolved
2026-08-31: kept fully generic (no acknowledgment line about the fellow's own recent work); B05's
example swapped from a real-sounding SEC rule-number format to a fully fictional placeholder
("Section 4.12"/"Section 4.13"). See `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question rubric — "Does it vary in wording? / Does context
flip the meaning? / Is exactness actually the point?" — for deciding whether a rule should match
on exact keywords or on semantic similarity (embeddings). Teaches the framework before any
example, walks it through a worked example (a generic classifier that misses "adviser" when it's
only looking for "investment adviser"), stress-tests it against a case where exact match is
actually correct (matching a specific regulation number or ID), and closes on a concrete audit
task.

**Why this topic, and why now:** this fellow's own last two weekly-work reports were both,
underneath, keyword/exact-match rules breaking in different ways — one checked for text patterns
that structurally couldn't appear in the data at all, another re-derived a rule instead of reading
a value directly, and a third (this week's) missed synonyms a title used instead of the exact
phrase the rule expected. This video is deliberately generic and topic-level — not a report of any
of those specific fixes — but explains the general pattern underneath all of them: brittle
exact-match rules break wherever real-world text varies more than the rule anticipated, and the
fix for THAT class of problem is measuring similarity of meaning (embeddings) rather than adding
an ever-growing list of exact keywords.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or describe any specific real bug from her own codebase — the worked example is
generic and hypothetical, matching the pattern used in the 2026-08-17 and 2026-08-30 STEM videos.

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Framework | All 3 questions shown together as a rubric, before any example | Framework-first, per the pattern that scored well on prior STEM videos |
| B04 Worked example | The keyword rule, the missed input, and the embedding-similarity comparison all shown together | Not narration-only — the actual "close in meaning space" idea must be visualized, not just asserted |
| B05 Falsifiability | The exact-match-is-correct counter-example (matching a specific ID/code), legible, visibly different resolution from B04 | Side-by-side or sequential-but-both-legible comparison to B04 |
| B06 Task | The 3 questions restated as an audit checklist | Actionable, distinct from B03's framework card |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi Jeedigunta |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Embeddings: How AI Tells Similar From Different (When Keyword Matching
Can't)" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi Jeedigunta. This video is about why keyword-matching rules quietly break
over time — and what embeddings actually do differently, so you know when you need them and when
you don't."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:35)**
VO: "Picture a rule that flags any document mentioning 'investment adviser.' It works great, until
someone writes 'RIA' — the industry's own acronym for the exact same thing — and the rule doesn't
know what that means. Nothing crashed. It just quietly stopped working for that one document."
Visual: a document titled with "RIA" sliding past a rule box checking for the literal phrase
"investment adviser," unflagged.

**B03. Framework (~0:35–0:58)**
VO: "Here's the check, before any example: three questions. One — does the wording actually vary
in the real world, or is there only one way to say this? Two — does context change what a phrase
means, so a fixed keyword could be right in one place and wrong in another? Three — is exactness
itself the point, like matching a specific ID or code, where a close-but-different match would
actually be wrong?"
Visual: rubric card, all 3 questions shown together (Wording Varies / Context Flips Meaning /
Exactness Is The Point).

**B04. Worked example (~0:58–1:25)**
VO: "Back to that adviser rule. Wording varies constantly — 'adviser,' 'advisor,' 'RIA' all mean
the same role. An embedding doesn't check for an exact phrase. It measures how close two pieces of
text are in meaning. 'RIA' and 'investment adviser' land close together in that space, even though
they don't share a single letter in common. A rule built on that closeness catches both — and
catches the next synonym nobody thought to add, too."
Visual: a simplified 'meaning space' diagram — "RIA," "investment adviser," and "advisor" plotted
close together; an unrelated term (e.g. "quarterly earnings") plotted far away.

**B05. Falsifiability case (~1:25–1:48)**
VO: "Now the case that would break this if applied everywhere. A rule that matches a specific
regulation number — say, 'Section 4.12' — should NOT use closeness of meaning. 'Section 4.12' and
'Section 4.13' might land close together in meaning space, because they're both provisions about
similar topics. But they are different rules with different requirements. Here, exactness is the
whole point. An embedding would blur exactly the distinction you need to keep."
Visual: "Section 4.12" and "Section 4.13" (fully fictional placeholder rule numbers — not real
citations) plotted CLOSE together in the same meaning-space diagram from B04, with a warning
marker — visually distinct treatment from B04's "close together = good" framing.
*[Stress-tests the rubric — the same closeness that helps in B04 actively hurts here. Fictional
rule numbers used deliberately to avoid any reader assuming a real regulation is being cited —
see FACTCHECK.md.]*

**B06. Scaffolded task (~1:48–2:08)**
VO: "Here's something to check today. Find one keyword-matching rule you rely on. Ask the three
questions: does the wording actually vary, does context change the meaning, and is exactness the
whole point. If the first two are yes and the third is no, that's a rule worth moving to
similarity matching before the next synonym quietly slips past it."
Visual: the 3 questions restated as a checklist card.

**B07. Takeaway (~2:08–2:22)**
VO: "A keyword list only knows the words you thought of. Embeddings measure the meaning you
didn't have to spell out — but only where closeness is actually what you want."
Visual: statement card.

**B08. Sign-off (~2:22–2:27)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi Jeedigunta.

---

## Production Gate Self-Check (pre-review)

- [x] Framework (B03) shown fully, before any example
- [x] B04's meaning-space visualization is legible, not narration-only
- [x] Falsifiability case (B05) uses a genuinely similar-looking scenario, not a strawman, and
      shows a visibly different resolution from B04 (gold/crimson warning treatment vs. B04's teal)
- [x] Scaffolded task (B06) is a concrete action, not a restatement of B03 (checkbox checklist,
      distinct visual shape from B03's numbered rubric badges)
- [x] Silent title card present; brand/fellow sign-off card present
- [x] Worked examples are clearly generic/illustrative, not attributed to the fellow's own
      real codebase — see FACTCHECK.md

**Actual runtime:** 143.819s (2:23.8), measured from the true 4K master — 9 beats, Kokoro
`af_bella` audio-first, all `actual_duration_s` locked in `beat_sheet.json`.

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-08-31. Both FACTCHECK open items
resolved (see `FACTCHECK.md`). Cleared to generate Kokoro audio and proceed to previz.

---

## Production complete — 2026-09-07

- Audio locked: Kokoro `af_bella`, all 9 beats + a real silent B00 track (ffmpeg `anullsrc`).
- `scenes.py` authored (9 Manim classes matching this beat sheet's `shot.manim.scene` names
  exactly); GATE A (static pre-flight) and GATE W (WCAG margin check) clean on all 9 before
  every render pass.
- **16:9 master**: `Embeddings_SaiPranaviJeedigunta_20260907_16x9.mp4` — 3840x2160 @24fps,
  143.819s. GATE V (frame QC) on the true clean master: 0 BLOCKER, 165 MAJOR (cosmetic-only,
  reviewed by eye via `_qc/contact_sheet_4k_16x9.png`).
- **9:16 short**: `Embeddings_SaiPranaviJeedigunta_20260907_9x16.mp4` — 1080x1920 @24fps,
  148.36s. Full reformat (parent is under the 180s Shorts cap, no beats dropped); every beat
  hand-redesigned for portrait in `short/scenes.py` — B04/B05's meaning-space diagrams rebuilt
  as tall/narrow vertical scatters. GATE V: 0 BLOCKER, 98 MAJOR (cosmetic-only, reviewed by eye
  via `_qc/contact_sheet_9x16.png`).
- See `BUILD-LOG.md` for the full dated build record and `PEDAGOGY.md` for the self-assessment
  against `PROOF.md`.
- Publishing: **NOT AUTHORIZED** (no publish step was run; nothing has been uploaded).
