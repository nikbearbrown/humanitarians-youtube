# Memory API — 2:50 Narration Script

**Runs with:** `memory-api-deck.html`. Six scenes, auto-advancing. Press **Space** to start; it paces itself and stops on the last slide.
**Total:** 2 min 50 sec · ~400 words · read at a normal pace, don't rush.

---

## ⚠️ Before you record

Scene 5 says one book stores memory locally instead of calling the hub. That comes from `medhavy_documentation/medhavi-cancer-textbook/ARCHITECTURE.md`, which is flagged as partly stale. **Confirm it before filming** — grep a book repo for `x-memory-api-secret`, or ask Prarthana.

If books *do* call the hub, swap scene 5's narration for the alternate at the bottom.

---

## SCENE 1 · THE PROBLEM · 26s

> Visual: "THE TUTOR FORGETS" slams in.

"A student spends a whole semester in one textbook. The tutor learns how they think — where they're solid, where they get stuck.

Next semester they open a different book. And the tutor there has never heard of them.

That's what the Memory API exists to fix. Two endpoints, two tables. It's small, and it's the difference between a tutor and a search box with a chat bubble."

---

## SCENE 2 · TWO TABLES · 30s

> Visual: two boxes — white, then black.

"There are two tables, doing genuinely different jobs.

`chat_memory_turns` is short-term. One row per message, tagged user or assistant. It's the transcript — what lets the tutor understand 'what about the other one?' as a follow-up instead of a brand new question.

`learner_profiles` is long-term. One row per student, holding untyped JSON. Topics they've seen, gaps they've shown, how deep they like explanations.

A transcript is what was said. A profile is what the tutor concluded."

---

## SCENE 3 · THE KEY · 34s

> Visual: `hub:` in yellow, `user_abc123` beside it. Callouts stack.

"Both tables key on the same field — `memory_subject`. This is the most important idea here, and it's easy to miss, because it's just a string.

The hub treats it as opaque. With one exception: if the subject starts with `hub:`, the profile route slices that off and stores the Clerk user ID separately.

That convention is the entire cross-book mechanism. Two books using the same subject share one memory. Two books using different subjects are strangers.

There's no identity resolution happening. It's a naming convention — and it works exactly as far as every book follows it."

---

## SCENE 4 · ROLLING WINDOW · 26s

> Visual: message bars; the oldest four tip over and fall away.

"Every exchange gets posted as a pair — the question and the answer.

Then it prunes. It keeps the most recent twenty-four turns, forty-eight rows, and deletes everything older for that subject.

So short-term memory is genuinely short. It's a rolling window, not an archive. If you're expecting to pull a student's full history out of this later — it isn't there."

---

## SCENE 5 · BUILT ≠ WIRED · 30s

> Visual: two panels. Red stamp lands on the right.

"Now the honest part.

The hub provides all of this — I read the code, it works. Whether the books actually *use* it is a separate question.

At least one textbook's architecture doc describes storing memory in local SQLite, scoped to that book alone. If that's still current, memory isn't crossing books yet, even though the machinery for it is sitting right here.

So treat this as infrastructure that's built and waiting — not a feature you can assume is live. If you're working on a book, finding out which side it's on is the first thing to check."

---

## SCENE 6 · RECAP · 24s

> Visual: 02 / 48 / 01.

"So: two tables — a transcript and a profile. Forty-eight messages kept in a rolling window. And one string, `hub:` plus a user ID, that decides whether two books are talking about the same student.

If you're wiring up a new book, that subject string is the thing to get right. Everything else follows from it."

---

## Alternate SCENE 5 — if books DO call the hub

"So put it together.

A student asks a question in the physics book. That book's chat backend posts the exchange to the hub under `hub:` plus their Clerk ID, and updates their profile. Next semester, in a different book, the same subject key pulls back everything the tutor already knew.

One student, one memory, many books.

And that's exactly why the persona proposal argues for one stable tutor per subject family. Cross-book memory only *feels* like continuity if the tutor on the other side feels like the same tutor."

> If you use this version, change the slide headline from `BUILT ≠ WIRED` to `ONE STUDENT, MANY BOOKS`, and swap the two panels for the flow.

---

## Recording

- Open the deck, press **F** for fullscreen in your browser, then **Space** to start.
- `←` `→` step manually if you'd rather record scene by scene and cut together.
- `R` restarts.
- Record at 1920×1080. The deck is a 16:9 box that scales to fill whatever window it's in — no letterboxing if your window matches.
- Fonts load from Google Fonts, so **be online the first time**; after that they're cached.
- Scene durations live in the `data-dur` attribute on each `<section>`, in milliseconds. Adjust if your read runs long.
