# Frictional log — Webhooks & Event-Driven Architecture

## 2026-10-30 — the project update, in two aspect ratios

**What I was working on.** A STEM explainer covering the shift from Polling to Webhooks in software architecture.

**What I tried, and what I expected.** 
- I initially tried to explain webhooks purely through the lens of incident alerts (like our n8n integration). 

**Where it resisted, and what I did next.** 
- Limiting the explanation to just "alerts" misses the broader AI context. The real reason webhooks are vital right now is LLM processing time. You can't hold an HTTP connection open for 45 seconds while an AI generates a response; it will time out. 
- I pivoted the script to focus on asynchronous processing. The core narrative shifted to explain that webhooks are necessary because AI takes too long to process data synchronously. 

**What Claude contributed, and what I did with it.** 
- Mine: The focus on the simplicity of the HTTP POST request (Scene 3).
- Claude's: The contrasting "Push vs Pull" visual metaphor in Scene 2, highlighting network exhaustion. 

**What I understand now, and what I still do not.**
- Understood: Webhooks are not just for sending notifications; they are a fundamental requirement for handling asynchronous AI inference in a scalable way.