# CARRY-OUT.md — skills--claude-liam-webapp-testing

**Carry-out (written first, per CARRY-OUT LAW):**

> Loaded and rendered are two different moments. Wait for the page to go
> idle before you touch anything — or you're testing a skeleton, not the
> real page.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the exact distinction (`load` event vs. `networkidle`)
without naming either term, and it survives being repeated by someone who
wasn't paying full attention.

**Wrong guess it defeats:** that a page which has "loaded" (arrived, is
visibly on screen, returned 200 OK) is already safe to inspect and click
into. Dynamic apps render their real content asynchronously, after the
initial load — a script that acts on load-not-idle grabs a placeholder,
not the button.
