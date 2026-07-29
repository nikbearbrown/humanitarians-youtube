````md
# Weekly Research Report: Personalized Project-Driven Reading Roadmaps

**Fellow:** Satwik Reddy Sripathi  
**Week ending:** July 28, 2026  
**Research project:** Personalized Project-Driven Reading Roadmaps  
**Research sources:** See `SOURCES.md`, the project manuscript, implementation report, and supporting project files.  
**Source status:** This video introduces the current research design and implementation approach. Proposed adaptive features and future extensions are presented as future work rather than completed capabilities.

This weekly research video asks:

**How can a research paper be transformed into a personalized reading roadmap based on a reader’s background, goals, and prerequisite knowledge?**

The video explains why a single fixed reading order may not work equally well for every reader. It introduces a roadmap structure in which concepts, sections, learning objectives, and prerequisite topics can be represented as nodes in a graph. Directed relationships between those nodes can then be used to recommend what a reader should study first, what may be read immediately, and what may be deferred.

The video also explains how faculty review contributes evidence to the roadmap. Faculty feedback is not treated as a simple score or unquestioned ground truth. It is used to support, reject, qualify, or request further review of proposed prerequisite relationships.

The final beat sheet contains **10 beats**. The complete video was generated locally using Brutalist, compiled at 1080p, reviewed end to end, and prepared separately for submission. The MP4 and generated media files are intentionally excluded from this repository.

## Production state

- Plan and beat structure: completed
- Beat-sheet lint: passed
- Narration generation: completed
- Audio timing: completed
- Visual beats: 10 of 10 filled
- Local compilation: completed
- Full-video review: completed
- Final pacing adjustment: completed
- Formal claim-level fact-check: requires final human review before publication
- YouTube publishing: handled separately through the Humanitarians AI review process
- MP4 and generated media: excluded from Git as instructed

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Weekly Research Report: Personalized Project-Driven Reading Roadmaps

## What this video is about

**Topic:** Personalized Project-Driven Reading Roadmaps

Research papers are normally written in one fixed sequence. However, readers begin with different levels of background knowledge, different goals, and different reasons for reading the same paper.

A reader who already understands the mathematical background may want to move directly to the method and experiments. Another reader may need to learn prerequisite concepts before the same sections become understandable. A third reader may only need the parts of the paper related to a specific project.

This project introduces a personalized reading-roadmap approach that attempts to account for those differences.

The roadmap can represent:

- concepts;
- paper sections;
- learning objectives;
- prerequisite topics;
- reader goals;
- recommended reading paths;
- approved relationships;
- provisional relationships;
- relationships requiring additional review.

The current project contains **10 beats**. Its timing is derived from the measured narration and beat durations recorded in `beat_sheet.json`.

## Central question

The project is organized around the following question:

> How can the same research paper be presented as different reading paths for readers with different backgrounds, goals, and prerequisite knowledge?

The proposed answer is to represent the paper and its supporting concepts as a structured graph rather than treating the paper’s printed order as the only possible learning sequence.

## Main ideas presented

The video introduces the following ideas:

1. A research paper presents one fixed reading order, but readers do not begin from the same starting point.
2. A personalized roadmap can recommend what a reader should study first.
3. The roadmap can identify sections that may be read immediately.
4. It can also identify concepts that should be reviewed before later sections.
5. Concepts, paper sections, and learning objectives can be represented as graph nodes.
6. Directed edges can represent proposed prerequisite or dependency relationships.
7. Faculty review can provide evidence for confirming, rejecting, or qualifying those relationships.
8. Approved and under-review relationships should remain visibly distinct.
9. Sample prerequisite data should not be treated as automatically verified ground truth.
10. Dynamic adaptation based on continuous reader behavior is future work unless separately implemented and evaluated.

## Current implementation boundary

The current implementation focuses on constructing and reviewing the roadmap structure.

The video does not claim that every prerequisite relationship is automatically correct. It also does not claim that the system has already demonstrated improved learning outcomes.

The current system should be understood as a structured research and implementation framework that can:

- organize concepts and sections;
- represent proposed dependencies;
- incorporate faculty review;
- distinguish approved relationships from uncertain ones;
- generate candidate reading paths;
- support review and revision of the roadmap.

