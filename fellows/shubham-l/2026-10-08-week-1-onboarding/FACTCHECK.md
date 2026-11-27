# FACTCHECK — Week 1: Onboarding to Medhavy

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about my first week on Medhavy: what the hub is, what it runs on, and how I got it running on my machine. The voice you're hearing is Liam, an A I narrator, reading my script. Week one was onboarding. Here's what I learned before writing a single line of code.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: I thought onboarding meant installing the app. It turned out to mean learning the map: what the hub does, which service owns which data, and the order things must happen in.

## B02 · FRAMEWORK
- Source: medhavy_documentation/STAKEHOLDER_OVERVIEW.md (line 25)
- Narration: Start with the purpose, because everything else hangs off it. Medhavy is an A I tutor that only answers from the textbook the student is reading, on the page they are on. The hub is the front door: students sign in once, and it hands each book a short-lived token that proves who they are.

## B03 · MECHANISM
- Source: DEVELOPER.md §1–2; README.md Architecture
- Narration: The stack is ordinary on purpose. A Next.js hub on top. Then the rule that saved me the most confusion: Clerk owns identity and roles, and nothing else. Supabase owns everything else, from classes to memory to analytics. Concept maps live as J SON in S3. When something breaks, first ask which owner it belongs to.

## B04 · WORKED_EXAMPLE
- Source: README.md Quick start
- Narration: Here's the setup, in the order the README gives it. Install, copy the example environment file, start the dev server on port three thousand. Then the step I almost skipped: the database migrations. There is no migration runner. You paste each S Q L file into Supabase yourself, in order. Then you make yourself an admin and register a book.

## B05 · FALSIFIABILITY
- Source: .env.example (names only); README.md
- Narration: To boot at all, the hub needs five values. Two Clerk keys, the Supabase address, the Supabase service role key, and the J W T secret that signs book tokens. One of those deserves respect: the service role key has full database access. I learned the names this week. The values never leave my machine.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: So, week one. The tutor stays on the page. Clerk owns identity, Supabase owns the rest. Setup has an order, and the S Q L step is manual. Five secrets boot the hub, and one of them is the keys to the whole database. And when two documents disagree, the developer guide wins.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Paste this into Claude on any project you're joining: read the setup docs, then give me a table of every external service, what data it owns, which environment variable connects it, and what breaks if it's missing. Flag anything with full database access. Look for the owner column. That's the map I wish I'd had on day one.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was Week 1: Onboarding to Medhavy. Shubham L., for Humanitarians A I. Thanks for watching.

## Limits stated in the film
- Claims are limited to what the cited files say; opinions are labelled as proposals on screen.
