# Enterprise Knowledge RAG Backend

Backend for an AI-powered enterprise and university knowledge search and
retrieval system using Retrieval-Augmented Generation (RAG).

The system is being developed as a modular monolith using FastAPI,
PostgreSQL, pgvector, BM25, semantic retrieval, hybrid search, reranking,
and a configurable LLM layer.

## Project objective

The final system will allow authorized users to:

- Authenticate securely.
- Upload enterprise or university documents.
- Store document metadata and permissions.
- Extract and preprocess document text.
- Split documents into meaningful chunks.
- Generate embeddings for document chunks.
- Perform semantic vector search.
- Perform BM25 keyword search.
- Combine lexical and semantic retrieval.
- Rerank retrieved chunks.
- Generate grounded answers using RAG.
- Return source references such as document name, page number, and chunk ID.
- Store useful search history and feedback.
- Evaluate different retrieval approaches.

The project is not intended to be only a PDF chatbot. Its research focus is:

```text
BM25
+ Semantic Retrieval
+ Hybrid Retrieval
+ Reranking
+ Retrieval-Augmented Generation
+ Evaluation
```

## Current development status

### Phase 1 — Project Foundation

Completed:

- FastAPI application.
- Modular backend folder structure.
- Environment-based configuration.
- `.env` and `.env.example` configuration files.
- Logging configuration.
- CORS configuration.
- Root endpoint.
- API health endpoint.
- Application information endpoint.
- Automated API tests.
- GitHub repository setup.

### Phase 2 — Database Foundation

Completed:

- PostgreSQL running through Docker.
- pgvector extension enabled.
- SQLAlchemy 2.x database engine.
- Psycopg PostgreSQL driver.
- SQLAlchemy session management.
- Alembic migration configuration.
- Initial database migration.
- Database connection health endpoint.
- Database connectivity tests.
- Insert and read verification using PostgreSQL.

Current test status:

```text
6 passed
```

## Technology stack

### Backend

- Python
- FastAPI
- Pydantic Settings

### Database

- PostgreSQL
- pgvector
- SQLAlchemy
- Psycopg
- Alembic

### Search and AI

- BM25 keyword retrieval
- Modular embedding service
- Semantic vector retrieval
- Hybrid retrieval
- Cross-encoder reranking
- Provider-independent LLM integration

### Testing and development

- Pytest
- Docker
- Docker Compose
- Git and GitHub

## Project structure

```text
enterprise-knowledge-rag/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging_config.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
│   ├── test_database.py
│   └── test_health.py
│
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── pytest.ini
├── README.md
└── requirements.txt
```

## Prerequisites

Install the following software:

- Python 3.12 or newer.
- Git.
- Docker Desktop.
- Visual Studio Code is recommended.

Verify Python:

```powershell
python --version
```

Verify Docker:

```powershell
docker --version
docker compose version
```

## Local setup

### 1. Clone the repository

```powershell
git clone [https://github.com/nabanna12/enterprise-knowledge-rag.git](https://github.com/nabanna12/enterprise-knowledge-rag.git)
cd enterprise-knowledge-rag
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Create the local environment file

Copy `.env.example` to `.env`.

PowerShell command:

```powershell
Copy-Item .env.example .env
```

The local `.env` file should contain:

```env
APP_NAME=Enterprise Knowledge RAG Backend
APP_VERSION=0.1.0
ENVIRONMENT=development
DEBUG=true
API_PREFIX=/api/v1
LOG_LEVEL=INFO

DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/enterprise_rag

SECRET_KEY=development-only-secret-change-before-production
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

Do not commit `.env` to GitHub.

## Start PostgreSQL and pgvector

Start the database container:

```powershell
docker compose up -d
```

Check the container:

```powershell
docker compose ps
```

The PostgreSQL container should show a healthy status.

Verify PostgreSQL:

```powershell
docker exec enterprise-rag-postgres pg_isready -U postgres -d enterprise_rag
```

Expected output:

```text
/var/run/postgresql:5432 - accepting connections
```

Verify pgvector:

```powershell
docker exec -it enterprise-rag-postgres psql -U postgres -d enterprise_rag -c "SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';"
```

## Database migrations