The following areas require additional evaluation or remain future work:

- continuous adaptation to reader behavior;
- automatic updating of reader knowledge states;
- large-scale learning-outcome evaluation;
- validation across many papers and academic domains;
- conflict resolution when reviewers disagree;
- longitudinal evaluation of reader progress.

## How the graph is interpreted

The roadmap graph should be interpreted carefully.

### Nodes

Nodes may represent:

- prerequisite concepts;
- paper sections;
- methods;
- datasets;
- mathematical foundations;
- learning objectives;
- reader goals;
- project tasks.

### Directed edges

Directed edges represent proposed relationships such as:

- concept A should be understood before concept B;
- section A provides background required for section B;
- method A depends on technique B;
- a reader goal requires a specific sequence of topics;
- one learning objective supports another.

An edge is not automatically true merely because it exists in the graph. Its meaning depends on its source, review status, and supporting evidence.

### Approved relationships

Approved relationships are those that have received sufficient supporting evidence or review for the current version of the roadmap.

They should be visually and structurally distinguishable from uncertain relationships.

### Under-review relationships

Under-review relationships may be:

- proposed by an automated process;
- inferred from source text;
- suggested by a reviewer;
- supported by incomplete evidence;
- disputed by multiple reviewers;
- awaiting additional validation.

These relationships should remain visible as uncertain rather than being silently converted into confirmed prerequisites.

## How faculty review is used

Faculty review contributes evidence to the graph rather than replacing the graph with a single score.

A faculty review may help determine:

- whether a prerequisite relationship is reasonable;
- whether a concept is essential or optional;
- whether a paper section depends on earlier material;
- whether the wording of a concept is accurate;
- whether two concepts should be merged or separated;
- whether a relationship should be approved;
- whether a relationship should remain provisional;
- whether additional evidence is required.

When multiple faculty reviews are available, they may agree, disagree, or emphasize different aspects of the same relationship.

The system should preserve that uncertainty when appropriate. Conflicting reviews should not be silently collapsed into certainty.

## Sample prerequisite files

Sample prerequisite files are structured inputs used to demonstrate, test, or initialize graph construction.

They may contain fields such as:

- source concept;
- target concept;
- relationship type;
- reviewer;
- confidence;
- evidence;
- approval status;
- comments;
- source section;
- timestamp or version.

A sample prerequisite file is not automatically verified ground truth.

Its purpose is to provide a reproducible structure for testing the graph-building process and showing how prerequisite evidence can be represented.

Before such data is used in a final roadmap, it should be reviewed for:

- correctness;
- consistency;
- missing concepts;
- duplicate relationships;
- conflicting evidence;
- unclear terminology;
- unsupported assumptions;
- appropriate approval status.

## Reader-specific routes

A reader-specific route may be generated using information such as:

- the reader’s existing background;
- the reader’s target project;
- the reader’s stated learning goal;
- concepts the reader already understands;
- concepts the reader has not yet studied;
- the prerequisite graph;
- section dependencies;
- approved and provisional relationships.

The route should be treated as guidance rather than a guaranteed optimal learning sequence.

A recommended route may change if:

- the reader’s goal changes;
- new prerequisite evidence is added;
- faculty review changes a relationship;
- the graph is revised;
- the reader demonstrates new knowledge;
- additional source material becomes available.

## Make your own version

Download the local Brutalist toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
````

Brutalist uses the beat sheet as the source of truth.

Each beat records information such as:

* narration;
* timing;
* visual intent;
* motion language;
* scene type;
* source references;
* build state;
* implementation notes.

For this project, begin with:

```text
beat_sheet.json
```

Preserve the reviewed version before experimenting. Create a copy or a new dated project folder rather than overwriting the completed project.

This project uses a compact explainer structure rather than a long documentary. The ten beats move from the reading-order problem, through graph construction and faculty review, to the current implementation boundary and future work.

## Research prompt

Use the following prompt before substantially rewriting the project:

