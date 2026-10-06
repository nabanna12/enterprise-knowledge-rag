# Enterprise Knowledge RAG Backend

Backend foundation for an AI-powered enterprise and university knowledge search
and retrieval system using Retrieval-Augmented Generation (RAG).

## Project objective

The final system will support:

- Secure user authentication.
- Document upload and metadata management.
- PDF text extraction.
- Text preprocessing and chunking.
- Embedding generation.
- PostgreSQL and pgvector semantic search.
- BM25 keyword retrieval.
- Hybrid retrieval.
- Reranking.
- RAG-based question answering.
- Source attribution.
- Retrieval and answer-quality evaluation.

## Current status

### Phase 1 - Project Foundation

Completed:

- FastAPI application.
- Environment-based configuration.
- Logging configuration.
- CORS configuration.
- Health endpoint.
- Application information endpoint.
- Basic pytest API tests.

## Technology stack

- Python
- FastAPI
- Pydantic Settings
- Pytest
- PostgreSQL and pgvector planned for Phase 2

## Local setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Start the development server

```powershell
uvicorn app.main:app --reload
```

### 5. Open the API documentation

```text
http://127.0.0.1:8000/docs
```

### 6. Check the health endpoint

```text
http://127.0.0.1:8000/api/v1/health
```

### 7. Run tests

```powershell
python -m pytest -q
```

## Project structure

```text
app/
├── api/
├── core/
├── db/
├── models/
├── repositories/
├── schemas/
├── services/
└── main.py

tests/
└── test_health.py
```

## Security note

The `.env` file contains local configuration and must not be committed to GitHub.

Use `.env.example` as a template for other developers.

The `.venv` directory is also excluded from GitHub because each developer should create their own virtual environment.

## Development phases

1. Project foundation
2. Database foundation
3. Authentication and authorization
4. Document management
5. PDF ingestion and extraction
6. Text preprocessing and chunking
7. Embedding generation
8. Semantic vector search
9. BM25 keyword search
10. Hybrid retrieval
11. Reranking
12. RAG pipeline
13. LLM integration
14. Source attribution
15. Incremental indexing
16. Search history and feedback
17. Testing
18. Evaluation
19. Security hardening
20. Docker and deployment preparation
