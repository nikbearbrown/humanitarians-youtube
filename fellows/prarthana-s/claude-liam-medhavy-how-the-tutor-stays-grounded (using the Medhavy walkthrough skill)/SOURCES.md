# SOURCES.md — How the Tutor Stays Grounded in Your Textbook

## Authority: source code

**`medhavi-cancer` @ `b8b6c2135c179067748855dfbc4064dd19fcb2f7`** (2026-09-17, clean tree)

| File | What it covers |
|---|---|
| `lib/chat-orchestrator.ts` | retrieval, SOURCES prompt, SSE order, conversation merge |
| `lib/local-orama.ts` | whole-book index, keyword/hybrid search, exact lookup |
| `lib/chunk-content.mjs`, `scripts/index-build.mjs` | chunking and the index build |
| `app/api/analyze-context/route.ts` | search / no-search decision, keywords |
| `app/api/chat/route.ts`, `app/api/chat-navigation/route.ts` | chat routes; highlight on/off |
| `app/api/chat-suggestions/route.ts` | page-title chip templates |
| `lib/two-api-sse.ts` | client stream; nonexistent `/suggest` preflight |
| `components/ui/SideChatPanel.tsx` | cards, "Dive deeper", typing effect, footer, Clear |
| `components/LayoutWrapper.tsx` | panel mount; chip fetch by path |
| `lib/memory-client.ts`, `lib/user-identity.ts`, `lib/persona-engine.ts`, `lib/chat-system-prompt.ts` | memory calls, user key, learner profile, system prompt |
| `prompts/cancer-system.txt`, `.env.example` | tutor prompt and example config; production values not visible |
| `content/docs/Chapter5/*` | titles used in the capture plan |

**`medhavi-hub` @ `efcc3f5217d9c338e7e7d7a0bfb719c4b339bd44`** (clean tree)

| File | What it covers |
|---|---|
| `app/api/memory/stm/route.ts` | short-term memory GET/POST/DELETE |
| `app/api/memory/profile/route.ts` | learner profile |
| `components/AdminDashboard.tsx` | Header name span `:578-580` (redaction finding); View All Textbooks tab `:679-694, 756`; Open Textbook `:809`. Admin route only; the student dashboard isn't used |
| `brutalist.art/skills/make/medhavy-walkthrough/scripts/capture_admin.py` (toolkit, read only) | Mask regexes `:21-24`, name-masking contexts `:37-40`, leak counter `:46`, which is why a reel-local wrapper is needed |

## Synthesis

- `AI-TUTOR-SOURCE.md` (this folder): the approved pre-capture source-research snapshot, with line references.
- `FACTCHECK.md` addendum: the suggestion chips are page-title templates.

## Reference only (not a source of claims)

`humanitarians-youtube/fellows/medhavy/2026-09-18-cancer-textbook-walkthrough/` was used for the file formats, the proven capture step names ("View All Textbooks", "5. Oncogenes", "Open AI chat", "Close panel") and the hub card text "Cancer textbook".

Its claims that the answer "uses this chapter as context" and "SQLite memory keyed by session" are contradicted by current code and are not reused.

## Live sites (captured and observed 2026-09-24)

- `https://hub.medhavy.com`: the admin view, through the masking wrapper.
- `https://cancer.medhavy.com`: Chapter 5 and the "Ask this textbook" tutor.

**Captures:**

| Run | What it is | Status |
|---|---|---|
| `run-signin` | signed out | kept as footage |
| `run-pilot` | discovery | not in the cut |
| `run-book` | landscape source | locked |
| `run-portrait-test` | layout test | not in the cut |
| `run-portrait` | vertical source | locked |

- **On-screen answers:** these are the live tutor's own output, shown unedited.
- **Recorded observations:** in FACTCHECK.md.
- **Where the captures live:** locally, excluded from GitHub.

## Toolkit

`brutalist.art` @ `6a8380a`:
- `CLAUDE.md`
- `skills/make/medhavy-walkthrough/` (SKILL.md, `references/capture-and-coverage.md`, `scripts/capture_admin.py`, `save_session.py`)
- `RENDER-TARGETS.md`, `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`, `OUTRO-LOCK.md`
- `runtime/remotion/src/scenes.json` (library lookup, read directly)

Not used: stock footage, generated imagery, paid models, third-party recordings.