> Research “Personalized Project-Driven Reading Roadmaps” for an educational explainer. Begin with the project manuscript, implementation report, `SOURCES.md`, `beat_sheet.json`, and the supporting project files in this folder. Identify the central research problem, the proposed roadmap mechanism, how prerequisite graphs are created, how sample prerequisite files are structured, how faculty reviews are mapped into graph evidence, how approved and uncertain relationships are distinguished, what has actually been implemented, and what remains future work. Locate primary sources, peer-reviewed research, official documentation, or original datasets for broader claims. Return a claim table containing: claim, exact source or citation, publication date when applicable, pinpoint evidence, confidence, and what still requires verification. Do not invent experimental results, implementation details, quotations, performance metrics, or deployed capabilities.

## Fact-check prompt

Run the following prompt after any narration or beat-sheet change:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, historical, technical, scientific, implementation, and capability claim. Compare each claim with the project manuscript, implementation report, `SOURCES.md`, and the strongest available primary source. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Pay particular attention to claims about personalization, prerequisite inference, graph construction, sample prerequisite files, faculty-review mapping, implemented capabilities, evaluation results, and future adaptation. Flag any visual that implies a relationship or capability not established by the evidence. Do not silently rewrite the narration. List every proposed correction for human review.

## Build and review loop

The human remains responsible for research judgment, factual approval, narrative quality, and publishing decisions. Brutalist performs the structured local build.

1. **Research and scope**
   Define the specific problem the video explains and identify the manuscript, implementation report, and supporting evidence.

2. **Create the project folder**
   Create a separate dated project folder for the weekly report.

3. **Write the narration**
   Draft the explanation in a form that can be spoken naturally.

4. **Create the beat sheet**
   Divide the explanation into focused moments with one main purpose per beat.

5. **Define the visual plan**
   Decide what the viewer should see during each narration segment.

6. **Separate current work from future work**
   Do not describe proposed adaptive capabilities as already implemented.

7. **Run the fact-check review**
   Create or update `FACTCHECK.md`. Mark unresolved claims with `[VERIFY: ...]`.

8. **Complete Gate P narration review**
   Read every narration line aloud and record the human review decision in `PEDAGOGY.md` or `NARRATION-GATE-P.md`.

9. **Generate local narration audio**
   Generate audio only after narration review. Measured audio durations become the timing source.

10. **Generate visual beats**
    Implement each beat using the appropriate Brutalist-supported visual language.

11. **Run build checks**
    Validate beat structure, branding, timing, and required metadata.

12. **Compile the review cut**
    Render the generated scenes and combine them with measured narration.

13. **Watch the complete video**
    Review pacing, synchronization, readability, factual implications, transitions, and whether the visuals teach the spoken point.

14. **Refine and rebuild**
    Update only the beats that require correction.

15. **Create the clean final output**
    Produce the final MP4 separately and keep it outside Git.

16. **Publish only after human approval**
    Successful compilation does not itself authorize publication.

## Typical commands

Run these commands from the Brutalist toolkit root.

```bash
# Inspect the available workflow
./art --help

# Generate or verify narration audio after approval
python3 runtime/scripts/generate_audio_kokoro.py "/absolute/path/to/this/project"

# Compile the project
./art run "/absolute/path/to/this/project"

# Inspect remaining work
./art todo "/absolute/path/to/this/project"

# Compile at 1080p on a resource-constrained system
python runtime/scripts/compile.py "/absolute/path/to/this/project" --height 1080
```

The exact supported commands may depend on the checked-out Brutalist version. Check each command’s `--help` output before adding new arguments.

## Beat-sheet and visual rules

* Treat `beat_sheet.json` as the source of truth.
* Audio duration is the timing clock.
* Regenerate and remeasure audio whenever narration changes.
* Keep each beat focused on one explanatory purpose.
* Prefer diagrams and concept visuals that teach the mechanism.
* Distinguish approved prerequisite relationships from relationships still under review.
* Do not present sample graph data as verified production data.
* Do not present future personalization features as already deployed.
* Keep important labels readable at normal viewing size.
* Avoid placing too many simultaneous elements in one beat.
* Use motion to show relationships, progression, comparison, or causality.
* Do not use motion only as decoration.
* Run the project lint and quality checks after structural edits.
* Treat the first successful compile as a review cut.
* Preserve the reviewed project before creating a new version.
* Keep final MP4 files and generated media outside Git.

## Voice and narration

The narration voice and related production metadata are recorded in `beat_sheet.json` and the generated audio artifacts.

For future weekly reports:

