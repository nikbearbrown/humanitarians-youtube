# Video Script — The Memory API

**Target length:** 7–8 minutes
**Audience:** developers joining the project
**Researched against:** `main` @ `efcc3f5`

---

## ⚠️ Read this before filming

The natural framing for this video is *"how a tutor remembers a student across different books."* **Verify that's actually true before you say it on camera.**

The hub provides a cross-book memory API — that part is real and I read the code. But `medhavy_documentation/medhavi-cancer-textbook/ARCHITECTURE.md` says that book stores memory in **local SQLite**, scoped to a session ID and to a user ID from the `textbook_session` cookie. If that's still accurate, the cancer book isn't calling the hub at all, and memory does *not* cross books today.

I can't settle it from the hub repo — the book repos aren't here, and those doc sets are flagged as partly stale. **Ask Prarthana or Nik, or grep a book repo for `x-memory-api-secret`.**

Two versions of the script below depending on the answer. The difference is one section; everything else holds either way.

---

## Cold open (0:00–0:40)

> **On screen:** a student in one textbook, then the same student opening a different one.

**Say:**

"A student spends a semester in Quantum Volume 1. The tutor learns they're comfortable with algebra but shaky on boundary conditions. Next semester they open the cancer textbook — and the tutor there has never heard of them.

That's the problem the Memory API is built to solve. It's a small piece of the hub — two endpoints, two tables — but it's what makes a tutor feel like a tutor instead of a search box with a chat bubble.

Let me show you how it works."

---

## 1. Two kinds of memory (0:40–2:00)

> **On screen:** `db-migrations/03_chat_memory_profiles.sql`

**Say:**

"There are two tables, and they do genuinely different jobs.

`chat_memory_turns` is short-term memory — the actual back-and-forth. One row per message, tagged `user` or `assistant`. This is what lets the tutor understand 'what about the other one?' as a follow-up rather than a new question.

`learner_profiles` is long-term memory — one row per student, holding a JSON blob. Topics they've seen, gaps they've shown, how deep they like explanations. This is the part that persists after the conversation ends.

Short-term is a transcript. Long-term is a judgment about the learner. Different lifetimes, different purposes."

> **Highlight:** `profile JSONB NOT NULL DEFAULT '{}'::jsonb`

"Notice the profile is untyped JSON. The hub doesn't care what's in it — it stores and returns whatever the book sends. The shape of a learner profile is decided by the books, not here."

---

## 2. The subject key (2:00–3:15)

> **On screen:** `memory_subject` column in both tables, then `app/api/memory/profile/route.ts` line 40.

**Say:**

"Both tables key on the same thing: `memory_subject`. This is the most important idea in the whole system, and it's easy to miss because it's just a string.

`memory_subject` is an opaque namespace key. The hub treats it as a bare identifier — with one exception."

> **Highlight:** `const clerkUserId = subject.startsWith("hub:") ? subject.slice(4) : null;`

"If the subject starts with `hub:`, the profile endpoint pulls the Clerk user ID out of it and stores that separately, so profiles can be looked up per human.

That convention — `hub:` plus the Clerk user ID — is the entire mechanism for cross-book memory. Two different textbooks that both use `hub:user_abc123` are reading and writing the same memory. Two books using different subject strings are strangers.

So there's no clever identity resolution here. It's a naming convention, and it works exactly as far as every book follows it."

> **Worth saying plainly:** "Note the short-term memory endpoint doesn't do this `hub:` extraction — only the profile endpoint does."

---

## 3. Writing a turn (3:15–4:30)

> **On screen:** `app/api/memory/stm/route.ts`, the POST handler.

**Say:**

"After every exchange, the book posts the pair — what the student asked, what the tutor answered."

> **Highlight:** the two-row insert with `now` and `later`.

"Small detail worth noticing: the assistant message is timestamped one millisecond after the user message. That's deliberate. Both rows are inserted together, and without that nudge the ordering between them would be arbitrary. A transcript that renders answers before questions is a confusing bug to chase, so it's pinned here."

> **Highlight:** the pruning block.

"Then it prunes. It keeps the most recent `maxTurns` times two messages — default 24 turns, so 48 rows — and deletes everything older for that subject.

