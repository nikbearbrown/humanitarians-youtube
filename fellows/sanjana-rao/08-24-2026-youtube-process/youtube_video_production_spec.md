# VIDEO PRODUCTION SPEC — Volunteer YouTube Submissions
### Machine-readable rewrite of the review-process brief

---

## 0. WHAT THIS DOCUMENT IS

The source brief describes a **human review workflow**. An AI cannot execute
a review workflow. It can only execute the production constraints buried
inside it.

This spec separates the two:

| Layer | Executable by AI | Executable by human |
|---|---|---|
| A. Production constraints | YES | — |
| B. Submission & review chain | NO | YES |

An AI reading this document acts on **Layer A only**. Layer B is included so
the AI knows what its output must survive.

---

## 1. MISSING INPUTS — REQUIRED BEFORE GENERATION

The source brief specifies **format** but not **instruction**. These four
fields are mandatory. Do not begin generation until they are supplied.

```yaml
project_name:        # string — used in filename, must match PM's project register
volunteer_name:      # string — used in filename
audience:            # NOT "students". Specify: level, discipline, prior knowledge.
                     # e.g. "First-year BSc biology students, no statistics coursework"
learning_outcome:    # ONE measurable behavior. Must survive the test in §1.1
runtime_target:      # minutes. Default 8 if unspecified.
```

### 1.1 Learning outcome validation gate

Reject and request rewrite if the outcome string contains:
`understand` · `appreciate` · `be aware of` · `learn about` · `know`

These name mental states. A camera cannot film a mental state.

**Accept only outcomes matching this shape:**

> After watching, the learner can `[VERB]` `[OBJECT]` `[CONDITION]`.

Valid verbs: construct, identify, calculate, distinguish, predict, label,
sequence, diagnose, translate, defend, refute, apply.

- REJECT: "Understand photosynthesis"
- ACCEPT: "Identify the two inputs and two outputs of photosynthesis from an unlabeled diagram"

---

## 2. LAYER A — PRODUCTION CONSTRAINTS (AI-EXECUTABLE)

### 2.1 Toolchain — non-negotiable

```yaml
generator: Brutalist
version: latest weekly release        # verify before each build; do not use cached version
substitution: forbidden               # no other deck/video tool is acceptable
```

Videos not produced with Brutalist are rejected at review regardless of
quality. Version drift is a rejection cause — the weekly release changes
output structure.

Operator tutorial (human-only reference, requires passcode `xT*76tpx`):
`https://us06web.zoom.us/rec/play/MA9SlwhFMvIjljNBYDHNr5fTkYltHU0CQGZ7U6tQlZlkq7T4EegNCO1iVVorqFj2fKS9n5xS8QMuZZaw.J6S3Whsd7ZJ0W48B`

### 2.2 Output artifacts — all three required

A submission is incomplete unless all three exist:

```yaml
1_video_file_landscape:
    aspect: 16:9
    resolution: 3840 x 2160        # 4K UHD, exact
    downscaling: forbidden
    filename: "{ProjectName}_{VolunteerName}_16x9"

2_video_file_vertical:
    aspect: 9:16
    resolution: 2160 x 3840        # vertical 4K — NOT a crop of the landscape master
    downscaling: forbidden
    filename: "{ProjectName}_{VolunteerName}_9x16"

3_source_code:
    destination: GitHub repository (public or org-accessible)
    scope: all code used to produce the film
    status: mandatory — no exceptions, every submission, every iteration
    deliverable: repository URL, submitted alongside the video

4_repository_url:
    submitted_with: both video files, in the same handoff
```

Base filename convention is unchanged — `{ProjectName}_{VolunteerName}` —
with the aspect suffix appended. Confirm with your PM whether they want the
suffix or two separate uploads; the source brief specifies only the base form.

### 2.3 Resolution and dual-aspect authoring

Build at native 4K from the first frame. Do not author at 1920×1080 and
upscale — brutalist typography and rule weights break under interpolation.

**The 9:16 version is a second layout, not a crop.** A 16:9 brutalist slide
cropped to vertical loses its left and right thirds, which is where the rule
lines, labels, and axis text live. Author the deck with a safe column and
emit two layouts from one content source:

```yaml
layout_strategy: single content model → two renders
safe_column: center 1080px of the 16:9 frame carries all critical text
vertical_reflow: stack elements that sit side-by-side in landscape
forbidden: center-crop of the landscape master
verification: read every text element at 100% zoom in BOTH renders
```

### 2.4 Mandatory intro

The first spoken line is fixed. Do not paraphrase, do not add a cold open
before it.

```
"Hi, I am {VolunteerName}, and this video is about {one-sentence summary}."
```

Constraints on `{one-sentence summary}`:
- One sentence, under 25 words
- States what the viewer will be able to do, not the topic name
- Written as speech — contractions allowed, clause stacking not

- REJECT: "...this video is about neural networks."
- ACCEPT: "...this video is about how to read a neural network diagram and trace one prediction through it."

### 2.5 Render integrity

Every one of these is checked frame by frame before handoff:

