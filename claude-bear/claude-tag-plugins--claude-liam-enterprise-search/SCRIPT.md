# enterprise-search — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 10 beats ≈ 2:40.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude just searches the company's docs and answers straight from the results. It's closer to this: search finds candidates, reading the document is what actually answers you. Liam — take them through it." | BrutalistHesitantWriter — types "Does Claude just search our docs and answer from the results?", corrects "results" → "documents" |
| B01 | 1 stakes / **4 anchor planted** | "Say you ask: what's our policy on contractor onboarding, and is there a prior decision already on file? Answering that means reaching into the company's own knowledge — chat, drives, tickets, wikis — not the open web." | THE ANCHOR — the onboarding question, sources fanning into one index |
| B02 | 2 wrong guess, falsified | "The easy assumption: run one search, and the top result already has the answer. But a search result is a snippet — about thirty-five words, just enough to judge whether a document is worth opening. It was never built to answer anything by itself." | a snippet card, truncated mid-sentence; "IS THE ANSWER" struck |
| B03 | 3 mechanism | "The loop runs in three steps. Search returns ranked snippets across every connected source. Read fetches the full text of the documents that matter, using the IDs from search. Feedback — upvote what you used, downvote what you rejected — trains the ranker, and it happens before the task is called done. Two bundled scripts handle the busy work: one for searching with pagination, one for reading up to fifty documents at a time." | `EnterpriseSearchAnatomy` (reused source component, mechanism-only) |
| B04 | 3 mechanism | "Two rules keep it honest. Always search the shared index first — it already ranks across every source, dedupes, and respects permissions — before falling back to one connector directly. And pagination is cursor-based: pass the cursor back exactly as given, never build one yourself, stop when there isn't one. One catch: an empty result can mean two different things — the content genuinely isn't indexed, or the identity asking simply can't see it. The API doesn't say which." | `EnterpriseSearchDesign` (reused source component, mechanism-only) |
| B05 | **4 anchor payoff** | "Back to the onboarding question: search turns up a snippet that mentions a policy — that's step one. Reading the full document is what actually surfaces the exception buried in the next paragraph. Marking that document as used is step three, and it's what makes tomorrow's search better." | THE ANCHOR RETURNS — same question, snippet → full doc → feedback |
| B06 | **5 both directions** | "Finding something doesn't mean you have the whole picture — some sources might not be connected yet. And finding nothing doesn't mean the answer doesn't exist — it might be a permissions gap, or a query that needs to broaden before you conclude that." | mirrored panels: FOUND (not the whole picture) / EMPTY (not proof it's missing) |
| **BCRY** | **6 carry-out** | "Enterprise search isn't one lookup — it's search for candidates, read the document that matters, then say what you used, so the next search ranks better." | the sentence, alone, serif, large |
| BHTF | handoff | "Your turn. Here's the prompt — read it with me: Search our internal docs for our policy on contractor onboarding. Read the full document, not just the snippet, and tell me if there's a prior decision on file. Then tell me what you used to answer, before you finish. Liam, in for Bear." | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | "enterprise-search. Liam, in for Bear." | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the anchor question; the loop mechanism waits until B03 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (a search result is the answer); B02 falsifies it with a case — a ~35-word snippet built for triage, not for answering |
| Exactly one inference flag | none needed — every claim is read directly off the source skill's own documented behavior, no inference beyond it |
| One anchor, planted early, paid off late | B01 → B05 (the contractor-onboarding question) |
| Both directions | B06 — a found result doesn't prove the full picture; an empty result doesn't prove nonexistence |
| No design judgment | B03/B04 state the loop and the rules as mechanism; B05/B06 restate the source's B05 "gets right/bites" content as fact (what a result does and doesn't tell you), never as a scorecard or verdict |

## Deliberately not claimed

- **Not a scorecard.** The source's B05 (`EnterpriseSearchTell`) and BVDT
  were a Teardown scorecard ("gets right" / "bites", a verdict recap) with
  the judgment baked into the visual itself. This redo drops that beat
  entirely — its two load-bearing facts (a snippet isn't an answer; empty
  results are ambiguous) are carried forward as B02 and B06, stated as
  mechanism, not score.
- **Not a claim that every internal-search tool works this way.** The
  Glean Client REST API is this reel's worked example, not a universal
  claim about every enterprise search product.
- **No accusation that the skill is poorly documented.** The source's gaps
  (feedback has no bundled script, error formats vary, the API cap is
  unstated) are Teardown critique of the skill's own documentation and are
  not carried into this Plain redo — they don't serve the viewer's question
  about how the loop itself works.

## Handoff prompt (BHTF, read aloud)

> "Search our internal docs for our policy on contractor onboarding. Read
> the full document, not just the snippet, and tell me if there's a prior
> decision on file. Then tell me what you used to answer, before you
> finish."

Why it's worth running: it forces the same three-step loop this reel
describes — search, read, report — on your own question, so you can watch
whether the assistant stops at the snippet or actually opens the document.

---
**GATE P — signed:** ______________________  (human)
