# AI-TUTOR-SOURCE.md — How the Tutor Stays Grounded in Your Textbook

**Central question:** When I ask Medhavy's tutor a question, what connects its answer back to the textbook?

**Fellow:** Prarthana Shetty · **Narration:** Kokoro `am_onyx` (Liam), AI voice, disclosed
**Status:** PRE-CAPTURE SOURCE-RESEARCH SNAPSHOT (2026-09-23, approved).
- This is the code research that informed the finished video.
- It was written before any capture, render or narration existed, and it is preserved unchanged as that snapshot.
- No product code was changed.
- What the live site actually showed, and how each claim was reconciled, is in FACTCHECK.md. The production record is in README.md and QC-REPORT.md.

## 0. What was read

| Repo | Commit | Tree |
|---|---|---|
| `medhavi-cancer` (the textbook app; the tutor lives here) | `b8b6c21` (2026-09-17) | clean |
| `medhavi-hub` (sign-in, access, memory API) | `efcc3f5` (2026-09-05) | clean |
| `brutalist.art` (toolkit) | `6a8380a` (2026-09-20) | — |

The authority is the **current source code**, not the older docs. Line numbers refer to the commits above. Every path below is relative to `medhavi-cancer/` unless it starts with `medhavi-hub/`.

**Reference only:** `humanitarians-youtube/fellows/medhavy/2026-09-18-cancer-textbook-walkthrough/`. Its FACTCHECK makes two claims that the current code **contradicts** (see §7). Do not reuse them.

---

## 1. The grounding flow, step by step

```
Student types question
   │
   ▼
[1] POST /api/analyze-context      decide: search or not? extract keywords
   │
   ▼
[2] POST /api/chat                 (server) retrieve textbook passages
   │    ├─ search the raw question          (top 10)
   │    ├─ search the extracted keywords    (top 8)
   │    ├─ exact lookup for "equation N.N" / "problem N"
   │    ├─ de-duplicate, rank by score, keep top 10
   │    └─ fallbacks if nothing was found
   │
   ▼
[3] Build prompt:  system instructions + learner profile + routing note
   │               + recent conversation turns
   │               + "SOURCES: Source 1 … Source N" + "QUESTION: …"
   │
   ▼
[4] Stream over SSE:  "sources" event FIRST → then answer "delta" events → "done"
   │
   ▼
[5] Panel shows "Top sources used:" cards above the answer, then types the answer out
   │
   ▼
[6] After the answer finishes: save this turn to the hub's memory; update learner profile
```

### Step 1: Should we search? (`app/api/analyze-context/route.ts`)

- The client sends the message and `lastMessages` (`lib/two-api-sse.ts:132-139`). The server reads **only `message`** (`route.ts:127`). No page, chapter or URL is sent or used.
- `isConversationalMessage` (`:13-42`) flags greetings, thanks, "ok", "who are you", "what did I ask", "help", and any message of 3 characters or fewer as conversational.
- `extractKeywords` (`:44-120`) lowercases the text, strips punctuation, drops stop-words and keeps up to 10 unique tokens (`:119`).
- Response (`:138-152`): `needs_search` is true only if the message is not conversational **and** has at least one keyword. `search_plan` is `[{ keywords, tags: ["textbook"] when TEXTBOOK_ONLY, limit: 8 }]`. `follow_up_questions` is always `[]`.

### Step 2: Retrieval (`lib/chat-orchestrator.ts:170-220`, `lib/local-orama.ts`)

- The client streams from **`/api/chat`** (`lib/two-api-sse.ts:184-196`). That route calls `streamChatOrchestrated` with `enableHighlightSource: false` (`app/api/chat/route.ts:23-30`).
- If `needs_search !== false` (`chat-orchestrator.ts:174`), `searchWithPlan` (`:137-159`) runs:
  1. `localSearch` on the **raw question**, limit 10 (`:140`)
  2. `localSearch` on each plan's keywords, limit 8 (`:143-154`)
  3. It de-duplicates by chunk id, sorts by score and keeps the **top 10** (`:156-158`).
- If that finds nothing and the routed "expert" has preferred tags, it retries once with those tags (`:177-188`).
- In TEXTBOOK_ONLY mode, anything that isn't tagged `textbook` or that lives under `/course*` is dropped (`:190`, `:38-48`).
- **Exact identifier lookup** (`:194-207`, `local-orama.ts:201-282`): if the question names "equation 1.13" or "problem 7" (optionally with "chapter N"), matching chunks are put **first**. This runs whether or not `needs_search` is true.
- **Scope fallback** (`:209-220`): if search ran and still found nothing, it searches the fixed phrase `"textbook course scope introduction overview"` and keeps up to 3 hits. The source cards for such a question will be generic intro/overview pages, not passages about the question.

