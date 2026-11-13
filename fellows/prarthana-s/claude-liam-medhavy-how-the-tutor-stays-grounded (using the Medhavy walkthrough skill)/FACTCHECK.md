# FACTCHECK.md — How the Tutor Stays Grounded in Your Textbook

**Status: FINAL (2026-09-29).** Every narrated claim is reconciled against the code and the locked footage.

**Basis:**
- **Code:** `AI-TUTOR-SOURCE.md` (approved 2026-09-23) against `medhavi-cancer@b8b6c21` and `medhavi-hub@efcc3f5`. Paths are relative to `medhavi-cancer/` unless marked otherwise.
- **Screen:** the locked captures `run-book` (landscape) and `run-portrait` (vertical source), with `run-pilot` as discovery.

**Status key:**
- **CODE** — code-derived; supported by source code. Server-side behaviour (retrieval, prompt assembly, memory) is code-only by nature and can't be seen on screen.
- **OBSERVED** — seen in the locked footage.
- **CODE + OBSERVED** — both.
- **script** — authored wording or an approved decision, not a product claim.

## Final claims

Each claim is the final narration, landscape unless marked.

| Beat | Claim | Code basis | Screen evidence | Status |
|---|---|---|---|---|
| B00 | Required opening, verbatim, first; AI narration disclosed | FELLOWS-SUBMISSION.md | On-screen running text "AI narration (Kokoro am_onyx)" | script |
| B01 | The sources on screen don't "prove" the answer; they "supply context for" it | `chat-orchestrator.ts:220-227`; no sentence-to-source mapping exists | — | CODE |
| B02 | Signed in myself before recording; nothing typed on camera | — | `run-signin` action log has no `type` step; the sign-in card is empty | OBSERVED |
| B03 | Signed in through the admin view, which gives access to the textbook shelf; open the Cancer textbook | `AdminDashboard.tsx:679-694, 756, 809` | `run-book` hub tab: Admin Dashboard → View All Textbooks → Cancer textbook → Open Textbook; header masked | CODE + OBSERVED |
| B04 | Chapter five, Oncogenes: the introduction page | `content/docs/Chapter5/meta.json`, `1_Introduction.mdx` | Sidebar → 5.1 Introduction to Oncogenes | CODE + OBSERVED |
| B05 | The tutor is "Ask this textbook"; its suggested questions come from this page's title | `LayoutWrapper.tsx:273-276`; `chat-suggestions/route.ts:19-41, 50-57` (fixed templates, not AI) | Chips read "Explain 5.1 Introduction to Oncogenes in simple terms." and similar (V10) | CODE + OBSERVED |
| B05 | …but when you ask something, the search runs across the whole textbook | `analyze-context/route.ts:127`; `two-api-sse.ts:135-138, 190-195` (no page sent); whole-book index `local-orama.ts:335-407` | Cards come from Ch.5.2, Ch.12, Ch.25 while 5.1 is open (V4) | CODE + OBSERVED |
| B06 | The cards arrive just before the answer text starts | Server sends sources (`:252`) before the model call (`:277`) | Cards and "Dive deeper (10)" visible about 0.2 s (`run-book`) / 0.3 s (`run-portrait`) before answer text (V1) | CODE + OBSERVED |
| B06 | These are the textbook passages the retrieval step surfaced and supplied as context for the answer | `chat-orchestrator.ts:220-225, 252-265` (the same results build SOURCES and the cards) | — | CODE |
| B07 | The cards don't say which sentence came from which passage | No citation mapping; the UI shows cards only (`SideChatPanel.tsx:870-906`) | The cards carry no sentence markers | CODE + OBSERVED |
| B08 | This opens all ten retrieved sources | `SideChatPanel.tsx:120, 877, 890-903` | "Dive deeper into all sources (10)" (V2); about 1.5 cards fit the panel, so "three show at first" is never said | CODE + OBSERVED |
| B08 | Here, some are less relevant than others | — | "Naked Antibodies" (Ch.25) and "Angiopoietin Functions in Angiogenesis" (Ch.12) for a gene-amplification question (V5) | OBSERVED |
| B09 | Opening one takes me to Gene Amplification, a different page from the one I was reading | `SideChatPanel.tsx:79-83, 203-240` | 5.4.2 card → 5.4 page → "On this page" → 5.4.2; the snippet matches the section's first sentence (V3, V4) | CODE + OBSERVED |
| B10 | A real question triggers a search of the textbook for related passages | `analyze-context/route.ts:13-42, 138-152`; `chat-orchestrator.ts:174-189` | "Thanks!" skipped search (V7, pilot only) | CODE (supported by V7) |
| B10 | Those passages are handed to the model as context | `chat-orchestrator.ts:227, 284` | — | CODE |
| B10 | The model also receives its tutor instructions and recent conversation context | `:279-283` | — | CODE |
| B10 | The same passages are shown to you, so you can check them | `:252-265` | Cards shown and openable | CODE + OBSERVED |
| B11 (landscape) | A follow-up can make sense because the model also receives recent conversation context | `:228-232, 283` | `run-book`: "Yes — here's a simpler way to think about gene amplification" (V6) | CODE + OBSERVED |
| B11 (vertical) | For a follow-up, the model still receives recent conversation context | `:228-232, 283` | `run-portrait` shows the question and cards; the reply body is below the frame | CODE (portrait footage doesn't show the reply) |
| B11 (both) | The search runs again on the new question, and here the new cards drift off topic | `analyze-context/route.ts:127, 135`; `chat-orchestrator.ts:176` | New cards "Angiopoietin Functions in Angiogenesis" (Ch.12) and "The Two-Hit Hypothesis" (Ch.4) in both takes (V6) | CODE + OBSERVED |
| B11 (both) | …so source cards are something to inspect, not automatic proof that every retrieved passage is relevant | Follows from the above | — | script |
| B12 | "AI can make mistakes. Please verify important information." | `SideChatPanel.tsx:1046-1048` | Legible in every panel frame (V9) | CODE + OBSERVED |
| B13 | Generated with textbook passages in its context, and those passages are exposed; more connected and easier to verify; not automatically correct; the cards are a place to check, not proof | AI-TUTOR-SOURCE.md §2, §7 | Verdict "Observed" line matches V1/V3/V5 | CODE + OBSERVED |
| B14 | Your Turn | — | — | script |
| B15 | Regular outro | SKILL.md §3, OUTRO-LOCK.md | — | script |

## Not claimed (AI-TUTOR-SOURCE.md §7 and the 2026-09-23 wording rules)

The narration does not claim any of the following:

- that answers are grounded only in the open chapter
- that the open page drives retrieval
- that the cards prove what the answer relied on
- a per-sentence citation
- that grounding guarantees correctness
- that the AI cannot hallucinate
- that every answer has sources
- that the tutor was trained on the textbook
- that the cards are the "best" passages
- a model name
- that memory is "per user"
- the UI label "Top sources used" (it isn't spoken at all)
- anything about a student dashboard (the account is admin; none is shown or described)
- the page-context or SQLite claims from the 2026-09-18 reel

These behaviours were checked on camera and were **not narrated**:
- **No "Most Relevant" badge appeared (V8).**
- **No automatic page switch occurred (V8).**
- **"Thanks!" showed no cards (V7, pilot only; not in the cut).**

Cards from another chapter (V4) and less-relevant cards (V5) were observed, and are narrated modestly in B05, B08, B09 and B11.

## Addendum (planning, 2026-09-23; approved)

The suggestion chips are **fixed templates using the current page title**, not AI-generated (`app/api/chat-suggestions/route.ts:19-41`). This is the one clear way the open page influences the tutor interface.

## Redaction finding (2026-09-23), resolved

The admin header renders the account's first name as one word (`medhavi-hub/components/AdminDashboard.tsx:578-580`). The toolkit's stock mask needs two or more capitalised words in list or card containers (`capture_admin.py:23, 37-40`), and its leak check counts only emails and codes (`:46`). So the stock driver would neither mask nor detect this name.

**Resolved:** the reel-local wrapper `capture/capture_masked.py` was built and self-tested, and used for every capture. See CAPTURE.md "Observed result".

---

## History: pilot results (run-pilot, 2026-09-24)

This is the historical record. The final statuses are in the table above.

| Check | Result | Narration impact |
|---|---|---|
| V1 | Verified: the cards and "Dive deeper into all sources (10)" are visible for about 0.3 s while "AI is thinking..." still shows | B06 says "The cards arrive just before the answer text starts." |
| V2 | Verified: N = 10. Only about 1.5 cards fit the panel width, because the row is clipped horizontally | B08 says "This opens all ten retrieved sources." **Never** say "three show at first." |
| V3 | Verified: the 5.4.2 Gene Amplification card opens the 5.4 page, and "On this page" leads to 5.4.2. The card snippet matches the section's first sentence. | B09 is included |
| V4 | Verified: the source is on 5.4 while 5.1 was open; other cards come from Chapter 12 and Chapter 25 | B09 says "a different page from the one I was reading" |
| V5 | Verified: "Naked Antibodies" (Chapter 25) and "Angiopoietin Functions in Angiogenesis" (Chapter 12) appeared for a gene-amplification question | B08: "Here, some are less relevant than others." Kept low-key, not framed as a defect. |
| V6 | Not observable in the pilot: the follow-up's reply top was off-screen. The answer visibly built on the first one (HER2 example). | Resolved in `run-book` (below) |
| V7 | Verified: "Thanks!" got no source cards | Not narrated; evidence only |
| V8 | Verified: no "Most Relevant" badge; the URL stayed on 5.1 | Not narrated |
| V9 | Verified: the footer warning is legible | B05, B12 |
| V10 | Verified: chips read "Explain 5.1 Introduction to Oncogenes in simple terms." and so on | B05 |
| M1 | No visible memory interference: the panel started empty and neither answer referred back to earlier turns | — |

Also seen on screen, not narrated:
- The answer ends with the "do you want to learn more about this?" link and uses the phrase "Your sources mention".
- Asterisks show literally during streaming and in "*MYC*".
- The chat bubble button overlaps the send arrow.

These were re-confirmed in `run-book`.

## History: corrected landscape capture (run-book, 2026-09-24)

- **Redaction:** clean.
  - The header reads "Admin account" from its first rendered frame (about 1.6 s) until it scrolls out of view (about 11 s).
  - Only textbook cards and aggregate counts appear on screen. No names, emails or codes.
- **Consistent with the pilot:**
  - V1: the cards and "Dive deeper (10)" arrive about 0.2 s before the answer text.
  - V2: N = 10.
  - Same first cards: Naked Antibodies, then 5.2.2.
  - V3/V4: the card opens 5.4, and "On this page" leads to 5.4.2.
  - V8: no badge and no automatic page switch.
  - V9: the footer is legible.
  - V10: chips follow the page title.
- **V6: VERIFIED.**
  - The follow-up question and reply are on screen.
  - New cards: "Angiopoietin Functions in Angiogenesis" (Chapter 12) and "The Two-Hit Hypothesis" (Chapter 4), plus "Dive deeper (10)".
  - The reply builds on the first answer: "Yes — here's a simpler way to think about gene amplification", followed by a gas-pedal analogy.
- **M1:** no visible reference to the pilot conversation in either answer.
- **Streaming:** it types visibly for about 1.5 s. Then the rest of the first answer appears at once, and the panel jumps to its end. The same thing happened in the pilot.

## History: portrait-source capture (run-portrait, 2026-09-24)

- **Redaction:** clean. The header reads "Admin account" from its first rendered frame (about 2.7 s in this take). No names, emails or codes.
- **Same as `run-book`:**
  - V1: cards and "Dive deeper (10)" appear about 0.3 s before the answer text.
  - First cards: Naked Antibodies, 5.2.2.
  - V2: N = 10.
  - V3/V4: 5.4.2 → 5.4 → 5.4.2 section.
  - V9: the footer is legible.
- **V6 (portrait):**
  - The follow-up question, "AI is thinking…", the new cards (Angiopoietin, Two-Hit) and "Dive deeper (10)" are all visible.
  - The reply body stays below the 720-px panel edge. Only its first words ("Yes — her") peek in.
  - So vertical B11 says only that the model "still receives recent conversation context" (CODE), not that the answer is shown building on it.
- **M1:** no visible reference to earlier runs.
