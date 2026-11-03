# enterprise-search

Ask an assistant something that lives in the company's own knowledge — a
policy, a prior decision, a project by name — and it's tempting to think one
search gives you the answer. It doesn't. The `enterprise-search` skill runs
a three-step loop: search returns ranked snippets (~35 words, built for
triage, not for answering), read fetches the full document, and feedback —
upvote what you used, downvote what you rejected — trains the ranker before
the task is called done. Two rules keep the loop honest: always search the
shared index first (it already handles cross-source ranking, dedup, and
permissions) before falling back to one connector directly, and pagination
is cursor-based — pass the cursor back exactly as given, never build one
yourself. One catch: an empty result can mean the content genuinely isn't
indexed, or that the identity asking simply can't see it — the API doesn't
say which.

**Topic:** ENTERPRISE SEARCH · CLAUDE SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-enterprise-search

---

## Chapters

0:00 Does Claude just search our docs and answer from the results?
0:12 One question, many sources — the anchor
0:24 A snippet, not an answer
0:38 Search, read, feedback — the loop
1:00 Design rules — index first, cursor pagination, empty-results logic
1:24 The anchor returns — snippet, document, feedback
1:39 Both directions — found isn't complete, empty isn't proof
1:52 Carry-out
2:00 Your turn
2:15 Outro

---

## YOUR TURN

"Search our internal docs for our policy on contractor onboarding. Read the
full document, not just the snippet, and tell me if there's a prior
decision on file. Then tell me what you used to answer, before you finish."

Why it's worth running: it forces the same three-step loop this reel
describes — search, read, report — on your own question, so you can watch
whether the assistant stops at the snippet or actually opens the document.

---

## Deliberately not claimed

Not a claim that every internal-search tool works this way — the Glean
Client REST API is this reel's worked example, not a universal claim about
every enterprise search product. Not a verdict on whether the skill's
documentation is good or bad (that's Teardown territory); this reel states
the mechanism and the boundary, and stops. No accusation that the tool is
unreliable — only that a snippet is a preview, not an answer.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
