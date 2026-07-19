# Claude Code Prompt — Render the Medhavy and HAI Variants

Paste the following into Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

```text
Render the two audience variants of Claude, Judged. Work through them one at a time and do not modify the canonical source reel.

Canonical source, for visual and factual reference only:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-judged/

Authoritative variant sheets:
1. /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-judged/beat_sheet.medhavy.json
2. /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-judged/beat_sheet.hai.json

Read these rules completely before acting:
- skills/make/medhavy/SKILL.md
- skills/make/hai/SKILL.md
- runtime/voices/wonder/VOICE.md
- runtime/voices/pragmatist/VOICE.md
- skills/make/audience-preset/brands/medhavy.md
- skills/make/audience-preset/brands/hai.md
- docs/remotion-best-practices/SKILL.md

Required outputs:
- youtube/medhavy-claude-judged/claude-judged-medhavy.mp4
- youtube/hai-claude-judged/claude-judged-hai.mp4

Do not produce double-prefixed slugs. Do not rename or overwrite either authoritative variant sheet. If a runtime tool insists on beat_sheet.json, create a build-only copy or symlink inside the variant directory and document it; the authoritative files remain beat_sheet.medhavy.json and beat_sheet.hai.json.

For each variant:
1. Verify the JSON parses and the closing order is B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO.
2. Run a PEDAGOGY.md pass before audio. It must explicitly check that B08 explains both when to use AI and when not to use AI. Stop if the verdict is not PASS.
3. Preserve the canonical factual claims and the visual argument. Re-render visual beats in the target palette; do not merely copy Claude-colored frames when that would violate the audience palette.
4. Medhavy: Wonder register, Kokoro af_kore, Medhavy palette, EB Garamond/Montserrat, Medhavy.com OutroCTA. Do not add an exercise beat.
5. HAI: Pragmatist register, Kokoro am_onyx, Humanitarians palette, EB Garamond/Montserrat, Humanitarians AI OutroCTA. Preserve the runnable cli_exercise inside B08, including ASK, OUTPUT, CHANGE, OUTPUT 2, and next step.
6. Generate fresh per-beat Kokoro narration from the variant narration. Do not reuse the canonical Bear audio. Measure the real audio and write actual_duration_s back only to the build copy used by the renderer.
7. Render every Remotion beat, including the new B08 artifact and B09 audience outro. Rebuild the QC sheet and inspect it for clipping, wrong palette, stale @NikBearBrown branding, and unreadable text.
8. Compile a clean 1920×1080 MP4. The narration is the master clock. No missing-media slates, no silent voiced beats, and no canonical audio.
9. Verify each final with ffprobe: 1920×1080, nonzero audio stream, duration consistent with summed measured beats. Open each final for human review.
10. Report exact output paths, duration, file size, voice, palette, PEDAGOGY verdict, and any remaining concern. Do not publish or push.

Use the repository's existing runtime scripts and Remotion components. If an expected command does not accept a variant filename, inspect the script and make the smallest audience-namespaced build adaptation; do not alter the canonical reel or weaken the requirements above.
```
