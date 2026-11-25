# Fellowship Renewal Request — Darshil S.

**Name:** Darshil Rakesh Shah\
**Role:** Software Engineer\
**Project:** AIEM (Artificial Intelligence in Emergency Medicine) (private repo: `medas-aggregation-frontend`)\
**Current agreement dates:**  09/01/2026 to 11/30/2026\
**Requested renewal dates:** 12/01/2026 to 02/20/2027 (December 1, 2026 – February 20, 2027 · ~3 months)\
**Fellows folder:** [fellows/darshil-s](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s)

---

## Completed

1. **Dev Environment CI/CD & Rollback Pipeline:** Designed and validated the baseline CI/CD pipeline for the development environment — GitHub Actions CI (lint/test/build gating on PRs), a tag-triggered build/push/deploy workflow to Google Cloud Run via Workload Identity Federation, and a manual `workflow_dispatch` rollback workflow for instant redeployment of any previously built image, plus the full keyless GCP trust chain (WIF provider trust + IAM impersonation) underneath it. 
2. **Staging Environment: Provisioning, Security Hardening, Observability & Integration Validation:** Provisioned isolated GCP/GitHub infrastructure for staging (dedicated Artifact Registry namespace, scoped WIF trust, IAM binding, Environment secrets/vars), validated the pipeline end-to-end including rollback, added required-reviewer and branch-restricted protection rules plus Cloud Run invoker/ingress restrictions and vulnerability-scan/monitoring hardening, and ran a full frontend-to-backend integration and CORS validation pass. 
3. **Technical Learnings & Deployment Strategy Design (Terraform, Docker, Canary/Blue-Green):** Covered frontend delivery architecture, Infrastructure-as-Code (Terraform) concepts alongside Cloud Run cost optimization, container build/caching/vulnerability-scanning fundamentals, and designed + implemented canary and blue-green deployment strategies on `medas-frontend-stage` using Cloud Run's revision and traffic-splitting model.

---

## Hours Status

**20+ hours documented for every reported week** across Weeks 1–10

---

## Weekly Evidence Index

| Week / dates | Actual hours | Video links | Log and work evidence |
|---|---:|---|---|
| **Week 1** · Sep 10, 2026 | 22 | [Video Link](https://drive.google.com/drive/folders/1x2RXbtMA039v8GMeHRIrBLB2PVPse0RM) | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-09-10-meddas-dev-pipeline-gcp-deployment/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-09-10-meddas-dev-pipeline-gcp-deployment/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-09-10-meddas-dev-pipeline-gcp-deployment) |
| **Week 2** · Sep 17, 2026 | 21 | [Video Link](https://drive.google.com/drive/folders/1-gfOrdm5ffNZutoZxxmB7WbM2zOkBJPk)| [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-09-17-stage-env-provisioning/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-09-17-stage-env-provisioning/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-09-17-stage-env-provisioning) |
| **Week 3** · Sep 24, 2026 | 23 |  [Video Link](https://drive.google.com/drive/folders/1GV2-1DdGiNzHyJJgL5AOkbp0h8dB2UEL) | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-09-24-medas-stage-environment-security/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-09-24-medas-stage-environment-security/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-09-24-medas-stage-environment-security) |
| **Week 4** · Oct 1, 2026 | 21 |  [Video Link](https://drive.google.com/drive/folders/1eMPlTlB5VtejDu9B7RwtxMAAYaGoZ-5p) | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-01-medas-stage-pipeline-validation/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-01-medas-stage-pipeline-validation/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-10-01-medas-stage-pipeline-validation) |
| **Week 5** · Oct 8, 2026 | 23 |[Video Link](https://drive.google.com/drive/folders/13YGA00dwKUT37_YFmDvJGTcQSAbJEh0C)| [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-08-medas-stage-hardening-observability/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-08-medas-stage-hardening-observability/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-10-08-medas-stage-hardening-observability) |
| **Week 6** · Oct 15, 2026 | 21 |[Video Link](https://drive.google.com/drive/folders/1cUihkN1IDFJvsiE_tEYR0cWgXoQmxafr)  | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-15-medas-fullstack-integration-validation/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-15-medas-fullstack-integration-validation/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-10-15-medas-fullstack-integration-validation) |
| **Week 7** · Oct 22, 2026 | 23 |[Video Link](https://drive.google.com/drive/folders/14rV6Q9TsvpRwKnijaCfN4NZchREd510Q) | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-22-frontend-architecture-delivery-learning/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-22-frontend-architecture-delivery-learning/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-10-22-frontend-architecture-delivery-learning) |
| **Week 8** · Oct 29, 2026 | 21 |[Video Link](https://drive.google.com/drive/folders/1gWNgGISuPlXQtb7h0Ev7AH4IYJ44XKLk) | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-29-terraform-cloudrun-billing-learning/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-10-29-terraform-cloudrun-billing-learning/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-10-29-terraform-cloudrun-billing-learning) |
| **Week 9** · Nov 5, 2026 | 23 | [Video Link](https://drive.google.com/drive/folders/1KkHKnjhcQ9k8sDdGoykoM6rQIE4DEeQv) | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-11-05-docker-layers-caching-scanning-learning/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-11-05-docker-layers-caching-scanning-learning/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-11-05-docker-layers-caching-scanning-learning) |
| **Week 10** · Nov 12, 2026 | 21 | [Video Link](https://drive.google.com/drive/folders/1GNPDrJrrN1HDq-uPR-CSHcc56bAMFwzf) | [Frictional log](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-11-12-canary-bluegreen-deployment/FICTIONAL.md) · [Weekly hours](https://github.com/nikbearbrown/humanitarians-youtube/blob/main/fellows/darshil-s/2026-11-12-canary-bluegreen-deployment/HOURS.md) · [Folder](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/darshil-s/2026-11-12-canary-bluegreen-deployment) |
| **Total (Weeks 1–10)** | **219** | | |


---

## Degree Relevance and Supervision

This fellowship directly applies my **M.S. in Information Systems** coursework — cloud infrastructure, software engineering practice, and systems/security design — to a real production deployment pipeline: designing CI/CD automation, cloud identity and access management (Workload Identity Federation, least-privilege IAM), containerization, and deployment-strategy engineering (canary/blue-green releases) are direct extensions of graduate coursework in systems architecture and cloud computing.

**Supervisor:** Sergey Atiyan (s.aityan@northeastern.edu)

---

## Authorization

- **Authorization type:** F1-OPT 
- **Current agreement through:** 11/30/2026

---

## Next Period Plan

**Requested renewal period:** December 1, 2026 – February 20, 2027 (~3 months).

With the dev and staging CI/CD, rollback, hardening, and deployment-strategy work now complete and validated, the next period extends the same proven pipeline to production.

 Deliverable 

 Provision production GCP infrastructure (Artifact Registry, WIF trust, scoped service account/IAM review) and GitHub production Environment (required-reviewer approval gates).

Trigger and validate the first production deploy (`v*` tag) and the production rollback workflow end-to-end.

Apply production-grade hardening (observability, canary/blue-green rollout) proven out in staging, and deliver a final runbook / documentation handoff. 

