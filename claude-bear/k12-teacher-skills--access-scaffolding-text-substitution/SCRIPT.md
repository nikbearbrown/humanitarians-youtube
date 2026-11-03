# SCRIPT.md — Same Text, Better Scaffold (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `access-scaffolding-text-substitution` (an ELA differentiation
walkthrough of the k12-lesson-differentiation plugin's access-scaffold
design) — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop, no verdict); cold open replaced
with the BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
A student can't access the grade-level text, so the easy move is a simpler
version. But swap the words and you lock them out of the grade-level
conversation. Keep the same text, and scaffold instead.

*(Text typed on screen: "My readers / can't read this — / so give them / a
simpler version?" — trigger word "simpler" corrects to "scaffolded", landing
on: "My readers can't read this — so give them a scaffolded version?")*

## Body — same text, what scaffolds do, the crutch test, the fade

**NB01 — Same text, two entries** (source B01, the split-column figure)
Same passage, both columns — the First Amendment. One tier gets it bordered,
with a reading protocol: circle the main idea, underline the evidence, and a
two-word vocabulary gloss — amendment, ratified. The other tier gets the
identical words, clean, with one analytical question underneath. Same text.
Different entry structure.

**NB02 — What scaffolds do, and don't** (source B02)
Scaffolds break the reading into steps, pre-teach the two hardest words, and
cut how much a reader has to hold in mind at once. What they don't do is
lower the target — both tiers still read the same passage and build toward
the same argument.

**NB03 — Scaffold or crutch** (source B02a)
A scaffold and a crutch look the same from outside — both raise performance
while they're on. The difference shows on removal: a scaffold fades as
skill grows; a crutch performs the reading for the student. Take it away —
if comprehension collapses, it was never a scaffold.

**NB04 — The fading schedule** (source B02b)
The fade is what tells the two apart. Once a student can read the passage
with support, remove one scaffold at a time — the glossary first, then the
sentence starters — until the same text stands on its own. A scaffold that
never comes off isn't a bridge. It's a detour.

## Close

**BCRY — carry-out**
An easier book swaps out the grade-level goal. The same text, scaffolded —
and later unscaffolded — keeps it.

**BHTF — your turn**
Your turn. Take a passage from your next lesson. Paste it into Claude and
ask for a scaffolded version for your below-level readers — a reading
protocol, a two-word vocabulary gloss, one anchor question — with the
passage's words left untouched. Then check both versions side by side: are
the words identical? If Claude changed or shortened the text, push back and
ask again.

**BOUT — outro**
Same Text, Better Scaffold. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is the standard differentiation move — a struggling reader gets an easier book |
| Wrong guess | B00 (WRITER LAW) | "simpler" corrected to "scaffolded" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source's B00 narration already stated the same trap in prose, so no separate wrong-guess beat is invented (beat-count discipline, below) |
| Mechanism | NB01–NB02 | the split-column same-text figure, then the concrete list of what scaffolds add and what they explicitly don't touch (the grade-level target) |
| Anchor | the First Amendment passage, named at NB01 and referenced through NB02–NB04 as "the same passage" | source is one worked example throughout, not a planted/paid-off separate case — nothing to return to that hasn't stayed on screen |
| Both directions | NB03 + NB04 | NB03 states the failure mode in one direction (comprehension collapses on removal → it was a crutch, not a scaffold); NB04 states the other (a scaffold that never comes off never becomes unnecessary — it's a permanent detour, not a bridge) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of the
source plugin's access-scaffold design (the split-column structure, what a
reading protocol and vocabulary gloss do, the scaffold/crutch removal test,
and the fading schedule) — not an inference about hidden mechanism. Per
simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 8 filled beats: B00 (composer-ask cold open) + B01/B02/B02a/B02b
(four body beats) + B03 (Claude-prompt verdict artifact) + B04 (handoff) +
B05 (outro) — BVDT/BHTF/BOUT in the source sheet are unfilled SLATE
placeholders, not part of the actual 8-beat build (metadata `"filled": 8,
"of": 8"`). This redo keeps the same shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW);
B01→NB01, B02→NB02, B02a→NB03, B02b→NB04 kept as one beat each; B03's
Claude-prompt suggestion ("give it the passage and tier description, ask for
the scaffold layer separately") is folded into BHTF's paste-ready prompt
rather than kept as a separate verdict-artifact beat, since B04 already
carried a viewer-facing version of the same prompt — keeping both would
repeat the same instruction twice, which CARRY-OUT LAW and the your-turn
handoff both treat as one slot, not two; B04 kept as BHTF, with its
paste-ready prompt carried over (trimmed to the do-not-change-the-words
constraint, which is the one instruction that matters for the redo's
narrower scope); B05 kept as BOUT, re-skinned to the Humanitarians AI outro.
Total: B00 + NB01–NB04 + BCRY + BHTF + BOUT = 8 beats, matching the source's
8 filled beats exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`K12Fig03TextScaffold` / `ClaudeWindow` / `K12Fig09ScaffoldVsCrutch` /
`K12Fig10FadingSchedule` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`).
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's mandated
cold-open swap; the source's original Remotion figures (`K12Fig03...`,
`K12Fig09...`, `K12Fig10...`) are not registered in this toolkit's scene
library, so NB01–NB04 are built fresh as GRAPHIC (Manim) beats carrying the
same teaching point instead of re-slating the source's bespoke components.
