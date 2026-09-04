# Engineering the AI Agent: Designing Workflows for the Real World

Source script (as supplied), kept verbatim for reference. `04_narration_tts_ready.txt`
is the condensed, TTS-normalized narration actually spoken in the reel — see
PEDAGOGY.md / SOURCES.md for how it maps to this original.

---

## Introduction: The Paradigm Shift (0:00 - 1:30)

**[Visual/Graphic]**
Fade in on a dark, sleek background. Text appears on screen, typing out: "Traditional Software vs. Agentic AI."
Cut to a split screen. On the left: a complex flowchart with hundreds of "If/Else" branches. On the right: a simple hub-and-spoke model with an "LLM Brain" in the center connecting to "Tools", "Memory", and "Action".

**[AI Voice Narration]**
Welcome. If you are learning how to build agentic AI, the first thing you need to do is forget how you used to write software.

In traditional software engineering, we write imperative logic for every possible edge case. If X happens, do Y. But the real world is messy. It doesn't fit into neat "If/Else" statements.

When you step into agentic AI engineering, your mindset has to shift. You are no longer writing a monolithic script to solve a whole problem. Instead, you are designing a system where an AI model handles the fuzzy, unstructured reasoning, while your deterministic code provides the boundaries, tools, and state management.

**[Visual/Graphic]**
Show a dashcam video or photograph of a massive pothole on an Indian road. Overlay text: "The Problem: Pothole Reporting. The Stakes: Lives & Infrastructure."
Transition to a clean graphic showing the GitHub repository for "coding-parrot / pothole-reporter".

**[AI Voice Narration]**
To understand how to design these workflows, we are going to reverse-engineer a brilliant open-source project called the *Pothole Reporter*.

Here is the problem: In India, thousands of accidents occur yearly due to potholes. Most of these potholes are actually under a maintenance warranty by a contractor. But citizens don't know who the contractor is, or which government official to email.

An app that just takes a picture of a pothole is not an agent. An agent is a system that bridges the gap between raw perception and highly contextualized action. Let's break down how to engineer that bridge.

## Act 1: Deconstructing the Problem (1:30 - 3:30)

**[Visual/Graphic]**
Title card: "Step 1: Deconstruction."
Show a graphic of a magnifying glass over the pothole photo. An AI bounding box highlights it. Text pops up: "Unstructured Variable = Visual Environment."

**[AI Voice Narration]**
When you approach a problem as an agentic engineer, you start by isolating the unstructured variables. What part of the problem cannot be hardcoded?

In this case, it's the physical environment. A pothole looks different in the rain, in the dark, or from different angles. You cannot write a traditional algorithm to catch them all reliably. This is where you deploy your reasoning engine. The first node in our workflow is a Vision Language Model. Its sole responsibility is perception and classification: look at a frame, find a pothole, gauge its size, and return a confidence score.

**[Visual/Graphic]**
The screen shows an AI "Thought Bubble" above the Vision Model. Inside the bubble: "I see a medium pothole. But where am I? Who is in charge?"
Text on screen: "Identify the Context Gap."

**[AI Voice Narration]**
But perception is not enough. The model is smart, but it has no localized context. It knows what a pothole looks like, but it doesn't know the jurisdictional boundaries of Bengaluru, India. It doesn't know who paved the road.

If you ask an LLM to write a complaint letter based just on a photo, it will hallucinate a generic response. Our job as engineers is to fill that context gap dynamically using Tools and Retrieval-Augmented Generation, or RAG.

## Act 2: Building the Agentic Pipeline (3:30 - 6:30)

**[Visual/Graphic]**
Title card: "Step 2: The Orchestration Pipeline."
An animated flowchart builds out horizontally across the screen:
1. Perception (Camera/Vision AI)
2. Tool-Use (GPS + OpenStreetMap)
3. Context/RAG (GIS Data + Contracts DB)
4. Action Synthesis (Drafting Email)

**[AI Voice Narration]**
Instead of letting the AI dynamically decide what to do next, this workflow uses a "Sequential Orchestration Pattern." This means the engineer enforces a strict, deterministic pipeline.

