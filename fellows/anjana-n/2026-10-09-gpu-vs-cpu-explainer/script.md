# Why GPUs Beat CPUs for AI — Full Script

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — `beats.json` specifies `am_onyx`; overridden to
`af_bella` so the narration is Anjana's, with no channel handle on this build
**Target length:** ~3:00 (16:9 master) / ~2:30 (9:16 cut)

---

## B00 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~13s

**Narration:**

"Use a GPU" is advice everyone repeats and almost nobody unpacks. The honest
answer isn't that graphics cards are mysteriously quicker — it's that the
workload has a shape, and one piece of hardware happens to match it. I'm Anjana.

**Composer ask:**

> Everyone says to train on GPUs rather than CPUs. What is it about the
> architecture that actually maps to an AI workload — cores, memory, something
> else — and where does a CPU still do the better job?

**Output lines (resolved on screen):**
- the workload is dominated by one operation
- thousands of cores, and the bandwidth to feed them
- CPUs keep the work that isn't that

---

## B01 — The Bottleneck (13s)

### Narration
Every layer of a neural network performs the same core operation: multiply a matrix of inputs by a matrix of weights, add a bias, and apply an activation function. Training means repeating this billions of times across thousands of batches. Inference means running it millions of times per day. The dominant computational cost of any AI workload is matrix multiplication. Understanding that single fact is the key to understanding why GPUs are the hardware of choice for AI.

### Visual direction
A simplified neural network layer appears: an input vector on the left, a weight matrix in the center, an output vector on the right. An arrow labeled "multiply" connects input to weights, another labeled "add bias + activate" connects weights to output. The weight matrix glows gold to emphasize it as the computational center. Below, a counter ticks up: "matrix multiplications per training run: 1B... 10B... 100B..." The label "the dominant cost" appears beneath.

---

## B02 — One Fast vs Many Wide (13s)

### Narration
A modern server CPU has up to 128 high-performance cores. Each core handles complex branching, deep pipelines, and low-latency single-threaded tasks exceptionally well. A GPU takes a different approach. An A100 has 6,912 CUDA cores — individually simpler, but designed to execute the same instruction across thousands of data elements simultaneously. This is the SIMD model: single instruction, multiple data. Matrix multiplication decomposes into thousands of independent multiply-and-accumulate operations — exactly the workload SIMD was built for.

### Visual direction
Left side: a CPU chip with 8 large cores arranged in a grid, each glowing blue. One core processes a single multiply-add operation — fast but sequential. A small queue of operations waits. A note clarifies: "up to 128 cores on server chips." Right side: a GPU chip packed with a dense grid of small green cores. All cores light up simultaneously, each handling one multiply-add. The entire batch completes in one step. Label below CPU: "optimized for complex sequential tasks." Label below GPU: "optimized for parallel throughput."

---

## B03 — Memory Bandwidth (13s)

### Narration
Core count alone doesn't determine throughput. The limiting factor is often memory bandwidth — the rate at which data can be delivered to the processing cores. A server CPU reads from DDR5 memory at roughly 50 to 100 gigabytes per second. A GPU like the A100 uses HBM2e — high bandwidth memory — delivering over two terabytes per second. That's a twenty-times advantage. When thousands of cores need continuous data, the memory interface becomes the critical path. Higher bandwidth means those cores spend less time waiting and more time computing.

### Visual direction
Two parallel pipelines. Top pipeline: a moderate tube labeled "CPU: DDR5" with data packets flowing through at a steady pace. A throughput meter beside it reads "~100 GB/s." Bottom pipeline: a wider tube labeled "GPU: HBM2e" with a dense stream of packets flowing rapidly. Its meter reads "~2 TB/s." The ratio "20x" appears between the two meters in gold. Label below: "memory bandwidth determines sustained throughput."

---

## B04 — Tensor Cores (13s)

### Narration
Modern NVIDIA GPUs include a second type of processing unit alongside CUDA cores: tensor cores. These are fixed-function hardware units designed specifically for small matrix multiplications — typically four-by-four blocks — completed in a single clock cycle. Where a CUDA core performs a scalar multiply-add, a tensor core performs an entire matrix multiply-accumulate. The A100 includes 432 tensor cores, and they support mixed-precision arithmetic — FP16 inputs with FP32 accumulation — reducing memory footprint while maintaining numerical accuracy. This is purpose-built silicon for the operation at the center of every AI model.

### Visual direction
Left side: a single CUDA core (green circle) with two numbers flowing in and one result flowing out. Label: "CUDA core: scalar multiply-add." Right side: a tensor core (larger purple square with inner grid pattern) with two 4x4 grids flowing in and one 4x4 grid flowing out. Label: "tensor core: matrix multiply-accumulate." Below, a precision diagram: an FP16 block labeled "16-bit inputs" connected by an arrow to an FP32 block labeled "32-bit accumulation." Label: "mixed precision: reduced memory, maintained accuracy." Count badge: "432 tensor cores per A100."

---

## B05 — The Full Picture (13s)

### Narration
GPUs outperform CPUs for AI workloads because of how well their architecture maps to the problem. Neural networks are dominated by matrix multiplication. GPUs provide thousands of cores for parallel execution. High-bandwidth memory keeps those cores supplied with data. And tensor cores accelerate the most critical operation in dedicated hardware. CPUs remain essential for orchestration, data loading, preprocessing, and the control logic that surrounds the compute. The two architectures are complementary — GPUs handle the dense numerical throughput while CPUs manage everything around it.

### Visual direction
A four-layer horizontal stack builds from bottom to top. Bottom layer: "matrix multiplication is the dominant cost" (gold bar). Second layer: "thousands of cores for parallel execution" (green bar). Third layer: "high-bandwidth memory interface" (blue bar). Top layer: "dedicated tensor core hardware" (purple bar). The stack glows as a unified advantage. To the right, a simple diagram shows CPU and GPU as two interlocking pieces: CPU labeled "orchestration, control, preprocessing" and GPU labeled "dense numerical compute." Both are outlined cleanly, showing they work together. Centered closing text fades in: "Complementary architectures. Each built for what it does best." Fade to dark.

---

## B06 — Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~24s

**Narration:**

Let's recap with Claude. The reason the gap is wide is that it isn't one
advantage, it's four that compound. The workload is dominated by matrix
multiplication. Thousands of simple cores run those multiply-accumulates at the
same time rather than one after another. High-bandwidth memory keeps them
supplied, which matters more than core count once you have enough cores. And
tensor cores put the most common operation into fixed-function silicon. None of
which makes the CPU redundant — it keeps the orchestration, the data loading and
the control logic, which is work a GPU is bad at.

**Artifact lines:**
- Matrix multiplication is the dominant computational cost of an AI workload.
- A GPU runs thousands of multiply-accumulates simultaneously — the SIMD model.
- Memory bandwidth, not core count, is often the limiting factor; HBM2e is
  roughly 20× DDR5.
- Tensor cores do 4×4 matrix multiply-accumulate in fixed-function hardware, in
  mixed precision.
- CPUs and GPUs are complementary: orchestration and control versus dense
  numerical throughput.

---

## B07 — Your Turn

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~30s

**Narration:**

Your turn. Take something slow you run regularly and work out what it actually
spends its time doing — not what it's for, what the inner loop is. Then ask
whether that loop is the same operation over independent data, because that's
the property that makes this kind of hardware help at all. And be honest about
whether you're compute-bound or just waiting on memory.


---

## B08 — Title outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

Anjana here, thanks for watching.

**Title:** Why GPUs Beat CPUs for AI
**Subline:** complementary architectures
**Handle:** (none)
