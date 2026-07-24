# PEDAGOGY.md — Session, Karaoke & Audiogram

Pedagogy audit against the SLATE-RUNNER checklist. Written before audio credits are spent.

## Act structure (required: hook → argument → reveal → how → close)

| Act | Beats | Present? |
|-----|-------|----------|
| Hook / cold open | B00 | ✓ — Byron reading over bare audiogram; "That's not a voice actor. That's a directed reading — and the direction is text." |
| Argument | B01–B03 | ✓ — [spoken word] era failure → session notes as the fix (style box + delivery tags + BREATH RULE) |
| Reveal / how | B04–B06 | ✓ — word clock: text already known → faster-whisper timing + SequenceMatcher → words.json |
| How (second tool) | B07–B09 | ✓ — audiogram: lyric-overlay decorates a finished video; waveform + karaoke in one command |
| Restraint / choice | B10 | ✓ — poem vs promo: burned-in words compete with listening vs. words ARE the visual |
| Close | B11 | ✓ — three tools, one sentence: session directs, karaoke clocks, audiogram makes sound visible |
| Outro / CTA | B99 | ✓ — brutalist.art · @HumanitariansAI |

Act structure: **PASS**

## Key-case cold open (must open on a problem or question, not a title card)

B00 opens on SOUND — the Byron reading is heard before any tool is named. The first statement
("That's not a voice actor") is an assertion that creates a question: then what is it? The
second sentence answers: "That's a directed reading — and the direction is text." The viewer
is immediately inside the mechanism before they know what the video teaches. **PASS**

## Gap-formula question beat (the question that creates the gap)

B00 ends on the implicit question the framing creates: how does text direct a reading? B01
opens the answer by showing what the old approach got wrong — establishing a gap between
"[spoken word] as a tag" and "[spoken word — delivery] as a direction." The viewer needs
to know what session notes are before they understand why they exist. **PASS**

## Utility-framing lint (every beat must be FOR the viewer, not about the tool)

- B00: shows the *result* before the explanation — viewer hears what a directed reading sounds like
- B01: explains WHY the old fix failed → viewer understands the failure mode they might hit
- B02–B03: shows HOW session notes are structured → viewer can author their own
- B04–B06: explains HOW align.py works → viewer can run it today
- B07–B09: explains HOW lyric-overlay adds the audiogram → viewer can run it on any finished video
- B10: names the choice the viewer will face on every surface → gives them the rule
- B11: summarizes the chain in one sentence → viewer leaves with a mental model

No beat is about the tool; every beat is about what the tool does for the viewer. **PASS**

## Vocabulary law (no jargon without a definition in the same beat or the prior beat)

- "session notes" — introduced in B00 narration as "the direction is text"; defined structurally
  in B02 (style box) and B03 (delivery tags) before the viewer needs to use the term
- "STYLE box" — shown as a literal paste in B02 with every field labeled
- "BREATH RULE" — named and explained in B02 narration; *why* (the slicer needs the cut)
  in the same sentence
- "align.py" — introduced with its purpose ("the word clock") before the command in B05
- "faster-whisper" and "SequenceMatcher" — B04 names them in context of their role; viewer
  doesn't need to know what they are, only what they do
- "words.json" — B05 narration names it as the output before B06 shows its contents
- "lyric overlay" — B07 introduces it as "decoration on a finished video" before B08 shows the command
- "audiogram" — appears in B00 as a visual that needs no definition; the word clock and overlay
  explain what makes it an audiogram

All new terms are visually anchored on first use. **PASS**

## Equation tangents (none — concept/workflow explainer, not a math video)

**N/A**

## Recap + chapter pointer (close must point toward next step or next video)

B11 delivers the sentence: "session directs the voice, karaoke clocks the words, audiogram makes
sound visible — the full chain is now yours." B99 points to the series and brutalist.art. **PASS**

## Length law (target ≤ 4:00 for an explainer intro)

13 beats × average ~14s = ~178s = 2:58. **PASS** (comfortably under 4:00)

## Narration script review (spot-check key beats)

- B00 "That's not a voice actor" — opens on the listener's state (hearing a reading), not a
  feature announcement. Hook works.
- B03 "This is the actual session that produced the She Walks in Beauty reading" — the worked
  example closes the loop between the heard reading (B00) and the tool on screen.
- B10 restraint beat — "You cannot be moved by verse and read it at the same time." Two sentences,
  one rule. The contrast (poem vs promo) is concrete enough to act on.
- B11 three-sentence close — symmetric with the three-tool arc. Clean landing.

No narration text flagged for revision. **PASS**

---

VERDICT: PASS
