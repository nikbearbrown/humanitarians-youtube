# FACTCHECK — ai-support-shift

Status: **GATE F — drafted before first render.** This reel's claims are
either (a) code-verifiable — the CODE/OUTPUT beats show the actual scripts
and their actual captured stdout, reproducible by running the two .py files
in this folder — or (b) plain-language framing claims about *why* companies
adopt chatbots, which are treated as reasoned framing, not statistics, and
carry no invented numbers on screen.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B01 | Companies adopt chatbots for cost, 24/7 availability, and instant response | ✅ PASS (framing) | Widely reported industry rationale (customer-service automation literature); stated as reasoning, not sourced statistics — no invented numbers on screen | No fix — framing claim only, correctly unquantified |
| 2 | B03/B04 | `support_bot_v1.py` matches only exact keyword substrings; falls to a generic fallback otherwise | ✅ PASS — code-verifiable | Script in this folder; `respond()` uses `any(k in text for k in keywords)` — literal substring match, no synonym/semantic logic | None — code shown is the code that ran |
| 3 | B04 | The 3rd test message ("charged twice by mistake... upset") produces the FALLBACK reply from v1 | ✅ PASS — reproduced | Actually ran: `python3 support_bot_v1.py` — captured stdout confirms fallback triggered (no keyword in RULES matches that message) | None — real captured output, not invented |
| 4 | B06/B07 | `support_bot_v2.py` matches on a signal-family per intent, and separately flags urgency/escalation words | ✅ PASS — code-verifiable | Script in this folder; `INTENTS[...]["signals"]` lists + separate `ESCALATE_SIGNALS` check, independent of intent match | None |
| 5 | B07 | The SAME 3rd message is handled by v2 with both a refund reply AND a human-escalation note | ✅ PASS — reproduced | Actually ran: `python3 support_bot_v2.py` — captured stdout confirms both the refund reply and escalation sentence appear | None — real captured output |
| 6 | B06 | Narration explicitly calls v2 "a simplified stand-in... not a real trained language model" | ✅ PASS — accuracy/anti-hype guard | v2 is keyword-family + substring matching, NOT an ML model — narration must not claim otherwise. Confirmed narration text includes the disclosure. | Required — DOUBLE-CHECK LAW / no-hype instruction from the user |
| 7 | B08 | Tradeoffs claim: complex/emotionally-loaded issues, edge cases, and trust remain open problems even with the better bot | ✅ PASS (framing) | Direct consequence of #4–#6: v2 is still pattern-matching (no true comprehension), so out-of-vocabulary phrasing and genuinely ambiguous emotional cases can still fall through; presented as reasoned limitation, not a cited statistic | No fix — framing claim, consistent with what the code can and can't do |

**No fabricated statistics, no invented industry survey numbers, no claim
that v2 "understands language" in the ML sense — every claim in this reel is
either directly reproducible from the two scripts in this folder or stated
as plain reasoning.**

**GATE F — ready to open for render.**
