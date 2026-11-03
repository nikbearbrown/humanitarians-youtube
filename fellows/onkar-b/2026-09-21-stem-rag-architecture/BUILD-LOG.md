# BUILD-LOG.md — hai-liam-rag-triangle ("Claude, Retrieved.")

Built with `ai-explainer` on the `claude-hai` channel (Liam's voice, Kokoro
`am_onyx`, @HumanitariansAI chip). Free path end to end: **$0.00**, no API key,
no Higgsfield, no paid call at any step.

Source: the author's own Week 3 STEM script (5 scenes, 2:45 target, dual render).

---

## Deviations from the supplied script — each one deliberate

**1. B00 no longer says "I am Onkar Bhujbal, a software engineer."**
The narrator is Liam (Kokoro `am_onyx`). The ai-explainer named-voice rule is
explicit that the substitute narrator "does not imitate … or claim to be him",
so a synthetic voice asserting first-person authorship of a real named person
is a violation, not a style choice. Rewritten to: *"This is Liam, narrating for
Onkar Bhujbal, a software engineer."* The script's own sign-off — "Liam, for
Onkar Bhujbal and Humanitarians AI" — already established exactly this
relationship, so the fix makes the open agree with the close.

**2. Five scenes became ten beats.**
The script's five scenes are all present and in order. Doctrine requires four
bookends the script did not have, so they were added around it:

| Script scene | Beat(s) |
|---|---|
| S1 HOOK | B00 (cold open, `ClaudeComposerAsk` — COLD OPEN LAW) |
| *(added)* | B01 executive summary, `BrutalistHesitantWriter` — EXECUTIVE-SUMMARY LAW |
| S2 THE FRAMEWORK | B02 (`RagTriangle`) |
| *(added)* | B02B the mechanism, `RagEmbeddingSpace` — see deviation 3 |
| *(added)* | B03 the ask half of an ask→result pair — ASK→RESULT LAW |
| S3 WORKED EXAMPLE | B04 (`RagPromptCompare`) |
| S4 FALSIFIABILITY | B05 (`RagTriangle`, poisoned) |
| *(added)* | B06 verdict artifact page |
| S5 SCAFFOLDED TASK | B07 (handoff, HANDOFF LAW — prompt read aloud verbatim then discussed) |
| S5 CLOSE | B08 (`HaiTitleOutro`, title restate — OUTRO LAW) |

**3. The runtime gap was closed with content, not with padding.**
First audio pass measured **2:16** against a 2:45 target. Per duration-planner
("duration is an output of the content, never a target") the fix is more
content or none — never a stretched hold. Two additions:

- **B02B, a new mechanism beat (20.6s).** The script said "run a vector search"
  and never said what the vector was — a real gap for a student audience, and
  the exact setup B05's context-poisoning beat needs ("closest is not correct").
- **B07 gained a closing move (+7.7s):** change one word of the context and
  re-run, so the viewer sees the answer track their text rather than the world.
  Bookends are exempt from the 45–70-word body budget, so this lands in the
  beat that can carry it.

Final measured runtime: **2:44.1**.

**4. Outro is `HaiTitleOutro`, not `ClaudeTitleOutro`.**
OUTRO-LOCK.md scopes `ClaudeTitleOutro` to claude-liam/@NikBearBrown reels and
**hardcodes** `@NikBearBrown` as a constant with no prop override. This reel
signs off for Humanitarians AI, so using it would have stamped the wrong
channel on the last frame. `HaiTitleOutro` (props: title, handle, subline,
logoFile) is the correct card and carries the HAI mark full-size per LOGO LAW.

