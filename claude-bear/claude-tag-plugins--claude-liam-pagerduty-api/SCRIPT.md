# The Routing Key, Not the Token — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-tag-plugins/claude-liam-pagerduty-api`).*
*Register: **Plain**. 7 beats. Source was a 7-beat Teardown-register reel
covering B00 cold open, B01 anatomy (two APIs + data model), B02 design
(sanity check, trace routing, log entries, From: header, gotchas), B05
teardown (gets right / bites), BVDT verdict, BHTF your-turn, BOUT outro.
Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes one PagerDuty credential handles everything — trigger an alert, just use your API token. It doesn't. Triggering runs through a separate routing key in the request body, no token involved. So what's the difference?" | Writer types "Can Claude trigger a PagerDuty alert with my API TOKEN?"; "TOKEN" hesitates and corrects to "ROUTING KEY" |
| NB01 | 3 mechanism | PagerDuty splits into two separate APIs, on two different hosts, each with its own way of authenticating. The REST API, at api dot pagerduty dot com, handles everything you read and manage — schedules, services, escalation policies, incidents, users. It authenticates with an Authorization header reading Token, then your key — not Bearer, not Basic. Events v2, at events dot pagerduty dot com, handles the alert lifecycle instead — triggering, acknowledging, resolving. It authenticates with a routing key sent in the request body, and sends no Authorization header at all. Under the hood, an alert fires on a service, which routes through an escalation policy to specific schedules and users, opening an incident — and every notification along the way is logged, which is the actual record of who got paged and why. | "REST=Token" + "EventsV2=routing_key" + "no-Bearer" chips |
| NB02 | 3 mechanism | Before touching any data, check your credentials with a sanity call: GET slash v1 slash users slash me, with that Token header. A 200 means you're good. A 401 comes back with an empty body — curl shows you nothing unless you print the HTTP status explicitly, with dash w or dash o slash dev slash null dash w. And once you start writing, not just reading: every mutation — triggering, acknowledging, resolving — needs a From header with a real email address. Leave it off, and you get a 400 that looks like it came from nowhere. | "check-first" + "empty-body" + "From-required" chips |
| NB03 | 3 mechanism | A few more things worth knowing. Raw curl calls to the slash oncalls endpoint need dash g, or the bracket-style filters get mangled — the bundled pd_oncall.sh script already handles that for you. Any object you reference in a request body — a service, an escalation policy — needs both an id and a type field, or you'll get a 400 naming the missing one. Events v2 error responses come back as plain text, not JSON, so piping them through jq breaks immediately. And the two APIs are rate-limited differently: REST gives you nine-sixty requests a minute with headers you can watch; Events v2 gives you no such per-request header at all. | "needs-dash-g" / "id-plus-type" / "plain-text-errors" / "different-limits" chips |
| **BCRY** | **6 carry-out** | PagerDuty splits in two: the REST API reads and manages everything with a Token header, while Events v2 triggers, acknowledges, and resolves alerts with a routing key in the body — no token there at all. Mix the two up, and you won't get an error message, you'll get an empty one. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. I want to connect Claude to PagerDuty. For three tasks — checking who's on call, triggering a test alert, and looking up why an incident paged someone — tell me which API you'd call, which host, and exactly how you'd authenticate for each one, before you write any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | The Routing Key, Not the Token. Liam, in for Bear. | OutroSeries — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-tag-plugins`, Teardown-shaped) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "You are working with the pagerduty-api skill... the key distinction: there are two completely separate APIs on two different hosts with two different auth schemes" (B00 cold-open framing) | reframed as a direct question: "Can Claude trigger an alert with my API token?" — same subject, sharper hook |
| Facts | two-API/two-host/two-auth split; data model chain (alert→service→escalation policy→schedule/user→incident, log entries = paged-why); sanity check; From: header; bracket-URL encoding; reference-object type field; Events v2 plain-text errors; rate limits | unchanged, all carried — see QUESTION.md's full fact list |
| Beat count | 7 beats: B00 composer-ask + B01/B02 anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn + BOUT outro | kept the same 7-beat shape: B00 carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01 (two APIs + data model), B02→NB02 (sanity check + From: header, the two most consequential design points); B05's "gets right/bites" list plus B02's remaining gotchas (bracket URL encoding, reference `type` field, plain-text Events v2 errors, rate limits) folded into NB03's neutral "worth knowing" facts, dropping only the verdict framing; BVDT folded into BCRY; BHTF kept, with the source's five-point Claude-Code-session watch-list replaced by one paste-ready prompt any viewer can run without a live PagerDuty account; BOUT kept |
| B00 | `ClaudeComposerAsk` cold open stating the two-API distinction directly, no wrong-guess framing | `BrutalistHesitantWriter` (WRITER LAW) — "TOKEN" → "ROUTING KEY", the actual wrong guess the body corrects |
| Register | Teardown-shaped (`modifier: "skill-teardown"`, B05 rates what the skill "gets right" vs "where it bites") | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroSeries`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | source's on-call-trigger-ack-resolve task, watched for five specific behaviors | reworked into one runnable, paste-ready prompt that tests the same REST-vs-Events-v2 reasoning (which API, which host, which auth scheme) for three tasks, without requiring a live PagerDuty account |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` for
B00/BHTF, `PagerdutyApiAnatomy`/`PagerdutyApiDesign`/`PagerdutyApiTell` for
the body, `ClaudeVerdictArtifact` for BVDT, `ClaudeTitleOutro` for BOUT), so
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's mandated
cold-open swap. None of the source's custom body components were reused for
NB01–NB03 even though they are REMOTION: `PagerdutyApiTell`'s on-screen text
bakes in a "right / bites" rubric, the same defect class the `notion-api` and
`confluence-api` siblings documented. NB01–NB03 instead reuse the generic
"chip row" Manim template (copied verbatim, mechanism and GATE T exemption
notes included, from the `claude-tag-plugins--claude-liam-notion-api`
sibling), parametrized entirely from neutral title/chip/caption strings.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the question; mechanism waits until NB01 |
| Wrong guess surfaced, falsified by a case | B00 states the guess (one token handles everything); NB01 states the actual two-API/two-auth split as the immediate correction |
| One anchor | N/A this reel — the wrong guess resolves immediately at NB01 rather than through a planted/paid-off scene; see `anchor_pair: "N/A"` in beat_sheet.json metadata |
| Both directions | NB02's two traps cover both practical failure directions of the same underlying cause (missing sanity check → an invisible 401; missing From: header → a 400 that looks unrelated) — both resolve to "verify explicitly before assuming success or blaming the wrong thing" |
| No design judgment | NB01–NB03 describe what the skill does and what to watch for; nothing rates whether the skill's documentation is well written |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the token is useless for anything Events-v2-adjacent.** The
  REST API and its Token header are exactly what you'd use to look up who's
  on call or trace an incident's log entries, before or after triggering
  through Events v2.
- **Not a full breakdown of every PagerDuty endpoint.** The source documents
  the full data model and every gotcha; this reel keeps the practical traps
  a general viewer would actually hit, not a complete API reference.
- **Not a documentation-quality verdict.** NB03 states the same facts as the
  source's B05 "gets right/bites" teardown, but never frames them as a rating
  of the skill's own writing — see QUESTION.md's "Deliberately reframed, not new."

## Handoff prompt (BHTF, read aloud)

> "I want to connect Claude to PagerDuty. For three tasks — checking who's on
> call, triggering a test alert, and looking up why an incident paged
> someone — tell me which API you'd call, which host, and exactly how you'd
> authenticate for each one, before you write any code."

Why it's worth running: it puts the NB01/NB02 distinction to a direct test —
whether Claude actually separates REST-Token reads from Events-v2-routing_key
triggers, out loud, before touching a real account.

---
**GATE P — signed:** ______________________  (human)