Let's walk through the agent's workflow.

**[Visual/Graphic]**
Highlight step 1. Show a phone mounted on a dashboard, capturing a frame. A timer shows "Every 8 meters."

**[AI Voice Narration]**
First: Perception. The app is set to drive mode. Instead of a fixed time interval, it triggers the camera every 8 meters of GPS delta. This is an engineering optimization to save on expensive AI API calls. The frame is sent to the vision model, which returns a positive match for a pothole.

**[Visual/Graphic]**
Highlight step 2. Show a raw GPS coordinate turning into a street address via an API call.

**[AI Voice Narration]**
Second: Tool-Use. The agent grabs the phone's exact GPS coordinates. It makes a deterministic tool call to OpenStreetMap to reverse-geocode the location into a street address.

**[Visual/Graphic]**
Highlight step 3. Show a database icon labeled "42,000 Procurement Contracts." A search query matches the location to a specific document.

**[AI Voice Narration]**
Third: Knowledge Grounding via RAG. This is the magic step. The system queries a local database containing the state's GIS boundaries and over forty-two thousand public road contracts. By matching the coordinates, the agent discovers exactly which City Corporation is responsible, which specific tender the road was built under, and the name of the winning contractor.

**[Visual/Graphic]**
Highlight step 4. An animated email draft writes itself on screen, filling in the blanks with the data retrieved in the previous steps.

**[AI Voice Narration]**
Finally: Action Synthesis. The agent takes all this context—the photo, the coordinates, the jurisdiction, and the contract details—and feeds it back to the LLM with a strict prompt template. The output is a highly precise, legally actionable email addressed to the exact commissioner responsible.

## Act 3: Guardrails and Constraints (6:30 - 8:30)

**[Visual/Graphic]**
Title card: "Step 3: Engineering Guardrails."
Visual of a red stop sign or a shield icon over the workflow.

**[AI Voice Narration]**
A good agentic engineer doesn't just design for success; they engineer for failure. When an agent interacts with legal systems or government bodies, autonomy is a liability. You need guardrails.

The Pothole Reporter implements three brilliant constraints.

**[Visual/Graphic]**
Bullet point list appears on screen, highlighting each point as it's spoken.
1. Fail-Safe Routing.
2. Probabilistic Language.
3. Human-in-the-Loop.

**[AI Voice Narration]**
First, Fail-Safe routing. If the location tool determines the pothole is on a National Highway, the workflow terminates immediately. National highways are maintained by a different body, and sending a complaint to the wrong local office is worse than sending no complaint at all. The system is hardcoded to refuse rather than guess.

Second, Probabilistic Language. The engineer wrote the synthesis prompt to force the AI to use words like "probable contract" or "may still be under warranty." Because the RAG matching is a best-guess based on public data, this prevents the LLM from making definitive, legally binding false claims.

Third, the Human-in-the-Loop pattern. The agent does everything up to the final mile. It drafts the payload. But it stops short of executing the action. It presents the email to the user for review. The human acts as the final legal gatekeeper, pressing 'send' from their own device.

## Conclusion: The Agentic Mindset (8:30 - 9:30)

**[Visual/Graphic]**
Zoom out to show the complete, finalized flowchart. The nodes glow to signify a working system.
Fade to a dark screen with three core takeaways in bold typography:
1. Isolate the reasoning.
2. Wrap it in deterministic tools.
3. Define how it fails.

**[AI Voice Narration]**
Agentic AI isn't about letting a chatbot run wild. It is about building a tightly controlled scaffolding around a reasoning engine.

As you design your own agentic workflows, remember the framework we covered today. First, isolate the core task that requires unstructured reasoning. Second, fill the context gaps by wrapping that reasoning in deterministic tools and data retrieval. And finally, define exactly how the system should fail gracefully, keeping a human in the loop where risk is high.

Build the boundaries. Let the AI do the thinking. That is how you engineer an agent for the real world.

**[Visual/Graphic]**
Fade to black. Outro music swells. Channel logo and "Subscribe/Like" graphic appear.