So short-term memory is genuinely short. It's a rolling window, not an archive. If you're expecting to query a student's full history later, it won't be there."

---

## 4. Reading it back (4:30–5:15)

> **On screen:** the GET handler.

**Say:**

"Reading is simpler. Pass a subject, get the turns back.

One thing to notice: it queries newest-first, takes the limit, then reverses before returning."

> **Highlight:** `.slice().reverse()`

"So you get the *most recent* N turns, delivered *oldest-first* — which is the order you want to paste into a prompt. Query descending to get the right slice, return ascending to get the right order. Easy to get backwards if you're reimplementing it.

The profile endpoint is a plain get and upsert. Nothing surprising there."

---

## 5. Security (5:15–6:30)

> **On screen:** `lib/memory-api-auth.ts`

**Say:**

"These endpoints are service-to-service. No user is logged in — a textbook's chat backend is calling the hub server to server. So the auth is a shared secret in a header: `x-memory-api-secret`, checked against `MEMORY_API_SECRET`."

> **Highlight:** the `isDev()` branch.

"And here's the part to pay attention to.

If `MEMORY_API_SECRET` isn't set and you're not in production, **auth is skipped entirely.** The function returns ok and the request goes through.

That's a deliberate developer convenience — you don't want to configure a secret to run locally. But it means the security of these endpoints depends on `NODE_ENV` being right in production. Get that wrong and anyone who can reach the URL can read every student's conversation history.

In production a missing secret is a 500 rather than an open door, which is the correct failure direction. Still worth knowing exactly what protects this."

> **Flag for the video:** `MEMORY_API_SECRET` is currently **not listed in `.env.example`**, even though `README.md` calls it required in production. Worth mentioning as a gap, or fixing before you film.

---

## 6. Where this actually stands (6:30–7:30)

### Version A — if books DO call the hub

**Say:**

"Put it together. A student asks a question in the physics book. The book's chat backend posts the exchange to the hub under `hub:` plus their Clerk ID, and updates their profile. Next semester, in a different book, that same subject key pulls back what the tutor already knew.

One student, one memory, many books. That's the payoff — and it's why the persona proposal argues for one stable tutor persona per subject family. Cross-book memory only feels like continuity if the tutor on the other side feels like the same tutor."

### Version B — if books still use local storage

**Say:**

"Now the honest part.

The hub provides this. Whether the books *use* it is a separate question. The cancer textbook's own architecture doc describes storing memory in local SQLite, scoped to that book — which would mean memory doesn't cross books today, even though the machinery for it exists here.

So treat this as infrastructure that's built and waiting, not a feature that's necessarily live. If you're working on a book, checking which side it's on is the first thing to find out.

That gap matters beyond tidiness: the tutor persona proposal leans on cross-book memory as its main argument. If memory isn't actually crossing books yet, that argument is describing a future rather than a present."

---

## Close (7:30–8:00)

**Say:**

"So: two tables, two endpoints, one naming convention holding it together. Short-term memory is a rolling window of the conversation. Long-term memory is an untyped JSON profile the books define. And `hub:` plus a user ID is what makes them the same student in two different places.

If you're wiring up a new book, that subject string is the thing to get right. Everything else follows from it."

---

## Recording notes

- **Don't show a real `MEMORY_API_SECRET`** on screen. Use a placeholder if you demo a request.
- **Don't show real student conversation content** from a live database. Seed fake rows if you want to show a query result.
- Good live demo if you want one: `curl` the STM POST twice, then GET, and show the rolling window pruning. Fast and makes the abstract concrete.
- If you cover the `hub:` convention, showing two different subject strings side by side makes the point faster than explaining it.

## Source files, for pulling clips

| File | Shows |
|---|---|
| `db-migrations/03_chat_memory_profiles.sql` | Both tables |
| `app/api/memory/stm/route.ts` | Turn write, pruning, ordering |
| `app/api/memory/profile/route.ts` | `hub:` extraction, upsert |
| `lib/memory-api-auth.ts` | Shared secret, dev bypass |
| `DEVELOPER.md` §8.6 | Route reference table |
