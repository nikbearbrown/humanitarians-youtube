# SCRIPT.md — Ask For It, Or It Isn't There. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-hubspot-api` (Teardown, walks the Anthropic `hubspot-api`
Claude plugin Skill for the HubSpot CRM API) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop,
no verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed calling HubSpot's contacts endpoint would hand back
everything about a contact. It won't — only the fields you name. So: does
calling the endpoint return everything, or only what I ask for?

*(Text typed on screen: "If I call the / contacts endpoint, / do I get back /
everything?" — trigger word "everything" corrects to "only what I ask for",
landing on: "If I call the contacts endpoint, do I get back only what I ask
for?")*

## Body — the uniform model, the working rules, the catch

**NB01 — One path, opt-in fields** (source B01, anatomy — the uniform URL
model and the properties-opt-in contract, the two facts that carry the whole
reel)
HubSpot's five record types — contacts, companies, deals, tickets, and
custom objects — all live under the same path:
/crm/v3/objects/{objectType}. List, get, create, update, delete, and search
work identically for all five; only the type name changes. But here's the
part that trips people up: a plain get or list call returns only a handful
of default fields — an internal ID and a couple of timestamps, plus one or
two type-specific fields like email for a contact. Every other property is
opt-in. You have to name exactly the fields you want, or the record comes
back looking almost empty — not because the field is missing, but because
you never asked for it.

**NB02 — Dedup keys and typed links** (source B01/B02, data model + design —
per-type dedup rules, typed associations, schema-first discipline)
Each record type has its own rule for duplicates. Contacts dedup on email —
create one that already exists and you get a conflict, not a copy. Companies
dedup on domain. Deals and tickets have no dedup key at all, so you have to
check before you create one. Links between records — a deal tied to a
contact, a contact tied to a company — are typed associations, discovered
and created through their own endpoint. Before writing anything, it pays to
read the property catalog first: the names and allowed values for every
field, so a request doesn't fail on a name you guessed wrong.

**NB03 — The catch: search lags behind** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Here's the catch: HubSpot's search endpoint is eventually consistent. Create
or update a record, then immediately search for it, and it might not show up
yet — the write and the search index aren't on the same clock. The skill
never says how long to wait or when to give up, so a script that searches
right after creating a record can silently miss it. A missing result doesn't
mean the record isn't there; it might just mean the index hasn't caught up
yet. If you need to be sure, look the record up directly by its ID instead
of trusting a search you just triggered.

## Close

**BCRY — carry-out**
A HubSpot record gives back only the properties you name — nothing else.
And a search run right after you create that record can still come back
empty, because the index hasn't always caught up yet.

**BHTF — your turn**
Your turn. Paste this into Claude: Use the hubspot-api skill to find all
contacts in the lead lifecycle stage created in the last 30 days, and return
their email and phone number. Then check what Claude does: does it pass
properties=email,phone, or does it come back with near-empty records? Does
it follow the pagination cursor through every page of results, or stop at
the first one? And does it mention that a contact created moments ago might
not show up in search yet, because the index takes a moment to catch up?

**BOUT — outro**
Ask For It, Or It Isn't There. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a read-shape question — does the contacts endpoint hand back everything, or only what's asked for? |
| Wrong guess | B00 (WRITER LAW) | "everything" corrected to "only what I ask for" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the uniform v3 path and the properties opt-in contract; then the per-type dedup rules, typed associations, and schema-first discipline |
| Anchor | the hubspot-api skill's contacts-endpoint call, named at B00 and carried through NB01–NB03 | source is a single worked API surface throughout (one Skill), not a planted-and-paid-off separate case — nothing is dropped that needs a later return |
| Both directions | NB03 + BCRY | NB03 states both failure directions for search: a record that exists can still fail to show up (false negative from lag), and the fix (look it up by ID) restores certainty; BCRY restates both core facts (opt-in properties, search lag) together, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence pair, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the hubspot-api Skill's SKILL.md and references/api.md specify (the uniform
v3 path, the properties opt-in contract, per-type dedup keys, typed
associations, and the documented eventual-consistency behavior of the search
endpoint) — not an inference about undocumented HubSpot internals. Per
simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy / design)
+ B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT (outro).
This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01's four concepts (uniform path, properties
opt-in, dedup keys, typed associations) split across NB01 (the two facts
that anchor the whole reel: uniform path + properties opt-in) and NB02 (dedup
keys + associations, folded together with B02's schema-discovery-first
practice, since both are "know this before you write" facts); B05's long
"gets it right / where it bites" list (uniform model as the central insight,
properties-opt-in documented clearly, the bundled helper scripts, specific
error-category mapping, documented rate-limit headers — versus search's
eventual consistency with no wait/retry guidance, the default property set
deferred to a second file, the unset v3 end-of-support date, the thin
18-filter workaround, association type IDs mostly external) is compressed
into NB03, keeping only the single fact a general audience needs and can act
on — the concrete search-lag gotcha — and dropping the several other gaps
(default property set location, v3 EOL timing, filter-cap workaround,
association ID table) that are real but secondary and would overload a
Plain-register general-audience beat; Teardown framing ("gets it right,"
"where it bites") is stripped to a plain mechanism-and-consequence
description, per the NO JUDGMENT register check; BVDT's verdict facts (the
opt-in contract and the search-lag gap, the two facts that matter most) are
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, re-scoped from a CSV-export task to a direct
properties-and-pagination-and-lag check (source's own task, trimmed to a
single paste-ready ask) — it stays concrete and runnable by any viewer today
with just a HubSpot skill connected; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`HubSpotApiAnatomy` / `HubSpotApiDesign` / `HubSpotApiTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway. The source's bespoke
`HubSpotApiAnatomy`/`HubSpotApiDesign`/`HubSpotApiTell` Remotion components
carried topic-specific labels tied to the Teardown cut's own beat count and
pacing; rather than reuse them as-is (their sparkLine props and beat framing
assume the source's own 7-beat split, not this redo's NB01–NB03 split), this
build uses the standard hai-simple GRAPHIC chip-row template (Manim,
per-beat-parametrized) already proven on sibling redos, matching the "one
idea per beat, ≤150 words" hai-simple BODY GRAPHIC convention.
