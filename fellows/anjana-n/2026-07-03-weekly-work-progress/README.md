**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 1 — Environment and Infrastructure

**Timeline:** June 29, 2026 – July 4, 2026

**Scope:** Development environment, external API configuration, and repository structure.

---

## Development Environment
- Python 3.11 with an isolated virtual environment
- Core dependencies:
  - **Ingestion:** Requests, BeautifulSoup, sec-edgar-downloader, yfinance
  - **NLP and modelling:** Hugging Face Transformers, PyTorch, spaCy (financial NER), sentence-transformers, scikit-learn
  - **Data and validation:** pandas, NumPy, Pydantic
  - **Storage:** ChromaDB
  - **Orchestration:** LangGraph
  - **Interfaces:** Streamlit, Plotly, FastAPI, Uvicorn
  - **Testing:** pytest

## API Configuration
- **SEC EDGAR:** full-text search API, rate limit of 10 requests per second
- **Financial Modeling Prep (FMP):** free tier, capped at 250 calls per day
- Credentials stored in `.env`, with a committed `.env.example` template for reproducible setup

## Repository Structure
- **Data directories:**
  - `data/raw/edgar/{ticker}/`
  - `data/raw/fmp/{ticker}/`
  - `data/processed/`
- **Working directories:** `models/`, `logs/`, `checkpoints/`, `notebooks/colab/`
- **Module layout:**

| Module | Responsibility |
|---|---|
| `ecis/ingestion/` | Source fetchers and caching |
| `ecis/preprocessing/` | Cleaning, normalization, chunking |
| `ecis/readers/` | Keyword, FinBERT, NER, and LLM readers |
| `ecis/extraction/` | Triangulation, deduplication, validation |
| `ecis/graphs/` | LangGraph pipeline and agent graphs |
| `ecis/db/` | Database access layer |
| `ecis/config/` | Settings and weight configuration |
| `ecis/scripts/` | Execution entry points |
