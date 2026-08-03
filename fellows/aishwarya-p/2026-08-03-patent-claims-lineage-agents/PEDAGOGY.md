# PEDAGOGY — Two Agents Read a Patent (hai cli-explainer)

A cli-explainer episode on designing two agents — Claims and Lineage — for reading patents beyond their abstracts. The episode's thesis: an honest `NotImplementedError` is worth more than code that looks finished but was built against a guessed API shape.

## Act structure

- B00 cold open, ClaudeComposerAsk, ask shown answered ✓
- PROBLEM beat (B01) before the CLI loop, no prompt yet — states the stakes (abstracts vs. claims) ✓
- Required revision cycle present: CLI (B02) → CODE (B03) → OUTPUT (B04), then CHANGE (B05) → OUTPUT (B06) ✓
- SUMMARY (B07) and NEXT STEPS present before outro ✓
- hai persona requirements per `skills/make/hai/SKILL.md`: CLI worked exercise inserted as second-to-last beat (B_CLI) ✓; Humanitarians AI outro as last beat (B09) ✓; `channel_title: "@HumanitariansAI"` set in metadata ✓
- Irreducibly-Human tangent: not used — no clean opportunity found; per SKILL.md, "most reels get none," not forced ✓

## Evidence discipline (source: this desk's own working files — theses/agent-recipe-STM.md, patent-intelligence/agents/, and the /hai Weekly Reports Weeks 0-9 document)

| Claim | Source | Verdict |
|---|---|---|
| B00: "Design two agents that read the second one, not the first" | Original Substack article "The Part of the Patent Nobody Reads" | OK — corrected from "Build" to "Design" during Gate P review, since neither agent is actually functional yet |
| B03: claims_agent.py raises NotImplementedError by design | Actual file content, patent-intelligence/agents/claims_agent.py | OK — verbatim from the real scaffolding |
| B04: "the client raises a clear error naming exactly what's missing" | Actual behavior of the uspto_client.py stub as built | OK |
| B05: ODP requires ID.me identity verification; BigQuery does not | Verified via web search during the actual build session (USPTO ODP registration docs) | OK |
| B05: "recognizing a constraint that only became clear once the pipeline's real needs were understood" | User-confirmed characterization of their own reasoning, Gate P review session | OK — explicitly confirmed by the author, not assumed |
| B06: claims_localized (text/language/truncated) and citation (publication_number/category) fields | Verified directly against BigQuery console schema view, screenshots reviewed live | OK — real schema, not documentation-sourced |
| B06: publication-number format mismatch caught by inspecting real sample rows | Actual session: a wildcard query for a guessed modern-format number returned nothing; a plain SELECT of 5 real rows revealed the older `US-XXXXXX-A` format | OK |
| B_CLI: worked-example query pattern | Modeled on the real schema fields confirmed in B06 | OK — but the specific patent number originally used (US-11791319) was never successfully queried (BigQuery sandbox quota was hit first); genericized during Gate P review to avoid implying a verified run |

## Friction protected

- Kept: the honest "blocked, not faked" framing in B03/B04 — this is the actual engineering decision made during the build, not a dramatized version of it.
- Kept: the real ODP→BigQuery pivot as the revision cycle, rather than inventing a cleaner-sounding but fictional revision — it's messier (three data sources considered, one bug found along the way) but it's what actually happened.
- Removed: the numpy/pkg-config dependency-conflict saga (the Brutalist toolkit's own install bugs) — real, but it's about building the video tool itself, not the patent agents; out of scope for this episode's thesis.
- Corrected during this review: B00's "Build" → "Design" (overstated completion state); B_CLI's specific unverified patent number → genericized (overstated a verified result that was never actually confirmed).

VERDICT: PASS
