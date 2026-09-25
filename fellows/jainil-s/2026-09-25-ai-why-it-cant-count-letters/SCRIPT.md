# SCRIPT — Why It Can't Count Letters

**Slug:** `ai-why-it-cant-count-letters` · **Voice:** Kokoro `am_onyx` · **Register:** Teardown · **Handle:** @HumanitariansAI

**Beats:** 9 · **Runtime:** 2:20.0 (measured from the generated narration — the master clock)

Narration as delivered. Durations are set by Kokoro at generation time;
the visuals conform to them, never the other way round.

---

## B00 · ASK — `ClaudeComposerAsk`  (12.69s)

Ciao. This is Liam, in for Bear. Ask a language model how many r's are in strawberry and it will often get it wrong. People treat that as proof the thing is stupid. It isn't. It is proof that the model never saw the letters at all.

## B01 · BLUF — `BrutalistHesitantWriter`  (16.47s) · `qc.sparse`

Here is the whole video in one correction. We assume the model reads text the way we do, one character after another. It does not. Text is chopped into chunks called tokens before the model ever sees it, and those chunks are not letters. Once you know that, a whole family of strange failures stops being strange.

## B02 · HERO — `TokenSplit`  (17.62s) · `qc.sparse`

So here is the actual split. I ran the word through a real tokenizer, and strawberry comes back as three pieces: s t, r a w, and b e r r y. Look at what that means. Not one of those pieces is a letter. The three r's you are asking it to count are buried inside two chunks, and the model has no view inside a chunk.

## B03 · TURN — `TokenSplit`  (13.53s) · `qc.sparse`

And it gets stranger. Put a single space in front of the same word and it stops being three tokens and becomes one. Same letters, same order, completely different input. The model is not being careless here. It genuinely received something different.

## B04 · EVIDENCE — `FormACard`  (31.33s) · `qc.sparse`

This is not a quirk of one word either. Raspberry splits after a single r. Blueberry splits cleanly in the middle. And digits group into arbitrary lumps, which is exactly why arithmetic on long numbers goes wrong in ways that look random. Every one of these is real output you can reproduce. And there is a reason behind the apparent randomness: the vocabulary is learned from how often sequences appear in text. Common ones earn a single token. Rarer ones get shattered into pieces. Blueberry survives intact because those halves are common words; strawberry does not.

## B05 · LAND — `WantQuote`  (11.29s) · `qc.sparse`

So the model is not bad at spelling. It is working with a vocabulary of about fifty thousand chunks instead of twenty-six letters, and counting letters means reaching inside a chunk it cannot open.

## B06 · FIX — `FormACard`  (21.06s) · `qc.sparse`

Which tells you what to do about it. If a task depends on individual characters, do not ask the model to do it in its head. Put spaces between the letters so each one becomes its own token, or hand the job to code, which does see characters. And stop reading these failures as evidence about reasoning. They are evidence about input. A model that cannot count the r's may still be perfectly good at the thing you actually hired it for.

## B07 · HANDOFF — `ClaudeComposerAsk`  (12.67s)

So here is your turn. Take a word you have watched a model get wrong, run it through any public tokenizer, and look at the split. Most of the time the mistake stops looking like a mistake and starts looking like the only answer it could have given.

## B08 · OUTRO — `HaiTitleOutro`  (3.33s) · `qc.sparse`

Why it can't count letters. Liam, in for Bear.
