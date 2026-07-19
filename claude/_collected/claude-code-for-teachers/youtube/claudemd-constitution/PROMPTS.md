# PROMPTS — claudemd-constitution

## B02 — Generate CLAUDE.md constitution
```
claude "Generate a CLAUDE.md for a class-website project:
  Bash: deployment=rsync, no npm build step
  Style: semantic HTML5, vanilla CSS, no Tailwind
  Verification: npm run lint-html after HTML change
  Architecture: static-HTML only, no backend,
    contact forms are mailto: links
  Environment: school server old mod_rewrite,
    paths end in .html"
```

## B05 — Remove constraint and retest
```
claude "Remove the 'NO backend' line from CLAUDE.md.
Now request a Contact page.
What does Claude propose?"
```
