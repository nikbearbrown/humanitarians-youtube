# SOURCES — Docker and Kubernetes for AI

Brief supplied by the requester (Likhith); points checked against the primary documentation below (retrieved 2026-10-21).

- Docker docs, "What is a container?" — https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/ — containers are isolated processes that package an application with everything it needs to run.
- Docker docs, "What is an image?" — https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/ — an image is a standardized package of files, binaries, libraries and configuration; images are built from layers.
- NVIDIA Container Toolkit docs — https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html — GPU containers use the host's NVIDIA driver; CUDA user-space libraries can ship in the image.
- Kubernetes docs, "Overview" — https://kubernetes.io/docs/concepts/overview/ — Kubernetes "provides you with": service discovery and load balancing, self-healing (restarts/replaces failed containers), automated rollouts, horizontal scaling.
- Kubernetes docs, "Horizontal Pod Autoscaling" — https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/ — adds or removes replicas in response to load.

## Corrections / de-sensationalising
- "Every dependency" / "runs identically anywhere": a container shares the host kernel, and GPU containers rely on the host's NVIDIA driver. B04 says "runs the same anywhere" with an on-screen note ("GPU hosts still need their own driver"); the verdict says "any compatible host".
- Kubernetes runs OCI container images through a container runtime (e.g. containerd); it does not need the Docker Engine itself. The reel frames Docker as the packaging step and Kubernetes as the runner, which is accurate.
- Auto-scaling is something Kubernetes does when configured (e.g. a HorizontalPodAutoscaler); restarts/replacement and Service load balancing are built in.
- Version numbers (B03), error text (B02), user counts (B05) and replica counts (B07) are illustrative and labelled so on screen.
- Falsifiability: Kubernetes adds operational overhead; for one small model it is often overkill (B09).
- "Thousands of users" is phrased as capability, not a measured figure.
