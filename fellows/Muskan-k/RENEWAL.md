# Renewal request — Muskan Khandelwal

- **Current agreement:** 1 Aug — 31 Oct
- **Requested period:** 1 Nov — 31 Jan

- **Project:** Mycroft
- **Repository:** https://github.com/nikbearbrown/mycroft
- **Reels & logs:** https://github.com/nikbearbrown/humanitarians-youtube — `fellows/Muskan-k/`
- **Drive (all reels):** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

## What the current period produced

A measurement-first vendor-intelligence pipeline — collectors (news, EDGAR, arXiv,
GitHub), an agent graph that writes one brief per company, with confidence,
anomalies, and a human review step — plus a weekly STEM explainer. Figures below
come from the dated change logs and reels in `fellows/Muskan-k/`, not estimates (the
one exception is weekly *hours*, which are self-reported — see `hours.md`).

- **Honest confidence, not invented scores.** Wrong-company news was being stored as
  real signals — 72 of 76 "Scale AI" signals were other companies' (a fake health
  score of 75). Added a name-role check: accuracy on unseen cases **10/16 → 16/16**,
  and it works for companies nobody configured by hand; failures now **reject**
  (fail-closed) instead of assuming a match.
- **UNKNOWN enforced in code, tested both directions** — a written instruction is a
  request, not a guarantee (two-layer enforcement, 17 tests).
- **Reliability.** A collector run that died after 2 of 50 companies → a token-budget
  pacer, a fixed retry-after parser, and skip-one-not-abort-all: **10/10 completed,
  0 aborts** on the run that used to fail. The 10-K/A extraction bug (**AMD FAILED →
  OK**). Timeouts on Postgres/Neo4j/Bedrock (verified ~10s on a dead IP).
- **Observability.** Langfuse trace grouping — one brief went from ~20 disconnected
  traces to **one trace with 92 nested observations**, tool calls traced for the
  first time. `print` → structured logging (**225 prints**, 76 converted across 9
  files) and a validated `settings.py` (**36** scattered `os.getenv` → one module,
  `require()` reports every missing key at once).
- **Least-privilege review UI.** Split the reviewer panel off the public page
  (anyone could approve) into a dedicated reviewer dashboard; fixed a silent bug
  where corrected briefs were filed as notes and never sent.
- **Twelve STEM explainers** on how modern AI works, each cut 16:9 + 9:16 in 4K and
  reviewed against the PROOF rubric.

### Evidence — Vendor Intelligence sprints

| Sprint | Folder | Drive | Log |
|---|---|---|---|
| Kickoff — fifty vendors, one brief | [folder](./2026-07-30-AI-Vendor-Intelligence/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-07-30-AI-Vendor-Intelligence/) |
| Identity fix — the wrong Cohere | [folder](./2026-08-09-vendor-intel-identity-fix/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-08-09-vendor-intel-identity-fix/) |
| Verify — confidently wrong | [folder](./2026-08-13-vendor-intel-verify/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-08-13-vendor-intel-verify/) |
| UNKNOWN guardrails — a request, not a guarantee | [folder](./2026-08-28-vendor-intel-guardrails/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-08-28-vendor-intel-guardrails/) |
| This week's fixes — wrong-company signals | [folder](./2026-09-11-vendor-intel-update/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-09-11-vendor-intel-update/FRICTIONAL.md) |
| Rate limits, fixed | [folder](./2026-09-25-vendor-intel-ratelimit/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-09-25-vendor-intel-ratelimit/FRICTIONAL.md) |
| One brief, one trace — Langfuse | [folder](./2026-10-02-vendor-intel-tracing/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-02-vendor-intel-tracing/FRICTIONAL.md) |
| Hardening — config, 10-K/A, timeouts | [folder](./2026-10-09-vendor-intel-hardening/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-09-vendor-intel-hardening/FRICTIONAL.md) |
| Loud by default — logging + settings | [folder](./2026-10-16-vendor-intel-logging-config/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-16-vendor-intel-logging-config/FRICTIONAL.md) |
| Who can approve — dashboard split | [folder](./2026-10-23-vendor-intel-dashboards/) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-23-vendor-intel-dashboards/FRICTIONAL.md) |

## STEM topics

| Week | Topic | Drive | Log |
|---|---|---|---|
| [4–8 Aug](./2026-08-09-loop-engineering/) | Agent loops — when to stop | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-08-09-loop-engineering/) |
| [11–15 Aug](./2026-08-13-rag-evaluation/) | Where RAG Breaks | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-08-13-rag-evaluation/) |
| [18–22 Aug](./2026-08-22-brief-eval-harness/) | Caught by Code (brief eval harness) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-08-22-brief-eval-harness/) |
| [25–29 Aug](./2026-08-28-open-vs-closed/) | Open vs Closed AI | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [folder](./2026-08-28-open-vs-closed/) |
| [1–5 Sep](./2026-09-04-multimodal-ai/) | Multimodal AI | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-09-04-multimodal-ai/FRICTIONAL.md) |
| [8–12 Sep](./2026-09-11-agent-harness/) | Agent Harness | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-09-11-agent-harness/FRICTIONAL.md) |
| [15–19 Sep](./2026-09-18-ai-compute/) | AI's Four Chips (CPU · GPU · TPU · NPU) | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-09-18-ai-compute/FRICTIONAL.md) |
| [22–26 Sep](./2026-09-25-system-one/) | System One | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-09-25-system-one/FRICTIONAL.md) |
| [29 Sep – 3 Oct](./2026-10-02-slm/) | Small Language Models | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-02-slm/FRICTIONAL.md) |
| [6–10 Oct](./2026-10-09-adlc/) | Agentic Dev Life Cycle | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-09-adlc/FRICTIONAL.md) |
| [13–17 Oct](./2026-10-16-kv-caching/) | KV Caching | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-16-kv-caching/FRICTIONAL.md) |
| [20–24 Oct](./2026-10-23-mixture-of-experts/) | Mixture of Experts | [drive](https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G) | [log](./2026-10-23-mixture-of-experts/FRICTIONAL.md) |

Weekly hours: [hours.md](hours.md) — **149 sprint / 128 STEM / 277 total** to date.
Weekly frictional logs: one per work folder (per the tables above).

## Plan for the requested period

Sprints 11–14, in order, each gating the next:

1. **Measure the briefs** (1–7 Nov). Hand-label a frozen fixture set of company
   briefs; report signal precision and confidence calibration per company. If a
   company's signals can't be verified, report that rather than tuning until the
   score looks good.
2. **Full sweep + coverage** (10–14 Nov). Run all ~50 vendors end to end; report
   coverage, the UNKNOWN rate, and the confidence distribution as a spread, not a
   single number.
3. **Close the review loop** (17–21 Nov). Feed reviewer corrections (now captured
   correctly) back into the entity check and brief regeneration; measure whether
   corrections reduce repeat errors.
4. **Finish the observability + config cleanup** (24–28 Nov). Alerts on the new
   structured logs; resolve the carried items below document for operators.
5. **Future work** (from 1 Dec). Propose and carry out the next topic.

Reporting continues as it has: a dated `FRICTIONAL.md` per work folder, weekly
`hours.md`, a signed `PEDAGOGY.md`.
