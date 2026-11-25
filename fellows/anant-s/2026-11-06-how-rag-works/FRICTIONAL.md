# Frictional log — How RAG Works

## 2026-11-22 — planning in show-tell, narration, audio and low-res previews

- **Drive:** https://drive.google.com/drive/folders/1w-Bz0R9QjZE2HX4Egg_fujYbSnVPtRb2

**What I was working on.** Film 7 in the series: how RAG works. I picked the topic, the `show-tell` format and the default claude-liam branding. Claude Code, using the brutalist.art toolkit, planned 17 beats (649 words), wrote the script and an evidence demo, then built the audio, `scenes.py` and low-res previews.

**What I tried, and what I expected.**

- I expected one worked question, carried through each pipeline step, to explain RAG without jargon cards.
- I expected the planning pronunciation check to be enough for "RAG".
- I expected each Manim clip to match its audio once the clock counted frames.

**Where it resisted, and what I did next.**

- **"RAG" was spelled R-A-G in context.** The planning note said no override was needed, but it had phonemized the word on its own. Whisper heard "R.A.G." and "Ragee". Claude pinned `RAG` → ɹˈæɡ and regenerated the three affected beats.
- **The first previews ran 1.8–2.8% short.** Manim floors `wait()` frames, so each wait dropped one. Claude changed `Clock.at` to wait exactly frames/fps.
- **No library figure could show this film's data.** Six `scene_search` queries found only fixed-content figures, so the retrieval steps used `ShowTellCard`s (B06 `search`, B09 `tabs`).
- **A rule update from the main session:** no terracotta arrows. The one arrow in this film became INK and was shortened clear of the model block.

**What Claude contributed, and what I did with it.**

- **Script and evidence:** Claude drafted the narration and wrote `demo/rag_demo.py`, a deterministic TF-IDF demo whose self-checks assert every ranking the film states. Four DOUBLE-CHECK corrections went into FACTCHECK (rows 9, 20, 21, 25), including dropping "searched … this way" because Lewis et al. used a dense retriever.
- **Build:** Kokoro audio (200.30 s), whisper check, alignment (17/17, 0 fallbacks), 11 drawn scenes, Gates A/W/B, previews checked at 15/50/85/99%.
- Accepted:
    - **The narration as drafted.** I approved it in the main session with "approve all six".
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - Retrieval scores here are word overlap: the warranty chunk scores 0.25 only because it shares "laptop".
    - A pronunciation check on a word in isolation does not show how it is read in a sentence.
- Not understood / not verified:
    - Whisper-base heard "The fix is in the store" as "The fixes in the store are"; the log asks for a human listen, and none is recorded.
    - The answer step is illustrated, not executed: no language model runs in the demo.

## 2026-11-23 — 4K gate failures, a redrawn ranking and the show-tell final

**What I was working on.** Getting the first 4K cut through GATE V and GATE T.

**What I tried, and what I expected.**

- I expected scenes that passed Gates A, W and B at low resolution, and the stock cards, to pass at 4K.

**Where it resisted, and what I did next.**

- **GATE V, B00 midpoint: low contrast 0.23 < 0.30.** Claude moved the dark model block to arrive at about 2.0 s, so it is on the 50% frame.
- **GATE T §8.6b on the B06** `search` **card:** its bordered rows read as text runs enclosing the labels. Claude redrew B06 as a Manim scene, `B06_Ranking`: the question's strip over the three best chunks' strips, open score bars, no box around any text, the ranking asserted against `evidence.json`.
- **GATE T §8.1 on the answer cards (B08, B10, B11):** a dark squiggle read as a 36 px text run. The squiggles became soft grey.
- **GATE T §8.1 on BDEFS (40 px):** the main session fixed the toolkit component (`ClaudeDefinitions` meanSize 48 → 52).
- **A concurrent writer reverted the B06 change** in `beat_sheet.json` within seconds. Claude re-applied it at 01:41 and it held.

**What Claude contributed, and what I did with it.**

- **Fixes and QC:** Claude diagnosed each failure, made the fixes, moved stale renders to `_superseded/2026-11-23-gateVT/`, built the 200.7 s show-tell master and ran GATE V, GATE T, strip, master and loudness checks plus hand QC. I reviewed the result.
- Accepted:
    - **B06 as a drawn Manim scene** instead of a card; cards dropped to 1 of 13 body beats.
    - **Soft grey squiggles** and the "illustrated" tag raised from 32 to 36.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - GATE T reads a bordered row as a text run, so a box around a label fails as overlap even when it looks clean.
    - What lands on the 50% frame decides GATE V's contrast reading.
- Not understood / not verified:
    - Why the other writer reverted `beat_sheet.json`; the log guesses it was the tail of the 4K build.

## 2026-11-24 — converting the film to the ai-explainer format

**What I was working on.** Making this film match the other five, which use the ai-explainer spine, with no footer. I asked for the conversion.

**What I tried, and what I expected.**

- I expected to swap the bookends and keep the body exactly as it was.
- I expected a five-line recap card to be enough.

**Where it resisted, and what I did next.**

- **The new beats needed new narration.** Claude drafted a B00 cold open, a B01 hesitant-writer summary and a BVDT recap; I approved them as previewed in chat (GATE P). The greeting is "Hello", which I chose for all three converted films.
- **The old opening beats defined the terms.** BIDEA and BDEFS were retired to `_superseded/format-show-tell/`; chunk, embedding and vector store are defined inline in the body, and RAG is expanded in B01.
- **The cold open had to be B00.** The body B00–B12 was renumbered B10–B22, with audio, clips, scene class names, cue ids and timing keys renamed together. No content changed.
- **The five-line BVDT card measured 51% fill.** Claude added a sixth line from the B22 body ("The 2020 paper that named it searched 21 million Wikipedia passages."), matching the six-line cards in the other films. The fill check was not waived.

**What Claude contributed, and what I did with it.**

- **Conversion and final:** Claude drafted the new narration, renumbered the body, built the 216.1 s master and ran all checks: GATE V 0/0 on 36 frames, GATE T PASS, bookend PASS, strip check 108/108, master PASS, −24.16 LUFS. Hand QC of all 18 beats is clean; sha256 matches `.verified.json`.
- Accepted:
    - **The new B00, B01 and BVDT narration**, as previewed.
    - **The sixth recap line** to pass the fill check.
    - **Terms defined inline** instead of a terms card.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - Renumbering is safe only when every file and key that uses a beat id is renamed together; the renumbered body rendered as before.
    - A sixth recap line was a content fix for a fill failure, not a waiver.
- Not understood / not verified:
    - `SCRIPT.md`, `CHECKS-REPORT.md` and `FACTCHECK.md` still use the show-tell beat ids and have not been regenerated.
    - Update, same day: they have since been refreshed to the ai-explainer build (SCRIPT, SHOTLIST and CHECKS-REPORT regenerated, with the originals kept as history; a dated conversion section added to FACTCHECK).
    - The film is not published; the Drive copy is still the labelled review cut.
