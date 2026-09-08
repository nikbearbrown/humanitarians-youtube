# Beat Sheet — "Upload to GitHub. No Code." (v3)

**Series:** Humanitarians AI · Fellows Tutorial · Sanjana · @HumanitariansAI
**Style:** Claude palette (cream `#FAF9F5`, warm ink `#3D3929`, terracotta `#D97757`), brutalist structure. **Intro & outro reuse the exact Claude scenes from the reference video** (`ClaudeComposerAsk` + `ClaudeTitleOutro`, EB Garamond serif); the body is the light-theme GitHub / Drive / Windows Explorer tutorial inside cream insets.
**Audio:** Kokoro `af_bella` voiceover (master clock) + SFX (clacks, chimes on Commit/Merge/Copied, whoosh). Narration opens with **"Hi, I'm Sanjana. This video is about…"**
**Masters:** 16:9 (3840×2160, ~3:08) + 9:16 Short (2160×3840, ~1:10), true 4K, 30 fps, AAC.

## LONG CUT — 16:9 (16 beats)

| # | Beat | Scene | Gist |
|---|------|-------|------|
| 1 | **Intro (reference style)** | `ClaudeComposerAsk` | Eyebrow "HUMANITARIANS AI · FELLOWS TUTORIAL" · serif "Upload to GitHub — No Code" · **"Hi, I'm Sanjana"** · composer types the ask · @HumanitariansAI |
| 2 | Golden Rule | GoldenRule | GitHub = TEXT & DOCS · Drive = MP4 & MEDIA · <25 MB & text → GitHub |
| 3 | Edge case | EdgeCaseCard | 30 MB README → text ✓ but >25 MB ✕ → Drive. "Size beats type." |
| 4 | **Step 1 — create a branch** | CreateBranchScene | branch **main ▾** → type `sanjana-rao` → **Create branch from 'main'** |
| 5 | **Step 2 — navigate** | BranchContext | now on `sanjana-rao`; open `fellows/` |
| 6 | **Step 3 — Add file** | AddFileMenu | Add file ▾ → Upload files |
| 7 | **Step 4 — Explorer** | ExplorerScene | Windows Explorer / Finder — find the folder, don't open it |
| 8 | **Step 5 — drag folder** | DragDropScene | drag the whole folder into the dashed box; `sanjana-rao/…` paths kept; progress → ✓ |
| 9 | **Step 6 — commit** | CommitScene | message + **Commit directly to the sanjana-rao branch** → green Commit changes |
| 10 | **Step 7 — pull request** | PRScene | base `main` ← compare `sanjana-rao` → Create → **Merged** (Nik Bear Brown) |
| 11 | Gotchas | GotchasScene | 25 MB/file · 100 files max (videos → Drive) · Chrome/Edge, not Firefox/Safari |
| 12 | Google Drive | DriveScene | upload the two MP4s → Share → Copy link |
| 13 | README link | ReadmeScene | paste `[▶ Watch on Google Drive](…)` → commit |
| 14 | Handoff scaffold | HandoffScaffold | copyable README card |
| 15 | End card | EndCard | **PUSHED? MESSAGE SANJANA.** |
| 16 | **Outro (reference style)** | `ClaudeTitleOutro` | serif **"Push It. No Code."** · @HumanitariansAI · "GitHub for text · Drive for video · you for the work" |

## SHORT CUT — 9:16 (14 beats)

Intro → Golden Rule → **create a branch** → navigate → Add file → Explorer → **drag folder** → commit → PR → Drive → README → Handoff → End → Outro. Same reference-style intro/outro, condensed narration.

## Notes
- Intro/outro are the repo's `ClaudeComposerAsk` / `ClaudeTitleOutro` — pixel-matched to the uploaded reference (EB Garamond loaded via `fonts.tsx`).
- A fake cursor drives every control; on Step 1 it types the branch name and clicks "Create branch", on Step 5 it drags a `sanjana-rao` folder chip into the box.

*Source: `runtime/remotion/src/fellows-github/` · timings in `timing-long.json` / `timing-short.json`.*
