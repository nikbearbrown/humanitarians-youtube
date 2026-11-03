# SOURCES — The Model That Doesn't Write Back

Reel: `weekly_updates/2026-09-25-the-model-that-doesnt-write-back/` · slug `claude-sai-the-model-that-doesnt-write-back`
Week of 2026-09-25. Subject: **Jev**, TypeSafe AI's "System One" decision model,
introduced gently for viewers who have used a chatbot but never met Jev.

## Raw-material provenance

Sai chose the subject and the register ("a nice and gentle introduction to Jev,
for people who might not be very familiar with it … use images, as many as you
can"). The facts come from TypeSafe's own launch post and documentation, read
directly, and from launch-week coverage. Each page the narration leans on is
archived in `evidence/sources/` as fetched on 2026-09-25, so every quoted phrase
can be grepped back to its source.

**Nothing in this reel came from calling Jev.** Jev is in paid early access; an
API call needs an account and spends money, and this is a Fellow Tier build.
Everything on screen is TypeSafe's published claim, labelled as such, or
arithmetic run locally on those published figures.

## Primary sources (TypeSafe)

| Source | Archived as | Used for |
|---|---|---|
| Diogo Almeida, "Introducing System One Models & Jev", TypeSafe AI blog, 15 Sep 2026 — https://typesafe.ai/blog/introducing-system-one-models-and-jev | `typesafe-blog-introducing-jev.html` | B00 (date, early access), B02 (parallel vs sequential; typed values vs text), B05 (70ms–500ms; $0.042/MTok; output free), B07 (40x–200x; tests built by "individuals on our model capabilities team"; "higher end of real world gains") |
| TypeSafe docs, Introduction — https://docs.typesafe.ai/introduction | `typesafe-docs-introduction.html` | B03 (Choice, Score, Noul and what each returns; all asked in one request) |
| TypeSafe docs, System One — https://docs.typesafe.ai/concepts/system-one | `typesafe-docs-system-one.html` | B01 (the Kahneman name), B03 (the refund example), B04 ("Calibration is measured across groups of predictions; it does not guarantee that an individual answer is correct"), B06 (text input only) |
| TypeSafe docs, Model jaggedness · jev-1.13 — https://docs.typesafe.ai/model-jaggedness/jev-1.13 | `typesafe-docs-jaggedness-jev-1.13.html` | B06 ("not a calculator"; "reads dates as text"; injected instructions can steer answers; "not trained to generate text") |
| TypeSafe docs index | `typesafe-docs-llms.txt` | cross-check of page names |

## Secondary sources (launch-week coverage)

| Source | Archived as | Used for |
|---|---|---|
| Simon Willison, "Jev introduces a new shape of LLM", 21 Sep 2026 — https://simonwillison.net/2026/Sep/21/jev/ | `simonwillison-2026-09-21-jev.html` | framing ("unstructured state in, typed probabilistic decisions out"); B07 "cheap enough to test"; his black-box caution (not in narration, see below) |
| SiliconANGLE, "TypeSafe AI exits stealth with $40M…", 16 Sep 2026 | `siliconangle-2026-09-16.html` | B07 "not independently verified"; founders; $40M seed (not on screen) |
| TechStock², "…Its 445x Cost Claim Is Still Self-Tested", 17 Sep 2026 | `ts2-2026-09-17.html` | B07's resolver: "A schema can guarantee that Jev returns one of the permitted shapes; it cannot guarantee the chosen answer is right." |
| Wikipedia, "Jev (AI model)" | not archived | cross-check only (founder spelling, jev-1.13, release date) |
| TechCrunch, 18 Sep 2026 | not archived | cross-check only (developer reactions) |

## Photographs (10) — all freely licensed, credited on screen

Fetched from Wikimedia Commons by `evidence/commons_fetch.py`, which refuses any
file that is not public domain, CC0, CC BY or CC BY-SA and writes a sidecar with
title, page URL, license, author, sha256 and fetch time (`images/src/*.json`).
The full per-file table is in `SHOTLIST.md`.

| Beat | Photograph | License |
|---|---|---|
| B01 | Fort Richardson telephone operators, 1950 (U.S. Army / DVIDS) | Public domain |
| B01 | U.S. Army Signal Corps operators, Toul, France (SC-49623) | Public domain |
| B01 | Daniel Kahneman — photo nrkbeta.no | CC BY-SA 2.0 (per Commons; the author's page cites 3.0 Norway) |
| B03 | Automatic letter sorting, Briefzentrum Härkingen — Hadi | CC0 |
| B03 | Locomotive pressure dials, Da Lat, Vietnam — Dragfyre | CC BY-SA 3.0 |
| B03 | Hand-operated railway switch, Mielec, Poland — PIVISO | CC0 |
| B06 | Thomas de Colmar arithmometer, 1860 — MKFI | Public domain |
| B06 | Greek–French Julian/Gregorian calendar, Sept. 1914 | Public domain |
| B06 | G. D. Tiepolo, *The Procession of the Trojan Horse into Troy*, c. 1760 | Public domain |
| B06 | Theodore Roosevelt's typewriter, Sagamore Hill — U.S. FWS | Public domain |

The two CC BY-SA photographs are placed unaltered beside others on a plate (a
collection, not an adaptation); they are credited by author and license on
screen and in `DESCRIPTION.md`.

## Honesty log

- **Every performance and price figure is TypeSafe's own.** The narration says
  "TypeSafe says" and B05's title reads "What TypeSafe says it costs". B07 then
  says who ran the tests.
- **"Can't hallucinate" is explained, not repeated.** TypeSafe's blog claims 0%
  hallucination "via guaranteed schema matching", and marks it "not empirical".
  B07 explains it the way TypeSafe's own docs and the TechStock² piece do: the
  shape of the answer is guaranteed, not its truth.
- **B04's "82 of 100" is a constructed illustration**, a seeded simulation of a
  perfectly calibrated source (`evidence/calibration.py`). It shows what the
  definition means. It is not a measurement of Jev, and the on-screen conditions
  line says "Seeded check".
- **B05's million-ticket total uses an assumed 500 tokens per ticket**, stated on
  screen. The arithmetic is in `evidence/cost.py`.
- **The founder's name is Diogo Almeida.** Some secondary sites spell it
  "Diego"; the primary post and SiliconANGLE say Diogo. He is not named in the
  narration, so the reel stays gentle and avoids claims about who "invented" what.
- **Left out on purpose:** the $40M seed and $200M valuation (not needed for an
  introduction); named customer results (TechCrunch's Vercel and Bryo anecdotes
  are single-developer reports); the Doom and Wikiracing demos (no free images,
  and the Doom demo runs on game state, not pixels); Simon Willison's caution
  that a bare probability is a black box and his hope that nobody uses it for
  hiring. That last one is worth a sentence if you want the reel sharper; it was
  cut for length and tone.
- **No generated images.** Every picture is a real photograph or painting.
