# PEDAGOGY audit — claude-liam-brand-guidelines

## Audience
Claude practitioners and makers on @NikBearBrown. They know how to use Claude but
may not have seen skills before. They can follow technical explanations.

## ONE idea
Brand consistency is a constraint problem, not a design problem. The skill makes it
executable by treating the brand guide as data, not logic.

## Predict-before-reveal
B01 poses an implicit question: "If you have a brand guide, how do you give it to Claude?"
The palette and typography beats answer it concretely before the design-tell beat names it.

## Concrete before abstract
The reel shows the actual hex values and font names (B03, B04) before explaining the design
insight (B05: "entirely data, no logic"). Viewers see the specifics before the principle.

## Useful friction
B05 names what the skill cannot do (no context adaptation, no readability judgment). This
prevents cargo-culting: the viewer knows when to reach beyond the skill.

## ILLUSTRATE LAW check
- B00: ClaudeComposerAsk (UI visible — cold open, REQUIRED) ✓
- B01: BrandGuidelinesAnatomy — folder tree illustration, NOT UI ✓
- B02: BrandGuidelinesPipeline — pipeline diagram, NOT UI ✓
- B03: BrandGuidelinesPalette — color swatch SELF-DEMO, NOT UI ✓
- B04: BrandGuidelinesTypography — type specimen SELF-DEMO, NOT UI ✓
- B05: BrandGuidelinesDesignTell — two-column Teardown, NOT UI ✓
- BVDT: ClaudeVerdictArtifact (UI visible — verdict, REQUIRED) ✓
- BHTF: ClaudeComposerAsk (UI visible — handoff, REQUIRED) ✓
- BOUT: ClaudeTitleOutro ✓

## HANDOFF LAW check
BHTF prompt: "I have a deck I want to make look like it came from Anthropic. Apply the
brand-guidelines skill. Start with the color system — tell me what you're changing and why
before you write any code."
- Narration reads the prompt aloud ✓
- Discusses it: explains why the "explain before acting" clause matters ✓
- Interesting: extends to viewer's own material ✓

## VERBATIM QUOTE LAW check
- B03 references exact hex values from SKILL.md: #141413, #faf9f5, #b0aea5, #e8e6dc,
  #d97757, #6a9bcc, #788c5d — cited as "Source: Anthropic, brand-guidelines SKILL.md"
- B04 quotes: "Headings (24pt and larger)", "Body Text: Lora (with Georgia fallback)"

## DOUBLE-CHECK LAW check
Source is the SKILL.md itself — no external claims. No model version numbers. No
invented metrics. The "honest caveat" in B05 distinguishes what the spec guarantees
(color/font application) from what it cannot judge (readability/context).

## VERDICT: PASS