Apply all migrations:

```powershell
alembic upgrade head
```

Show the current migration:

```powershell
alembic current
```

Create a new migration after changing SQLAlchemy models:

```powershell
alembic revision --autogenerate -m "describe schema change"
```

Apply the new migration:

```powershell
alembic upgrade head
```

Do not manually edit the database schema when a change should be represented in the project. Create an Alembic migration instead.

## Start the FastAPI server

Run:

```powershell
uvicorn app.main:app --reload
```

The server will be available at:

```text
http://127.0.0.1:8000
```

## API documentation

Open the interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Current endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Confirm that the backend is running |
| GET | `/api/v1/health` | Check API health |
| GET | `/api/v1/info` | Return application information |
| GET | `/api/v1/health/database` | Check PostgreSQL connectivity |

Database health response:

```json
{
  "status": "healthy",
  "database": "postgresql",
  "message": "Database connection is working."
}
```

## Run tests

Run the complete test suite:

```powershell
python -m pytest -q
```

Current expected result:

```text
6 passed
```

The tests currently verify:

- Root API endpoint.
- API health endpoint.
- Application information endpoint.
- PostgreSQL connectivity.
- Existence of the migrated table.
- Insert and read operations.

## Stop and restart services

Stop the FastAPI server:

```text
Ctrl + C
```

Stop PostgreSQL without deleting data:

```powershell
docker compose down
```

Start PostgreSQL again:

```powershell
docker compose up -d
```

Stop PostgreSQL and delete the local database volume:

```powershell
docker compose down -v
```

Warning: `docker compose down -v` deletes local PostgreSQL data. Do not use it unless you intentionally want to reset the local database.

## Security rules

Do not commit the following files or directories:

```text
.env
.venv/
__pycache__/
*.pyc
.pytest_cache/
```

The `.env` file may contain:

- Database passwords.
- JWT secrets.
- LLM API keys.
- Cloud service credentials.

Use `.env.example` as the safe configuration template.

## Planned API endpoints

Future API endpoints include:

```text
POST   /api/v1/auth/register
POST   /api/v1/auth/login

GET    /api/v1/users/me

POST   /api/v1/documents
GET    /api/v1/documents
GET    /api/v1/documents/{document_id}
DELETE /api/v1/documents/{document_id}

POST   /api/v1/search
POST   /api/v1/chat

GET    /api/v1/search/history
POST   /api/v1/feedback
```

These endpoints are planned and are not all implemented yet.

## Development roadmap

1. Project foundation — completed.
2. Database foundation — completed.
3. Authentication and authorization.
4. Document management.
5. PDF ingestion and text extraction.
6. Text preprocessing and chunking.
7. Embedding generation.
8. Semantic vector search.
9. BM25 keyword search.
10. Hybrid retrieval.
11. Reranking.
12. RAG pipeline.
13. LLM integration.
14. Source attribution.
15. Incremental indexing and document versions.
16. Search history and feedback.
17. Unit and integration testing.
18. Retrieval and RAG evaluation.
19. Security hardening.
20. Docker and deployment preparation.

## Future evaluation

The system will support comparisons between:

```text
BM25
Semantic Retrieval
Hybrid Retrieval
Hybrid Retrieval + Reranking
```

Planned retrieval metrics:

- Precision@K.
- Recall@K.
- Mean Reciprocal Rank.
- nDCG@K.

Planned RAG and system metrics:

- Answer relevance.
- Faithfulness or groundedness.
- Context relevance.
- Citation correctness.
- Retrieval latency.
- Reranking latency.
- End-to-end response latency.

## Team

### Alpha Coders

- Nabanna Choudhury
- Sushil Madhesia
- Kaushik Handique
- Debasish Boruah

Department:

```text
Computer Science and Engineering
```

## Current project limitation

The current repository contains the backend foundation and database foundation only.

The following components are planned for future phases and should not yet be described as completed:

- Authentication.
- Document upload.
- PDF processing.
- BM25 indexing.
- Semantic retrieval.
- Hybrid retrieval.
- Reranking.
- LLM integration.
- RAG responses.
- Frontend integration.

## License

A project license will be added after the team decides how the code should be shared.
