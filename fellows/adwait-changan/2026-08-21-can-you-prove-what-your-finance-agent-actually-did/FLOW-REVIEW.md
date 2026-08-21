# FLOW-REVIEW — Can You Prove What Your Finance Agent Actually Did?

Watch-free projection for an AI reviewer (Codex/Claude) or a human. Ground truth is
`beat_sheet.json`; real code under the Mycroft project root (see `SOURCES.md`, PR #17).

- **Fellow / narrator:** Adwait Changan · Onyx (`am_onyx`) · @HumanitariansAI · Pragmatist
- **this week** · 15 beats, ~4.5 min · 16:9
- **Thesis:** scattered evidence isn't auditable; a bundle that hash-validates the whole chain,
  packages it, and can be independently verified is — while integrity is still not approval.

## The flow
| # | Act | Visual | Beat's job |
|---|---|---|---|
| B00 | COLD OPEN | ClaudeComposerAsk | The audit question + the answer (validate by hash, package 54, verify, 41 tests). |
| B01 | Scattered Proof | CwcConceptCard | Five capabilities, all in different files. |
| B02 | Scattered Proof | MedhavyConceptCard | Belonging must be provable, not assumed. |
| B03 | Validate, Then Package | CwcConceptCard | Act title — `bundle.py`. |
| B04 | Validate, Then Package | ClaudeCodeBeat | Real cross-artifact hash validation (review + scenario). |
| B05 | Validate, Then Package | ClaudeScienceChipGrid | The seven things checked before packaging. |
| B06 | Validate, Then Package | ClaudeWindow | 54 artifacts + manifest.json / manifest.sha256 / REVIEW.md. |
| B07 | Verify, Independently | CwcConceptCard | Act title. |
| B08 | Verify, Independently | ClaudeWindow | verify-bundle → INTEGRITY_MATCHED_HUMAN_REVIEW_OPEN. |
| B09 | Verify, Independently | ClaudeScienceChipGrid | Seven tamper cases rejected; 9 bundle tests, 41 total, CI green. |
| B10 | Verify, Independently | MedhavyConceptCard | SHA-256 = integrity, not identity/adequacy/approval. |
| B11 | Verify, Independently | ClaudeWindow | Recipe DRAFT; release BLOCKED_PENDING_HUMAN_REVIEW; five gates open. |
| BVDT | VERDICT | ClaudeVerdictArtifact | Proof you can audit + disclosures. |
| BHTF | YOUR TURN | ClaudeComposerAsk | "…if an agent cannot prove exactly which data, code, tests, and decisions produced it — can you really audit it?" |
| BOUT | OUTRO | ClaudeTitleOutro | Title restate. |

## Confirmed facts (must stay exact)
54 packaged artifacts · manifest.json + manifest.sha256 + REVIEW.md · verify status
`INTEGRITY_MATCHED_HUMAN_REVIEW_OPEN` · 7 tamper cases rejected · 9 bundle tests · **41 total** ·
both CI checks green · SHA-256 = file integrity only · recipe DRAFT · release
BLOCKED_PENDING_HUMAN_REVIEW · five gates: materiality, causal explanation, evaluation adequacy,
scenario approval, distribution.

## Review prompt (paste to Codex / a reviewer)
> Review the flow of this 15-beat explainer (`FLOW-REVIEW.md` + `beat_sheet.json`). You cannot watch
> the video. Check: (1) logical flow scattered → validate/package → verify; (2) every code excerpt
> matches the real files in `SOURCES.md` verbatim; (3) the 54-artifact count, the 7 validated inputs
> (B05), and the 7 tamper cases (B09) match `bundle.py` / `test_bundle.py`; (4) the verify status
> string is exact; (5) the SHA-256 "integrity not approval" disclaimer is present and correct;
> (6) recipe DRAFT / release BLOCKED / five gates are stated; (7) the 41-tests + CI claim; (8) pacing
> for B04 (code) and BVDT (~33s). Return: beat | issue | severity | fix. Mark anything needing the
> repo as VERIFY.
