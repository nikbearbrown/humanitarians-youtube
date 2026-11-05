# PEDAGOGY — hai-calling-voice-ai

## The one thing a viewer should leave with

*You do not send text to a voice model. The text becomes sounds first, and the voice itself
is a block of numbers rather than a recording of anyone.*

## Structure

1. **Ask** (B00) — the disclosure comes first, because the film's own narration is the
   evidence. A viewer is listening to the thing being explained.
2. **BLUF** (B01) — not text, sounds; the voice is a file.
3. **What** (B02) — the three steps: phonemes, samples, file.
4. **Terms** (B03) — phoneme, voice, sample rate, inference.
5. **Evidence** (B04-B06) — a real phonemizer output, a real call with its real return
   values, and the real file sizes.
6. **Careful** (B07) — no cloning, and the duty to disclose.
7. **Your turn** (B08) · **Outro** (B09).

## Why self-reference is the right choice here

Most explanations of text-to-speech use a diagram. This one uses the audio the viewer is
already hearing, which means every claim is checkable without leaving the video. The
disclosure in B00 is not a disclaimer bolted on — it is the first piece of evidence.

## The transferable move

Notice the gap between an interface and a mechanism. `create(text, voice=...)` takes a
string, so it *looks* as though the model reads words. It does not. A viewer who learns to
ask "what does this function actually pass down?" has taken something that generalises well
past speech synthesis.

The second move is proportion. 310 MB of model, 26 MB for every voice it can produce, zero
cost, no account. Those numbers reframe what a voice model is — not a service you call, a
file you own.

## What the viewer is asked to do

Find the phoneme output of any text-to-speech tool they already have, feed it their own
name, and read the result aloud. That is what the model hears instead of their spelling.
