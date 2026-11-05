<h1 align="center">Task Management System (FastAPI)</h1>

<p align="center">
  The foundation of a task management API with FastAPI, SQLAlchemy and PostgreSQL:
  project layout, database models, Alembic migrations and a Docker setup for development
  and production.
</p>

<p align="center">
  <img alt="Python 3.10" src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.116-009688?logo=fastapi&logoColor=white">
  <img alt="SQLAlchemy 2.0" src="https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=sqlalchemy&logoColor=white">
  <img alt="PostgreSQL 13" src="https://img.shields.io/badge/PostgreSQL-13-4169E1?logo=postgresql&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white">
</p>

## Status

**Early stage.** The infrastructure is done: configuration from environment files, the database connection and session dependency, the first models (`users` and `products`), Alembic, and Docker Compose files for development and production. The task endpoints are not written yet; the API currently answers on `/` only.

## What is in place

- **Layered layout** ready for growth: `models/`, `schemas/`, `routes/`, `services/`, `core/` and `utils/` packages.
- **Configuration** with `pydantic-settings`, read from `.env.dev` (development) or `.env.prod` (production).
- **Database:** SQLAlchemy 2.0 on PostgreSQL, a `SessionDep` dependency for routes, tables created at startup through FastAPI's lifespan.
- **Migrations:** Alembic, configured in `db/` to read the same settings and the models' metadata (autogenerate ready).
- **Models:** `users` (email, password, creation date) and `products` (title, content, published flag, owner, creation date), linked by a foreign key with cascade delete.
- **Docker:** a `python:3.10-slim` image; `docker-compose-dev.yml` runs the API with hot reload next to PostgreSQL 13, and `docker-compose-prod.yml` runs the published image on port 80.

## Getting started

### With Docker (development)

```bash
git clone https://github.com/ay-boutera/Task_Management_System.git
cd Task_Management_System
# create .env.dev (see below), then:
docker compose -f docker-compose-dev.yml up --build
```

The API runs on http://localhost:8000, with the interactive docs at http://localhost:8000/docs.

### Without Docker

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The tables are created at startup. Alembic is ready for the first migration: `alembic revision --autogenerate -m "message"`, then `alembic upgrade head`.

### Configuration

`.env.dev` and `.env.prod` are ignored by Git. They hold the database settings:

```env
DATABASE_HOSTNAME=postgres     # "postgres" inside Docker Compose, "localhost" otherwise
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=change-me     # must match POSTGRES_PASSWORD in the compose file
DATABASE_NAME=fastapi
```

## Project structure

```
app/
├── main.py          # FastAPI app and lifespan
├── config.py        # settings (pydantic-settings)
├── database.py      # engine, session dependency, table creation
├── models/          # SQLAlchemy models
├── schemas/         # Pydantic schemas (to come)
├── routes/          # API routers (to come)
├── services/        # business logic (to come)
├── core/            # security and authentication (to come)
└── utils/
db/                  # Alembic environment and migrations
Dockerfile
docker-compose-dev.yml
docker-compose-prod.yml
```

## Author

[Boutera Ahmed Yassine](https://github.com/ay-boutera)
