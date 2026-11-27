# FACTCHECK — Week 6: Medhavy 2.5 and What We Could Do Differently

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about the Medhavy two point five plan, what it adds on top of two point oh, and some ideas for doing things differently. The voice you're hearing is Liam, an A I narrator, reading my script. Week six, I looked at the plan for two point five, and thought about what we could do differently.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: I went in expecting a finished spec. Two point five is an open question: the plan names one addition, an M C P interface, and says the details are still to come. That makes it a good place to think.

## B02 · FRAMEWORK
- Source: medhavy-2.5/README.md
- Narration: Two point five is defined in one sentence: the full two point oh scope plus an M C P interface for talking to Medhavy. M C P, the Model Context Protocol, lets A I assistants call an application's tools in a standard way. Everything else in the twelve-line README is pointers back to the two point oh plan.

## B03 · MECHANISM
- Source: medhavy-2.5/README.md (line 12)
- Narration: And the README is honest about it. It's planning documentation, not an implemented integration, and the details come after the product owner specifies them. So I want to be clear: everything after this point is my own proposal. Not the team's plan, and not decided. These are ideas to bring to the next planning conversation.

## B04 · WORKED_EXAMPLE
- Source: my proposal; builds on README.md Features (memory, glossary, access APIs)
- Narration: My first idea: start with read-only tools that wrap what the hub already does. Search a textbook the user can access. Look up a glossary term, since that A P I exists. List my classes. And deliberately no write tools at first. Publishing should stay inside two point oh's review workflow, where a human approves every exact revision.

## B05 · FALSIFIABILITY
- Source: my proposal; medhavy-2.0/README.md (approval + isolation principles)
- Narration: Here's the difference I'd push for. The easy way bolts an M C P server on with its own access rules and lets it write content. The way I'd argue for builds on two point oh: the same access check every book already uses, read-only until reviewed, and piloted in isolation first. An A I interface should inherit the human gates, not route around them.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: Week six. Two point five is two point oh plus an M C P interface, and right now it's a placeholder. My proposal is to start small: read-only tools over what the hub already does, behind the same access check, piloted in isolation. Those are ideas for discussion, not decisions.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Ask Claude to propose the first five M C P tools for an app that already has accounts and a review process, read-only first, the access check each must pass, and what should stay out of M C P entirely. Pay most attention to that last list. What an A I interface refuses to do is the real design.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was Week 6: Medhavy 2.5 and What We Could Do Differently. Shubham L., for Humanitarians A I. Thanks for watching.

## Limits stated in the film
- Claims are limited to what the cited files say; opinions are labelled as proposals on screen.
