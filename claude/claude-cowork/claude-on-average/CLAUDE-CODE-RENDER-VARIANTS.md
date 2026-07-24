# Claude Code Prompt — Render the Medhavy and HAI Variants

Run Claude Code from `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art` and paste:

```text
Render the Medhavy and HAI audience variants of Claude, On Average. Work one variant at a time. Do not modify the canonical source reel.

Canonical source, for factual and visual reference only:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-on-average/

Authoritative variant sheets:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-on-average/beat_sheet.medhavy.json
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-on-average/beat_sheet.hai.json

Read completely before acting:
- skills/make/medhavy/SKILL.md
- skills/make/hai/SKILL.md
- runtime/voices/wonder/VOICE.md
- runtime/voices/pragmatist/VOICE.md
- skills/make/audience-preset/brands/medhavy.md
- skills/make/audience-preset/brands/hai.md
- docs/remotion-best-practices/SKILL.md

Required outputs:
- youtube/medhavy-claude-on-average/claude-on-average-medhavy.mp4
- youtube/hai-claude-on-average/claude-on-average-hai.mp4

Do not rename or overwrite the authoritative variant sheets. If a runtime command requires beat_sheet.json, make a documented build-only copy or symlink inside that variant directory. Never touch the canonical beat_sheet.json, audio, media, or MP4.

For each variant:
1. Validate the JSON and confirm the ending is B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO.
2. Run a PEDAGOGY.md audit before audio. It must explicitly pass the explanation that generative variance is useful for exploration but unsafe as unverified authority for exact or high-consequence outputs. Stop unless VERDICT: PASS.
3. Preserve the source facts: Claude generates token by token; responses are samples from a context-conditioned distribution; temperature zero narrows selection but does not guarantee a context-independent fixed answer. Do not add unsupported claims.
4. Re-render all visual beats in the audience palette instead of copying stale Claude-colored frames.
5. Medhavy: Wonder register, Kokoro af_kore, Okabe-Ito Medhavy palette, EB Garamond/Montserrat, Medhavy.com OutroCTA. No exercise beat.
6. HAI: Pragmatist register, Kokoro af_kore, Humanitarians palette, EB Garamond/Montserrat, Humanitarians AI OutroCTA. Preserve B08's runnable cli_exercise: five-run comparison, variance table, consequence controls, and concrete next step.
7. Generate fresh Kokoro narration for every beat. Never reuse canonical Bear audio. Measure audio and write actual_duration_s only into the build copy.
8. Render all Remotion beats, including the B08 sampling-boundary artifact and B09 audience outro. Rebuild and inspect a QC sheet for clipping, stale colors, stale @HumanitariansAI branding, and unreadable text.
9. Compile clean 1920×1080 outputs using narration as the master clock. No missing-media slates and no silent voiced beats.
10. Verify each final with ffprobe: 1920×1080, audio stream present, non-trivial file size, and duration consistent with measured beats. Open both finals for human review.
11. Report exact output path, duration, size, voice, palette, PEDAGOGY verdict, and remaining concerns. Do not publish or push.

Use the existing runtime scripts and Remotion components. If a command cannot accept the variant filename, make the smallest audience-namespaced build adaptation without weakening these requirements.
```
