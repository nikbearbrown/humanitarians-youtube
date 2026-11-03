# PEDAGOGY — What Is Prompt Injection? (STEM/AI concept video)

Explains prompt injection using real, current 2026 sources: the direct/indirect distinction, the structural reason it differs from SQL injection, and real, named, cited statistics on current scale and severity.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real attack surface stated plainly (webpage, document, email) ✓
- B01 — the real direct/indirect distinction, with indirect correctly identified as more dangerous ✓
- B02 — the real structural difference from SQL injection ✓
- B03 — three real, named, cited statistics on current scale ✓
- B04 — why agents genuinely make it worse (severity scales with tool access) ✓
- B05 — HANDOFF, a concrete, self-diagnostic prompt ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| "topped OWASP's list... hasn't moved since" | OWASP LLM Top 10 2025, cyberdesserts.com guide | OK — real, corroborated |
| Direct vs. indirect injection distinction | Corroborated across multiple real sources | OK — standard, well-established distinction |
| "Anthropic dropped its direct prompt injection metric... arguing indirect is the more relevant enterprise threat" | cyberdesserts.com citing Anthropic's Feb 2026 system card | OK — real, specific, correctly attributed |
| "73% of audited production AI deployments" | Cisco, 2026, via softwareseni.com | OK — real, specific, correctly attributed |
| "OWASP ranks it #1 specifically because indirect attacks scale" | OWASP LLM Top 10, via multiple sources | OK — real, corroborated |
| "1 in 8 reported AI breaches" involve autonomous agents | HiddenLayer 2026 report, via softwareseni.com | OK — real, specific, correctly attributed |

## Friction protected

- Kept: the video does not imply prompt injection is a solved problem or that any current mitigation fully addresses it — the handoff frames it as an ongoing, structural surface to audit rather than a checkbox to tick.
- Kept: the structural argument (no separator between data and instruction) is presented as a property of language models in general, not a flaw in any specific vendor's model.

VERDICT: PASS
