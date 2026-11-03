# FACTCHECK — Week 24 work video, *Read the Receipt Backwards* (Mastercard Agent Pay)

Every claim the script may make, with its verification level. **Nothing enters the script until
its row reads ✅.**

**Levels:**
- **primary read**: the source page itself was opened and the words were read (2026-09-28,
  built-in browser; Mastercard's site returns HTTP 403 to automated fetches).
- **live run**: executed on the code, in a fresh, empty Python 3.12 venv.
- **repo record**: stated in the build's own README / DESIGN_DECISIONS.
- **case study**: cited from `14-mastercard-agentic-ai-payments.md` (corrected 2026-09-28).

Framing rule for this film (Tanmay, 2026-09-28): the build uses **public information only**, so
where Mastercard's record is silent, the build is silent too, *by design*. Those places are said as
"Mastercard hasn't published how that works, so the build doesn't pretend to know". They're never
called gaps, defects or shortfalls. The review findings are presented as the method working.

---

## Part 1 — Mastercard, in Mastercard's words

| # | Claim | Level | Source | Status |
|---|---|---|---|---|
| M1 | Verifiable Intent "creates a tamper-resistant record of what a user authorized when an AI agent acts on their behalf" and "provides cryptographic proof of authorization that consumers, merchants, and issuers can rely on" | primary read | [Mastercard, "How Verifiable Intent builds trust in agentic AI commerce"](https://www.mastercard.com/global/en/news-and-trends/stories/2026/verifiable-intent.html), March 5, 2026 (Pablo Fourez) | ✅ verbatim |
| M2 | "It confirms the cardholder authorizing the AI agent, captures the consumer's specific instructions and records the interaction between the agent and merchant resulting in a purchase" | primary read | as M1 | ✅ verbatim. **Load-bearing**: Mastercard's own record names the cardholder, the instructions and the merchant, which are the receipt lines the film reads |
| M3 | Opening question on the same page: "How do we know an agent is doing exactly what we asked — and nothing more?" and "trust cannot be implied. It must be proven." | primary read | as M1 | ✅ verbatim. Usable as the film's framing question |
| M4 | Co-developed with Google; the specification and "an initial reference implementation" were open-sourced; integration into Agent Pay's intent APIs "in the coming months" | primary read | as M1 | ✅. **Don't say it's live in Agent Pay**: the page says "coming months" (case study §3.3/§6.4 keeps this open) |
| M5 | "Mastercard's Agent Pay Acceptance Framework begins by registering and verifying AI agents before they are permitted to transact on the Mastercard network" | primary read | [Mastercard, "Agentic token framework: Driving trusted AI transactions"](https://www.mastercard.com/global/en/news-and-trends/stories/2025/agentic-commerce-framework.html), Oct 14, 2025 | ✅ verbatim. **Wording correction:** the case study's "must be registered and verified before they can transact" isn't on this page; the film uses the page's own words |
| M6 | The same page lists merchants' questions: "How can they distinguish between legitimate AI agents and malicious bots? How do they know the consumer authorized the agent to make the purchase? How can they know if the agent has carried out the consumer's instructions correctly?" | primary read | as M5 | ✅ verbatim |
| M7 | Web Bot Auth "builds on the IETF RFC 9421 standard"; Mastercard partnered with Cloudflare | primary read | as M5 | ✅. Context only, if used |
| M8 | Agentic tokens "can carry task-specific authority and be restricted by agent, merchant, category, spending limit, timeframe or usage rules. Combined with verifiable intent, they can connect a user's permission to the resulting transaction in a form that can be checked and enforced" | primary read | [Mastercard EEMEA newsroom, Signals report release](https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2026/august/building-trust-for-agentic-commerce-mastercard-signals-report-explores-the-path-forward/), Aug 2026 | ✅ verbatim. **"can"**: capability language; no mechanism, no default |
| M9 | "Before money moves, this layer can verify who is acting, what the user authorized and which limits apply, while maintaining an auditable record of the agent's activity" | primary read | as M8 | ✅ verbatim. It maps onto the receipt's lines (who / what / which limits) |
| M10 | Mastercard has not published a default for a category the consumer never configured, a merchant-restriction mechanism, or the record's signing scheme and fields | case study §3.2, §4, §4b; repo DD004/DD005/DD011 | — | ✅ **as absence**. Said as "hasn't published", not "hides" |
| M11 | Decision Intelligence Pro is a separate fraud-scoring system; no Mastercard source connects it to Agent Pay's flow | case study §2, §6.3 | — | ✅. One scope line only, if any |

## Part 2 — The build (v2), in the build's own record and on a live run

| # | Claim | Level | Evidence | Status |
|---|---|---|---|---|
| B1 | Built from public sources only: Mastercard releases, filings, standards bodies, and on-record reporting | repo record | README "What this is" | ✅ |
| B2 | One linear pipeline: input validation → registration/verification → ownership → permissions → Authorization Gate (unconfigured categories only) → Verifiable Intent record | repo record + live | README diagram; `orchestrator.py` | ✅ |
| B3 | **82 tests, 82 pass**, in a fresh, empty venv (Python 3.12), cache-free copy of v2 | live run | 2026-09-28 run | ✅. Say "82 tests, all passing" |
| B4 | The receipt (`IntentRecord`) has: `agent_id`, `consumer_id`, `category`, `merchant`, `amount`, `transaction_date`, `authorized_via`, `created_at` | live (source) | `src/intent_record.py` L28–35 | ✅ |
| B5 | It's written only for a completed purchase; a halted one leaves no receipt | repo record + tests | `test_happy_path.py` | ✅ |
| B6 | `agent_id` is vouched for by registration **and** verification, two separate reasons (`unregistered_agent`, `unverified_agent`) | live (demo) | demo scenarios 5–6; DD006 | ✅ |
| B7 | **The Morgan receipt.** Before round 2, Devon's agent claiming to buy for Morgan **completed**, and the receipt named Morgan as authorizing it. Nothing compared the agent's registered owner with the claimed consumer | repo record + live reconstruction | README #5, case study §4b ("confirmed directly against the running pipeline before the fix"); reconstructed 2026-09-28 in scratch with only Step 1b removed: `COMPLETED`, `consumer_id: morgan-02`, `authorized_via: authorization_gate` | ✅. **On screen it's labelled a reconstruction**, never a run of the shipped code |
| B8 | Now: the ownership check (Step 1b, DD009) rejects it outright, `agent_consumer_mismatch`, before permissions or the Gate run | live run | v2 | ✅ |
| B9 | **The category line.** On the original build, `Household_Staples`, $70, dated after Devon's window, **completed** through the Gate; the receipt read `category: Household_Staples`, `authorized_via: authorization_gate`. The same purchase as `household_staples` escalated `outside_timeframe` | live run | original zip, 2026-09-28 | ✅ |
| B10 | v2 compares category labels in one canonical spelling (DD012); that purchase now escalates `outside_timeframe` and never reaches the Gate | live run + tests | `test_category_normalisation.py` | ✅ |
| B11 | v2 deliberately does **not** map synonyms: `groceries` still goes to the Gate as unconfigured, because mapping synonyms would mean inventing a taxonomy Mastercard hasn't published | repo record + test | DD012; `test_synonym_is_still_unconfigured` | ✅. Frame as the method stopping where the record stops |
| B12 | `amount` / `transaction_date`: round 1 found a NaN or negative amount passed as ordinary; validation now rejects them | repo record + live | README #1–2; v2 live | ✅. **One line only** (W23 territory) |
| B13 | `authorized_via` records which path wrote the receipt: `within_configured_limits` or `authorization_gate` | live | `intent_record.py`; demo | ✅ |
| B14 | The Gate ships with **zero default criteria**; the demo's `< $75` rule exists only so the demo runs and isn't Mastercard's (DD004) | repo record | DD004; `demo.py` | ✅. Say once, as a deliberate boundary |
| B15 | **The merchant line.** v2 accepts `merchant`, carries it onto the receipt, and checks it against nothing: shoes (`footwear`) bought at `greenleaf-grocery` complete, and the receipt reads `merchant: greenleaf-grocery` | live run | v2, 2026-09-28 | ✅. Named scope, DD011: merchant restriction is a confirmed *dimension* (M8), but its mechanism isn't published |
| B16 | The build's receipt is a plain object with no cryptography, on purpose, because the signing scheme isn't published (DD005) | repo record | DD005 | ✅ |
| B17 | Three review rounds after the first build passed its own tests: adversarial (4 findings), second review (7), third review (2) | repo record | README "What building it surfaced" | ✅. Only if needed; not the spine |

## Part 3 — General claims (not about Mastercard's implementation)

| # | Claim | Level | Status |
|---|---|---|---|
| G1 | A signature or tamper-resistance protects a record **after** it's written (you can tell if it changed, and who wrote it). It can't make the facts inside it true; it seals whatever it's given | general property of digital signatures; RFC 9421's scope is message integrity and authenticity, not the truth of the content | ✅ **as a general statement**, phrased "a seal can only seal what it's handed". **Never** "Mastercard's Verifiable Intent can be wrong": the film doesn't claim anything about the real system's correctness |
| G2 | The move: read any record your system writes backwards, and for each line name the check that earned it; a line nothing checked is carried, not proved | the film's own method | ✅ (it's a method, not a fact) |

## Rejected or not to be said

| Claim | Why |
|---|---|
| "Agents must be registered and verified before they can transact" (as a quote) | Not verbatim on the primary page (M5); use the page's wording |
| "Verifiable Intent is live in Agent Pay" | The page says "in the coming months"; production status is unresolved (case study §6.4) |
| "Mastercard's system has this flaw" / "the real receipt could name the wrong person" | Nothing public supports it; the build is illustrative (README non-claims) |
| "The merchant check is missing" / "a gap in the build" | It's a documented scope boundary (DD011): the mechanism isn't public. Say "carried, not checked, because Mastercard hasn't published how that check works" |
| "A confident, wrong answer" | W23's phrasing; avoid it |
| DI Pro figures (20–300%, 85%) | Out of scope; separate system |
