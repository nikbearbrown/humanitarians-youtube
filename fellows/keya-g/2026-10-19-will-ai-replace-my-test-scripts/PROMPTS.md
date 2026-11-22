# PROMPTS — Will AI Replace My Test Scripts?

**No open generation slots.** Three Remotion compositions (`ClaudeComposerAsk` twice, `BrutalistHesitantWriter`), two more
bookends (`ClaudeVerdictArtifact`, `LogoOutro`), and nine Manim scenes still to be written. No image model and no paid
API. Narration is generated locally with Kokoro voice `af_bella`.

## B01: the on-screen typed ask

> Will AI replace my test scripts?

Result lines: "A script looks for an ID" · "An AI agent looks for the picture" · "Who decides what correct means?"

## B03: the hesitant writer

Typed first, in terracotta, then deleted:

> AI will replace testers.

Replaced by:

> AI will change what testers spend their time on.

## BHTF: Your Turn (typed on screen, and read aloud in the narration)

> Here's a Selenium test with a fragile locator. Suggest a more stable one, and explain what a self-healing tool and an AI testing agent would each do if it broke, using closing a popup as the example.

The spoken version adds: "And next time a test fails, ask: did the app break, or did the page just change?" That
sentence is in the narration only, not on screen, as in `SCRIPT.md`.

## Pronunciation (voice only; the on-screen text and the narration text are untouched)

Set in `metadata.pronounce`, as Keya specified:

| Word | IPA | Note |
|---|---|---|
| Keya | `kˈeɪjɛə` | "Kay-yeah". Without it the voice says "KEE-uh". |

Checked, **not** overridden (the narration used the engine's default for these four):

| Word | Engine phonemes | Reads as | Verdict |
|---|---|---|---|
| Selenium | `sɛlˈiːniəm` | seh-LEE-nee-um | Standard pronunciation. |
| JUnit | `dʒˈeɪ jˈuːnɪt` | JAY-YOO-nit | Standard ("J-Unit"). |
| Healenium | `hiːlˈiːniəm` | hee-LEE-nee-um | Keya's note listed both hee-LEE-nee-um and HEE-lee-nee-um; the engine default (the first) is used, with no override. For the second, add `"Healenium": "hˈiːliːniəm"` to `metadata.pronounce` and regenerate B07. |
| RPA | `ˌɑːɹpˌiːˈeɪ` | R-P-A, letter by letter | Standard. |

Listen clips are kept outside this folder (in the session scratchpad) because they are scratch:

- the four words in their own script sentences: `pron/mp3/beat-P1.mp3` to `beat-P4.mp3`
- the alternative Healenium sentence: `pron_alt/mp3/beat-PALT.mp3`

To change a word, add it to `metadata.pronounce` in `beat_sheet.json` and regenerate the beats that contain it.
