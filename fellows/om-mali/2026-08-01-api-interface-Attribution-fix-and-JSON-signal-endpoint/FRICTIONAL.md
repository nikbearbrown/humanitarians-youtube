# Frictional log: 2026-08-01

**API and interface: attribution fix and JSON signal endpoint**

This log records where the week's work pushed back and what I did about it. The details trace to
`docs/worklog.md`, `docs/relevance_fix_design.md`, `docs/json_signal_contract.md`, the n8n node
code and the screenshots in `pics/` in the project repo.

---

## What I was working on

The previous week ended with a known wrong answer in production. A Show HN post for Bento, a
slide tool, had become the top story for both OpenAI and Anthropic, so their Community Opinions
praised presentation software. This week I set out to answer three questions about the tracker's
output:

1. **Is it right?** Fix the attribution so a company's opinion is about that company.
2. **Can other systems use it?** The JSON signal was being generated every run and going nowhere.
   Give it a documented contract and an endpoint other parts of Mycroft can pull from.
3. **Is it honest about its limits?** Make sure missing or thin data is visible in that output
   rather than silently dropped.

## What I tried, and what I expected

**Attribution.** A story is relevant to a company only if one of the company's query terms
appears in the story title, case-insensitive. Top-story selection, which drives both the
narrative and the comment fetch, only considers relevant stories. If none are relevant, the
company gets no top story and its opinion degrades instead of describing the wrong subject.

I made a deliberate scope decision: the Buzz Score itself is still computed over all matching
stories. The score weights are held fixed through Phase 1 so scores stay comparable, and an
incidental mention is still a weak attention signal. Only what we claim the community is saying
is gated, not how much attention a company gets.

I expected this to remove Bento and leave clean, company-specific stories for everyone.

**The endpoint.** I expected this to be the easy half. The dashboard had already established the
pattern (Webhook, read, respond), and the signal JSON already existed in the `Code in Python`
node. It looked like a matter of copying the dashboard workflow and swapping the transform.

## Where it resisted, and what I did next

**The fix had to exist twice.** n8n code nodes cannot import modules, so the filter lives inline
in `node code/Get Metrics.py`, and a testable copy lives in `story_relevance.py`. I wrote eight
tests against the reference, including the real Bento case, asserting it is not selected even
though it has the most points. The two copies have to be kept in step by hand.

**That duplication had already gone wrong elsewhere.** When I ran the full suite, it showed that
`compute_buzz_score.py`, the reference copy of the scoring node, was still the week 3 version. It
was missing the acceleration bounds and the velocity path, so it no longer matched the live node
or the tests. Worse, `test_acceleration` returned its result instead of asserting it, so it could
never fail. I synced the reference to the node and turned the return into an assert.

**The fix worked, and then showed its own limit.** After pasting the new `Get Metrics` into the
live n8n node and re-running, Bento was gone from both companies. OpenAI's top stories became real
OpenAI news (ChatGPT under EU platform rules, OpenAI's Q2 revenue). Anthropic's became a tmux
interface for Claude Code, a Claude account switcher and a merge queue for Claude agents. Those
are real stories that really name Claude, but they are third-party tools, not news about the
company. A title can name a product without being about it. I decided to show that boundary in
the video rather than tune it away, because any tuning would be guessing.

There is also a tradeoff in the other direction. A multi-word term such as "Microsoft Copilot"
only matches when the full phrase is in the title, so a story titled "Microsoft ships a Copilot
update" is filtered out and the company degrades. I chose that conservative direction on purpose:
degrading is better than misattributing. The lever if it over-degrades is adding the distinctive
single token to the watchlist.

**The endpoint was not just a copy.** The existing signal was schema 1.0 in practice but had
never been written down, so I formalised it with field meanings and stability rules, then added
an additive 1.1 that carries theme, tone, structured sentiment and a sector block, so consumers
pinned on 1.0 are unaffected. The sector block needed a `sector_narrative` column, and that
migration was not as simple as adding one. The earlier Save Snapshot insert had written to an
unquoted `sectorNarrative`, which Postgres silently folds to lowercase `sectornarrative`, so the
live table could already hold sector data under the wrong name. I wrote the migration as check
first, then rename the lowercase column if it exists (keeping its data) or add a new one if it
does not, and ran it against the live table so old rows stayed readable instead of being split
across two near-duplicate columns. I also had to decide what the endpoint returns when no
complete run exists. It returns `{"complete": false, "entities": []}` with HTTP 200, so a
consumer gets a well-formed empty signal instead of an error.

**The honest output was mostly flags.** When I read the endpoint's output for the 2026-07-30 run,
only Anthropic, OpenAI and Google had a sentiment reading. Meta was low-confidence and degraded,
NVIDIA was degraded, and seven more companies were degraded with zero comments. That is not a
bug. It is what the data supports on a given day, and showing it as flags rather than hiding
those rows is the point of the contract. But it does mean the opinion layer is thin for most of
the watchlist.

## What Claude contributed, and what I did with it

Claude wrote the code-side pieces: the relevance filter in `Get Metrics`, `story_relevance.py`
and its tests, the richer email digest node, the contract document, the `Signal Endpoint`
transform and the externalised watchlist config. When my suite run exposed the stale scoring
reference, I had it sync the file to the live node and turn the return into an assert.

The worklog for this cycle lists what could not be done from code, and that list was my work:
pasting the new `Get Metrics` and digest code into the live n8n nodes and re-verifying a full run,
confirming Bento no longer topped OpenAI or Anthropic, building the endpoint workflow in n8n
(Webhook, SQL query, the Signal Endpoint transform, Respond to Webhook), running the
`sector_narrative` migration, building the separate pipeline-failure alert workflow
(`HN Buzz Failure Alert.json`), setting up the SMTP credentials, and confirming the digest
actually arrived. I then re-exported all four workflows into the repo, so the exported graph
finally matches what runs. It had been flagged stale since week 7. The before-and-after comparison in the
video comes from reading the real output after that re-run.

The judgment calls were also mine. Claude's change was correct by its own tests, and the tests
could not tell me that Anthropic's new top stories were about tools rather than the company. That
came from reading them. Deciding to say so on camera, rather than present the fix as complete,
was a choice about what the video should claim. The narration is in my own words.

## What I understand now, and what I still do not

**Understood.** The original bug was upstream attribution, not the analyser: the model summarised
correctly what it was given. Fixing the input fixed the output, and the relevance audit fields
(`relevanceFiltered`, `storiesConsidered`, `relevantStories`) now show per run how much the filter
is cutting. A contract is more than a JSON shape. It needs field meanings, a versioning rule,
an empty state and a rule that consumers ignore unknown fields. Duplicated code between n8n nodes
and testable reference files drifts unless something checks it.

**Not yet understood or verified.**

- The title rule cannot separate a company from its ecosystem. I do not yet know a rule that would
  without introducing new false positives.
- Whether the multi-word term tradeoff is over-degrading any company in practice. I have not
  measured how often each company ends up with no relevant story.
- The watchlist governance is only partly closed. The version guard exists, but `'v1'` is still
  hardcoded in both the writer and the reader, and a v2 watchlist is waiting on a human approval I
  have not given.
- Whether the contract's stability rules hold up will only be known once a real consumer pins on
  a version and the schema has to change.
