# Storyboard

## Video

Project Progress: Branch Workflow and Core Site Fixes

## Structure

### 0:00-0:20 - Cold open

- Intro line begins the video.
- On-screen greeting: `Hello, Rushali!`
- Preview the workflow and the three main fixes.

### 0:20-0:46 - Progress framing

- Explain that the work involved several independent issues.
- Frame the branch-per-bug workflow as the safety pattern behind the week.

### 0:46-1:16 - Branch workflow

- Show the core Git flow:
  - `git switch main`
  - `git pull origin main`
  - `git switch -c fix/issue-name`
  - `git status`
  - `git add <files>`
  - `git commit -m "describe the fix"`

### 1:16-1:40 - Branch sanity checks

- Show the quick checks:
  - `git status`
  - `git diff --stat`
  - `git log --oneline -1`
- Explain that each branch should still represent one clean change.

### 1:40-2:04 - `80-days-to-stay` route fix

- Explain the path mismatch problem.
- Show the redirect from `/80-days` to `/80-days-to-stay`.
- Mention that navigation was aligned with the canonical route.

### 2:04-2:32 - Route file map

- Show where the fix lived:
  - `app/80-days-to-stay/page.tsx`
  - `next.config.mjs`
  - `components/Footer/Footer.tsx`
- Explain that route behavior depends on page, config, and navigation agreeing.

### 2:32-3:06 - Donate page refactor

- Explain that the visible GoFundMe option was disabled.
- Show the `donationOptions` array and `enabled` pattern.
- Mention the dark-mode text visibility fix.

### 3:06-3:36 - Footer branding and cleanup

- Explain the branding simplification.
- Show that Notes and Newsletter are hidden until ready.
- Mention removal of unfinished project links like Boyle, Wilkes, and Zebonastic.

### 3:36-4:02 - Validation and handoff

- Show the behavior checks the next developer should run:
  - `/80-days` redirects correctly
  - donate page shows active options
  - dark-mode text stays readable
  - footer links match the current project state

### 4:02-4:20 - Your turn

- Invite the next developer to trace one fix from branch to changed files to final behavior.
- Mention that the next video will cover reusable components and merge strategy.

### 4:20-4:26 - Outro

- Close with `@HumanitariansAI`
