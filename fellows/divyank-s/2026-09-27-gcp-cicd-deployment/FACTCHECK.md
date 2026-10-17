# FACTCHECK.md — Claude, Shipped.

## Method note (read first)

No single source document — this reel covers well-established DevOps and
cloud-engineering practice (GitHub Actions, pull-request gating,
environment promotion, Docker, Kubernetes/GKE, and the three deployment
strategies). Per the DOUBLE-CHECK LAW, every claim is kept at the level of
**stable, publicly documented mechanism**, never a specific version
number, GCP price, quota, or console-UI detail (all of which change
frequently and would date the video or require a live source check this
build doesn't have).

## Claim-by-claim

| Beat | Claim | Category | Note |
|---|---|---|---|
| A1-2/A1-3 | GitHub Actions workflows trigger on push/pull_request; a PR-triggered run can be wired as a required status check | General/stable | Core, long-stable GitHub Actions/branch-protection mechanism, publicly documented by GitHub itself |
| A1-4 | Branch protection rules make a required status check actually block merging; without that setting a passing/failing check is informational only | General/stable | Documented GitHub branch-protection behavior, not version-specific |
| A2-2 | Dev/staging/production as three environments with escalating risk/strictness | General/stable | Universally used industry pattern, not tied to one vendor or tool |
| A2-3/A2-4/A2-5 | "Build once, deploy many" (promote the same artifact/image rather than rebuilding per environment) is a foundational CI/CD principle | General/stable | A widely-taught, foundational CI/CD principle (not attributed to one specific source here, since it's common knowledge across the field, not a single citable origin) |
| A3-1/A3-2/A3-3 | Docker packages an application with its runtime/dependencies into an immutable image, portable across environments | General/stable | Docker's own documented core value proposition, unchanged since its introduction |
| A3-4/A3-5 | Kubernetes' core job: scheduling, self-healing/restart, scaling, service discovery/traffic routing | General/stable | Kubernetes' own documented core responsibilities (the "control loop" model), stable across versions |
| A3-5 | GKE setup path: create a cluster, point kubectl at it, define a Deployment + Service, apply them | General/stable | The standard, long-stable GKE/kubectl workflow — no specific `gcloud`/`kubectl` command syntax, version, or flag is quoted on screen, to avoid a claim that could go stale |
| A3-6 | GKE Autopilot vs. Standard: Google-managed nodes vs. self-managed node pools, same Kubernetes API | General/stable | GKE's own documented mode distinction |
| A4-2 through A4-6 | Rolling/Blue-Green/Canary definitions, and their respective pros/cons/use cases | General/stable | Widely-documented, vendor-neutral deployment-strategy concepts taught across the industry (not specific to GKE or any one tool); no specific tool name (e.g. a particular service-mesh product) is claimed to implement canary, since that would need per-tool verification not done here |

## What was deliberately left out

- No specific `gcloud`, `kubectl`, or GitHub Actions YAML syntax is shown
  verbatim as if it were guaranteed-correct, current syntax — the beats
  describe the mechanism and the steps in prose, not a copy-pasteable
  script that could break on a version bump.
- No GCP pricing, quota, or SLA numbers.
- No claim that any one specific tool (e.g. a named service mesh or
  ingress controller) is required for canary — the reel states canary
  *needs* traffic-splitting infrastructure and metrics, without naming a
  specific product, since verifying one specific product's current
  canary support was out of scope for this build.

## Corrections applied

None — first draft, no prior version to correct against.
