# PEDAGOGY — claude-liam-hubspot-api

## Skill
hubspot-api (claude-tag-plugins / hubspot)

## Learning objective
Understand HubSpot CRM v3's uniform object model, the properties opt-in read contract, and the five most important operational patterns (list, search, create, batch, associate).

## Prior knowledge assumed
Knows what a CRM is; has done REST API work; unfamiliar with HubSpot specifics.

## Key concepts
1. Uniform v3 URL: same path pattern for contacts/companies/deals/tickets/custom objects
2. Properties are opt-in — reads without `properties=` return near-empty records
3. Each object type has its own dedup key (contacts→email, companies→domain)
4. Associations are typed — v4 endpoints for labels, v3 for basic linking
5. Search is eventually consistent and has a hard 10,000-result cap

## VERDICT: PASS

The skill covers the v3 model cleanly and the bundled helper/script pattern is correct.
Key gap: the default property set per object type isn't shown inline — developers have to
read references/api.md to know what comes free without `properties=`.
