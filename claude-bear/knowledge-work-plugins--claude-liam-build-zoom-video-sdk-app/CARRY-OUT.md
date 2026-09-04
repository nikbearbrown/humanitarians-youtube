# CARRY-OUT.md

**Carry-out line:** Build Zoom Video SDK App doesn't build you a Zoom
meeting — it builds a custom video session, full control over the
experience, on whichever of six platforms your app runs.

**Wrong guess it's built to defeat:** that "build a Zoom video SDK app"
means Claude assembles a client that joins an actual Zoom meeting — the
same participant experience you'd get opening the Zoom app. The actual
value is narrower and more useful: this skill applies specifically after
the work has been routed to a custom-session workflow, where the point is
to NOT use the standard Zoom meeting UI at all — to build your own video
experience, with your own interface, on top of Zoom's infrastructure,
across Android, Flutter, iOS, Linux, macOS, or React Native.

**Secondhand test:** "It doesn't build you a Zoom meeting — it builds a
custom video session you control completely" survives being repeated by
someone who wasn't fully listening, and stays true. It compresses the
distinction that matters (a Zoom meeting vs. a custom video session built
on Zoom's SDK), not the topic (Zoom integrations in general).
