# CARRY-OUT.md

**Carry-out line:** build-zoom-meeting-app doesn't hand Claude a
video-calling engine to invent — it hands Claude Zoom's own Meeting SDK,
wired into an app you already have as a join flow, an embed, or the
lifecycle around the call.

**Wrong guess it's built to defeat:** that "build a Zoom meeting app"
means Claude writes a new video-calling system from scratch — its own
signaling, its own media pipeline. It doesn't. The actual value is that
Claude reads a SKILL.md spec and follows it to wire Zoom's existing
Meeting SDK (or, where it fits better, the Video SDK) into an app you
already have — the join, the embed, the lifecycle around the meeting.

**Secondhand test:** "Claude doesn't invent the video engine — it wires
in Zoom's own SDK" survives being repeated by someone who wasn't fully
listening, and stays true. It compresses the distinction that matters
(invent an engine vs. wire in an existing SDK), not the topic (Zoom
integrations in general).
