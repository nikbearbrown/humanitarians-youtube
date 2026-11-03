# FACTCHECK.md — claude-liam-medhavy-cancer-textbook-walkthrough

Source = hub repo at `efcc3f5` (`README.md`, `DEVELOPER.md`, `docs/creating-a-new-textbook.md`) and the cancer textbook doc set `medhavy_documentation/medhavi-cancer-textbook/{ARCHITECTURE,API,USER_GUIDE}.md`. Screen = visible in `capture/run-signin.mp4` / `capture/run-book*.mp4` on 2026-09-18.

| Beat | Claim | Basis | Status |
|---|---|---|---|
| B00 | Hub layers a real-time AI assistant onto the textbook; answers cite where they came from | ARCHITECTURE.md (AI chat subsystem), API.md `POST /api/chat` SSE; Screen: "Top sources used" | PASS |
| B00 | Real screens, own account, names masked | `capture/*-actions.jsonl`, `capture/redaction.jsonl` | PASS |
| B01 | Knows the book and chapter (page context), what you already asked (memory), which course gave you the book (class enrollment); cites pages used | API.md: `analysisResult` page context + short-term SQLite memory keyed by `sessionId`; ARCHITECTURE.md long-term learner profiles per user; hub README classes assign textbooks; Screen B09/B10 | PASS |
| B02 | hub.medhavy.com is the front door | Screen: landing "Access Your Textbooks" | PASS |
| B03 | Sign in with email or username and password; nothing typed on camera | Screen: Clerk card "Email address or username"; action log has no `type` on run-signin | PASS |
| B04 | New users create an account, then get access from an instructor or admin | README "Access requests", "Classes & invites"; `DEVELOPER.md` §5.2 | PASS |
| B05 | Dashboard shows books you can open, pending, to request; admin sees every book | `DEVELOPER.md` §9 StudentDashboard ("quick stats"); admin `/dashboard` → `/admin` observed; Screen: View All shelf | PASS (student tiles described from source, not shown) |
| B06 | Book opens in its own tab; "Two Powerful Ways to Learn" | Screen: popup tab `cancer.medhavy.com`, home headings | PASS |
| B07 | Sidebar lists chapters and sections; headings, figures with source, underlined key terms, On this page | Screen: chapter 5 tree, Figure 5.2.1 "Source: NIH National Cancer Institute", outline | PASS |
| B08 | Cmd-K search, keyword and meaning together; hits in chapter 14 and 30 | ARCHITECTURE.md Orama hybrid (keyword + vector); Screen: 14.3 and 30.6 results | PASS |
| B09 | Panel "Ask this textbook"; suggested prompts; answer uses chapter as context; lists top sources first | Screen: panel heading, four suggested prompts, "Top sources used", "Dive deeper into all sources (10)"; API.md context object | PASS |
| B10 | Follow-up remembers the thread; ten-fold amplification | Screen (recon run): "using your example … 2 → 20 … 10-fold"; API.md memory | PASS |
| B11 | Simpler terms / analogy on request | Screen: answer-3 | PASS |
| B12 | Three-line summary; "AI can make mistakes" footer is the site's | Screen: answer-4, footer text | PASS |
| B13 | Night mode toggle | Screen: Toggle Theme → `dark` class | PASS |
| B14 | In one answer the top sources included angiogenesis sections | Recon run 2026-09-18 00:21: "Naked Antibodies", "Angiopoietin Functions in Angiogenesis" listed under Top sources for the oncogene question | PASS (observed in a pilot, disclosed as such) |
| B14 | Student dashboard counts not shown (admin account); instructor tools not shown | Observed redirect; single account | PASS |

Numbers spoken: none beyond "two copies … twenty … ten-fold" (from the answer on screen) and chapter numbers (on screen).