* choose one consistent local Kokoro voice;
* record the voice selection in the beat sheet;
* review narration before generating audio;
* preserve pronunciation consistency for technical terms;
* regenerate audio when narration changes;
* do not manually stretch visual timing to hide narration changes;
* verify synchronization after every narration revision.

## Useful project files

* `README.md` — project overview and rebuild guide
* `beat_sheet.json` — narration, timing, beat structure, motion metadata, and build state
* `narration.md` — complete narration script
* `scenes.py` — Python or Manim-compatible scene definitions
* `anim.json` — animation configuration
* `remotion-src/` — Remotion scene implementation
* `PEDAGOGY.md` — teaching strategy and narration-review information
* `NARRATION-GATE-P.md` — narration gate documentation
* `FACTCHECK.md` — claim-level evidence, verdicts, and required corrections
* `SOURCES.md` — research references and supporting sources
* `VISUAL-PLAN.md` — visual treatment and beat-level design
* `BUILD-PROMPT.md` — build instructions and generation context
* `BUILD-LOG.md` — build decisions and troubleshooting notes, when present
* `SHOPPING.md` — external media or pantry requirements, when used
* `pantry/` — approved source assets, when used
* `clips/` — derived video clips; excluded from this submission
* `media/` — derived render assets; excluded from this submission
* `mp3/` — generated narration audio; excluded from this submission
* final `.mp4` files — excluded from Git and distributed separately

## Build result for this report

The reviewed local build produced:

* 10 of 10 filled beats;
* successful beat-mix lint;
* measured per-beat narration;
* synchronized audio and visual compilation;
* a 1080p output;
* a complete end-to-end human review;
* a final pacing-adjusted submission version;
* no MP4 committed to this project folder.

The build emitted a motion-distribution warning because the `illustrate` motion language was used more frequently than the recommended balance.

This warning did not prevent compilation. Future revisions may diversify the motion language where that change improves comprehension rather than adding variation only for its own sake.

## Current limitations

This video is an introduction to the roadmap method and current implementation. It does not establish that every prerequisite relationship is automatically correct.

Important limitations include:

* prerequisite quality depends on the quality and completeness of the source information;
* faculty reviewers may disagree;
* graph relationships may require revision;
* reader background information may be incomplete;
* reader goals may be ambiguous or change over time;
* a proposed route is guidance rather than a guaranteed optimal sequence;
* evaluation is required before making claims about improved learning outcomes;
* sample prerequisite files may contain illustrative rather than validated relationships;
* dynamic reader adaptation remains future work unless separately implemented and evaluated;
* visual simplifications should not be mistaken for the full underlying data model.

## Future work

Potential future work includes:

* improved aggregation of faculty review;
* explicit representation of reviewer disagreement;
* confidence scoring for graph relationships;
* stronger provenance for each prerequisite edge;
* improved reader-profile modeling;
* dynamic updates to reader knowledge states;
* adaptive route generation;
* evaluation across multiple research papers;
* evaluation across different academic domains;
* comparison with fixed-order reading;
* usability studies;
* longitudinal studies of reader progress;
* measurement of comprehension and task completion;
* improved visualization of uncertainty;
* integration with additional learning resources.

These items should be presented as proposed directions unless implementation and evaluation evidence is available.

## Final human checklist

* Can a new viewer explain why one fixed reading order may not serve every reader?
* Is the personalized-roadmap mechanism understandable?
* Are nodes, edges, prerequisites, and reading routes visually distinguishable?
* Is faculty review shown as evidence rather than unquestioned ground truth?
* Are approved and under-review relationships clearly different?
* Are sample inputs clearly presented as sample or illustrative data?
* Are current capabilities separated from future work?
* Is every important factual or technical claim supported?
* Does any visual imply more certainty than the evidence supports?
* Does the narration remain synchronized with the visuals?
* Is all text readable at ordinary playback size?
* Did a human watch the complete output?
* Was at least one refinement pass completed?
* Were access permissions verified before sharing?
* Is the MP4 excluded from Git?
* Are generated clips and narration audio excluded from Git?
* Has an authorized human reviewer approved publication?

## Publication note

The final MP4 is not stored in this repository.

The video is intended to be shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload it as an unlisted video and add it to the appropriate Humanitarians AI playlist.

A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->

```
```
