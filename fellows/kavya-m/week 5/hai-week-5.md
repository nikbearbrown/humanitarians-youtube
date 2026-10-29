# /hai Weekly Report — Week 5

| | |
|---|---|
| **Volunteer** | Kavya Mehta · AI Data Engineer · OPT, 20 hrs/week |
| **Profile** | [humanitarians.ai/kavya-mehta](https://www.humanitarians.ai/kavya-mehta) |
| **Project** | Brutalist (Humanitarians AI) · Manager: Jash |
| **Reporting week** | 2026-10-12 to 2026-10-18 |
| **Status** | Prepared with Addams from project evidence · confirmed by the volunteer on 2026-10-29 |

## Executive summary

Two videos were produced for this week: *Ontologies for Observability at Scale* (2:00, 8 beats) and
*CabStream, Week 2 Progress* (2:18, 8 beats). The explainer argues that naming the same service three
ways is a modeling problem, not a model-size problem. The progress video covers CabStream's move toward
Azure in Terraform. Final renders were produced 2026-10-27 to 2026-10-29.

## Work completed

| Artifact | Link | Status |
|---|---|---|
| Topic explainer | [STEM WEEK 5](https://drive.google.com/drive/folders/1vIj05MOkZ5nJrQbfFylxjREQ09_WZ2Qy) | Final |
| Progress video | [PROGRESS WEEK 5](https://drive.google.com/drive/folders/1dih10GuIGENxQWj4suEFB0z_ro5le0Oe) | Final |

**Progress video:** six Terraform resources (Event Hubs, a Databricks workspace, Storage, Key Vault)
defined over two days. Key Vault initially shipped without a personal read-access policy, which was fixed
the next day. The video says plainly that the git history can't confirm `terraform apply` ran.

## Tier justification

| Activity | Tier | Argument |
|---|---|---|
| Producing both videos with Claude Code | **Tier 1** | AI-drafted production is AI fluency. |
| Choosing Terraform over portal clicks | **Tier 5** | Resources set up by clicking through the portal can't be reviewed, diffed or rebuilt. If the workspace were lost or misconfigured, nothing would record what it had been. Terraform makes every resource a reviewable file, and the Key Vault gap was caught and fixed in exactly that way. |
| The Key Vault access gap | **Tier 3** | A secrets store without the right read policy either blocks the people who need it or, if widened carelessly, exposes credentials. The fix granted personal read access deliberately, rather than opening it broadly. |
| Not claiming `terraform apply` ran | **Tier 4** | The video states what the evidence can and can't prove. A defined resource is not a running one. |

## Struggle and friction

**Topic video:**
- Its first compile came out at the tool's default 720p. A resolution check caught it, and it was
  recompiled at 4K.

**Progress video:**
- The Key Vault policy gap, fixed in a follow-up commit.

## Hours (confirmed)

| Research | Exploration | Building | Review/QC | Documentation | Meetings | Total |
|---|---|---|---|---|---|---|
| 6 | 4 | 4 | 2 | 3 | 1 | 20 |

## Tools

- **Claude Code:** used.
- **Gru:** not used yet. The Terraform design choices are SDD material.
- **CRITIQ:** not used yet.

## Reflection

1. **Has `terraform apply` run?** The git history doesn't show it. The check is `terraform state list`, or
   the resource group in the Azure portal. Until then, the resources count as designed, not deployed.
2. **Does CabStream have one thing with two names?** Yes. A trip's identity across layers: the raw Kafka
   event in bronze, the deduplicated record in silver, and the fact row in gold. Without one stable trip
   key, the layers can't be reconciled, which is the same problem the ontology video solves for services.

## Next steps

- **Week 6 (Oct 19–25):** confirm whether `terraform apply` ran (`terraform state list`), and repoint the
  producer at Event Hubs.
- **Week 6:** the first Gru SDD section, covering the Terraform resources and access policies.
- **Week 6:** the first Tier 3 data-access note, on whether a Text-to-SQL agent should see raw trip rows.

---

## Five-week summary

Beyond Tier 1 production, weeks 1–5 show:
- **Tier 4:** problem formulation, calibration, and catching a false fix
- **Tier 5:** metric definitions, the dedup-in-silver choice, Terraform over portal clicks
- **Tier 3 (from week 4):** data-access judgments on location data and secrets, in line with the chosen
  ceiling

Exploration time from week 6 continues on Tier 3.
