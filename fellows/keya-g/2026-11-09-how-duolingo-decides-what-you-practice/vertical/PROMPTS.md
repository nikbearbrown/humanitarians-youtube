# PROMPTS — How Duolingo Decides What You Practice Next

**No open generation slots.** Three Remotion compositions (`ClaudeComposerAsk` twice, `BrutalistHesitantWriter`), two
more bookends (`ClaudeVerdictArtifact`, `LogoOutro`), and Manim scenes still to be written. No image model and no paid
API. Narration is generated locally with Kokoro voice `af_bella`.

## B01: the on-screen typed ask

> Explain how Duolingo decides which word I should practice next.

## B03: the hesitant writer

Typed first, in terracotta, then deleted:

> Reviews are random.

Replaced by:

> Duolingo predicts when you'll forget each word.

The typed corrected sentence is the same as the narration's second sentence; the wrong one is shortened so the correction
finishes typing before the 50% point of the beat (the writer cannot type faster than one frame per keystroke).
There is no lead silence on B03, matching the week 2 film.

## BHTF: Your Turn (typed on screen, and read aloud in the narration)

> Explain Duolingo's half-life regression using one word I'm learning. Show what its half-life means, and when I should
> practice it next. Use example numbers.

The spoken version adds: "And next time an old word comes back in a lesson, ask: was I just about to forget it?" That
sentence is in the narration only, not on screen, as in `SCRIPT.md`. "Use example numbers" is both spoken and on
screen. It tells the viewer that the half-life Claude gives is illustrative, since a learner's real per-word
half-lives are not public.

## Pronunciation (voice only; the on-screen text and the narration text are untouched)

Set in `metadata.pronounce`:

| Word | IPA | Notes |
|---|---|---|
| Keya | `kˈeɪjɛə` | "Kay-yeah" |
| shimasu | `ʃiːmˈɑːs` | Test clip option B: shee-MAHS, final u dropped. Used in B02 and BVDT. |
| mimasu | `miːmˈɑːs` | Test clip option B: meeh-MAHS, final u dropped. Used in B02 and BVDT. |
| Leitner | `lˈaɪtnɚ` | "LITE-ner". Used in B06 and B09. |

Regenerated for these changes: B02, B06, B07, B09, B10, BVDT and BHTF (B07, B09, B10 and BHTF for the new narration;
B02, B06, B09 and BVDT for the pronunciations). The other beats were left as they were.

The test clips from the earlier round are kept in `mp3/_pron-tests/` for reference. `mp3/` is not committed.

Still on Kokoro's default, in case you want them changed: Ebbinghaus (`ˈɛbɪŋhˌaʊs`, "EB-ing-house"; the German is
closer to "AY-bing-hows").
