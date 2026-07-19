# PEDAGOGY — claude-liam-example-skill

## Skill reviewed
`anthropics/claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md`

## What learners will be able to do
- Distinguish skills (model-invoked) from commands (user-invoked) and agents (spawned by Claude)
- State the four frontmatter fields: name and description (required), version and license (optional)
- Understand that the description field is the trigger — it tells Claude when to activate the skill
- Know the optional directory structure: references/, examples/, scripts/ for complex skills
- Apply the best-practice rule: avoid overlap with other skills' trigger conditions

## What makes this teachable
The skills vs commands vs agents distinction is the foundational concept — stated at the top, not buried.
The description-as-trigger pattern with concrete examples (specific phrases, keywords, topic areas) makes the activation mechanism actionable.
The optional file structure gives a clear path from a simple single-file skill to a complex multi-file skill.

## Gaps the teardown surfaces
- version and license frontmatter fields are documented but their runtime effect isn't explained
- The trigger mechanism (how Claude matches descriptions) is unspecified — no guidance on matching approach, length, or phrase importance
- "Test that the skill activates for expected queries" is advice without a testing methodology
- No guidance on description length — longer or shorter descriptions, effect on match quality
- Overlap avoidance is listed as a best practice but no guidance on how to detect or resolve overlap between two skills

## VERDICT: PASS

Skills vs commands vs agents distinction, description-as-trigger with good patterns, optional directory structure, and 5-point content guidelines are well-specified.
The trigger mechanism remaining unspecified and missing testing methodology are the key teachable gaps for anyone building their first model-invoked skill.
