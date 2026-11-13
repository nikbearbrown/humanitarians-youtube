# FACTCHECK — Lookup, Not Training

Every claim spoken on camera, checked against its source.

**Checked against:** `medhavi-hub`, branch `chaitanya` @ `3775687`.
**Checked on:** 2026-10-05, at port-in time.
**Method:** each on-camera claim matched to a line in the cited documents; every
cited path tested with `git ls-files` to confirm a reader could actually open it.

## Verdicts

| # | Claim on camera | Source | Verdict |
|---|---|---|---|
| 1 | Nothing is trained on the textbook. No training run, no model of our own anywhere in this project | `docs/how-the-tutor-uses-the-textbook.md:11` | **PASS** — "no fine-tuning step, no training run, and no model artifact of our own anywhere in this project" |
| 2 | The model is OpenAI's, off the shelf — the same one anybody can rent | same `:11`; `docs/ai-models.md:34` | **PASS** |
| 3 | A student asks; the system searches the textbook and pulls the most relevant passages *before* the question reaches the model | `:47–49`, `:77` | **PASS** — retrieval runs in-process against a local Orama index |
| 4 | It sends both together — question and passages — and answers from what's in front of it | `:77` (retrieval local; the model call carries the context) | **PASS** |
| 5 | Correct a mistake in chapter twelve and the tutor is corrected too | `:17` | **PASS**, with a sequencing note below |
| 6 | It can cite the section it got the passages from | `medhavy_documentation/STAKEHOLDER_OVERVIEW.md:46` | **PASS** — "cites the relevant section" |
| 7 | Renting a model per question costs about a cent | `docs/ai-models.md:46` | **PASS** — "on the order of **one cent** at mini-tier pricing" |
| 8 | Running our own would need a GPU server all day — hundreds of dollars a month | `docs/ai-models.md:46` | **PASS** — "roughly $300–800+/month on AWS for something in the 7–8B class" |
| 9 | The search only works because the textbook was indexed ahead of time | `:47–49` | **PASS** — `npm run index:build` reads every MDX file and writes the index |
| 10 | By default that index is rebuilt whenever the book is built | `:51` | **PASS** — "`npm run dev` and `npm run build` both regenerate it automatically" |
| 11 | If content changes and the index isn't rebuilt, the tutor keeps answering from the old version — confidently, no error, no warning | `:87` | **PASS** — near-verbatim: "a tutor confidently answering from content that no longer exists. Nothing errors." |
| 12 | If a tutor seems to describe a chapter that no longer exists, check that first | `:87` | **PASS** — "rebuild the index first" |

Twelve claims, twelve pass. The narration was written from the document rather
than from recollection of it, and in several places it is close to verbatim —
which is why this is the cleanest fact-check of the five reels.

The reel also hedges correctly where the evidence stops: claim 10 is spoken as
"**by default**," and `description.txt` records why — the documentation
describes the rebuild as automatic during a build, but the trigger could not be
confirmed against the book repositories' own build configuration, which are not
present in this repo.

## Provenance problem — the primary source is not committed

`SOURCES.md` lists S2 as `medhavi-hub/docs/how-the-tutor-uses-the-textbook.md`,
and that file carries most of this reel's claims: 1, 3, 4, 5, 9, 10, 11, 12.

**It is untracked.** It exists on the author's machine and is not in the
repository, so anyone following the citation finds nothing. Checked with
`git ls-files --error-unmatch`; the other four cited paths are all tracked and
resolve:

| Source | State |
|---|---|
| `docs/how-the-tutor-uses-the-textbook.md` | **untracked — local only** |
| `docs/ai-models.md` | tracked |
| `medhavy_documentation/STAKEHOLDER_OVERVIEW.md` | tracked |
| `medhavy_documentation/physics-vol-1/ARCHITECTURE.md` | tracked |
| `medhavy_documentation/medhavi-cancer-textbook/ARCHITECTURE.md` | tracked |

This does not make any claim false — the claims were verified against the file
as it exists locally. It makes eight of them **unauditable by anyone else**,
which for a reel whose whole argument is "you can check where this came from"
is the wrong failure to carry.

Two ways out: commit the doc, after which the citation resolves and nothing else
changes; or re-cite those claims to the tracked architecture docs where they
overlap and mark S2 explicitly as internal-only.

## Understated — "one catch" is three

**Beat B08** opens "There is one catch worth knowing," and covers index drift
(`:87`). The same document records two more failure modes of the same species,
both silent:

- `:91` — hybrid mode needs the OpenAI key at **build** time, not run time,
  because embeddings are baked into the artifact. A build without it "produces a
  keyword-only index that runs perfectly well and quietly under-performs."
- `:93` — changing `OPENAI_EMBEDDINGS_MODEL` puts vectors in a different space
  and "breaks retrieval silently." Changing it requires a full rebuild.

Index drift is the right one to put on camera — it is the most likely and the
easiest to diagnose. But "one catch" asserts completeness the document does not
support. "The one worth knowing about" would carry the same weight and be true.

## Sequencing note on claim 5

B05 says correcting chapter twelve corrects the tutor. The source says you
"change the textbook content **and rebuild the index**" (`:17`). B08 supplies
the rebuild three beats later, and `:51` confirms it is automatic in normal use,
so the claim resolves — it is simply asserted before its precondition is stated.
No correction needed; recorded because the two beats depend on each other.

## Scope of this check

Verified against the repository at one commit on 2026-10-05. Not covered: the
book repositories' own build configuration (not present here), whether a live
deployment sets the embeddings key, pacing, or anything about the audio.
