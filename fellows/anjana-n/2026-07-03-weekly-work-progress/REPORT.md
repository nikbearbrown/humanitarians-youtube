# Weekly Report: Week 1 (Phase 1)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** June 29 – July 4, 2026
**Total hours:** 21.0

---

## Summary

- Proposal and initial system architecture defined for ECIS and the Decision Scorecard.
- Codebase review led to a revised architectural model ahead of implementation.
- Implementation started with the seam schema and the ingest scaffold.
- Data sourcing plan revised after researching open-source transcript sources.
- One Claude artifact and two Substack articles completed.

---

## Work Completed

### 1. ECIS Proposal Development & System Architecture Design
*Project Proposal & System Architecture · System Design*
- Developed the project proposal and initial system architecture for ECIS and the Decision Scorecard.
- Defined:
  - problem scope
  - multi-reader extraction approach
  - triangulation framework
  - scoring methodology
  - proposed toolchain
  - data sourcing strategy
  - success criteria
  - phased implementation plan
- **Deliverable:** project proposal document; initial system architecture; toolchain specification; phased implementation plan
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs
- **Status:** Complete

### 2. Dev Environment Setup
*Development · Environment Setup*
- Local environment, repo scaffold, Python project structure.
- Confirmed which dependencies install cleanly.
- **Deliverable:** working local dev environment
- **Status:** Complete

### 3. Codebase Reading + Architectural Reformulation
*Development · Architecture*
- Codebase review to understand the existing architecture and governance model.
- Refined the architectural approach before implementation began.
- **Deliverable:** revised architectural model
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/architecture
- **Status:** Complete

### 4. Installing Dependencies + Basic Code
*Development · Implementation*
- Installed project dependencies.
- **Deliverable:** foundational codebase
- **Status:** Complete

### 5. Start of Implementation: Seam Schema + Ingest Scaffold
*Development · Implementation*
- Designed the shared seam schema.
- Started the first ingest/normalize scaffold in repo conventions.
- **Deliverable:** seam schema design; ingest scaffold
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/ingestion
- **Status:** Complete

### 6. Data-Source Research
*Research · Data Sourcing*
- Researched open-source data sources to obtain earnings call transcripts.
- **Deliverable:** revised data sourcing plan
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/docs/data-layer.md
- **Status:** Complete

### 7. Reformulation Diagram (React Component)
*Artifact · Claude Artifact*
- Interactive React component with a before/after toggle: the previously proposed model vs. the revised model.
- **Deliverable:** Claude Artifact: Reformulation Diagram
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### 8. Substack Article: "When the Earnings Call Ends, Who Was Really Listening?"
*Writing · Substack Article*
- Frames the information gap between institutional and retail investors during earnings calls.
- Introduces the two-system prototype built to narrow it: a signal reader plus a trust judge.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/earnings-call-ai-retail-investor-gap
- **Status:** Complete (published)

### 9. Substack Article: "Your Data Has Two States: What You Got, and What You're Allowed to Trust"
*Writing · Substack Article*
- Explains the raw-versus-verified data boundary in a data pipeline.
- Explains why no record enters the trusted store without passing a formal validation gate.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/data-two-states
- **Status:** Complete (published)