**The search engine** (`lib/local-orama.ts`):
- It is an in-process Orama database built from `.orama/docs.json` (`:124-133`, `:292-333`). If that file is missing, it chunks `content/docs/**/*.md(x)` at runtime (`:135-185`).
- The index is built by `scripts/index-build.mjs`, which runs on `dev`, `build` and `postinstall` (`package.json:6-10`).
- Fields searched are `title`, `section`, `keywords` and `content`, with boosts 3 / 2 / 5 / 1 (`:349-355`).
- **Hybrid mode** (keyword + meaning) is only on when `LOCAL_ORAMA_HYBRID=1` and the index contains embeddings (`:80`, `:297-298`, `:360-371`). The weights are text 0.6, vector 0.4 (`:367`), and the query embedding comes from `text-embedding-3-small` by default (`:81`, `:87-96`). Otherwise the search is keyword-only (`:380-386`). `.env.example:10` sets it to 1, but **the production setting is not visible in the repo**.
- **Chunking** (`lib/chunk-content.mjs`):
  - Text is split at `##`/`###` headings (`:17-42`), then packed into roughly 1,100-character paragraph chunks (`:14`, `:163-165`).
  - Each numbered exercise gets its own chunk (`:150-161`).
  - Equation tags and problem numbers are lifted into `keywords` (`:89-116`).
- Each chunk handed to the model is capped at 4,000 characters (`local-orama.ts:14`, `:400`). Since chunks are about 1.1 kB, they normally go through whole.
- The whole book is one index. **No filter restricts results to the chapter the student has open.**

### Step 3: What the model receives (`chat-orchestrator.ts:222-288`)

The messages go in this order (`:279-285`):

1. **System: base tutor prompt.** Loaded from `CHAT_SYSTEM_PROMPT_FILE` or `CHAT_SYSTEM_PROMPT` (`lib/chat-system-prompt.ts:25-40`). `.env.example:15` points to `prompts/cancer-system.txt` (the "HELIX" tutor prompt). Production's value isn't in the repo.
2. **System: persona prompt.** This is a per-learner style hint ("step-by-step", "example-first", "brief", "deep"). It is built from keyword signals in past questions (`lib/persona-engine.ts:25-60`, `:71-88`).
3. **System: routing note.** A regex picks one of six "experts" (mechanism / diagnostics / treatment / definitions / navigation / general) and adds guidance text (`:75-135`, `:237-243`). The note always says: *"cite source-backed facts, avoid fabrication, and explicitly mark uncertainty when evidence is missing"* (`:242`). This is an **instruction** to the model, not an enforcement mechanism.
4. **Conversation turns.** Up to the last 20 messages (see §5).
5. **User message** (`:227`):
   ```
   SOURCES:
   Source 1 [textbook]: <section title> (<url>)
   <chunk text>

   Source 2 [textbook]: …

   QUESTION:
   <student's question>
   ```
   If nothing was retrieved, the `SOURCES:` block is left out entirely and only `QUESTION:` is sent.

The model is `OPENAI_MODEL`, defaulting to `gpt-4o-mini` (`:8`). Temperature 0.35 applies only to gpt-4/3.5 models (`:11`, `:286`). **Don't name the model on screen unless it's verified in production.**

The base prompt also tells the model: *"Do NOT invent page numbers, section numbers, or quotes you cannot verify"* (`prompts/cancer-system.txt:83`). It also asks the model to end with a `[do you want to learn more about this?](url)` link when helpful (`:160-163`). Nothing in the code makes the model cite `Source N`, and nothing checks the answer against the sources afterwards.

---

## 2. What the source cards actually are

**Where they come from:** the server sends the `sources` SSE event **before it calls the model** (`chat-orchestrator.ts:252-265` comes before the `openai.chat.completions.create` call at `:277`). The cards are the same `effectiveResults` array whose texts were put into `SOURCES:` (`:220-225`). So they show exactly what retrieval supplied as context, in the same order, and they were fixed before a single word of the answer existed.

