# RIFF.md — Liam, in for Bear (evidence-led)

Observations come from `capture/run-05.mp4` and its screenshots. Interpretations name their source. No claim of a human usability test; one admin account, production tenant, names masked.

| Beat / window | Visible observation | Interpretation (source) | Narration gist | Next experiment |
|---|---|---|---|---|
| B02 / 3.4–16.8 s | Tiles: 79 users, 11 admins, 68 learners, 0 pending. Registry rows with URL + `public` badge. | The tiles are the health check; the registry is the product. Status is the whole per-book policy (`DEVELOPER.md` §5.1). | Numbers, then registry, then the three statuses. | Flip one book to `hidden` and watch a student library (needs a student account). |
| B03 / 17.4–28.4 s | Every book has an Open Textbook button. | Open = mint JWT + redirect (§4.1). CORS whitelist on register is source-only (§5.1). | Open mints and redirects; CORS is a source fact. | Follow the token into a textbook site once the sites stop bouncing to the hub. |
| B04 / 29.0–40.0 s | Masked rows, role select per row, "Admin role locked" badges. | Lock = API 403 on demote (§3). Select = `set-role`. | First hundred accounts, role select, admin lock. | Promote a fictional account on a dev tenant; confirm the lock afterwards. |
| B05 / 40.6–59.2 s | View Admins short list; Classes shows two cards (8, 13 students), Create Class, Archive. | Enrollment is the access grant (§5.2 access oracle). | Classes are where instructors live; enrollment is the mechanism. | Create a class with a domain-limited invite; try joining with the wrong domain. |
| B06 / 59.8–70.8 s | Import field (`e.g. 20260411_120000`), Grant Access, four session rows. | Import pulls a pipeline run from S3; review/export live in the editor (`docs/concept-map-editor.md`). | Import, review, export; grant access. | Open one session and try Export with a pending node: it should refuse. |
| B07 / 71.4–78.7 s | Access Requests heading; empty. | Approve/deny per §5.3; not exercised. | Empty today; here is where asks land. | Request a private book from a student account, then approve here. |
| B08 / 95.8–124.5 s | Tiles 80 / 429 / 36 / 51; DAU bars; platform breakdown; masked leaders; Students and Instructors views. | PostHog HogQL proxy (§11.2). First-party counter is separate and non-atomic (§11.1). | Numbers; breakdown; trade-off: rough stats, not billing. | Compare a user's PostHog session count with `user_analytics_summary` for the same day. |
| B09 / 126.3–133.2 s | Name editor above Clerk's profile card. | Name is Clerk's; role is public metadata (§3, §9). | Clerk owns the profile; role lives in metadata. | Change the name and confirm PostHog identify picks it up on next load. |

**Verdict material (B10):** working on screen: registry, roles + admin lock, classes, concept-map sessions, empty request queue, analytics. Not shown: student and instructor screens (single account). Open defect: all three textbook sites 307 to the hub with a `localhost` `blocked_url`, so the handoff could not be shown end to end.

**Not manufactured:** no click on a real user's role, no class creation, no textbook deletion, no request approval. Production is not a sandbox.
