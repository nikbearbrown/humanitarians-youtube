# SHOTLIST — meddas-dev-pipeline-gcp-deployment
## Total: 2:28 (148.3s) · 9 beats

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | INTRO | bookend | REMOTION | ClaudeComposerAsk | 12.95s | Cold open, Claude cream skin; title card |
| B01 | CONTAINERIZATION | remotion | REMOTION | GitHubCallChain | 22.19s | Source → Node build → Nginx → container image |
| B02 | CLOUD INFRASTRUCTURE | remotion | REMOTION | GitHubCallChain | 19.22s | Image → Artifact Registry → Cloud Run |
| B03 | SECURE AUTHENTICATION | remotion | REMOTION | GitHubCallChain | 21.01s | GitHub Actions → Workload Identity Federation → GCP IAM |
| B04 | AUTOMATED CI/CD | remotion | REMOTION | GitHubCallChain | 22.21s | PR → lint/test/build → tag → build/push/deploy |
| B05 | INSTANT ROLLBACK | remotion | REMOTION | GitHubCallChain | 16.85s | Previous image → rollback workflow → redeployed |
| B06 | ENVIRONMENT-AWARE DESIGN | remotion | REMOTION | GitHubCallChain | 19.43s | Dev → staging → production, same pipeline |
| B07 | CLOSING | bookend | REMOTION | ClaudeVerdictArtifact | 9.19s | 5-line verdict card, Claude cream skin |
| B08 | OUTRO | bookend | REMOTION | ClaudeTitleOutro | 5.29s | Title restate + "This is Darshil" sign-off |

## Lane summary (body beats B01–B06, excluding bookends B00/B07/B08)

| Lane | Count | Beats |
|---|---|---|
| remotion (GitHubCallChain diagrams) | 6 | B01 B02 B03 B04 B05 B06 |
| card (bookend) | 2 | B00 B07 |
| outro | 1 | B08 |

No vox stills, no Manim, no pantry assets — every beat is diagram-driven
Remotion, matching the source script's "On screen: Diagram — …" direction for
each of its eight slides (slide 1 intro + slide 8 closing folded into the
bookend patterns; slides 2–7 map 1:1 to B01–B06).

## Pantry slates

None. No open slots — all 9 beats render from coded Remotion patterns already
proven in this book (`ClaudeComposerAsk`, `GitHubCallChain`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`).
