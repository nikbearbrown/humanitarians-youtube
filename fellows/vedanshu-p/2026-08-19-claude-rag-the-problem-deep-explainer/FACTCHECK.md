# FACTCHECK — Three Ways To Be Wrong.

| # | Claim (beat) | Source | Verdict |
|---|---|---|---|
| 1 | Hallucination splits into intrinsic (contradicts a source) and extrinsic (unverifiable against any source) (B08, B09) | Ji et al., 2023 (ACM Computing Surveys); Huang et al., 2023 (arXiv:2311.05232) | ✅ — both real, checkable surveys; the split is stated plainly, not sensationalized |
| 2 | Grounding a model in retrieved documents measurably *reduces* — not eliminates — hallucination in dialogue, per human evaluation (B10, BVDT) | Shuster et al., 2021, Findings of ACL: EMNLP 2021 (arXiv:2104.07567) | ✅ — verified as a reduction claim; no rate number is asserted on screen, matching the paper's own careful framing |
| 3 | Models are trained once on a fixed snapshot, deployed, and do not continue learning — a stated design property, not a bug (B12, BVDT) | OpenAI, 2023, GPT-4 Technical Report (arXiv:2303.08774) | ✅ — vendor technical reports state a knowledge cutoff explicitly; no specific date is asserted here |
| 4 | Context windows are token-bounded, have grown across model generations, and have never been unbounded (B18) | OpenAI, 2023 (same report) | ✅ — used only for the qualitative "bounded, growing" claim; no specific token count stated |
| 5 | Long-context accuracy is highest when the needed fact sits at the start or end of the input, and drops when it's buried in the middle, even when the whole input fits (B19, B20, BVDT) | Liu et al., 2024, TACL (arXiv:2307.03172) | ✅ — verified as an ordering claim; no accuracy percentages appear anywhere in this reel |
| 6 | The chapter's three-panel worked example (invented benefit / retired policy / wrong paragraph from a full manual) (B26) | chapters/02-the-problem.md, Figure 01 + "Worked example" section | ✅ — rebuilt natively (REBUILD LAW), not screenshotted; scenario matches the chapter's own framing, no invented specifics beyond it |
| 7 | A bigger context window does not, by itself, fix hallucination, stale knowledge, or the lost-in-the-middle effect (B22, B23, BVDT) | chapters/02-the-problem.md, "Why a bigger window doesn't fix any of them" section | ✅ — this is the chapter's own argument, restated; B22's box/lost-item metaphor makes no claim beyond "size ≠ the variable that matters" |
| 8 | Chapter 2 bridges to representation/comparison as the next topic, without itself presenting a retrieval mechanism (B27, B28) | chapters/02-the-problem.md, "Bridge" section | ✅ — B27/B28 name the missing step (deciding which passage matters) without depicting HOW Chapter 3 resolves it; no mechanism invented or borrowed from later chapters |

## Datable-claim check

No model version number, specific knowledge-cutoff date, or specific
context-length figure (e.g., "128k tokens", "GPT-4o") appears anywhere in
this reel's narration or on-screen text — matching the chapter's own explicit
choice not to state a cutoff date because it "shifts from one release to the
next." The reel will not date itself as models change.

## Real-person / real-object check

No real, named person, product, organization, or specific real object appears
anywhere in this reel's narration, on-screen text, or planned VOX stills. All
eight VOX beats depict generic, invented documentary metaphors (an office
desk, a stage magician, an archive, a buried desk, an oversized suitcase, a
hand with a magnifying glass) — see `SOURCES.md` for the full list. All are
Tier 1 under Gate D2; none require a rights escalation or a `.source.txt`
sidecar (unless a real stock/archive photo is substituted for an AI-generated
one at pantry-fill time, in which case that specific file gets its own sidecar
per the parent provenance rule).

## Numbers-on-screen audit

Every number that appears in a beat's `graphic.production_viz` or Remotion
`props` was checked against the claim it illustrates:
- B10, B19, B20: explicitly qualitative — no invented rate/percentage.
- B18: three unlabeled "generation" columns with different bar heights —
  illustrates growth + a ceiling, no specific token counts.
- B22: a box scaling 1.6× then 2.2× — arbitrary demonstration multipliers,
  not a claim about any real context-window ratio.
- BVDT: the four recap lines carry no numbers beyond the citations
  themselves.

**GATE F: ✅ CLOSED.** All 8 rows verified against their cited sources or the
chapter's own text; no fabricated-but-fluent claims found; no claim requires
a rights escalation beyond what's already logged in `SOURCES.md`.
