# SOURCES — Dead Links, Live Redirects.

Every on-screen claim traces to a commit, a file, or literal command output in
`humanitarians_html`. Nothing here is reconstructed from memory.

## Scope

This reel covers the work done **after** `claude-hai-fellows-portal-refactor` was
built. That video's material ends at the role-tiering work (`0e8dc55`,
2026-06-09); this one runs from `0e125f1` (2026-08-10) to `HEAD` of branch `dev`.

⚠️ These are **not adjacent commits** — 26 commits sit between them, covered by
neither reel. See *Scope gap* below.

- Repo: `github.com/nikbearbrown/humanitarians_html`, branch `dev`
- Range: `0e125f1`..`b952855` — 11 commits, all **2026-08-10**, author `RishabhHM`
- Verified with: `git log --all --since=2026-07-29`

| commit | time | subject |
|---|---|---|
| `0e125f1` | 02:24 | Merge branch 'main' into dev |
| `13c3370` | 02:55 | chore: Ignore local-only dirs, wire up check-links script |
| `aa2f33f` | 02:56 | fix: Point 80 Days to Stay project link to /80-days |
| `0d012b9` | 02:56 | chore: Remove unlaunched Newsletter link from footer |
| `b501c2b` | 02:56 | fix: Style admin tools artifact links as buttons |
| `c89299f` | 02:57 | refactor: Consolidate duplicate Gru/CRITIQ/Tic TOC/Cajal tool artifacts |
| `4af984f` | 03:03 | fix: Restore legacy artifact files needed by redirects, exclude from Tools listing instead |
| `143df5f` | 03:05 | refactor: Remove dead /tools route, now fully superseded by /ai1/tools redirect |
| `aa5a8df` | 03:08 | feat: Replace /medhavy placeholder with real project content |
| `d2ccfeb` | 03:10 | fix: Remove dead Boyle Substack link from Projects page |
| `b952855` | 03:18 | feat: Add mycroft/medhavy/dayhoff.humanitarians.ai subdomains, point footer at them |

**The six minutes that make the video.** `c89299f` (02:57) deletes five artifact
files; `4af984f` (03:03) restores them. The commit message states the cause
directly: *"Restore legacy artifact files needed by redirects, exclude from Tools
listing instead."* The trap was hit in the real history and fixed six minutes
later — it is not a device invented for the reel.

## Commit → beat map

| beat | source |
|---|---|
| B00 INTRO | framing; the three findings listed are `d2ccfeb`/`0d012b9` (dead links), `143df5f` (dead route), `c89299f` (duplicates) |
| B01 PROBLEM | same three, restated as categories |
| B02 ASK 1 | intent behind `13c3370` |
| B03 CODE 1 | `scripts/check-links.mjs` lines 2, 27, 32–45; `package.json` script entry added in `13c3370` |
| B04 OUTPUT 1 | the crawl + `link-report.md`; easy fixes are `d2ccfeb`, `0d012b9`, `aa2f33f` |
| B05 ASK 2 | intent behind `c89299f` |
| B06 CODE 2 | literal `git show --stat c89299f` output |
| B07 OUTPUT 2 | the 404; cause is `rootFilesMovedToArtifacts` in `next.config.mjs` |
| B08 CHANGE | intent behind `4af984f`, taken from its commit message |
| B09 CODE 3 | `lib/html-meta.ts` as changed by `4af984f`, quoted verbatim |
| B10 OUTPUT 3 | redirect resolves + Tools lists once |
| B11 ASK 4 | intent behind `b952855` |
| B12 CODE 4 | `middleware.ts` as created by `b952855` |
| B13 OUTPUT 4 | `mycroft.humanitarians.ai` + footer, `b952855` |
| B14 SUMMARY | the four lessons, each traceable above |
| B14F FUTURE WORK | absence of CI/redirect tests — verified by inspection, see below |

## Verified specifics

**"5 files changed, 2612 deletions"** — literal output of `git show --stat c89299f`:
`cajal-reference.html` 440, `critiq-reference.html` 443, `gru-reference.html` 397,
`gru.html` 875, `tictoc-reference-v2.html` 457.

**"/tools … still shipping 288 lines"** — `143df5f` diffstat: `ToolsBrowser.tsx` 79
+ `[slug]/page.tsx` 88 + `page.tsx` 121 = 288 deletions.

**"a redirect is a reference"** — `next.config.mjs` `rootFilesMovedToArtifacts`
lists eight filenames; all five deleted by `c89299f` are in it. Each maps
`/<file>` → `/artifacts/<file>` with `permanent: true`. There is also a pattern
redirect `'/:file(.*\\-tool\\.html)'` → `/artifacts/:file`.

