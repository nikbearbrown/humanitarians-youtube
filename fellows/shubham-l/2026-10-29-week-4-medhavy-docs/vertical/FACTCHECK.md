# FACTCHECK — Week 4: Reading the Medhavy Docs

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about reading Medhavy's documentation end to end to learn how the whole project fits together. The voice you're hearing is Liam, an A I narrator, reading my script. Week four, I read the project documentation end to end.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: I pictured Medhavy as one big app. The docs describe a fleet of apps: a hub that controls access, and separate textbook sites that each check with it. That picture made every other document make sense.

## B02 · FRAMEWORK
- Source: docs/ (directory); medhavy_documentation/
- Narration: The docs folder has five files, and the trick that helped me was reading each as the answer to one question. Which model answers students? How is a new textbook added? How are concept maps reviewed? How do we move the database? And how should a tutor sound? The per-book documentation sits alongside.

## B03 · MECHANISM
- Source: docs/creating-a-new-textbook.md
- Narration: Adding a textbook has two halves. The book is its own site. The hub gets a registration entry. And the two are connected by exactly one endpoint, access verify. The book asks the hub whether this reader is allowed, and the hub answers. One small contract is why the fleet can grow without the hub being rewritten.

## B04 · WORKED_EXAMPLE
- Source: docs/tutor-persona-proposal.md
- Narration: The persona proposal was my favourite read. It layers the tutor's instructions: a core Socratic engine at the bottom, then a family, QUANTA for physics, HELIX for biology, then the book, then one professor's course overlay. When layers conflict, the core wins. Important caveat: this is a proposal, not shipped behaviour.

## B05 · FALSIFIABILITY
- Source: docs/ai-models.md (line 8)
- Narration: And the single fact that would save a new developer the most time. The tutor's model isn't installed anywhere. It's a name sent with each request, so changing it is one environment variable and a restart. Which means if the tutor goes silent, the model is almost never the cause. Check the key and the billing first.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: Week four. Medhavy is a fleet, a hub and its satellite books, joined by one contract. The tutor persona plan stacks layers with the core on top of every conflict. And the model is a setting, not a dependency. With the map in place, week five was the plan for what comes next: Medhavy two point oh.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Give Claude a folder of docs and ask: for each one, what single question does it answer, rank them by time saved in week one, and what question does none of them answer. That last part is the gold. The missing question is usually where new developers lose a whole day.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was Week 4: Reading the Medhavy Docs. Shubham L., for Humanitarians A I. Thanks for watching.

## Limits stated in the film
- Claims are limited to what the cited files say; opinions are labelled as proposals on screen.
