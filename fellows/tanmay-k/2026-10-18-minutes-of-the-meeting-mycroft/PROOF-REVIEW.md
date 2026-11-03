# Feedback: "Minutes of the Meeting" (working title): Tanmay Kulkarni, Week 27 work video

**Stage:** script, draft 1 (Gate P PASS, 2026-10-17) reviewed, then draft 2 after the edits below. No beat sheet,
components or audio yet. Reviewed from `SCRIPT.md` and `FACTCHECK.md`. The production gate is checked as **intent**
(what each claim beat will show) and is re-checked on rendered frames later.

**Verdict:** **draft 1 scored 10/12.** After four narration edits and an evidence-panel pass, **draft 2 scores 12/12**.
Production gate: PASS as intent. **Four beats changed (B02, B07, B09, B11) and need a Gate P re-read** before a beat
sheet is built.

## Read-through (PLAYBOOK §1e): the joins

| Join | Finding | Action |
|---|---|---|
| B07 | **A viewer holds "forty-five, thirty-five, twenty" and then hears pieces of 0.37, 1.75, 0.05.** The biggest weight contributed the least, and nothing said why. The question would sit open for the rest of the film | **[EDIT]** B07 now says the chair's scale runs one to five, strong sell at the bottom and enter a full position at the top, so a smaller weight on the top can outweigh a bigger weight on the bottom. Neutral arithmetic, no judgment of the design. FACTCHECK W10 extended (`signalScores`, `recScores`; the 0.82 confidence factor is noted as left out) |
| B09 | "Requests where a number wasn't a number" was never shown, so a first-time viewer cannot picture it | **[EDIT]** B09 now names them: growth typed as the letters A, B, C, and sentiment left as empty text. Traced to `d07` and `d08`, the only two requests in the corpus that produce NaN (checked by running the parse step over all 25) |
| B09 | The last two sentences ("my test breaks the copy on purpose… it does") repeat a Week 25 device: breaking my own copy to see the checks notice (W25 B07, S06) | **[EDIT]** replaced by one clause, "a test keeps that slip from coming back". The beat keeps only what is new: a defect found in my own copy, shown with its fix |
| B01 → B07 | The cold open's "must strictly match: sell" pays off when the chair writes SELL | keep |
| B03 → B08 | B03 plants the defaults (an empty request filled in); B08 pays off with "a number somebody typed looks exactly like a number the chair filled in" | keep; B03's two cards must be visibly different stocks so the viewer does not think the meeting changed company |
| B02 → B11 | B02 states no question; B11 asks three. The framework arrives only at the close | **[EDIT]** B02 now carries the question as a promise: "who had a vote, and how much?" |

## Rubric

| Criterion | Draft 1 | Draft 2 | Why |
|---|---|---|---|
| Explicit framework | **1** | **2** | Draft 1 named the idea only at the close. Now B02 states the question, B03 names the chair and the voices, and B07 shows the weights and the scale |
| Reusable rubric | 2 | 2 | Three questions the viewer can take to any AI step: have you read the minutes, who had a vote, how much of one. They are asked once, but they are the film's through-line |
| Worked example | 2 | 2 | One stock, c11, walked end to end: the request, three voices, the weighing, the briefing |
| Falsifiability / edge | 2 | 2 | B09 (my copy disagreed, fixed) and B10 (what is still open; nothing sent) |
| Active task | **1** | **2** | Draft 1's B11 asked a real question with no scaffold. Now it gives a good answer ("names the voices and their weights") and a weak one ("the AI will figure it out") |
| Friction | 2 | 2 | B07: STRONG_SELL against ENTER_FULL_POSITION, "nobody has made a mistake", and the weights set against the pieces they produce |

**Draft 1: 10/12. Draft 2: 12/12.**

## Production gate (intent), for the beat sheet to honour

| Check | Result |
|---|---|
| Sources on screen | **Fixed:** every claim beat now names a committed file in its evidence panel (`FACTCHECK.md` W1–W20): B01 (results c11), B03 (c06, audit), B04–B07 (c11), B08 (c06 briefing), B09 (RUN_LOG, parity results), B10 (hand-off log, frontmatter) |
| Evidence at the moment of assertion | To be set with cues once audio exists. Each panel must be up while its claim is spoken |
| Side-by-side | B05: three seats; B08: the typed and the defaulted 0.5, identical; B09: the two minute-takers' lines, then equal |
| Invented numbers labelled | **Fixed:** "Invented" label on every beat that shows a number (B01, B03–B08); B02 says it once aloud |

## Boundaries checked

- **W25 (porting, parity, rounding, tests on the line):** the only trace is B09's one clause that a test keeps the slip from coming back. No rounding panel, no threshold, no "test on the line". The deliberate-break device was removed (above).
- **W26 (a bad or missing value quietly becoming a plausible one):** B03/B08 describe defaults as how the workflow starts a meeting, and B08's point is about the *briefing*, not the substitution. Nearest beat: W26 B03 ("which price was used"); the thesis here is who voted and how much, not which value was substituted.
- **No critique:** defaults, the weighting and the NaN behaviour are "how the workflow works". The only mistake named is mine (B09). The finance is not judged (FACTCHECK "Not claimed").
- **Committed files only:** no guard, no fixture builder, nothing from the session. `d07` and `d08` are committed fixtures.

## Risks to watch at the next stages

- **Short fragments** ("Invented.", "Four out of four.", "Who had a vote?"): the audio step must check by Whisper that Kokoro voices them as written.
- **B07 is the densest beat** (weights, scale, three pieces, a total, a band): the stills must show the scale and the three pieces on one frame, and the cues must light each as it is spoken.
- **B03's two cards:** two different companies in one beat; keep them visibly distinct.
- **Length:** 740 words, roughly 3:45 to 4:30 with holds, shorter than W26's ten beats; no padding needed.
