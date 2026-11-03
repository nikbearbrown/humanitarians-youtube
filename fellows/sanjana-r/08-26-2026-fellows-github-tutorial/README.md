# Upload to GitHub. No Code. — Humanitarians AI Fellows Tutorial (v2)

A **Claude-styled** (cream + terracotta) brutalist tutorial with **voiceover**, teaching non-developer fellows how to push a folder to GitHub using only the web interface — with the **Windows/Mac folder drag-and-drop** flow — and where video belongs. Customized for **Sanjana** · **@HumanitariansAI**.

## The masters (both true 4K, 30 fps, with audio)

| File | Aspect | Resolution | Length | Use |
|------|--------|-----------|--------|-----|
| `UploadToGitHub-NoCode-16x9-4K.mp4` | 16:9 landscape | 3840×2160 | ~3:08 | Main YouTube video |
| `UploadToGitHub-NoCode-9x16-Short-4K.mp4` | 9:16 vertical | 2160×3840 | ~1:10 | YouTube Shorts |

**Intro & outro** reuse the exact Claude scenes from the uploaded reference video (`ClaudeComposerAsk` + `ClaudeTitleOutro`, EB Garamond serif). The intro opens with Sanjana's spoken hello ("Hi, I'm Sanjana. This video is about…"). The body is the light-theme GitHub/Drive/Explorer tutorial.

**Audio:** Kokoro `af_bella` voiceover (local, free, no account) + subtle SFX (keyboard clacks, chimes on Commit/Merge/Copied, whooshes). Narration is the master clock — the visuals are cut to the voice.

> Native 4K flat-vector render — do **not** run Topaz/upscaling. Judge at forced **2160p**, not "Auto."

## What it teaches (the 7-step flow)

1. **Create a branch** — branch `main ▾` → type `sanjana-rao` → **Create branch from 'main'**.
2. **Navigate** — now on your branch; open `fellows/`.
3. **Add file → Upload files** (top-right dropdown).
4. **Open Windows Explorer / Finder**, find your folder — *don't open it*.
5. **Drag the whole folder** into GitHub's dashed box; the folder path is kept on every file; wait for the progress bars.
6. **Commit** — message, keep *Commit directly to the `sanjana-rao` branch*, click green **Commit changes**.
7. **Open a PR** — base `main` ← compare `sanjana-rao` → Create → a maintainer (Nik Bear Brown) merges it.
- **Gotchas** — 25 MB/file, 100 files max (videos → Drive); use **Chrome/Edge**, not Firefox/Safari.
- **Video → Drive → link in README** — the golden rule: text & <25 MB → GitHub, video/big → Drive.

Real target for fellows: <https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows>

## Companion files
- `beat-sheet.md` — 15-beat long / 13-beat short structure, palette, motion & sound
- `script.md` — the full voiceover script (long + short)
- `PROOF-REVIEW.md` — self-assessment against the PROOF rubric

## Fellow folder README template (what a fellow copies into their own folder)

```markdown
# <Firstname Lastname> — Fellow

Beat sheet & script are in this folder.
The final videos live on Google Drive:

[▶ Watch on Google Drive](https://drive.google.com/…/your-folder)
```

## Delivery / next steps
- Delivered to this folder (not pushed to GitHub, per project convention).
- **Open item (confirm with Professor Brown):** whether tutorial MP4s live in a `Tutorials/` Drive subfolder or the general finished folder.

*Rendered with the brutalist.art Remotion toolkit · source: `runtime/remotion/src/fellows-github/`.*
