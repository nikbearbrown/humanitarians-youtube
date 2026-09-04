# Madison Week 1: Persona-Aware LLM Visibility Research Design

**Fellow:** Karishma Suresh Kumar  
**Project:** Madison  
**Organization:** Humanitarians AI  
**Reporting date:** September 4, 2026  
**Phase:** Research and design  
**Hours contributed:** 20 hours

## Weekly Summary

This week I developed the initial Madison project proposal for studying
persona-aware LLM visibility. The work focused on defining the research gap,
research question, experimental structure, proposed evaluation metrics,
technical pipeline, milestones, and next steps.

This was research and design work. I have **not** yet built the evaluation
prototype, run the proposed experiments, or collected experimental results.

## Research Gap

Traditional search visibility examines where a brand or product appears in a
ranked list of search results. AI assistants often respond with a synthesized
answer or a short set of recommendations, so conventional ranking measures do
not fully explain visibility in this setting.

An aggregate visibility score also risks hiding differences between users.
People with different goals and constraints may receive different
recommendations even when they ask the same underlying question. The project
therefore treats user persona as an explicit dimension of LLM visibility.

## Research Question

The initial research question is:

> How does a brand's visibility in LLM-generated recommendations vary across
> user personas, prompt formulations, models, and repeated runs?

The related practical question is not only, “How often is this brand
recommended?” but also, “Who is this brand being recommended to?”

## Initial Personas

The first proposed test category is laptop recommendations. Initial personas
represent distinct needs rather than demographic stereotypes:

- **Student:** prioritizes affordability, portability, and battery life.
- **Software developer:** prioritizes memory, processing performance, and
  development-tool compatibility.
- **Creative professional or video editor:** prioritizes display quality,
  graphics performance, and media workflows.
- **Enterprise buyer:** prioritizes security, manageability, support, and
  organizational requirements.

These personas are provisional and will be reviewed to ensure that their
requirements are specific, relevant, and not based on unsupported assumptions.

## Controlled Prompt Progression

I designed an initial progression for testing how recommendation visibility
changes as context is introduced:

1. Ask a broad product-category question without a persona.
2. Add explicit functional requirements and constraints.
3. Add a defined user persona while keeping the underlying task consistent.
4. Repeat equivalent questions using controlled wording variations.
5. Repeat tests across models and multiple runs while documenting settings.

This design is intended to separate the effect of persona requirements from
uncontrolled changes in the underlying question.

## Proposed Evaluation Metrics

The proposal identifies several complementary measures:

- **Mention frequency:** how often a brand appears across responses.
- **Prominence:** where and how strongly the brand is presented in an answer.
- **Competitor share:** which competing brands appear and their relative
  presence.
- **Prompt coverage:** whether visibility holds across equivalent prompt
  variations.
- **Persona coverage:** the personas for which a brand is or is not
  recommended.
- **Run stability:** how consistent the observations are across repeated runs.

No metric values have been calculated yet.

## Proposed Python Evaluation Pipeline

The proposed pipeline will:

1. Load versioned persona, prompt, model, and run configurations.
2. Execute controlled recommendation prompts through approved model interfaces;
3. store responses with timestamps and documented generation settings;
4. extract brand mentions, recommendation order, and competitor mentions;
5. calculate aggregate and persona-level metrics;
6. compare results across prompts, personas, models, and repeated runs; and
7. export auditable tables and visual summaries for human review.

This pipeline is a design proposal and has not yet been implemented.

## Risks and Methodological Considerations

- LLM outputs may vary across wording, model versions, context, and repeated
  runs.
- A single response is one observation, not a conclusive measurement.
- Poorly designed personas can introduce stereotypes instead of useful
  personalization.
- Reproducibility requires versioned prompts, documented settings, repeated
  tests, and retained raw responses.
- Automated extraction and scoring will require human validation.

## Milestones and Next Steps

1. Review and refine the research question and persona definitions.
2. Finalize the controlled prompt templates and experiment configuration.
3. Define the metric formulas and annotation rules.
4. Build a small Python evaluation prototype.
5. Run a limited pilot and inspect extraction and scoring quality.
6. Refine the methodology before expanding data collection.
7. Analyze and communicate results only after the protocol and outputs have
   been reviewed.

## Communication Deliverables Completed

I also completed two Humanitarians AI videos this week:

- **What Is LLM Visibility?** — AI/STEM explainer
- **Persona-Aware LLM Visibility: Madison Weekly Update** — project update

Both videos were produced in 16:9 and 9:16 formats. The four files were
uploaded to YouTube and the designated Google Drive folder, and the links were
sent to my project manager for review.

## Status at the End of Week 1

The project proposal and initial research design are complete. Prototype
implementation, experiment execution, and results analysis remain future work.
