# Frictional Log: Week 2 Architecture Roadmap & Scope Transition

**Date:** 2026-09-25  
**Fellow:** Priya Adlakha  

### 1. What was attempted and expected
Establish a shared architecture roadmap with Ameya for the fine-tuning worker, map out data ingestion pipelines, and evaluate whether existing causal LM fine-tuning SDKs could be used out of the box.

### 2. Where the system resisted
- Standard LLM fine-tuning frameworks (Axolotl, TRL) assume autoregressive text generation with token completion masking, which does not cleanly match discrete, bidirectional decision models like Laya.
- Project scope required generalization to arbitrary user datasets without hardcoded prompt templates.

### 3. What was done about it
- Defined a decoupled 5-stage worker specification separating configuration/pre-flight, data ingestion mapping, model instantiation, training loops, and artifact export.
- Agreed on division of ownership: Ameya owns RL training algorithms while I own configuration schemas, universal data mapping, and end-to-end testing suites.

### 4. What was learned
- A declarative Pydantic configuration layer is essential to decouple training code from diverse user dataset schemas.
