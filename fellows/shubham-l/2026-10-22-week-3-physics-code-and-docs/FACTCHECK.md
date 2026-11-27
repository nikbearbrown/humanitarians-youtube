# FACTCHECK — Week 3: Inside the Physics Code and Docs

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about going through the physics engine's code structure and documentation, and how the A I tutor draws simulations on demand. The voice you're hearing is Liam, an A I narrator, reading my script. Week three, I went through the physics code layout and its documentation.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: I assumed authors place every simulation by hand. In fact the simulations have two doors: authors place them in chapters, and the A I tutor can request the same components mid-conversation.

## B02 · FRAMEWORK
- Source: physics-vol-1/ARCHITECTURE.md (line 135)
- Narration: This line from the architecture doc is the whole feature. The tutor can put an interactive simulation inside its own answer by calling a tool. The doc calls this the main thing separating the physics book from the cancer book. So I traced exactly how a tool call becomes a working widget.

## B03 · MECHANISM
- Source: physics-vol-1/ARCHITECTURE.md (How It Works: End-to-End)
- Narration: Here's the path. The student asks in the side chat. The chat route builds context and memory and calls the model with tools attached. The model answers with a tool call, like generate projectile widget. That call streams to the page, a resolver maps it to a widget type, and the widget renders either a server-drawn image or a live explorer.

## B04 · WORKED_EXAMPLE
- Source: physics-vol-1/API.md (Physics Widget Generation Flow)
- Narration: The model doesn't write simulation code. It picks from four tools, and each maps to one widget type. Two return images drawn on the server. Two mount live components with sliders. I liked that it's a closed menu. The model can only ask for widgets the team has already built and tested.

## B05 · FALSIFIABILITY
- Source: physics-vol-1/ARCHITECTURE.md (line 193); docs/handoff/15-gaurav-handover-answers.md
- Narration: An honest limit. Everything here comes from the documentation. The physics source lives in a separate repository I didn't have locally this week, so I haven't read kinematics line by line or its tests. The docs are detailed, and same components serve both doors. But a description isn't the code. That's next.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: Week three. The tutor can draw simulations inside its answers. The path runs from the chat route, through a tool call, to a resolver and a widget. Four tools, a closed menu. And I'm clear about what I've verified: the documentation, not yet the source.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Ask Claude to design a closed set of tools an A I tutor may call to show diagrams: names, inputs, what each returns, why a closed menu beats letting the model write drawing code, and three tests per tool. Read the tests closely. That's where you'll see whether the design is really safe.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was Week 3: Inside the Physics Code and Docs. Shubham L., for Humanitarians A I. Thanks for watching.

## Limits stated in the film
- Claims are limited to what the cited files say; opinions are labelled as proposals on screen.
