# Frictional Log: Week 1 Onboarding & Model Research

**Date:** 2026-09-18  
**Fellow:** Priya Adlakha  

### 1. What was attempted and expected
Review candidate research tracks for Humanitarians AI / Iacon Optimus, set up local development and toolkits (Optimus, Brutalist), and select a tractable model architecture suitable for autonomous tool selection on modest compute.

### 2. Where the system resisted
- Multiple project directions lacked objective, automated reward mechanisms, creating risk of ambiguous evaluation criteria.
- Setting up the local Brutalist rendering environment required resolving local audio/video tool dependencies.

### 3. What was done about it
- Chose the FunctionGemma 270M tool-routing problem because Google publishes working baselines (58% before tuning, 85% after) and tool execution can be verified objectively in sandbox environments.
- Installed required media tools and verified Optimus runtime connectivity.

### 4. What was learned
- Bounded, high-clarity research questions with objective success metrics are significantly easier to iterate on than open-ended text generation tasks.
