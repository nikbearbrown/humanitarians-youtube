# FACTCHECK — Week 7: The Pilot Isolation Rule

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about the pull request Chaitanya and I opened to add a pilot isolation rule to the Medhavy two point oh notes. The voice you're hearing is Liam, an A I narrator, reading my script. Week seven, Chaitanya and I opened a docs pull request on Medhavy.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: I used to think a pilot is safe because it's small. It's safe only when it's separate. A tiny pilot that shares a login or a database with the live system can still hurt real students.

## B02 · FRAMEWORK
- Source: git show --stat 1876c3b (branch docs/pilot-isolation-rule)
- Narration: Here's the change itself. Two files, twenty-eight lines added, all documentation. A new section in the two point oh README, and one new row in the decisions table. The professor asked for it so that developers, and A I agents working in the repo, know the pilot has to stay separate. One note in the PR: merging to main redeploys the hub, so it should be merged at a sensible time.

## B03 · MECHANISM
- Source: medhavy-2.0/README.md — Pilot isolation rule (branch docs/pilot-isolation-rule)
- Narration: The rule is short. The pilot uses only its own Clerk, its own Supabase project, its own analytics and its own server, with test accounts only. Never a production or dev key. Never read or write a live service. And the line written for agents especially: if a task seems to need live data, stop and ask a human. Don't work around it.

## B04 · WORKED_EXAMPLE
- Source: medhavy-2.0/README.md — Why (branch docs/pilot-isolation-rule)
- Narration: What I like is that every reason is concrete. Logout is shared, so leaving the pilot would sign people out of the live books. Roles are shared, so a test admin would be a real admin. The database connection reaches real student data. Dev holds real data too. The prod disk is about eighty-nine percent full. And branches aren't protected.

## B05 · FALSIFIABILITY
- Source: medhavy-2.0/06-decisions-and-evidence.md §6.2 (branch docs/pilot-isolation-rule)
- Narration: Where it lives matters. We put the rule in the two point oh README, because that's the first file a developer or an agent opens, and recorded it as a decision in the decisions table, next to lane C, the isolated pilot. Its status today is honest: a branch and a pull request, waiting for review and a safe moment to merge.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: Week seven. A small, docs-only pull request with a big rule: the two point oh pilot runs fully separate, on its own accounts, database, analytics and server. Agents stop and ask when a task seems to need live data. And every reason behind it is a concrete way real students could be affected.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Before your next pilot, ask Claude to interview you about everything it shares with production: login, roles, database, servers, analytics, deploy branches. Then have it write an isolation rule with a reason for each, plus a stop and ask a human clause for agents. Answer honestly. The shared things you forget are the dangerous ones.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was Week 7: The Pilot Isolation Rule. Shubham L., for Humanitarians A I. Thanks for watching.

## Limits stated in the film
- Claims are limited to what the cited files say; opinions are labelled as proposals on screen.
