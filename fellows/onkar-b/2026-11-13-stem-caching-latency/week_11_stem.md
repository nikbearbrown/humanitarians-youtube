# Week 11: Caching, Latency, and AI Compute

**Series:** STEM AI Explainer
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A person walks into a massive, maze-like library to find a specific book. Once they find it, they leave. The next day, they need the exact same book, and start walking through the maze from scratch.
**ON SCREEN:** `REDUNDANT COMPUTE`
**VO:**
Hi, I am Onkar Bhujbal. If you look up a difficult math equation today, you don't calculate it again from scratch tomorrow—you just remember the answer. Computers, by default, are not that smart. Unless you tell them otherwise, they will process the exact same massive machine learning calculations a thousand times in a row. Today, we are talking about Caching, Latency, and why AI scalability depends on memory.

### SCENE 2 — COMPUTE VS. MEMORY
**VISUAL** — A balance scale. On one side: a complex processor glowing red hot (Compute). On the other side: a cool, sleek memory chip (RAM/Cache).
**VO:**
In computer science, there is a constant trade-off between time complexity and space complexity. When dealing with Large Language Models and Vector Databases, time is your enemy. AI inference requires heavy, expensive compute cycles. To scale these systems, engineers trade space for time. We use cheap, abundant RAM to store the answers to expensive questions. 

### SCENE 3 — THE IN-MEMORY DATABASES
**VISUAL** — A diagram showing an API request hitting a "Redis" node first. It instantly bounces back. Behind Redis sits the heavy SQL and Vector databases, sitting idle.
**VO:**
Tools like Redis and Memcached are known as in-memory data stores. Unlike traditional databases that write to a physical hard drive, Redis stores data entirely in volatile RAM. This makes it volatile—if the server loses power, the data vanishes—but it makes read-speeds incredibly fast, dropping latency from hundreds of milliseconds down to the single digits.

### SCENE 4 — THE CACHE INVALIDATION TRAP
**VISUAL** — A cached answer says "Apples cost $2". A database in the background updates to "$4", but the cache continues confidently handing out the "$2" answer.
**VO:**
But caching introduces one of the hardest problems in software engineering: Cache Invalidation. If the underlying truth changes, your high-speed cache will confidently serve outdated lies. You have to implement strict Time-to-Live expirations, ensuring the cache periodically deletes itself and forces the system to calculate fresh answers.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Trade space for time.`
**VO:**
Protect your expensive compute layers. Put a high-speed memory shield in front of your AI.
Liam, for Onkar Bhujbal and Humanitarians AI.