# RIFF.md — Liam, in for Bear (evidence-led)

| Beat / window | Visible observation | Interpretation (source) | Next experiment |
|---|---|---|---|
| B02–B04 / run-signin | Landing; Clerk sign-in; Clerk sign-up. Nothing typed. | Identity lives in Clerk; the hub holds roles as metadata (`DEVELOPER.md` §3). | Sign up a fictional student on a dev tenant and film the onboarding intake. |
| B05 / run-book 3.3–15.0 | Admin shelf with Open Textbook; click opens a new tab. | Token minted per book, 24 h (§4.1). Student tiles exist in `StudentDashboard` (§9) but not on this account. | Film the same beat from a student account. |
| B06 / p2 1.6–14.7 | Book home: "Two Powerful Ways to Learn", getting started, beta disclaimer. | Middleware verified the token and set `textbook_session` (creating-a-new-textbook §3). | Reload after hub logout: the page should bounce (§4.4). |
| B07 / p2 14.7–33.6 | Chapter 5 tree; 5.2 with figure "Source: NIH", underlined terms, On this page. | Fumadocs MDX; KaTeX/Mermaid available (ARCHITECTURE.md). | Hover an underlined term to test the glossary popup (articles API). |
| B08 / p2 34.0–41.6 | Cmd-K; "Warburg effect" → 14.3 and 30.6 with snippets. | Orama hybrid search. | Search a paraphrase ("aerobic glycolysis") to see the vector half work. |
| B09 / p2 43.0–63.3 | Panel with four section-specific prompts; question typed; answer streams; "Top sources used" first. | Retrieval over the chapter + SSE stream (API.md). Pilot run: top sources drifted to angiogenesis sections for this question. | Ask the same question from a chapter-4 page and compare the sources. |
| B10 / p2 63.4–80.8 | Follow-up uses "your example", 2 → 20, "10-fold". | Short-term memory keyed by session (API.md, hub memory API). | Clear the panel and re-ask: the numbers should be gone. |
| B11 / p2 80.9–97.8 | Simpler-terms + analogy answer. | Prompt shape steers the same retrieval. | Ask for a step-by-step derivation on a KaTeX-bearing section. |
| B12 / p2 97.9–112.3 | Three-line summary; "AI can make mistakes" footer. | The disclaimer is the site's. | Compare the summary against 5.7 Summary in the book. |
| B13 / p2 114.2–124.6 | Dark mode. | Reading comfort only. | — |

**Verdict material:** works on screen: sign-in path, handoff, chapters, search, tutor with sources and memory, night mode. Watch: retrieved sources can wander; read them. Not shown: student dashboard tiles, instructor tools, glossary popups.
