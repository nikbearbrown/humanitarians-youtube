# FACTCHECK — Episode 1, "What Makes an AI Agentic"

DOUBLE-CHECK LAW: every on-screen and spoken claim is listed, judged, and sourced.
This episode is **definitional teaching material**, so most claims are definitions rather
than empirical findings — which is exactly why the standard here is *"does it survive a
sceptical reading"*, not *"is there a citation"*.

| # | Claim (beat) | Verdict | Basis / fix |
|---|---|---|---|
| 1 | "A language model completes text: prompt in, generate, text out, then it stops." (B02) | **ACCURATE** | Definitional. Describes the inference contract of an autoregressive LM, independent of vendor or version. No model named, so it cannot date. |
| 2 | "It has no memory of the last answer unless you paste it back in." (B02) | **ACCURATE, deliberately scoped** | True of the *model*. Products layer conversation history and memory features on top — which is precisely the layering this series unpacks. Narration says "a language model", not "a chatbot product", to keep the distinction honest. |
| 3 | Flight-booking artifact (B03) | **ILLUSTRATIVE — labelled on screen** | Not a transcript of any product, and not attributed to any vendor. The disclosure sits in the spark line directly beneath the card: "**Nothing was actually booked.**" *(Revised after visual QC — it was originally a fourth artifact line, which the component numbered "4.", making the disclaimer read as a fourth plan step. See `_qc/REPORT.md` D2.)* |
| 4 | "An agent is a model inside a loop that can call tools and read results." (B00, B04–B05, BVDT) | **ACCURATE** | The consensus working definition, and the one the shipped code implements. Stated as a definition the episode adopts and defends, not as a citation of authority. |
| 5 | B06 code — eleven lines, shown verbatim (B06) | **VERIFIED BY EXECUTION** | `agent_loop.py` is in this folder. `run()` is reproduced character-for-character, including the two inline comments. Line count checked: the `run()` block is 11 lines. Run: `python3 agent_loop.py` → `rows in the sales file: 3`. |
| 6 | "Without a step budget, a confused agent runs forever." (B06) | **ACCURATE** | Directly demonstrated by the shipped code: remove `max_steps` from the `for` and the loop is unbounded. The narration's "bills you for the privilege" is a register flourish over a true mechanism. |
| 7 | "The loop adds state, feedback, and a stopping rule." (B07, BVDT) | **ACCURATE** | Each maps to a named element of the shipped code: `observations` (state), `result` fed back into `think()` (feedback), `max_steps` (stopping rule). |
| 8 | Six failure modes (B08) | **ACCURATE, non-exhaustive** | Presented as "six failure modes arrive" — not "the six". Each is a real, documented class of agent failure. Caption reads "every one of these becomes yours", which is a statement about ownership, not about completeness. |
| 9 | "A doer that is wrong sends the email, deletes the row, charges the card." (B08) | **ACCURATE as illustration** | Generic consequences of tool-use with side effects. No incident, company, or product is referenced, so nothing to over-claim. |
| 10 | Three-condition test for reaching for an agent (B09, BVDT) | **EDITORIAL — flagged as such** | This is the fellow's recommendation, not a cited standard. Narration frames it as advice ("when should you actually reach for one?"), never as an industry rule. Kept because the HAI channel's remit is exactly this judgement. |

## Corrections applied during authoring

- **Removed a comparative capability claim.** An early B02 draft said models "cannot do
  arithmetic reliably" — a claim that dates badly and varies by model. Cut; the beat now
  makes only the structural point about one-turn completion.
- **Removed all version and vendor specifics.** No model names, parameter counts,
  context-window sizes, benchmark numbers, or pricing appear anywhere in the episode. The
  episode is intended to stay correct for the life of the playlist.
- **Softened "the six failure modes" → "six failure modes"** so the list is not read as
  exhaustive.
- **B03 artifact given a self-disclosing line** so the illustration cannot be mistaken for
  a captured product transcript even if the frame is screenshotted alone. After visual QC
  this line was moved out of the numbered list and into the spark line, where it reads as
  the episode's judgement rather than as a fourth step of the plan.

## Anti-dating audit

Searched the full narration and every prop string for: model names, version numbers,
benchmark scores, prices, dates, company names, and "state of the art" phrasing.
**Zero hits.** The only proper nouns in the episode are Humanitarians AI, Onyx, Adwait
Changan, and the Model Context Protocol (named once in B00 as the destination of the
playlist — a protocol name, not a version).

## Verdict

> FACT GATE: CLEARED. No unverifiable or dating claim survives in the shipped script.
> Items 3 and 10 are labelled illustrative/editorial on screen and in the narration.
