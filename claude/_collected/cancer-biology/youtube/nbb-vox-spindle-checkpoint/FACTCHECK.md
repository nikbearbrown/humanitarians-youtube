# FACTCHECK.md — NBB wrapper: vox-spindle-checkpoint

**Date:** 2026-07-16  
**Scope:** New wrapper beats only (NBB00, NBB01, NBB02, NBB03). Body beats B01–B13 inherit the source reel's FACTCHECK (on file at `../vox-spindle-checkpoint/FACTCHECK.md`).

---

## NBB00 — Liam cold open

| Claim | Verdict | Source/Derivation |
|---|---|---|
| "A dividing cell reaches the moment of maximum readiness and then stops" | ✓ | Directly supported by B01 narration: "At the most critical moment in cell division, a cell stops. Chromosomes are lined up and ready." |
| No factual claims are made — the cold open only frames a question | ✓ | The cold open is framed as a question, not a declarative claim. No data, numbers, or mechanism stated. |

No fabrication. The cold open is a question frame only.

**Verdict:** PASS

---

## NBB01 — Bear verdict

| Claim | Verdict | Source/Derivation |
|---|---|---|
| "One unattached kinetochore out of 92 can block the entire cell from dividing" | ✓ | B07 narration: "One unattached kinetochore, out of 92, generates an inhibitory signal that arrests the entire cell." (46 chromosome pairs × 2 kinetochores = 92 kinetochores total — arithmetically correct.) |
| "Rogue kinetochore assembles MCC, which inhibits APC/C, which leaves securin intact, which keeps separase inactive" | ✓ | B08 narration: "That unattached kinetochore assembles the Mitotic Checkpoint Complex — MCC. MCC diffuses outward and inhibits APC/C, the ubiquitin ligase that would otherwise destroy securin. Securin stays intact. Separase stays inactive." Exact match. |
| "Chain holds until the last attachment is made" | ✓ | B09 narration: "The checkpoint is a single-condition veto — it cannot be partially satisfied." B10 confirms resolution on last attachment. |
| "Speed for accuracy" trade-off | ✓ | B10 body text: "All in under a minute" (fast resolution once checkpoint satisfied), vs the pause duration (illustrative 4 min in B12). Trade-off is inherent in the mechanism described. This is analysis, not a fabricated data claim. |
| "Costs real minutes at every division" | ✓ | B12 narration: "The cell waits 4 minutes" (labeled Illustrative in source FACTCHECK). Verdict labels this as "costs real minutes" — consistent with the illustrative value and the known minutes-scale metaphase pause in the literature. |
| "Weaken the checkpoint: aneuploidy, a hallmark of cancer" | ✓ | B11 narration: "When the spindle checkpoint is weakened — through mutation or overexpression of inhibiting proteins — cells separate chromosomes before every kinetochore is ready. The result is aneuploidy: wrong chromosome counts, a hallmark of many cancers." |
| "Checkpoint optimizes for fidelity over throughput" | ✓ | Analytical synthesis, not a fabricated external claim. Directly derivable from the mechanism described: the checkpoint halts division to ensure accuracy — this is the architectural trade-off the mechanism embodies. |

No fabrication. All claims are direct derivations or direct quotes from the locked body beats.

**Verdict:** PASS

---

## NBB02 — "Your turn" handoff

| Claim | Verdict | Source/Derivation |
|---|---|---|
| The prompt asks about SAC weakening in cancer — is this a real, answerable question? | ✓ | Yes. Spindle assembly checkpoint mutations are documented in many cancer types (e.g., colorectal, breast, lung). The prompt is a valid exploratory question for a frontier LLM. |
| No factual claims are made in the beat narration | ✓ | The narration only directs the viewer to run the prompt. No data or mechanism stated. |

No fabrication.

**Verdict:** PASS

---

## NBB03 — Claude title outro

No factual claims. Title restate + handle + subline derived from verdict.

**Verdict:** PASS

---

## Overall wrapper factcheck

All new wrapper beats pass factcheck. Body inherits source FACTCHECK.

VERDICT: PASS