**5. Register is plain-direct, not full Teardown.**
The `claude-hai` channel's register is Plain, the audience is students, and the
supplied script is plain-direct. Teardown survives where it belongs — in the
judgment lines of B05 ("the failure is upstream of the model, which is exactly
where nobody is looking") and the B06 verdict.

**6. ASK→RESULT applied once, not per illustration beat.**
Read literally, ASK→RESULT LAW would put a composer micro-beat in front of
every generated graphic — which collides with ILLUSTRATE LAW's anti-wallpaper
rule (the UI appears only where the UI is the subject) and would spend ~40s of
a 2:45 reel on interface. One pair (B03 → B04) carries the signature move at
the reel's most load-bearing exhibit. Logged here rather than silently decided.

**7. B01's correction is a single-word swap, because a phrase cannot work.**
`ai-explainer` SKILL.md (EXECUTIVE-SUMMARY LAW) instructs: "when the
misconception lives in a phrase, put the whole phrase in `triggerWords`." The
shipped component cannot do that. `BrutalistHesitantWriter.tsx` tokenises with
`text.split(/(\s+)/)` and matches `triggers.indexOf(core.toLowerCase())` on a
single token, so a multi-word trigger never fires — it renders as ordinary
text and **no correction happens at all**, which is silently the exact defect
the law exists to prevent.

Caught by frame-level QC before the compile: the first render of B01 typed
"RAG trains the model on your private files." and never corrected it. Reworked
to a single-word trigger whose corrected sentence still stands alone as the
reel's claim:

```
typed:     RAG memorizes your private files. / Only as good as the search.
trigger:   memorizes  →  quotes
corrected: RAG quotes your private files.    / Only as good as the search.
```

"memorizes" is the reel's actual misconception (B04's narration dismantles it
in as many words: "it never memorized your number"), so the swap is the
pedagogy, not a synonym change. This is a toolkit doc/code mismatch worth
fixing upstream — either the matcher should support phrases or the SKILL.md
instruction should be corrected.

**8. Two timing defects found by frame-level QC, both fixed at the root.**

- *B01 — the correction was cut off.* `BrutalistHesitantWriter` is registered
  at 606 frames (20.2s) and types at a fixed rate, but the beat's audio is
  10.58s, and `remotion_scenes.py` conforms with ffmpeg `tpad -t`, which
  **trims** anything longer. Half the performance was being discarded. Fixed by
  speeding the writer (`charMs` 42 → 13, fewer hesitations) and shortening
  line 2, then verifying with single-frame `remotion still` renders at frames
  150/250 before committing to a video render: the corrected claim is fully on
  screen by 8.3s, holding 2.2s before the cut.
- *B02 / B05 / B04 — the stamp and spark line were cut off.* Same trim, my own
  components' fault: I registered them longer than their beats (750 frames for
  a 20.76s beat), so every reveal after `beat ÷ registered` was discarded — the
  claim stamp (0.76) and spark line (0.84) never appeared. Fixed by registering
  each pattern **just under** the shortest beat that uses it (RagTriangle 620,
  RagPromptCompare 560, RagEmbeddingSpace 610), so the conform freeze-holds a
  fraction of a second instead of trimming content. Rationale is commented in
  `Root.tsx` beside the compositions.

---

## GATE L — two punts, both built (never slated)

`./art scenes` found no parameterized component for a three-stage triangle, for
a same-question-twice prompt comparison, or for an embedding field — only
leads whose content is hardcoded to other films. Per GATE L a miss is a design
card, so three components were authored, each registering a 16:9 **and** a
`916` id from one file (dual-aspect law):

| Component | Ids | Reusable for |
|---|---|---|
| `RagTriangle` | `RagTriangle`, `RagTriangle916` | any three-stage loop with a fragile middle stage; `poisoned` prop breaks it in place |
| `RagPromptCompare` | `RagPromptCompare`, `RagPromptCompare916` | any "same input, different context" comparison |
| `RagEmbeddingSpace` | `RagEmbeddingSpace`, `RagEmbeddingSpace916` | embedding/nearest-neighbour retrieval, semantic ranking |

`HaiTitleOutro916` was also registered: it did not exist, which meant a
vertical cut of **any** @HumanitariansAI reel was previously blocked at the
outro (RENDER-TARGETS.md §3 blocks rather than centre-cutting).

Verification: `tsc --noEmit` → **0 errors** (the tree's 0-error state is
preserved, per PORT-LOG.md). `./art scene-index` → **613 → 620** renderable
compositions.

## Build record

| Step | Result |
|---|---|
| Beat sheet authored, SHOW blocks first | 10 beats, 0 slates, 0 human slots |
| CHECKS-REPORT.md written before first compile | 10 SHOW / 0 HOLD / 0 PUNT |
| Kokoro audio (`am_onyx`) | 10/10 beats, **164.1s**, $0.00 |
| Remotion 4K (`--scale=2`, PNG frames, crf 16) | see `beat_sheet.json` → `shot.remotion.rendered` |
| Visual QC (frame-level, 9-point rubric) | `_qc/REPORT.md` |
| Review cut | `hai-liam-rag-triangle-slate.mp4` |
| Clean master | `./art final` → 4K landscape |
| Vertical companion | `./art vertical` → `vertical/` |

Nothing was published. The masters stay in this folder for human review.
