# Video Requirements: How to Upload Video Files to GitHub Without Code

## Overview

**Topic**: How to upload video files to GitHub without code
**Format**: Brutalist (fully code-generated, no talking head)
**Tool**: Brutalist video production
**Audience**: Fellows, students, and volunteers contributing to shared repos with no prior Git experience

## Core Message

Non-coders can contribute to GitHub repos using the web interface. The key rule is knowing what goes where.

- **GitHub** holds text, beat sheets, and .md files
- **Google Drive** holds MP4s and large media files
- Rule of thumb, if it is under 25 MB and text-based, use GitHub. If it is video or large media, use Google Drive.

## Technical Specs

- **Resolution**: 4K, 3840x2160
- **Formats required**: Both 16:9 landscape and 9:16 vertical
- **Style**: Brutalist, code-generated
- **Voiceover**: None, on-screen text carries all instructions

## Delivery Split

### To GitHub (fellow's named folder, via branch and PR)

- `beat-sheet.md`
- `script.md` or narration file
- `README.md` with a link to the Google Drive video
- Any process notes

### To Google Drive (shared channel folder)

- Final 16:9 MP4 at 3840x2160
- Final 9:16 MP4 at 2160x3840
- Share link pasted into the GitHub `README.md` so the video is findable from the repo

### Notification

After the PR is merged and the MP4s are in Drive, message Sanjana with links to both. No first-pass review is required before pushing.

## GitHub Folder Setup

Before uploading anything, the fellow needs to:

1. Navigate to `humanitarians-youtube/fellows/` on their own branch
2. Create a new folder named after themselves, for example `firstname-lastname`
3. Place all beat sheets, .md files, and documentation inside this folder
4. Open a PR to merge into main, then notify Sanjana

Note, GitHub's web UI does not have a direct "create folder" button. Create a folder by creating a new file and typing `foldername/filename.md` in the name field. The slash tells GitHub to make the folder.

## Brutalist Style Requirements

Since this is fully Brutalist with no talking head, the entire video is code-generated. Plan for:

- **Typography as the star**, large monospace or bold sans-serif type doing most of the storytelling. File names, folder paths, and commands displayed as full-screen text moments.
- **Hard color blocks**, one color assigned to GitHub segments, a different color for Google Drive segments, so viewers visually track which platform they are on at any moment.
- **Screen recording insets**, when showing the GitHub or Drive interface, frame recordings inside heavy borders or offset them within a colored background rather than letting them float edge to edge.
- **Motion cues**, text slams in, cuts are hard, no soft fades.
- **Text overlays for every action**, since there is no voiceover, on-screen text carries the instruction. Examples, "CLICK ADD FILE", "DRAG THE FOLDER", "COMMIT TO YOUR BRANCH".
- **Sound design**, sharp mechanical cuts, keyboard clacks, notification sounds. No music bed or minimal industrial texture only.

## Beat Sheet Skeleton

| Beat | Time | Content |
|------|------|---------|
| 1 | 0:00 to 0:08 | Title slam, "UPLOAD TO GITHUB. NO CODE." |
| 2 | 0:08 to 0:22 | Golden rule shown as two hard color blocks. Left, GitHub color, "TEXT AND DOCS". Right, Drive color, "MP4 AND MEDIA". |
| 3 | 0:22 to 0:40 | Create named folder in `fellows/`. Show the trick of typing `yourname/README.md` to force folder creation. |
| 4 | 0:40 to 1:05 | Switch to a branch, upload beat sheet and .md files, commit. |
| 5 | 1:05 to 1:30 | Hard cut to Drive color. Upload MP4s to shared Drive folder. Get share link. |
| 6 | 1:30 to 1:50 | Back to GitHub color. Paste Drive link into `README.md`. Commit. |
| 7 | 1:50 to 2:10 | Open PR to main. Merge. |
| 8 | 2:10 to 2:25 | End card, "PUSHED? MESSAGE SANJANA." |
| 9 | 2:25 to 2:35 | Channel outro card. |

## Open Items

- No dedicated Drive subfolder exists for tutorial content. Decide whether to create a `Tutorials/` folder inside the channel Drive or drop this video into the general finished folder. Confirm with Professor Brown before fellows begin following this workflow, otherwise MP4s will scatter.

## Production Checklist

- [ ] Beat sheet finalized in `beat-sheet.md`
- [ ] Script or narration text drafted for on-screen overlays
- [ ] Brutalist color palette selected, GitHub color and Drive color assigned
- [ ] Screen recordings captured at 4K
- [ ] 16:9 export at 3840x2160 rendered
- [ ] 9:16 export at 2160x3840 rendered
- [ ] MP4s uploaded to Google Drive, share links generated
- [ ] `README.md` in GitHub folder updated with Drive links
- [ ] PR opened from fellow branch to main
- [ ] Sanjana notified after merge
