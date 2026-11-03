# CARRY-OUT.md

**Carry-out line:** Contact Center, web doesn't hand you a drop-in chat
widget — it wires the Zoom Web SDK's chat, video, and campaign embeds into
your own site through events, context, and postMessage, the same way every
time.

**Wrong guess it's built to defeat:** that "Contact Center, web" means Claude
drops a finished, ready-made chat widget onto your page — a visible box you
paste in and you're done. The actual value is that Claude reads a SKILL.md
spec and wires the underlying SDK plumbing: engagement events, app-context
integrations, and Smart Embed postMessage workflows, all sitting inside your
own site's code, not a pre-built visual element.

**Secondhand test:** "It doesn't drop in the widget — it wires the events
underneath it" survives being repeated by someone who wasn't fully
listening, and stays true. It compresses the distinction that matters
(wiring SDK events vs. handing over a finished UI element), not the topic
(Zoom web chat in general).
