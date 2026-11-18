# PROMPTS — How Google Docs Lets Two People Type in the Same Sentence

**No open generation slots.** Three Remotion compositions (`ClaudeComposerAsk` twice, `BrutalistHesitantWriter`), two
more bookends (`ClaudeVerdictArtifact`, `LogoOutro`), and Manim scenes still to be written. No image model and no paid
API. Narration is generated locally with Kokoro voice `af_bella`.

## B01: the on-screen typed ask

> Explain how Google Docs lets two people type in the same sentence.

## B03: the hesitant writer

Typed first, in terracotta, then deleted:

> The last person to type wins.

Replaced by:

> Every keystroke gets merged.

The on-screen lines are the ones in `SCRIPT.md`. They are set on short lines (landscape: "The last person / to type wins."
and "Every keystroke / gets merged."; portrait: three short lines each, at a larger size) so the whole correction finishes
typing before the 50% point of the beat. The writer cannot type faster than one frame per keystroke, so line count and
length are what keep it inside the time. There is no lead silence on B03, matching the week 5 film. The whole sentence is the trigger
phrase, so the correction replaces the sentence, not one word.

## BHTF: Your Turn (typed on screen, and read aloud in the narration)

> Explain operational transformation using the word 'cat', when one person inserts a letter and another deletes one at
> the same time.

The spoken version adds: "And next time you edit a shared document, ask: whose change just moved my text?" That sentence
is in the narration only, not on screen, as in `SCRIPT.md`. The narration says "the word cat" without the quote marks;
the on-screen prompt keeps them, as written in `SCRIPT.md`.

What a good answer should show, so you can judge what Claude gives back: the word is c, a, t. One person inserts a letter
(say an s at the start, giving "scat") while another deletes the t at position 3. Applied as sent, the delete would hit
the wrong letter (the "a"); transformed, it shifts by one place and removes the t, leaving "sca". If Claude's answer does
not shift the delete, it has missed the point of the beat.

## Pronunciation (voice only; the on-screen text and the narration text are untouched)

Set in `metadata.pronounce`:

| Word | IPA | Notes |
|---|---|---|
| Keya | `kˈeɪjɛə` | "Kay-yeah" |

Only Keya is set. Everything else is on Kokoro's defaults. Preview of what Kokoro will say, from the phonemizer, to check
by ear:

| Written | Kokoro's phonemes | Reads as |
|---|---|---|
| Control Z | `kəntɹˈoʊl zˈiː` | "control zee" (American). If you want "zed", it needs a respelling. |
| CRDTs | `sˌiːˌɑːɹdˌiːtˈiː` | "C-R-D-T", spelled out. The plural "s" looks dropped: it may sound like "CRDT". |
| operational transformation | `ˌɑːpɚɹˈeɪʃənəl tɹænsfɔːɹmˈeɪʃən` | Normal. |

"Luiz" is not in the narration (it appears only in the blog's example and in your notes), so there is nothing to set.

Not touched: anything beyond Keya. If "Control Z" or "CRDTs" sound wrong when you listen, say which and I will add a
pronunciation entry for it and regenerate only the beats that contain it (B02, B08 and BVDT for Control Z; B09 for
CRDTs).