```yaml
images:      all rendered — no broken links, no alt-text placeholders,
             no empty containers, no partially loaded assets
text:        legible at 100% zoom on a phone screen in the 9:16 render
formatting:  no clipped elements, no overlapping layers, no overflow,
             no default-font fallbacks where a brutalist face was specified
export:      verify the uploaded YouTube stream serves 2160p —
             a 4K source file that YouTube transcodes down is a failure
```

---

## 3. LAYER B — SUBMISSION CHAIN (HUMAN-EXECUTABLE)

The AI does not perform these steps. It produces output that enters them.

```
STAGE 1  FELLOW  →  DRIVE
         Fellow uploads both renders + GitHub URL to the shared folder:
         https://drive.google.com/drive/folders/1PCcSc-HN2uReHp0_a72ppKj7GpmWI8d2
         Fellow notifies Sanjana Rao or Pooja that the upload is ready.
         Files are named correctly BY THE FELLOW at upload time — see §3.3

STAGE 2  SANJANA / POOJA  →  REVIEW
         First-pass review of the submission.

STAGE 3  QUALITY CHECKS
         The six-criteria acceptance gate (§3.1) is applied.
         Any single failure = REITERATE → return to STAGE 1.
         Re-uploads repeat the GitHub commit for the revised version.

STAGE 4  PUBLISH
         Upload to the Humanitarians AI YouTube channel
         Playlist: "Queue"
         Awaiting review by: Prof. Brown and Prof. Nina
```

**Terminal state clarification.** Publishing to the Queue playlist is not
approval — it is submission to the *next* review layer. Prof. Brown and
Prof. Nina review after upload, not before. The AI's output is therefore
built to survive two independent reviewers, not one.

### 3.0 Conflict with the original brief — resolve before circulating

The two descriptions of this flow do not agree:

| | Original brief | This flow |
|---|---|---|
| Who uploads to Drive | Project PM | Fellow |
| Who renames the file | Project PM | Fellow (implied) |
| Project PM's role | Routes and renames | Not mentioned |

Two versions of "who renames the file" is the failure that produces a Drive
folder of inconsistently named videos. **Decide one:**

- **(A) Fellow uploads and names.** Faster, one fewer hop. PMs become
  notification recipients rather than gatekeepers. Requires the naming
  convention to be published to every fellow.
- **(B) PM uploads and names.** Enforces naming at a single choke point.
  Slower, and PM-less fellows still route to Sanjana/Pooja.

The flow above assumes **(A)**, since it names the Fellow as the uploader.
If PMs still handle renaming, say so and I'll insert them back into STAGE 1.

### 3.3 Naming — enforced at upload, not after

Whoever uploads applies this. Both files, same base:

```
{ProjectName}_{VolunteerName}_16x9
{ProjectName}_{VolunteerName}_9x16
```

No spaces. No dates. No `_final`, `_v2`, `_FINAL2`. Re-uploads overwrite or
replace — version history lives in GitHub, not in filenames.

### 3.1 QUALITY CHECKS — the six acceptance criteria

Applied at STAGE 3 by Sanjana / Pooja. This is the gate the AI's output must
clear. Build to it directly.

| # | Criterion | Pass condition | Objective? |
|---|---|---|---|
| 1 | Brutalist format | Produced with current-week Brutalist; visual system intact | Yes |
| 2 | 4K on YouTube | Stream serves 2160p after upload — not just the source file | Yes |
| 3 | Both aspect ratios | 16:9 and 9:16 both delivered, both natively laid out | Yes |
| 4 | Render integrity | Images rendered, text legible, no formatting breaks (§2.5) | Yes |
| 5 | Intro line | Exact form in §2.4, name and summary present | Yes |
| 6 | Knowledge gained | See §3.2 — needs definition | **No** |

### 3.2 Criterion 6 is not yet testable

"Knowledge is gained out of the video" is the only criterion on this list a
PM cannot check the same way twice. Five PMs will pass five different videos
under it. It is a feeling, not a gate.

It becomes testable the moment it is bound to the `learning_outcome` declared
in §1. Proposed replacement wording:

> **6. Outcome delivered.** The video's stated learning outcome appears
> on screen or in narration within the first 30 seconds, and the video
> demonstrates that specific behavior at least once. A viewer with the
> declared prior knowledge could perform the outcome after one watch.

Checked as: *"Can I name the one thing a viewer can now do that they
couldn't before? If I can't say it in a sentence, it fails."*

This also gives REITERATE feedback something to point at. "Knowledge wasn't
gained" is not actionable. "The outcome was 'trace one prediction through a
network' and the video never traces one" is a fix.

**Loop implication for the AI:** build every asset to be regenerable.
Rejection is expected at least once. Hard-coded values, manual edits made
outside the code, and untracked assets make iteration expensive. Everything
that shapes the final frame lives in the repository.

---

## 4. WEEKLY CADENCE AND SHORTS SCHEDULING

### 4.1 The unit problem — read this first

"4 videos weekly" and "2 videos each week" are both true because they count
different things. The spec resolves it as:

