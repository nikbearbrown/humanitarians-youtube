# Claude, Code Review.

You paste a diff and ask Claude to review it before you merge. The natural
guess is that it reads the way a senior engineer would — broad judgment,
catching whatever looks off. It doesn't. `code-review` is a **skill**: a
folder Claude reads before it acts, containing one file, `SKILL.md`, that
names exactly three things to check (security, performance, correctness)
and exactly what triggers it (a PR link, a diff, or "review this before I
merge"). A diff that adds a database call inside a loop — one extra query
per row — gets flagged, because performance is on the list. A logic bug the
file never mentions can sail straight through, because it was never on the
list to begin with.

**Topic:** CODE-REVIEW · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-code-review

---

## Chapters

0:00 Claude, review my code — it catches everything, right?
0:10 Before you merge, something decides what counts
0:16 The guess: broad, human-style judgment
0:23 Run it twice — same categories, every time
0:31 A skill is a folder: one file, SKILL.md
0:40 Anchor planted — one query per customer
0:46 What code-review checks: security, performance, correctness
0:52 It names its own cue
0:58 How the skill works: read, check, return
1:05 Anchor payoff — same loop, flagged
1:11 A flag is real signal
1:16 Clean isn't a certificate
1:26 Carry-out: know the list, know the limit
1:34 Your turn
1:47 Outro

---

## YOUR TURN

"Before you review my code, read the code-review SKILL.md and tell me
exactly what you're about to check — the categories, and the phrase that
triggers you. Then review this diff: [paste it]"

Watch two things when Claude answers: does it name the three categories
before it looks at your code, and does its finding land inside one of
those three — never outside the list it just gave you?

---

## Deliberately not claimed

Not a verdict on whether a three-category checklist is the right scope for
a code review — that's Teardown territory; this reel states the mechanism
and its edges, and stops. Not that every skill works this way — this reel
describes `code-review` specifically, not skills in general. Not a claim
that a clean review means the diff is safe — only that nothing on this
list tripped.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #CodeReview #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
