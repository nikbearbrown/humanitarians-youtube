# Frictional log — Vendor Intelligence update: One Brief, One Trace

## 2026-10-02 — weekly project-update reel, 16:9 + 9:16
- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(10/12, gate PASS), `vendor-intel-tracing.mp4`, `short/vendor-intel-tracing-short.mp4`.
Source: my Langfuse trace-grouping change log. (YouTube / Drive: TBD.)

**What I was working on.** A reel on the Langfuse trace-grouping fix: one brief was
logging ~20 disconnected traces all named `ChatBedrockConverse`, because the callback
was attached to the model and `get_llm()` builds a fresh model per call. The fix put
the handler on the run (`trace_config()` → `graph.invoke()`), giving one trace with 92
nested observations and, for the first time, traced tool calls.

**What I tried, and what I expected.**
* The content I pasted actually contained TWO changes — this tracing fix *and* a
  rate-pacing change. I expected to cover both.

**Where it resisted, and what I did next.**
* The rate-pacing change was the same work already shipped in the 2026-09-25
  "Rate Limits, Fixed" reel — covering it again would duplicate a whole reel. I chose
  to build *only* the Langfuse change, and to structure it around a reusable lesson
  ("trace the run, not the model") rather than a flat changelog. That earned 10/12 from
  PROOF — higher than the usual changelog floor — because it has a real transferable idea.

**What Claude contributed, and what I did with it.**
* Mine: the change log, and the scope decision (only Langfuse; drop the duplicate).
* Claude's: flagged the overlap before building, authored the focused reel, ran PROOF.

**What I understand now, and what I still do not.**
* Understood: catching duplicate content *before* building saves a wasted reel; and an
  update built around a genuine reusable lesson scores like an explainer.
* Not resolved: PROOF noted a boundary case (when "trace the run" doesn't apply — e.g.
  a model built once and reused) would push it to 12/12.
