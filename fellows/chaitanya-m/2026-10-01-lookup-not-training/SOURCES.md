# SOURCES — Lookup, Not Training

**Reel:** `claude-hai-lookup-not-training`
**Channel:** claude-hai (@HumanitariansAI) · Bella (`af_bella`) · Pragmatist
**Verified:** 2026-10-01

## Primary sources

| # | Source | Used for |
|---|---|---|
| S1 | Author's script — `open-book-not-trained-script.md` (5 scenes, ~400 words) | Body scene order, visuals, the phrase to land, the protected cost comparison |
| S2 | `medhavi-hub/docs/how-the-tutor-uses-the-textbook.md` | Scene 1 (nothing trained), Scene 2 (the question→search→passages→model path), Scene 4 (index build + the silent-drift failure mode) |
| S3 | `medhavi-hub/docs/ai-models.md` | Scene 3's cost reasoning, and that the model is rented per-token rather than self-hosted |
| S4 | `medhavi-hub/medhavy_documentation/physics-vol-1/README.md` + `ARCHITECTURE.md`, `medhavi-cancer-textbook/ARCHITECTURE.md` | The per-book index-build behaviour |
| S5 | `medhavi-hub/medhavy_documentation/STAKEHOLDER_OVERVIEW.md` | That the tutor cites the relevant section |

## DOUBLE-CHECK LAW — claim ledger

| Claim in narration | Verdict | Evidence |
|---|---|---|
| Nothing is trained on the textbook | ✓ | S2: "There is no fine-tuning step, no training run, and no model artifact of our own anywhere in this project." |
| "There is no training run, and no model of our own anywhere in this project" | ✓ | S2, near-verbatim (see above) |
| The model is OpenAI's, off the shelf, and never changes | ✓ | S2: "The model is OpenAI's, off the shelf. It never changes." S3: "`OPENAI_MODEL` is just a name we send with each request." |
| The system searches the textbook and pulls the handful of most relevant passages | ✓ | S2: "the system searches the textbook, takes the handful of most relevant passages, and includes them in the request" |
| It sends the question and those passages together | ✓ | S2 §3 "Prompt assembly": the retrieved passages are assembled into the request alongside the persona prompt, page context, profile and recent turns |
| "It's an open-book exam, not a study session" | ✓ | S2 states this sentence verbatim as its own summary. Spoken **once**, in B04, undressed |
| Correcting content corrects the tutor; a trained model would need retraining | ✓ | S2: "to change what the tutor knows, you change the textbook content and rebuild the index. You never retrain anything, and there is nothing to retrain." |
| The tutor can point at the section it got an answer from | ✓ | S5: the tutor "answers using only the current textbook's content, **cites the relevant section**…" |
| A tutor answer costs about a cent | ✓ | S3: "a full tutor answer costs on the order of **one cent** at mini-tier pricing" |
| Self-hosting would cost hundreds of dollars a month before any question | ✓ | S3: "a GPU instance running 24/7 — roughly $300–800+/month on AWS … before ops time." The "before anyone asked" clause is the 24/7 idle cost, which is what that figure is |
| The textbook is indexed ahead of time so it can be searched quickly | ✓ | S2 §1 and S4: `npm run index:build` walks the MDX content and writes a serialized search index loaded at runtime |
| **"By default,** that index is rebuilt whenever the book is built" | ✓ as hedged — see *Open item* below | S2: "`npm run dev` and `npm run build` both regenerate it automatically before starting or compiling, so **in normal use** it stays in step." S4 (physics-vol-1 README): "The Orama index is built automatically during `npm run dev` and `npm run build`." |
| Stale index → the tutor answers from the old version, confidently, no error, no warning | ✓ | S2 §"Two failure modes with no visible symptom": "The symptom is a tutor confidently answering from content that no longer exists. Nothing errors." |
| "That's the first thing to check" | ✓ | S2: "If the tutor seems to be describing an old version of a chapter, rebuild the index first." |

## Corrections applied to the script

1. **Scene 2 — "before that question goes anywhere near the AI."** Not accurate in all
   configurations. S2's own table: retrieval calls OpenAI "No — **except to embed the
   query when hybrid mode is on**." With hybrid search enabled the question *is* sent to
   OpenAI (the embeddings endpoint) before the search runs. Narration changed to
   **"before that question reaches the model that writes the answer"** — true in both
   keyword-only and hybrid configurations, and it preserves the script's point exactly.

2. **Scene 4 — "That index gets rebuilt whenever the book is built."** Softened to
   **"By default, that index is rebuilt whenever the book is built"** (see Open item 1).

3. **Scene 2's visual — "three highlighted passages."** No source states the number of
   passages retrieved; S2 says only "top-k" and "the handful of most relevant passages."
   The reel therefore **never states or implies a count**: narration says "a handful,"
   and the on-screen passage group carries a trailing ellipsis so the three cards drawn
   read as "some of them," not as "exactly three." See the count audit below.

## Open items (unresolved, stated rather than papered over)

1. **The reindex trigger could not be confirmed against the actual code.** The author
   asked for code-level confirmation before narration was finalised. The book repos
   (`medhavi-quantum-volume-1`, `medhavi-cancer`, `physics-vol-1`) are **not present on
   this machine** — only their documentation is, under
   `medhavi-hub/medhavy_documentation/`. So no `package.json` could be read to see
   whether `index:build` is wired as an unconditional `prebuild`/`predev` hook or is
   conditional.
   What three independent documents do say: the index is rebuilt "automatically during
   `npm run dev` and `npm run build`" (S4), and "in normal use it stays in step with the
   content" (S2). What the same source also says: drift "does happen when content is
   edited on a server without a rebuild, or when a deploy ships without re-running the
   build step" (S2), and physics-vol-1's ARCHITECTURE.md states only the requirement —
   "The index must be rebuilt whenever chapter content changes" — not an automatic
   guarantee.
   **Resolution: the conservative phrasing. Narration says "by default."** It is correct
   whichever way the hook is wired, and it is the author's own stated fallback for
   exactly this case. Re-check against a book repo's `package.json` if one becomes
   available.

## Count audit (author's rule: state no count that isn't verified against source)

| Count the reel could have stated | Status |
|---|---|
| Number of passages retrieved | **Not stated, not implied.** Source gives only "top-k" / "a handful". Narration says "a handful"; the illustration shows three cards plus a trailing "…" so no count is asserted |
| Number of verification steps / checks in the pipeline | **Not stated anywhere.** S2 numbers four stages of its own diagram, but the reel makes no claim about how many steps or checks run |
| "for three reasons" (B05) | **Stated, and self-evidencing.** It counts the reel's own three arguments, which the next three beats then deliver one each — not a claim about the system. All three are independently sourced above (fixability S2, citation S5, cost S3) |
| Cost figures | Stated: "about a cent", "hundreds of dollars a month". Both verified verbatim against S3; the exact `$300–800+` band is deliberately not spoken, to avoid dating the video |
| Model names / versions | **Not stated.** `gpt-4o-mini` and the embeddings model name are in S3 but are left out — they date the video (DOUBLE-CHECK LAW) |

## Wording rules (author's, enforced)

- **"RAG", "embeddings", "vector search", "retrieval-augmented" appear nowhere** in
  narration, on-screen copy, card text, props, chapter names, or the description. The
  mechanism is called *looking things up* and *searching the book* throughout.
- **The phrase lands once.** "It's an open-book exam, not a study session" is spoken
  exactly once, at the end of B04, as its own sentence, with nothing added to it. The
  episode title is deliberately **"Lookup, Not Training."** rather than anything
  containing "open-book", so the outro's title restatement cannot dilute it.