```yaml
content_pieces_per_week: 2        # two distinct scripts, two distinct topics
files_per_content_piece: 2        # 16:9 render + 9:16 render
files_uploaded_per_week: 4        # 2 × 2
```

**One video = one script rendered twice.** The 9:16 is not a second video and
does not count toward the weekly two. Everywhere below, "video" means a
distinct content piece; "file" means a render.

### 4.2 Standard week

| Slot | Content | Renders |
|---|---|---|
| A | STEM or AI topic of the fellow's choosing | 16:9 + 9:16 |
| B | Progress update on the fellow's project | 16:9 + 9:16 |

Total: 2 videos, 4 files.

### 4.3 Substitution rule — the two-week window

Slot B is flexible week to week. A fellow may substitute a passion-topic
video for the project update, **provided the research-update floor holds
across any rolling two-week window:**

```yaml
window: 2 weeks
videos_in_window: 4              # 2 per week
research_updates_required: >= 1  # minimum, across the window
substitutable: the remaining 3
```

Legal patterns over two weeks (R = research update, P = passion/STEM topic):

```
R P | P P     valid — floor met in week 1
P P | R P     valid — floor met in week 2
R P | R P     valid — exceeds floor, default pattern
P P | P P     INVALID — no research update in the window
```

The floor is a minimum, not a target. Two updates in two weeks is the
default; one is the exception a fellow can take when a week goes sideways.

**Ambiguity flagged:** the source says "at least one of the four videos over
two weeks." Written literally, a fellow could post one research update every
two weeks indefinitely and stay compliant — meaning project progress is
documented half as often as the standard week implies. If the intent was
"one per week, with a two-week grace period for a missed one," the rule needs
that wording. Confirm which.

### 4.4 Shorts (9:16) scheduling

These are publishing rules, applied at STAGE 4. They constrain scheduling,
not production.

```yaml
minimum_spacing: 60 minutes after the previously scheduled Short
scope: channel-wide, across all fellows — not per-fellow
implication: Shorts queue globally; a fellow's 9:16 may publish
             later than their 16:9 by design
```

**Why this matters for the AI's output:** the 9:16 will not be viewed
adjacent to its 16:9 counterpart. It must stand alone. It cannot open with
"as we saw in the main video" or assume prior context. The intro line in
§2.4 is required in both renders for exactly this reason.

### 4.5 Short linking

Every Short links to the most popular existing video on a related subject.

```yaml
link_target: highest-view-count video in a related subject area
scope: the Humanitarians AI channel library
selection: check current view counts at scheduling time — not from memory,
           not the last one used
required: yes, every Short
```

Selection is done at STAGE 4 by whoever schedules, since the most popular
related video changes over time. The fellow supplies the subject area; the
scheduler picks the target.

---

## 5. GENERATION SEQUENCE

Execute in this order. Do not skip forward. **Run once per content piece —
twice per week.**

```
1.  Collect the five fields in §1
2.  Validate learning_outcome against §1.1 — halt and request rewrite on failure
3.  Write the intro line (§2.4) FIRST — it forces the summary to be specific
4.  Run: storyboard [content]      → one idea per scene, safe-column layout
5.  Run: deck [content]            → blueprint + brutalist HTML, dual-aspect
6.  Render 16:9  → 3840×2160
7.  Render 9:16  → 2160×3840  (re-layout, not crop)
8.  Frame-check both against §2.5
9.  Name files with aspect suffix
10. Commit all source to GitHub, capture URL
11. Self-check against the six criteria in §3.1
12. Upload both renders + GitHub URL to the Drive folder, correctly named
13. Notify Sanjana Rao or Pooja
```

---

## 6. REJECTION CAUSES — CHECK BEFORE HANDOFF

**Format**
- [ ] Produced with current-week Brutalist release
- [ ] 16:9 render is exactly 3840×2160, natively authored
- [ ] 9:16 render is exactly 2160×3840, re-laid-out and not cropped
- [ ] YouTube stream serves 2160p after upload, both versions
- [ ] Filenames follow `{ProjectName}_{VolunteerName}` + aspect suffix

**Integrity**
- [ ] Every image renders — zero placeholders, zero broken assets
- [ ] All text legible at 100% zoom, checked in the 9:16 render on a phone
- [ ] No clipping, overlap, overflow, or font fallback

**Content**
- [ ] Opens with the exact intro line: name + one-sentence summary
- [ ] Summary states a capability, not a topic name
- [ ] Learning outcome is a behavior, not a mental state
- [ ] The video demonstrates that behavior at least once
- [ ] Every scene covers exactly one idea
- [ ] Audience is specified to a level that changed the script

**Cadence**
- [ ] 2 content pieces this week, 4 files total
- [ ] Research-update floor met across the rolling two-week window
- [ ] 9:16 stands alone — no references to the 16:9 version
- [ ] Subject area supplied for the Short's link target

**Handoff**
- [ ] Both renders uploaded to the Drive folder, correctly named at upload
- [ ] GitHub repository exists and URL is included with both files
- [ ] Sanjana or Pooja notified
- [ ] Self-checked against all six quality-check criteria (§3.1)
