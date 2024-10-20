# Alfred AI FastAPI Project Management API

This project is a Project Management API built with FastAPI, SQLAlchemy, and SQLite. The API allows users to manage projects and their associated tickets.

## Folder Structure

```bash
app/
├── api/
│ ├── errors/
│ │ ├── http_error.py
│ │ ├── validation_error.py
│ ├── routes/
│ │ ├── api.py
│ │ ├── home.py
│ │ ├── projects.py
├── core/
│ ├── config.py
│ ├── events.py
├── db_models/
│ ├── base.py
│ ├── crud.py
│ ├── session.py
├── main.py
├── project_management.db
```

### Crud

The provided code in [crud.py](app/db_models/crud.py) defines a set of CRUD (Create, Read, Update, Delete) operations for managing projects using SQLAlchemy.

```python
from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket
```

These CRUD functions provide the basic operations needed to manage projects in the database. They interact with the database using SQLAlchemy sessions and perform operations such as creating, reading, updating, and deleting projects. Each function ensures that the database is updated and the changes are committed, providing a consistent and reliable way to manage project data.

### Routes

These files defines the API endpoints for managing projects using FastAPI.

```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

import app.db_models.crud as crud
from app.api_models.projects import ProjectCreate, ProjectResponse
from app.api.dependencies.sqldb import get_db
```

- **FastAPI Imports**: 'APIRouter' is used to create a router for the API endpoints. 'HTTPException' is used to handle HTTP errors. 'Depends' is used for dependency injection.
- **SQLAlchemy Import**: 'Session' is used to manage database sessions.
- **CRUD Operations**: The 'crud' module contains functions for creating, reading, updating, and deleting projects.
- **API Models**: 'ProjectCreate' and 'ProjectResponse' are 'Pydantic' models used for request and response validation.
- **Database Dependency**: 'get_db' is a dependency that provides a database session.
- **Router**: An instance of `APIRouter` is created to define the project-related endpoints.

#### Projects

[projects.py](app/api/routes/projects.py)

This file defines a set of CRUD (Create, Read, Update, Delete) endpoints for managing projects. Each endpoint interacts with the database through the crud module and uses Pydantic models for request validation and response formatting. The get_db dependency ensures that each endpoint has access to a database session.

## .env Instructions

Create a `.env` file in the `app/` directory with the following contents:

```env
APP_ENV=dev
```

## Using the Dockerfile

### Build the Docker Image

To build the image, navigate to the root directory of the project and run:

```bash
docker build -t <image_name> .
```

### Run the Docker Image

To run the docker container with the environment variables, run:

```bash
docker run --env-file app/.env -p 8000:8000 <image_name>
```

This command will:

- Use the environment variables in the `.env` file
- Map the container's port 8000 to the host's port 8000
- Run the container in the background
- Start the FastAPI application with the `dev` flag for FastAPI (separate from the environment variable to enable debug mode)

# Project Management API Documentation

The Project Management API is designed to facilitate the management of projects and tickets within those projects. It provides a set of endpoints for creating, retrieving, updating, and deleting both projects and tickets.

## Endpoints

### Project Endpoints

| Operation                | HTTP Method | Endpoint                 | Description                       |
| ------------------------ | ----------- | ------------------------ | --------------------------------- |
| **Create a new project** | `POST`      | `/projects/`             | Create a new project              |
| **Retrieve a project**   | `GET`       | `/projects/{project_id}` | Retrieve a specific project by ID |
| **Update a project**     | `PUT`       | `/projects/{project_id}` | Update a specific project by ID   |
| **Delete a project**     | `DELETE`    | `/projects/{project_id}` | Delete a specific project by ID   |

## Running the Application Locally

To run the application locally, make sure you have Python installed. Then follow these steps at the root directory of the project:

1. Install depdencies: `pip install -r requirements.txt`
2. Run the application: `fastapi dev app/main.py` You may use `dev` or `prod` as the `fastapi` argument
3. Navigate to `http://localhost:8000` to view the application

- Note: The application will run in debug mode by default. To disable debug mode, set the `APP_ENV` environment variable to `prod`.

## License

This project is licensed under the MIT License. See the License file for details.
