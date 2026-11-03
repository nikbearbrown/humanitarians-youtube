# Weekly Report: Week 15 (Phase 15)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** October 4 – October 10, 2026
**Total hours:** 33.75

---

## Summary

- Management behavior analytics added:
  - **Guidance language tracker:** detects shifts from specific to vague forward guidance.
  - **CEO vs. CFO tone divergence:** flags calls where the gap between the two executives' tone exceeds historical norms.
- Signal-to-market mapping expanded:
  - signal-to-price impact correlation (Pearson and Spearman, 1/5/30-day)
  - three-way surprise analytics: predicted vs. consensus vs. actual
  - multi-horizon reaction window analysis
- **Preliminary finding:** NLP-vs-actual surprise outperforms consensus-vs-actual. This raises the question of whether traditional analyst consensus adds value over purely language-based signals.
- Dashboard gained a company-level analytics report view and a sector summary view (mood index, cross-sector heatmap).
- Outputs:
  - two Claude artifacts
  - one Substack article
  - two videos

---

## Work Completed

### Management Behavior Analytics

#### 1. Guidance Language Tracker
*Development · Management Behavior Analytics*
- Detects shifts from specific to vague forward guidance across consecutive earnings calls.
- Tracks changes in:
  - numerical specificity
  - time horizon references
  - qualifier density
- **Deliverable:** guidance language tracker with specificity change detection
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/management.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/features.py
- **Status:** Complete

#### 2. CEO vs. CFO Tone Divergence Analysis
*Development · Management Behavior Analytics*
- Compares sentiment and confidence between the CEO and the CFO on the same earnings call.
- Flags calls where the divergence exceeds historical norms.
- **Deliverable:** CEO–CFO tone divergence analysis module
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/management.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/speaker_roles.py
- **Status:** Complete

### Signal-to-Market Mapping

#### 3. Signal-to-Price Impact Correlation Scoring
*Development · Signal-to-Market Mapping*
- Measures which extracted signal features correlate most with subsequent price movement.
- Uses Pearson and Spearman correlations across 1-day, 5-day, and 30-day horizons.
- **Deliverable:** signal-to-price correlation module with feature importance ranking
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/impact.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/stats.py
- **Status:** Complete

#### 4. Surprise Score Analytics
*Development · Signal-to-Market Mapping*
- Compares NLP-predicted guidance direction against consensus analyst estimates and against actual reported outcomes.
- Cross-tabulates the surprise combinations to show where the pipeline adds value beyond consensus.
- **Deliverable:** surprise score analytics module with three-dimensional comparison
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/surprise.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/surprise.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/consensus.py
- **Status:** Complete

#### 5. Reaction Window Analysis
*Development · Signal-to-Market Mapping*
- Computes excess returns at 1-day, 5-day, and 30-day horizons to show how the market's response unfolds.
- Identifies underreaction drift versus overreaction reversion patterns.
- **Deliverable:** reaction window analysis module with multi-horizon return curves
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/impact.py
- **Status:** Complete

### Dashboard

#### 6. Company-Level Analytics Report View
*Development · Dashboard*
- Per-company view showing:
  - linguistic profiles
  - management confidence trends
  - guidance specificity changes
  - signal-to-price correlations
- **Deliverable:** company-level analytics dashboard view
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

#### 7. Sector Summary Dashboard View
*Development · Dashboard*
- Covers all tracked sectors with:
  - a mood index time series
  - a cross-sector heatmap
  - sector-level sentiment composites
- **Deliverable:** sector summary dashboard view with mood index and heatmap
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

### Debugging

#### 8. Debugging & Issue Resolution
*Development · Debugging*
- Identified and resolved issues across the pipeline. Main ones:
  - GICS sector classification mapping
  - CEO/CFO speaker matching for dual-title executives
  - mood index normalization
- **Deliverable:** resolved issues and verified fixes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase15.py
- **Status:** Complete

### Research

#### 9. Sector-Level Aggregation & Benchmarking Research
*Research · Sector Analytics*
- Researched sector-level aggregation methods and industry benchmarking approaches.
- Focus: rolling company-level NLP signals up into sector-wide intelligence.
- **Deliverable:** research notes on sector aggregation and benchmarking methods
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 10. Management Behavior Analysis Research
*Research · Management Behavior*
- Reviewed management behavior analysis techniques in the financial NLP literature:
  - executive language decisiveness metrics
  - hedging quantification
  - tone divergence methods
- **Deliverable:** research notes on management behavior analysis in financial NLP
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 11. Architecture Review
*Research · Architecture*
- Reviewed the full ECIS system in light of the new business analytics layer.
- Assessed component boundaries, data flow, and integration points.
- **Deliverable:** architecture review
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/architecture
- **Status:** Complete

### Writing

#### 12. Substack Article: "Turning Earnings Calls into Competitive Intelligence"
*Writing · Substack Article*
- Explores how strategy and analytics teams mine competitors' earnings calls for signals on:
  - pricing
  - demand
  - hiring
  - expansion plans
- Covers how those signals then feed internal dashboards.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/earnings-calls-competitive-intelligence-signals
- **Status:** Complete (published)

### Artifacts

#### 13. Management Confidence Tracker
*Artifact · Claude Artifact*
- Interactive per-company trend line of confidence scores across quarters.
- Drill down into the score drivers: hedging ratio, numerical specificity, and qualifier density.
- **Deliverable:** Claude Artifact: Management Confidence Tracker
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 14. Feature Importance Ranker
*Artifact · Claude Artifact*
- Interactive table ranking which NLP signal features correlate most with price movement across time horizons.
- Features ranked: hedging, tone shift, confidence, and direction.
- **Deliverable:** Claude Artifact: Feature Importance Ranker
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split:
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 15. Video: "ECIS Episode 10: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update covering Week 15 development progress and the business analytics layer additions.
- **Deliverable:** Video: ECIS Episode 10
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-ecis-explained
  - https://drive.google.com/drive/folders/1STQmHnVFLFYWcN2ARxxeVIruCuDszEfv
- **Status:** Complete

#### 16. Video: "Why GPUs Beat CPUs for AI"
*Documentation · Video Production*
- STEM educational video on why GPUs suit AI workloads, covering:
  - SIMD parallelism
  - memory bandwidth
  - tensor cores
  - why matrix multiplication is the computational bottleneck
- **Deliverable:** Video: Why GPUs Beat CPUs for AI
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-gpu-vs-cpu-explainer
  - https://drive.google.com/drive/folders/12zdqQ455NrC1zzBrWvkzrAUQSAmzN2Fq
- **Status:** Complete
