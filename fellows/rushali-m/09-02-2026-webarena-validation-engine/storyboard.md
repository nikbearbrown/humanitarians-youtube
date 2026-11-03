# Storyboard

## Video

From WebArena Findings to a Practical AI Web Validator

## Paper

**WebArena: A Realistic Web Environment for Building Autonomous Agents**  
**Authors:** Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig

## Submission Details

- Fellow: Rushali Moteria
- Date: Wednesday, September 2, 2026
- Channel: `@HumanitariansAI`
- Runtime: `1:48.45`
- Formats: 4K landscape `3840x2160` and portrait `2160x3840`

## Structure

### 0:00-0:14 - Paper and Personal Framing

- Open with: `Hi I am Rushali and the video is about WebArena and my proposed AI web validation architecture.`
- Display the paper and author information.
- On-screen greeting: `Hello, Rushali!`

### 0:14-0:31 - What WebArena Shows

- Introduce the 812 long-horizon tasks and the 10.59% best GPT-4 end-to-end success result.
- Highlight premature stopping, observation bias, and missed details.

### 0:31-0:46 - Representation Insight

- Compare screenshots, raw DOM, and accessibility-tree observations.
- Explain why compact semantic context is a useful design direction.

### 0:46-1:00 - Stage One: Ingestion

- Show the headless browser visiting a URL and waiting for dynamic rendering.
- Emphasize capturing the page users actually see.

### 1:00-1:15 - Stage Two: Transformation

- Show raw HTML becoming clean Markdown or an accessibility tree.
- Distinguish the proposed token-reduction target from a result established by the paper.

### 1:15-1:32 - Stages Three and Four

- Show multi-page cross-checking for dates, prices, and calls to action.
- Show strict JSON output containing bug type, severity, URL, and evidence.

### 1:32-1:48 - Humanitarians AI Impact

- Explain how the design could become an AI agent for automated web checking.
- End with structured evidence flowing into GitHub Issues, Jira, or CI/CD.
- End card: `@HumanitariansAI`.

## Visual Notes

- The supplied architecture diagram is used during the pipeline explanation.
- Landscape and portrait use identical narration and audio; only the composition changes.
- Portrait cards are vertically stacked with bounded text panels and generous spacing to prevent overflow or overlap.
