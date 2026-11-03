# Divyank Singh

[singh.divya@northeastern.edu](mailto:singh.divya@northeastern.edu) | [GitHub](https://github.com/singhdivyank) | [LinkedIn](https://linkedin.com/in/singh-divyank)

## Summary

AI Engineer with 3 years of experience designing and deploying scalable, low-latency, and production-grade Agentic AI solutions with measurable accuracy & efficiency gains using Claude Code to accelerate development. Proven ability to translate responsible AI architecture into business impact. Specializing in RAG retrieval & evaluation, and multi-agent orchestration.

## Skills

- **Programming:** Python, Java, JavaScript (React, Next.js), SQL, TypeScript, PySpark
- **Frameworks:** LangGraph, LangChain, CrewAI, FastAPI, Spring Boot, PyTorch
- **LLM APIs & SDKs:** Anthropic APIs, OpenAI APIs, Google Gemini, Vercel AI SDK
- **Observability & Monitoring:** LangSmith, OpenTelemetry, Prometheus, Grafana
- **Vector Databases:** Weaviate, Pinecone, PostgreSQL (pgvector), Redis
- **Prompt Engineering:** Chain-of-Thought (CoT), Tool Calling, Structured Output
- **Cloud AI:** GCP (Vertex AI, BigQuery, Cloud Run), Docker, Kubernetes, MLflow, Git, GitHub Actions

## Work Experience

### Fox Corporation — AI Engineer (Co-op)

**Jun 2025 – Aug 2025 · Tempe, AZ, USA**
_Python, Google Document AI, Docker, Cloud Run, GitHub Actions, FastAPI_

- Shipped scalable serverless SaaS enterprise Document Processing platform, extracting tables from unstructured PDFs; improving customer satisfaction by reducing manual effort from **4 hrs to 5 mins** & obtaining ~**200ms** p50 latency/call.
- Pipelined layout-specific coordinate-aware heuristics & rule-based parsing backend, achieving ~**90%** extraction accuracy.
- Decoupled ingestion and extraction services through async REST APIs, ensuring horizontal scaling across **1000+ PDFs**.
- Executed **200+ unit and integration tests** using PyTest, reducing production issues by **40%** & ensuring CI/CD readiness.
- Enforced IAM policies and analyzed Cloud Monitor logs, tracking performance bottlenecks and achieving **99.9% uptime**.

### Northeastern University — AI Engineer - MLOps TA

**Jan 2025 – Apr 2026 · Boston, MA, USA**
_LangGraph, LangSmith, Weaviate, MLflow, Vertex AI, Kafka, Redis_

- Implemented scalable production-grade RAG agent with tool calling for autonomous knowledge access to **100+ students**.
- Saved **$1K/yr** in LLM API costs by token optimization via semantic caching and multi-model routing (Anthropic, GPT).
- Enhanced throughput under **100+ concurrent requests/day**, architecting event-driven workflow using pub/sub messaging.
- Iteratively improved relevance to **0.80** by designing evaluation harness using LLM-as-a-judge scores and A/B testing.
- Orchestrated 4-stage **DAG** governing prompt versioning, retraining triggers, and model drift monitoring in production.

### Celebal Technologies — AI Engineer

**Sep 2023 – Dec 2023 · Jaipur, India**
_Python, LangChain, LangSmith, OpenAI APIs, Pinecone, Hugging Face_

- Developed customer support chatbot for insurance provider, cutting ticket resolution time by **65%** using ReAct prompts.
- Engineered RAG indexing pipeline using NER, achieving **92%** accuracy across **10K+ profiles** and ensuring compliance.
- Improved groundedness to **1.5x** on internal benchmarks, optimizing retrieval by chunking strategies and metadata filters.
- Designed secure authentication and fine-grained RBAC for AI workflows using JWT, enabling governance & compliance.

### CrossML Pvt. Ltd. — AI Engineer

**Aug 2022 – Aug 2023 · Chandigarh, India**
_Python, LangChain, LangSmith, OpenAI APIs, BigQuery, Kubernetes_

- Spearheaded development of RAG retail question-answering chatbot at fast-paced startup, generating **$200K** in revenue.
- Engineered scalable ELT workflows on **150K records**, downstreaming AI analytics tasks using SQL for data wrangling.
- Reduced hallucination by **5%** through citation grounding and designing Pydantic classes for structured output validation.
- Optimized inference throughput, supporting **3x** traffic by auto-scaling Infrastructure as Code (IaC) using Terraform.
- Collaborated cross-functionally with product and business teams, curating CoT data for Supervised Fine-Tuning (SFT).

## Projects

### Real Estate PWA

**Jun 2026 – Jul 2026**
_JavaScript, HTML, CSS, IndexedDB, Service Workers, ONNX_ · [GitHub](https://github.com/singhdivyank/repair-cost-estimator)

- Developed offline-first property cost estimation mobile and desktop web app, eliminating backend dependencies by **100%**.
- Engineered frontend using Vanilla JavaScript with CDN modules, reducing bundle size by **40%** and runtime overheads.
- Embedded **on-device SLM** (Qwen2.5-0.5B) and integrated SpeechSynthesis API (voice), enabling low-latency inference.

### AI Recruitment Agent

**May 2026 – Jun 2026**
_Next.js, LangGraph, Prometheus, PostgreSQL, FastAPI_ · [GitHub](https://github.com/singhdivyank/AI-recruitment-agent-system/tree/main)

- Automated hiring funnel using agents for autonomous candidate selection, outreach emails, & bias mitigation guardrails.
- Orchestrated agentic workflows by fan-out/fan-in pattern & distributed microservice architecture, achieving ~**35s TTFT**.
- Architected hybrid RAG retrieval pipeline (pgvector, vector embeddings, CrossEncoder re-ranking), obtaining **0.83 recall**.
- Visualised hiring decisions and monitored token level costs on Grafana dashboard, enabling audits and transparency.

### Anomaly Detection

**Jan 2025 – Dec 2025**
_Java, TypeScript, React, Go, Scikit-learn, PostgreSQL_ · [GitHub](https://github.com/singhdivyank/Anomaly-Detection/tree/main)

- Built real-time analytics platform for electrical grid operators, detecting demand-response violations across IOT streams.
- Architected scalable ML workflow (IsolationForest, LightGBM) on **33M+ rows** served via gRPC, achieving **92% accuracy**.
- Developed full-stack product, integrating Spring Boot WebSocket with React hooks and achieving ~**200ms** p50 latency.

### Big Data Text Classification

**Oct 2024 – Apr 2025**
_Apache Spark, Delta Lake, PySpark, Scikit-learn, Seaborn_ · [GitHub](https://github.com/singhdivyank/partisanflow-nlp)

- Developed predictive modeling solution on distributed computing platform, classifying political bias with **0.81 F1 score**.
- Engineered scalable ETL and Feature Engineering pipelines on **2TB+ corpus** through batching, eliminating OOM errors.
- Built ML workflow combining Logistic Regression and statistical aggregation, improving classification accuracy to **87%**.

### Voice Agent

**Jan 2024 – May 2024**
_Google Gemini, CrewAI, OpenTelemetry, TypeScript, Vercel, Docker_ · [GitHub](https://github.com/singhdivyank/voice-assistant)

- Extended no-cost medical diagnosis to rural areas, orchestrating multi-agent Conversational AI supporting **15 languages**.
- Built full-stack application, integrating asynchronous STT/TTS pipelines and React front-end with **sub-500ms** latency.
- Containerised deployment behind NGINX proxy for load balancing & SSL termination, enabling **zero-downtime** scaling.
- Integrated Model Context Protocol (MCP) servers as human-in-the-loop (HITL) gates, ensuring responsible AI practices.

### Reinforcement Learning for Supply Chain

**Mar 2026 – Apr 2026**
_Python, OpenAI Gym, PyTorch, Seaborn_ · [GitHub](https://github.com/singhdivyank/multi-echelon-rl-inventory)

- Implemented continuous-action **PPO** agent to optimize inventory restocking under seasonal demand across **5K episodes**.
- Optimized costs by **25%** and improved service levels by **10%** over stable baselines, exposing single-environment win bias.

## Education

### Northeastern University

**Masters in Artificial Intelligence**
Sep 2024 – May 2026 · Boston, MA, USA

### Thapar University

**Bachelors in Computer Science**
Jul 2018 – Jun 2022 · Patiala, India