**Three subdomains** — `SUBDOMAIN_PROJECTS` in `middleware.ts` contains exactly
`mycroft.humanitarians.ai`, `medhavy.humanitarians.ai`, `dayhoff.humanitarians.ai`.

**"Rewrite, don't redirect"** — `middleware.ts` calls `NextResponse.rewrite(url)`,
not `redirect`. The file's own comment states the reason: *"this rewrites the
request to the project's existing internal page so the subdomain URL stays
visible."*

**B14F claims** — verified by inspection, not assumed:
- No CI runs the checker: `.github/` is gitignored (`.gitignore`, "Local-only /
  not for version control"), and `check-links` is a manual `npm` script.
- No redirect-destination test exists anywhere in the repo.
- `SUPERSEDED_ARTIFACT_FILES` is a hand-written literal `Set`, not derived from
  the `-tool.html` naming rule it describes — so it drifts by construction.

## Provenance — the redirect predates the delete

The `rootFilesMovedToArtifacts` list that breaks in B07 was **not written in this
reel's commit range**:

```
git log --all -S "rootFilesMovedToArtifacts" -- next.config.mjs
→ 2073715  2026-07-15  nikbearbrown
  "Add AI+1 hub: tools, lectures, visualizations, 108 simulations;
   retire /tools with redirects"
```

Four weeks before the delete, by a different author, in a commit about something
else entirely. This is the actual reason the delete looked safe, so **B08 states
it on air** ("four weeks earlier, a different author, the commit that built the
AI plus one hub — inherited config is still your config"). Omitting it would make
the mistake look more careless than it was.

The same commit also created the `/tools → /ai1/tools` redirect that B00's output
lines describe as having superseded the dead route, and that `143df5f` later
cleaned up after.

## Scope gap — chosen, not overlooked

Reel 1's content ends at `0e8dc55` (2026-06-09). This reel begins at `0e125f1`
(2026-08-10). **26 commits sit between them, covered by neither reel:**

| author | count | dates | subject |
|---|---|---|---|
| `RishabhHM` | 6 | 2026-07-01 | GoFundMe section removed from donate page; A–Z video sort with toggle; course-listing metadata; duplicate Computational Skepticism folders merged; misspelled slug fixed |
| `nikbearbrown` | 17 | 2026-07-15 – 07-17 | The AI+1 hub (tools, lectures, visualizations, 108 simulations); fellow video submissions; explainers page; YouTube publisher; Vercel 250MB tracing fixes |
| `Nik Bear Brown` | 3 | 2026-07-21 | Site-wide broken-link pass; Clients & Testimonials page; Substack/Spotify header buttons removed |

Excluded because they do not belong to this reel's spine: the July 1 batch is
course/donate/sorting work, and the July 15–21 batch is a different author's
feature program. Two consequences worth recording:

1. **The July 1 `RishabhHM` batch is undocumented by any reel.** It is a
   candidate for its own short video, not a fit for this one.
2. **`9d59ca1` (2026-07-21) was a prior site-wide broken-link pass**, by a
   different author. This reel never claims its crawler was the first link
   audit — the only primacy the narration implies is that it is the first
   *automated* one, which `13c3370` supports.

**Verified with:**

```
git log --all --since=2026-06-10 --until=2026-08-10 --format="%h %ad %an %s" --date=short
```

## Notes and judgment calls

- **`scripts/check-links.mjs` is gitignored** ("Local-only / not for version
  control"). It exists on disk and is quoted from there. The `package.json`
  entry that invokes it *is* committed, in `13c3370`. Worth knowing: the script
  the video teaches is not currently in the repo for a viewer to find.
- **`link-report.md` is dated 2026-06-10**, before this commit range, and is
  gitignored as generated output. B04 shows a *fresh* run rather than the
  committed report, so no stale counts reach the screen. No specific finding
  counts are spoken.
- **Commits not given their own beat**: `b501c2b` (button styling) and `aa5a8df`
  (/medhavy placeholder → real content) are real work in range but are cosmetic
  and content-authoring respectively, with no teachable mechanism. `aa5a8df` is
  acknowledged indirectly — `/medhavy` is one of the three subdomain targets in
  B11–B13. `0e125f1` is a merge with no independent content.
- **No fabricated numbers.** Where a count would date the video (how many dead
  links the crawler found), the narration describes the category instead.