**Payload per card** (`:255-263`): `id`, `title` (the chunk's section heading), `url` (the page), `tag`, `score`, `fullContent` (the chunk text, up to 4,000 chars) and `snippet` (the first 200 chars).

**How they render** (`components/ui/SideChatPanel.tsx`):
- The label is **"Top sources used:"** (`:872`). That is the product's wording. The cards are retrieval results, not a record of what the answer used.
- The first **3** cards are shown (`:120`, `:877`). If there are more, the button reads **"Dive deeper into all sources (N)"** (`:890-903`), and N can be up to 10.
- Each card is 180×110 px and shows a tag badge ("Textbook"), the section title and the start of the chunk text, faded at the bottom (`:37-110`).
- The retrieval **score is not displayed**. `showScores` is passed in but never used inside `SourceCard`.
- Clicking a card with a URL navigates **within the textbook** to that page (`:79-83`, `:203-240`).
- The cards sit **above** the answer bubble text in the same message (`:870-906`, then the answer at `:908-932`).
- A "Most Relevant" badge exists (`:102-106`), but it needs a `highlight_source` event. `/api/chat` disables that (`app/api/chat/route.ts:29`). Only `/api/chat-navigation` enables it (`app/api/chat-navigation/route.ts:29`), and the client never streams from that route. **Expect no "Most Relevant" badge.**

**What the cards do NOT show:**
- which card(s) the model actually drew on
- whether a sentence in the answer is supported by any card
- that every card is on-topic (keyword/hybrid ranking can surface off-topic sections; the reference pilot saw angiogenesis sections for an oncogene question)

**When there are no cards:**
- if the message looked conversational (Step 1), no search runs, so no cards appear and the model answers from instructions and conversation only
- if search returned nothing and the scope fallback also returned nothing

**Safe wording:** *"These are the textbook passages the retrieval step surfaced and supplied as context for the answer."*

---

## 3. How streaming works

1. The panel adds an empty assistant bubble and shows **"AI is thinking..."** with bouncing dots (`SideChatPanel.tsx:514-522`, `:910-929`).
2. The client makes two sequential requests: `/api/analyze-context` (JSON), then `/api/chat` (`text/event-stream`) (`lib/two-api-sse.ts:132-196`).
   - Before the chat request, it tries a navigation preflight to `/api/chat-navigation/suggest` (`:149-180`). **No such route exists.** Only `app/api/chat-navigation/route.ts` does, so the preflight should fail quietly and the page should not auto-switch. Verify this live (§6).
3. The server writes `data: {json}\n\n` lines (`chat-orchestrator.ts:248`) in this order:
   - `sources` (if any)
   - `moe` (the routing info, which is logged, not shown)
   - `related_queries` (only if the analyzer returned some; currently always empty)
   - many `delta` events carrying text fragments as the model generates them (`:290-295`)
   - `done` (`:321`), or `error` (`:326`)
4. The client parses these lines and dispatches each type (`two-api-sse.ts:202-337`):
   - `sources` → attach the cards to the bubble (`SideChatPanel.tsx:581-585`)
   - `delta` → append to a typing buffer
5. The **typing effect is client-side**: the buffer is released 3 characters per animation frame (`:534-572`). What's on screen is paced by the browser, not a live view of token timing. On `done`, any remaining buffer is flushed at once (`:596-610`).
6. Only after the answer finishes do the copy / regenerate / thumbs-down buttons appear (`:938-963`). The footer always reads **"AI can make mistakes. Please verify important information."** (`:1046-1048`).

Rate limit: 30 answer requests per user per 5 minutes, held in memory per process (`lib/rate-limit.ts:5-7`). Both chat routes also require verified textbook access (`app/api/chat/route.ts:11-12`).

---

## 4. Retrieval vs. the open chapter: an explicit correction

- Nothing in the analyze → chat path carries the current page. The client never sends `pathname` to either endpoint (`two-api-sse.ts:135-138`, `:190-195`), and `LayoutWrapper` mounts the panel without page props (`components/LayoutWrapper.tsx:273-276`).
- The search runs over the **whole book's index** (§1 Step 2).
- **The one page-aware piece** is the **suggested-prompt chips** shown before the first message. These come from `/api/chat-suggestions` with `{ path }` (`LayoutWrapper.tsx:50-80`). They change with the page. The answer's retrieval does not.

So: **not grounded only in the open chapter.** The cards may come from any chapter or appendix.

---

## 5. Conversation-context behavior (memory)

Two sources of prior turns are merged before the model call (`chat-orchestrator.ts:228-232`).

**A. Client history.** This is the panel's own message list, stored in the browser's `localStorage` per user per textbook (`SideChatPanel.tsx:362-408`). It is sent as `lastMessages` (`:524-527`, `:752`). The server cleans it (roles user/assistant only, drops "as an AI language model"-style replies, drops a trailing duplicate of the current question) and keeps the last `STM_MAX_TURNS × 2` = **20** messages (`:50-68`, `:17`).

**B. Server short-term memory (STM)** in the hub.
- The key (`userKey`) is `hub:<userId>` when the hub verifies the `textbook_session` cookie. Otherwise it is `token:<sha256 of cookie>`, and failing that `anon:<sessionId>` (`lib/user-identity.ts:57-92`, `chat-orchestrator.ts:228`).
- It is fetched via `GET {hub}/api/memory/stm` (`lib/memory-client.ts:32-38`). That endpoint reads the Supabase table `chat_memory_turns`, filtering **only by `memory_subject`**, newest first, then reversed (`medhavi-hub/app/api/memory/stm/route.ts:26-37`).
- After the answer finishes, the question and full answer are appended (`chat-orchestrator.ts:309-315`, `memory-client.ts:40-54`). The hub trims to the latest `maxTurns × 2` rows (`stm/route.ts:69-76`). It records `textbook_origin` but **GET does not filter on it**.
- The **learner profile** is updated from the question's wording (`:317-318`, `persona-engine.ts:25-60`).

**Merge:** `[...stm, ...clientContext].slice(-20)` (`:232`). Because the same recent turns can exist both in STM and in localStorage, the merged context may repeat turns. This is observed from code only. It affects prompt size, not the claims below.

**Clearing:** the panel's clear button empties localStorage and calls `/api/chat/clear`, which deletes this user's STM rows (`SideChatPanel.tsx:481-491`, `app/api/chat/clear/route.ts`, `stm/route.ts:96-106`). **It does not reset the learner profile.**

**What this means for grounding, and why it's the honest riff for the follow-up beat:**
- **Retrieval uses only the current message.** It does not use the conversation. Prior turns are not sent to analyze-context (it ignores them) and are not added to the search term.
- So for a follow-up like *"explain that in simpler terms"*:
  - the keywords are roughly `explain, simpler, terms`, and the source cards may be **unrelated** to the topic
  - or the message may be judged conversational, in which case **no cards appear**
- The answer can still stay on topic because the model sees the earlier turns. In that case the **conversation**, not the new cards, is carrying the continuity, and the earlier answer's cards are the relevant ones to check.

**Legacy note:** `lib/chat-memory/sqlite.ts` exists but is **not imported anywhere**. The live memory path is the hub's Supabase API.

---

## 6. What to verify in the live browser capture

You sign in yourself. I won't type credentials. Record the account type (student or admin) and say which one on screen.

| # | Verify | Why | If it fails or can't be shown |
|---|---|---|---|
| V1 | Ask a content question (e.g. a suggested chip). "Top sources used:" cards appear **before or while** answer text types in | Confirms the sources-first stream order (§3) | Report the observed order exactly |
| V2 | Count the cards: 3 visible, and "Dive deeper into all sources (N)" with N ≤ 10. Expand it once | Confirms §2 rendering | Note the actual N |
| V3 | Open one card; it navigates to a textbook page in the same tab. Show that page's section heading matching the card title | Makes the "inspect the source" point real | Document it if the click does nothing |
| V4 | Do any cards come from a **different chapter** than the page you're on? Ask from, say, a Chapter 5 page about a Chapter 14 topic | Shows search spans the whole book (§4) | If all cards match the open chapter, don't claim cross-chapter; just say "the book" |
| V5 | Are any cards visibly off-topic? | The honest riff (§2) | If none are, don't invent one |
| V6 | Follow-up "explain that in simpler terms": do cards change, go off-topic or disappear, while the answer stays on topic? | Shows retrieval is per-message and continuity comes from conversation (§5) | Report what happened; don't force it |
| V7 | Send "thanks" or "hi": expect **no source cards** | Shows search is skipped for conversational messages | Note it if cards do appear |
| V8 | No "Most Relevant" badge; page does not auto-switch after asking | Confirms §2/§3 code reading | If either happens, drop the claim and re-read the code |
| V9 | Footer "AI can make mistakes. Please verify important information." is legible in frame | Required on-screen caveat | Always keep it in frame |
| V10 | Suggested chips differ between two different pages | Confirms the only page-aware piece (§4) | Say "suggested prompts" only |
| V11 | DevTools → Network (optional, no edits): `/api/analyze-context` then `/api/chat` (event-stream); a 404 on `/api/chat-navigation/suggest` | Hard evidence for §3 | Skip it if it risks showing a cookie or token on screen |
| V12 | Answer ends with a "do you want to learn more about this?" link | Prompt behavior (§1 Step 3), not guaranteed | Don't narrate it unless it's seen |
| V13 | Student-only screens (dashboard counts) | Only possible with a student account | If you use admin, show the shelf and say "admin view" |

**Redaction:** mask emails, names and `CLS-` codes before recording (per `SKILL.md` §0). The panel shows "U" and "AI" avatars, not names, but check the hub header and the dashboard.

---

## 7. Limitations and claims we must NOT make

**Do not say:**

1. "The tutor only uses the chapter you're reading." Retrieval is whole-book; only the prompt chips are page-aware (§4).
2. "The source cards show which passages the answer relied on" / "the answer cites these cards." The cards come before generation, and nothing links sentences to cards (§2). The UI's own label says "used"; we must not repeat that as a fact.
3. "Grounding guarantees the answer is correct."
4. "The AI can't hallucinate" / "it only answers from the book." The model also sees its instructions, a learner profile and prior conversation. Nothing verifies the output.
5. "Every answer has sources." Conversational messages skip search, and some questions return only generic scope pages (§1).
6. "It finds the best passage" / "the most relevant one is highlighted." The ranking is keyword or keyword+vector scoring; the highlight is disabled on the live route.
7. "It uses AI embeddings / semantic search" as a certainty. Hybrid depends on a production env flag we can't see. "Searches the textbook" is always safe.
8. "It was trained on your textbook." Nothing is trained; passages are retrieved per question.
9. A specific model name (e.g. GPT-4o-mini), unless confirmed in production.
10. From the reference reel, do not reuse:
    - "answer uses chapter as context" / "page context" (the analyzer ignores the page)
    - "SQLite memory keyed by sessionId" (the live memory is the hub API, keyed by user)
11. "Clearing the chat erases everything the tutor knows about you." The learner profile remains (§5).
12. Memory is scoped per textbook. The STM read filters only by user key; whether turns from other Medhavy books can mix in is **unverified**, so don't say either way.

**Known limitations to state on screen or in the Verdict:**

- Source cards are retrieval results, not a citation audit.
- Follow-up questions are searched on their own words.
- The typing speed is a UI effect.
- Production config (model, hybrid flag, system-prompt file) is inferred from `.env.example`, not observed.

---

## 8. Safe narration claims

Opening (required, verbatim):
> "Hi, I am Prarthana Shetty, and this video is about how the tutor stays grounded in your textbook."
> "This walkthrough uses AI narration to present my investigation of how that grounding works."

(Do not suggest the voice is Prarthana's. If named, it's "an AI narrator voice.")

Body claims that the code supports:

- "When you ask a question, the system first searches the textbook for passages related to your words."
- "It searches the whole book, not just the page you have open."
- "The passages it finds are placed into the model's context, labeled as sources, alongside your question."
- "The model also receives its tutor instructions and your recent conversation, so those shape the answer too."
- "Before any of the answer appears, the textbook sends those passages to your screen."
- "These are the textbook passages the retrieval step surfaced and supplied as context for the answer."
- "The cards don't tell you which sentence came from which passage, so they're a place to check, not proof."
- "You can open a card and read the section it came from."
- "The answer then streams in, piece by piece."
- "For a follow-up, the search runs on your new words. If the new cards look unrelated, the earlier answer's sources are the ones to check."
- "A simple 'thanks' doesn't trigger a search, so no sources appear."
- "Grounding makes the answer more connected to the textbook and easier to inspect. It doesn't make it automatically correct."
- "The site says it too: AI can make mistakes. Please verify important information."
- Your Turn: "Ask your textbook a question, then open one of the sources it lists and check the answer against it."

Conditional (only if V-check observed):
- V4 → "Here, one of the sources came from a different chapter."
- V5 → "One of these sources is off-topic, which is a reminder that search isn't understanding."
- V6 → describe exactly what the follow-up's cards did.
- V7 → "No sources for 'thanks'; the tutor skipped the search."
