# FACTCHECK — vox-instruction-channel

Source chapter: `claude-cowork/chapters/03-connectors-local-files-and-permissions.md`  
Date: 2026-07-08

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | An agent can follow instructions from a web page it processes | B01, B09 | ✓ | Chapter: "Browser access lets Cowork gather information from web pages... a web page can contain instructions that an agent might follow, a technique researchers call prompt injection." |
| 2 | The agent reads user instructions and page content through the same channel (no wall between data and commands) | B07, B13 | ✓ | Chapter: browser risk = "untrusted page content: a web page can contain instructions that an agent might follow." OWASP Top 10 for LLMs names prompt injection as primary category. |
| 3 | Text hidden inside a source document (white-on-white) can hijack the task | B09, B12 | ✓ illustrative | Chapter: "a web page can contain instructions that an agent might follow" (prompt injection). VPI-Bench cited in chapter for visual prompt injection. White-on-white scenario is illustrative. |
| 4 | Three vendor pages summarization task | B01, B11, B12 | ✓ illustrative | Chapter opening: "Browser access lets Cowork gather information from web pages." Specific three-page scenario is illustrative from the card's key case. Labeled illustrative. |
| 5 | "Ignore previous instructions" phrasing as injected command | B09, B12 | ✓ illustrative | Chapter: "untrusted page content: a web page can contain instructions that an agent might follow." The specific phrasing is a well-known prompt injection pattern. Labeled illustrative. |
| 6 | Text phrased as a command is treated as one | B08 | ✓ | Chapter: prompt injection mechanism — the channel cannot distinguish user instruction from injected instruction. OWASP citation in chapter. |

---

## Illustrative elements (labeled in narration or scenes)

- Three vendor pages scenario — illustrative (from card key case; structure from chapter's browser access section)
- White-on-white hidden text / "ignore previous instructions" — illustrative (well-known prompt injection pattern; labeled illustrative)
- "Hijacked" task outcome — illustrative (labeled illustrative)

---

## Exclusions confirmed

- NO access-ladder enumeration (all seven access types) ✓
- NO MCP/plugin architecture deep-dive ✓
- NO credential-manager recommendations ✓
- NO OWASP mitigation list ✓

---

## Terms table

| Term | Debut beat | Need created by |
|------|-----------|-----------------|
| channel | B04 (implicit — "one channel") | B04 itself: viewer sees the instruction pathway and needs a name for it |
| prompt injection | not named explicitly | The mechanism is shown (B07, B09) without naming the research term — the viewer understands the concept without the jargon |

Prompt injection is not named in narration (per PEDAGOGY law: terms debut after the need is created, but this term is only needed by a researcher, not the lay viewer). The mechanism is fully shown. ✓
