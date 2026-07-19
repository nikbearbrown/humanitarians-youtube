# SOURCES — claude-liam-internal-comms

## Primary source
- `anthropics/skills/skills/internal-comms/SKILL.md` — the Anthropic internal-comms skill definition
- `anthropics/skills/skills/internal-comms/examples/3p-updates.md` — 3P format spec and examples
- `anthropics/skills/skills/internal-comms/examples/faq-answers.md` — FAQ format spec and examples
- `anthropics/skills/skills/internal-comms/examples/company-newsletter.md` — newsletter format
- `anthropics/skills/skills/internal-comms/examples/general-comms.md` — fallback format

## Beats sourced from
| Beat | Source |
|---|---|
| B00 | SKILL.md trigger block, 3P example |
| B01 | SKILL.md comm-type routing table (7 types → 4 files) |
| B02 | examples/3p-updates.md verbatim format + workflow |
| B05 | Teardown synthesis — router insight, gets-right/bites |
| BVDT | SKILL.md + examples synthesized |
| BHTF | Handoff prompt constructed from 3P format spec |
| BOUT | Standard outro |

## No external sources used
All content derived directly from SKILL.md and example files in the skill repo.
