# Frictional log: What Is RAG?

_Both entries were written on 2026-11-08 from the build chat, after the work they describe, and drafted by Claude. Tanishaa: read them and correct anything that is not what happened._

## 2026-11-05 — Setting up Brutalist and scripting "What Is RAG?" (written 2026-11-08)
- **Working on:** installing the Brutalist toolkit and scripting my first weekly STEM/AI explainer.
- **Tried:** asked Claude to install Brutalist without me using the terminal. Expected the toolkit's own `./setup --install` to just work.
- **Resisted:** the Mac had no Homebrew, Node or ffmpeg, and its Python was too old (3.9). Installing Homebrew would have needed my admin password in a terminal, so I approved a different route: micromamba, which installs everything into my user folder. The first install still failed: a graphics library (pycairo) could not build. Claude switched to a prebuilt version and the readiness check passed, except math-equation rendering (no LaTeX).
- **Resisted:** the first script ran about 2 minutes. I asked for 2–3 minutes, so it gained a beat on how search finds the right passage (embeddings).
- **Contributions:** Claude drafted the script, the beat plan and a real retrieval demo (`demo/rag_demo.py`). I chose the topic and the voice (Bella), set the length, and approved the script.
- **Understand now:** RAG adds a search step before the answer and does not change the model itself. **Still unsure:** _[Tanishaa: what is still unclear to you?]_

## 2026-11-06 — Building, reviewing and fixing the video (written 2026-11-08)
- **Working on:** the 16:9 and 9:16 masters.
- **Tried:** watched the first preview. Expected the on-screen items to appear as Bella said them.
- **Resisted:** the intro greeting said "Hej, HAI", so I asked for "Hi, Tanishaa". In the "use it when / skip it when" beat (about 1:36–2:00), items appeared late.
  - Cause: reveal times had been estimated from word position, which drifts at every pause, and each fade took over a second.
  - Fix: word times were measured from Bella's audio with faster-whisper (`timing/words.json`), reveals now start 0.2 s before each word, and fades take 0.35 s. This was checked with frames before and after each cue word.
- **Resisted:** the 9:16 version failed the toolkit's text-size check several times. On a 3840 px tall frame, body text has to be about 92 px at design size. The portrait scenes were redesigned to show fewer, larger words (first sentences only, short footnotes) instead of switching the check off. The first vertical export also came out at 1216×2160 until it was rebuilt with `--height 3840`.
- **Contributions:** Claude found the causes and made the fixes. I spotted the greeting and the lag, and asked for the vertical version.
- **Understand now:** on-screen text has to be timed to the real audio, not estimated, and vertical video needs its own layout with less text. **Still unsure:** _[Tanishaa: anything?]_
