# Week 7 Summary: Redesigning Source Control at Anthropic (Scion & Antique)

## Video Links

- [16:9 video](https://drive.google.com/file/d/1xz1x9fcxEY6vCJDcc-OE6IVJkftIRW4m/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/14iKqr9zQUYYMyc6btWhrs1l7shz42fl4/view?usp=drive_link)

In Week 7, we tear down Anthropic's engineering blog post **"Redesigning source control at Anthropic"** (published October 2026), detailing how a team of seven engineers migrated Anthropic's monorepo from git to an in-house version control system called **Scion**—alongside the **Antique** code review surface, code search, and directory-level IAM—in just five months.

As Claude shifted software engineering bottlenecks from writing code to developer infrastructure, daily merged changes exploded more than tenfold from ~2,500/day in May 2026 to **30,401/day on September 9, 2026**. With a ~100 GB main branch history, a >25 GB compressed working copy, and 25 million CI checkouts per day (>600 PB/day of naive git traffic), git's offline, decentralized model and hundreds of internal mirrors became the primary bottleneck.

## Key Highlights

- **6 Principles for Agent-Scale Source Control** (building on Google's Piper & Meta's Sapling): Always-online clients, client-server asymmetry, comprehensive API access (zero-checkout CI queries), horizontal scalability with zero packfiles, cheap lock-free server commits, and optional sparse/virtualized working copies.
- **Changesets & Recursive Derived Data**: Metadata stored as changesets in a **Spanner** write-ahead log (recording only file changes relative to the first parent) with immutable, compressed, hash-deduplicated blobs in **Cloud Storage**. Root trees, file blame, path history, and commit graph skip lists are computed recursively as derived data.
- **3-Tier Content-Addressed Checkout Architecture**: Per-node `scion-daemon`, regional in-memory `scion-cache`, and authoritative `scion-server` speaking identical RPCs with >99% cache hit rates, shrinking infrastructure CPU/RAM footprint by **200x** and reclaiming **25% of CI CPU capacity**.
- **Monorepo Speedups (`scn` vs. `git`)**:
  - Developer `status`: 3.9s → 19ms (**207x faster**)
  - Agent `new worktree`: 7.1 min → 5.1s (**84x faster**)
  - Developer `pull latest`: 87s → 3.5s (**25x faster**)
  - Agent total source control time per CR: 34 min → 3.7 min (**9.2x faster**, saving **~11,000 agent hours/day**)
  - CI & compute checkouts: **8.0x–8.8x faster**, saving **~280,000 machine hours/day**
- **Building Agent-Scale Software with Claude**: Built with **Claude Mythos Preview** and **Claude Tag** (12,257 changes across `scm/` and `antique/`). Claude Mythos Preview rewrote the handwritten git-to-Scion ingestion prototype to use **20x less memory** and run **4x faster**, while engineers shifted to reviewing **intent**, telling Claude "no" on invariant violations, running Slack component **"superfans"**, and replacing global merge queue locks with post-merge automated testing.

## Chapters

- `0:00` - Introduction: The 12x Merge Surge & Scion Migration
- `0:17` - Why Decentralized Git Strained at Agent Scale
- `0:34` - Monorepo Merge Trajectory & Mirror Bottlenecks
- `0:51` - Six Principles for Agent-Scale Source Control
- `1:09` - Scion Data Structures: Changesets & Derived Data
- `1:26` - 3-Tier Content-Addressed Checkout Architecture
- `1:45` - Building Scion with Claude Mythos Preview & Claude Tag
- `2:03` - Monorepo Benchmarks: Git vs. Native Scion (`scn`)
- `2:22` - Security, Slack Superfans & Post-Merge CI
- `2:37` - Your Turn to Explore
- `2:50` - Outro

---
*Created by Hrishikesh for RamanEffect.*
