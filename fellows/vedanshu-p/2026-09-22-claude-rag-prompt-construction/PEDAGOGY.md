# PEDAGOGY — Labels Are Not Decoration. (personal-author ai-explainer)

Concept explainer of *RAG Foundations*, Chapter 8 ("Prompt Construction and
Context Injection"). Built with the **`ai-explainer`** skill — the Claude cut.

**Tier note.** `ai-explainer` is FELLOW TIER — free and safe by default. This
build runs entirely on the free path (Kokoro `am_onyx`, Remotion), spends
**$0.00**, calls no paid API and makes no network request.

Personal author channel: persona and sign-off are the book's author, Vedanshu
Daxesh Patel (`@VedanshuDaxeshPatel`). IN-FOR-BEAR LAW does not apply — the
narrator is named as themself in B00 and signs off as themself in BOUT.
Never publishes.

**Book root.** Built into `D:\ai1-cli-main\youtube\` per CLAUDE.md rule 3.
Folder dated **2026-09-22** per explicit instruction.

**Siblings.** The second ai-explainer in this series after the Ch. 4 chunking
reel, and it follows that reel's spine exactly. Shares chrome (`EmbedChrome`)
and beat clock (`ChunkChrome`) with Chapters 3–7, so the whole set cuts together.

## The ONE idea

> The augment stage is an assembly, not a concatenation — labelling, placement
> and one grounding instruction change what the model does with what you
> retrieved. And none of it buys a guarantee.

## Why this chapter suits a concept explainer, not a CLI demo

Chapter 8 is the first chapter in a while whose subject is a *judgment* rather
than a mechanism. There is no algorithm to implement and no measurement to take
— the claims are about layout, ordering and instruction-following, and two of
the three rest on documented guidance rather than on something this reel could
run and verify.

Running a demo here would have been worse than not running one. A single
hand-built prompt comparison proves nothing about prompt structure in general,
and dressing it up as a result would misrepresent the evidence the chapter
actually has. So the reel illustrates the anatomy, reports the one solid
research finding honestly, and is explicit about where the guidance stops being
settled.

## Act structure (the ai-explainer spine)

- **B00 INTRO** — `ClaudeComposerAsk`, ask shown answered (COLD OPEN LAW).
- **B01 BLUF** — `BrutalistHesitantWriter` (EXECUTIVE-SUMMARY LAW). The writer
  types the misconception the chapter names — that assembling a prompt is
  "concatenate a few strings together" — and corrects the whole phrase.
- **B02 ANATOMY** — the chapter's Fig. 01, rebuilt: same content, two layouts.
- **B03 POSITION** — Lost in the Middle. The one peer-reviewed finding.
- **B04 FALSIFIABILITY** — the two evidence tiers, drawn unequal.
- **B05 GROUNDING** — the instruction, and the drift it does not stop.
- **B06 PREDICT** — `ProblemPredictCard`, the gap held open.
- **B07 REVEAL** — the chapter's Fig. 02, rebuilt, with the resolution added.
- **BVDT VERDICT** — `ClaudeVerdictArtifact`, six lines ending on the honest one.
- **BHTF NEXT STEPS** — `ClaudeComposerAsk`, `"Your turn."` (HANDOFF LAW).
- **BOUT OUTRO** — `TitleOutroChannel`, exact title restate, signature.

ILLUSTRATE LAW: the Claude UI appears only at B00, BVDT and BHTF. Every inner
beat illustrates its concept instead — no composer wallpaper.

## Friction protected

- **Kept: the ordering rule is not settled, and the reel says so at length.**
  B04 is a whole beat spent on the distinction between a peer-reviewed finding
  and one vendor's internal testing. This is the chapter's most unusual move and
  the easiest thing to sand off; it is instead the reel's falsifiability beat.
- **Kept: grounding instructions do not work reliably.** B05 and the verdict
  both carry it. A reel that explained prompt structure and implied it solves
  faithfulness would be teaching the opposite of the chapter.
- **Kept: the deceptive shape of the drift.** The ungrounded sentence is drawn
  as confidently as the grounded one, because that is what makes the failure
  survive review. Flagging it visually would have been easier and wrong.
- **Kept: no numbers on the position figure.** The chapter reports a direction;
  the figure draws a direction.
- **Dropped: a live demo.** See above — one hand-built comparison would be
  anecdote dressed as evidence.
- **Dropped: XML-tag syntax specifics.** The chapter references the technique
  and its source; the reel teaches the *principle* (labelled, separated, tagged)
  rather than one vendor's markup, which would date the video.
- **Dropped: RAGAS.** In the chapter's reference list but not load-bearing for
  any claim this reel makes.

## Evidence discipline (DOUBLE-CHECK LAW) — full detail in SOURCES.md

Every on-screen claim carries its citation, and the two tiers of evidence are
kept visually distinct rather than flattened. The chapter's own fact-check
record (`.verified.json`: verified, GATE 4, 0 discrepancies) is logged.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01/B02 before the worked case at B06)
- WORKED EXAMPLE ✓ (the chapter's own resignation question)
- FALSIFIABILITY ✓ (B04)
- SCAFFOLDED VIEWER TASK ✓ (BHTF — print the prompt your system actually sends)
- FOUR BOOKENDS ✓
- NO-SOURCE-NO-VERDICT ✓

Full classification in CHECKS-REPORT.md: 10 SHOW / 1 justified-HOLD / 0 PUNT.

## VERDICT: PASS

Beat sheet reviewed against the chapter before audio. Proceeding to Kokoro audio
→ Remotion render → compile at 4K → frame-level visual QC.
