# PEDAGOGY — claude-liam-enterprise-search

## Skill reviewed
`anthropics/claude-tag-plugins/enterprise-search/skills/enterprise-search/SKILL.md`

## What learners will be able to do
- State the three-step search loop: search → read → feedback (UPVOTE what used, DOWNVOTE what rejected)
- Know the two bundled scripts: es_search.sh (search with cursor pagination) and es_read.sh (fetch full document text)
- Understand the index-first rule: search the enterprise index before fanning out to per-source APIs
- Know the base URL gotcha: -be suffix for backend host, not the web UI host (HTML body = wrong host)
- Apply the empty-results rule: broaden query before concluding content isn't indexed; two reformulations → fall back and say so

## What makes this teachable
The three-step loop with mandatory feedback distinguishes this from a plain search API — the ranker learns from both positive and negative signals.
The bundled scripts cover the hot path concisely; es_search.sh handles cursor pagination and datasource filtering.
The index-first rule is the operational insight: fanout to per-source APIs wastes calls and misses cross-source deduplication.

## Gaps the teardown surfaces
- Feedback is the only operation with no bundled script — one curl per event, and the negative label (DOWNVOTE) will be the first thing skipped
- Error format varies across endpoints: /search has ErrorInfo with errorMessages; /getdocuments error shape isn't described in the skill body
- Permissions gap silently returns empty results — indistinguishable from content not being indexed without investigation
- The 50-document cap in es_read.sh is script-enforced; the actual API limit isn't stated
- Credential placeholder instruction ("set to any placeholder value") is confusing — implies the injected credential is ignored

## VERDICT: PASS

Security note, three-step loop with feedback, two bundled scripts, index-first rule, base URL -be suffix gotcha, and cursor pagination are well-specified.
Feedback has no script (making DOWNVOTE easy to skip) and the permissions-vs-missing-content ambiguity are the key teachable gaps.
