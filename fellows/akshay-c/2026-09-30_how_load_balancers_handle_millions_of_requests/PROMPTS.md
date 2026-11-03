# Prompts — How Load Balancers Handle Millions of Requests

## Production Direction

Create a brutalist-style technical explainer about how load balancers distribute large volumes of application traffic.

Visual principles:
- Dark background with high-contrast typography.
- Simple diagrams rather than decorative imagery.
- Keep labels readable and inside safe margins.
- Keep arrows clear of text and boxes.
- Use consistent server, request, and load-balancer visual language.
- Prefer simple motion that reinforces the networking concept.
- Avoid unnecessary visual clutter.
- Landscape master: 3840x2160 at 24 fps.
- Humanitarians AI branding.
- Creator: Akshay Chavan.

---

## B00 — Millions of Requests

Visual prompt:
Show a large stream of incoming application requests to communicate very high request volume. Establish immediately that a popular application may need to process traffic at massive scale.

Key idea:
Millions of incoming requests.

Motion:
Animate multiple request indicators entering the frame.

---

## B01 — One Server Bottleneck

Visual prompt:
Show many incoming requests converging on a single backend server. Visually communicate that one server has finite capacity and becomes the bottleneck under sufficiently high traffic.

Key idea:
One server cannot indefinitely absorb increasing traffic.

Motion:
Requests converge toward one server.

---

## B02 — More Servers

Visual prompt:
Replace the single-server architecture with a pool of backend servers. Show that adding servers increases capacity but creates a routing question: which backend should receive each request?

Key idea:
Horizontal scaling introduces traffic distribution.

Motion:
Reveal multiple servers and incoming requests.

---

## B03 — Load Balancer

Visual prompt:
Place a load balancer between incoming users or requests and the backend server pool. Clearly show requests entering the load balancer before being forwarded to backend servers.

Key idea:
The load balancer becomes the traffic-distribution layer.

Motion:
Requests move toward the load balancer and then toward servers.

---

## B04 — Round Robin

Visual prompt:
Demonstrate round-robin routing by distributing successive requests across backend servers in sequence.

Key idea:
Each new request can be sent to the next available server in rotation.

Motion:
Sequentially route requests to different servers.

---

## B05 — Least Connections

Visual prompt:
Show multiple backend servers with different active-connection loads. Route the next request toward the server with fewer active connections.

Key idea:
Routing decisions can account for current backend load.

Motion:
Compare server loads and direct the request toward the less-busy backend.

---

## B06 — Health Checks

Visual prompt:
Show the load balancer checking backend server health. Mark one backend server as unavailable while the others remain healthy.

Key idea:
Health checks identify backends that should not receive normal traffic.

Motion:
Perform health-check indications across the server pool and highlight the failed server.

Layout requirement:
Ensure the UNAVAILABLE label remains completely inside the frame and does not overlap surrounding elements.

---

## B07 — Route Around Failure

Visual prompt:
Show incoming traffic bypassing the failed backend server and being routed to healthy servers instead.

Key idea:
A failed backend does not have to take down the entire service.

Motion:
Traffic paths visibly avoid the unavailable server.

---

## B08 — Scalable, Resilient Service

Visual prompt:
Present the load balancer and healthy backend pool as one unified service. Reinforce the mental model that traffic distribution across multiple servers enables scaling and improves resilience.

Key idea:
Many backend servers can function as one scalable service behind a load balancer.

Motion:
Resolve the architecture into a clean final system diagram.

---

## B09 — Humanitarians AI Outro

Pattern:
ClaudeTitleOutro

Visual prompt:
Use the established Humanitarians AI branded Remotion outro.

Title:
How Load Balancers Handle Millions of Requests

Handle:
@HumanitariansAI

Purpose:
Close the explainer with consistent Humanitarians AI branding.

Motion:
Hold branded outro long enough for the closing narration and title to be comfortably readable.

---

## Safety / QC Requirements

- No overlapping text.
- No arrows crossing labels unnecessarily.
- No cropped labels or diagrams.
- Keep important elements within safe margins.
- Maintain consistent typography and visual hierarchy.
- Do not introduce unrelated branding or creator attribution.
- Humanitarians AI handle must be @HumanitariansAI.
- Technical visuals should support the narration rather than introduce unsupported claims.
