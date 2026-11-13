# Week 28 — Topic Selection

**Selected:** `claude-for-design/the-chromatic-manipulation`
**Source:** the essay "The Chromatic Manipulation: How Color Psychology Controls Emotion in Music", which the topic folder is built on
**Decided:** 2026-10-25

## How it was chosen

- `git fetch origin` (plain, no prune) refreshed the local `origin/*` refs: 98 remote branches. Every later
  command was `ls-tree` / `show` / `grep` against a ref. Nothing was checked out, pushed or modified.
- Pool: every `claude-for-*` topic folder on every branch, variant prefixes normalised
  (`nbb-`, `claude-liam-`, `medhavy-vox-`, `vox-`, `cli-`, `hai-`, `riff-`, `qmcg-`), singletons only.
- Filter: every content word of the topic shared by at most 3 paths library-wide, and none recurring in our own
  Week 15–27 notes. Five topics survived; one was drawn at random (unseeded).
- Rejected draws on the way: `variational-bound` (about 16 variants), `nine-weights-convolution` (in our own
  Week 18/19/20/26 notes), `classifying-supernovae` (a fellow's video on the same subject).

## Known exception, accepted by Tanmay

`claude-for-design` was our Week 24 collection, and Weeks 25–26 excluded used collections. Tanmay decided to keep
this pick because the **topic** has not been used, and the keyword `chromatic` appears in no other path.

## Build state of the folder

A beat sheet with its README, BUILD-PROMPT, SOURCES and `beat_sheet.json`; no production files (FACTCHECK, SRT, YouTube
metadata) were on `main` when the topic was drawn.
