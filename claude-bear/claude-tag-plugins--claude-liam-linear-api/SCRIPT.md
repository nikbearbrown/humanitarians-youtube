# SCRIPT.md — There's No REST API Here. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-linear-api` (Teardown, walks the `linear-api` Skill) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Linear has a REST API — endpoints like slash issues, slash
projects. It doesn't. There's one GraphQL endpoint for everything. So: how do
you actually call the Linear API with Claude?

*(Text typed on screen: "How do I call / the Linear REST API / with Claude?"
— trigger word "REST" corrects to "GraphQL", landing on: "How do I call the
Linear GraphQL API with Claude?")*

## Body — the GraphQL model, the workflow patterns, the rate-limit gotcha

**NB01 — One endpoint, two ID systems** (source B01, anatomy)
Linear's API has exactly one endpoint: POST to api.linear.app slash graphql.
Reads are queries, writes are mutations — everything goes through that same
URL, never a REST-style path. Two ID systems live side by side: a UUID, which
the API expects for every operation, and a human-readable identifier like
ENG-123, which only works when you're reading. Pass an identifier where a
mutation expects a UUID and you get back INVALID_INPUT. The Authorization
header is different too — the key goes in by itself, with no "Bearer"
prefix. And an HTTP 200 doesn't mean it worked: GraphQL returns 200 for most
errors, with the real failure sitting in the body, under dot-errors.

**NB02 — The workflow patterns** (source B02, design — minus the rate-limit
reveal, held back for NB03)
A few patterns keep this manageable. Start with the viewer query — a quick
sanity check that confirms who you're authenticated as. Before creating or
updating anything, look up the UUIDs you'll need: a team's UUID for a new
issue, a workflow state's UUID to move one along. Description and comment
text is just Markdown — nothing fancier. And a mutation's response carries
its own success field, separate from the HTTP status and separate from
dot-errors — check that too, because it can be false even when both of the
others look fine. One more quirk: most connections don't return a total
count. To know how many issues are on a team, you paginate and count, or
read an aggregate field instead.

**NB03 — The one that catches REST developers** (source B05, teardown
analysis — re-registered Teardown → Plain, kept as the single most teachable
fact rather than the full "gets it right / where it bites" list; this is the
gap PEDAGOGY.md itself names as the key one)
Here's the one that catches people coming from REST: Linear's rate limit
doesn't come back as the usual 429. It comes back as HTTP 400, with an error
code of RATELIMITED buried in the body — the exact same status you'd get from
a broken query. A retry loop written to watch for 429 never fires. And when
you do read the reset time, it's in epoch milliseconds, not seconds — divide
by a thousand or the wait comes out wrong.

## Close

**BCRY — carry-out**
There's one endpoint, not many — and neither a 200 nor a 400 tells you the
truth by itself: a 200 can still mean it failed, and a 400 can just mean
you're rate-limited.

**BHTF — your turn**
Your turn. Paste this into Claude: show me the GraphQL query I'd send to
list my open issues in Linear, and the mutation to move one to "In
Progress," using real field names and IDs. For each one, tell me exactly
what I'd check in the response to know it actually worked — not just that
the HTTP status came back 200. Then tell me what changes about that check if
I've been rate-limited.

**BOUT — outro**
There's No REST API Here. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a lookup question — how do you call the Linear REST API? |
| Wrong guess | B00 (WRITER LAW) | "REST" corrected to "GraphQL" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source's B01 states the same wrong guess in prose ("no slash-issues, slash-projects... if you find yourself constructing a URL with object names in the path, stop"), so nothing is invented, only relocated to the cold open |
| Mechanism | NB01–NB02 | the one-endpoint/two-ID-system/auth-header/HTTP-200 model; the viewer sanity check, UUID discovery, Markdown bodies, success-boolean check, and the no-totalCount connections quirk |
| Anchor | the rate-limit behavior, named in NB03 and resolved in BCRY | planted as "the one that catches REST developers" in NB03, paid off in BCRY's both-directions sentence (a 200 can still fail, a 400 can just mean rate-limited) — same object (the status-code check), stated once fully and then compressed |
| Both directions | folded into BCRY | BCRY states what a 200 does not prove (success) and what a 400 does not prove (a broken query) — matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the linear-api Skill's source material specifies (the single GraphQL
endpoint, the two ID systems, the auth header format, the HTTP-200-on-error
behavior, the workflow patterns, and the rate-limit status code) — not an
inference about hidden model or server internals. Per simple's ONE-FLAG LAW,
when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy/design) +
B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT (outro).
This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each,
except the rate-limit reveal is moved out of B02's content and into NB03,
where it becomes the compressed stand-in for B05; B05's "gets it right /
where it bites" list (five things praised: the no-REST-paths note, the
two-ID-system separation, the HTTP-200-on-errors documentation, Markdown
bodies, the no-Bearer-prefix flag — versus five gaps: the buried 400-not-429
distinction, the missing totalCount-detection guidance, the easy-to-miss
epoch-ms footnote, the opaque UUID-required failure mode, and the
never-stated three-layer success checklist) is compressed into NB03, keeping
only the single fact PEDAGOGY.md itself names as the key gap ("rate limit
HTTP 400 vs 429 distinction is easy to miss for developers coming from REST
APIs") and dropping the other four gaps, which are secondary per the
source's own verdict; Teardown framing ("gets it right," "where it bites")
is stripped to a plain mechanism-and-consequence description, per the NO
JUDGMENT register check; BVDT's verdict facts (the endpoint/ID-system model,
the auth header, the workflow patterns, the rate-limit gap) are merged into
the single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with
the source's admin-workspace-specific instructions ("list issues assigned to
me in the ENG team...") replaced by a prompt that asks Claude to produce and
explain the query/mutation shape directly, so it's runnable by any viewer
today without an existing Linear workspace or API key; BOUT kept, re-skinned
to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT =
7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`LinearApiAnatomy` / `LinearApiDesign` / `LinearApiTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/NO-PANTRY
LAW required no substitution beyond B00's cold open, which this redo
replaces per hai-simple's mandate anyway.
