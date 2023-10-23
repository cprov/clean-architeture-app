# clean-architecture-app

## description
Clean Architecture example.

A poor-man Sli.do re-implementation, record questions for an event

## concept
1. Minimal functionality.


## Setup

1. Install dependencies with `poetry install`

2. Run
   1. `uvicorn ca_app.main:app --reload`: base
   2. options
      1. host: `--host 0.0.0.0`
      2. port: `--port 8080`

5. Test
   1. `pytest`: base
   2. `pytest --cov=ca_app --cov-report=term-missing`: coverage with stdout
   3. `pytest --cov=ca_app --cov-report=html`: coverage with html


## references
1. [FastAPI official docs](https://fastapi.tiangolo.com/)
2. [alembic official tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
