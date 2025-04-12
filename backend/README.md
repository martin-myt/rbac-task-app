# RBAC Task Management API

A FastAPI-based backend for a Role-Based Access Control (RBAC) task management system.

## Features

- User management with Auth0 integration
- Task management with role-based permissions
- PostgreSQL database integration
- RESTful API endpoints
- Role-based access control (admin, manager, user)

## Prerequisites

- Python 3.9+
- Poetry
- PostgreSQL
- Auth0 account
- Docker and Docker Compose

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   poetry install
   ```

3. Create a `.env` file in the backend directory with the following variables:
   ```
   AUTH0_DOMAIN=your-auth0-domain
   AUTH0_API_AUDIENCE=your-api-audience
   AUTH0_ISSUER=https://your-auth0-domain/
   POSTGRES_SERVER=localhost
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=rbac_task_app
   ```

4. Set up the database:
   ```bash
   poetry run alembic upgrade head
   ```

## Running the Application

### Using Docker (Recommended)

Start the application and database:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

### Local Development

Start the development server:
```bash
poetry run uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

### Using Docker

Run tests in the Docker container:
```bash
docker-compose run app poetry run pytest
```

### Local Development

Run tests locally:
```bash
poetry run pytest
```

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── api_v1/
│   │       ├── endpoints/
│   │       │   ├── users.py
│   │       │   └── tasks.py
│   │       └── api.py
│   ├── core/
│   │   ├── auth.py
│   │   └── config.py
│   ├── db/
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models/
│   │   ├── user.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── task.py
│   └── services/
│       ├── user.py
│       └── task.py
├── tests/
├── alembic/
├── poetry.lock
├── pyproject.toml
└── README.md
``` 