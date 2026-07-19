# FACTCHECK — instructional-brief-generator
**Build an Instructional Brief Generator with Claude**
Source: `claude-for-education-a-practitioners-guide/chapters/03-prompting-claude-like-an-instructional-designer.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B01 | The quality gap is explained by whether instructors specified what students know, what they don't know, and what 'done' looks like before starting | ✓ | cli-ideas.md hook: "The quality gap between instructors who get useful AI outputs and those who don't is almost entirely explained by whether they specified what students know, what they don't know, and what 'done' looks like before they started." |
| 2 | B02 | The instructional brief has eight fields: Learner Profile, Prior Knowledge, Misconception, Outcome, Constraints, Modality, Assessment Evidence, Review Criteria | ✓ | cli-ideas.md: lists exactly these eight fields. Consistent with chapter's instructional brief framework (Chapter 3 is the instructional brief chapter). |
| 3 | B02 | The generated prompt must address the stated misconception explicitly | ✓ | cli-ideas.md: "Verify the generated prompt explicitly references the misconception (not just the topic)." |
| 4 | B06 | The three-field prompt is noticeably less targeted than the eight-field prompt | ✓ | cli-ideas.md: "Check that a prompt generated from a 3-field brief is noticeably less targeted than one from an 8-field brief — this is the video's key demonstration." |
| 5 | B07 | Every empty field is a default Claude fills in on its own | ✓ | Chapter's core argument: without specification, Claude uses its defaults — the most common interpretation, the most typical approach. The brief replaces each default with the instructor's decision. |

---

## Exclusions confirmed
- No full LMS integration
- No student-specific brief customization
- No automated lesson sequencing

## Synthetic scenarios
The specific brief field content, generated prompts, and diff output are illustrative scenarios consistent with Chapter 3's instructional brief framework. Not transcripts of actual Claude sessions.
