### Project Management API

#### Overview

This project is a Project Management API built using FastAPI, SQLAlchemy, and SQLite. It allows users to manage projects and their associated tickets. The architecture is designed to be modular, scalable, and maintainable, leveraging the strengths of each technology to provide a robust API.

#### Features

- **Create, Read, Update, and Delete (CRUD) Operations**: Manage projects and tickets with ease.
- **FastAPI**: High-performance web framework for building APIs.
- **SQLAlchemy**: Powerful ORM for database interactions.
- **SQLite**: Lightweight and easy-to-use database.
- **Pydantic**: Data validation and settings management.
- **Loguru**: Advanced logging capabilities.

#### Folder Structure

```
.github/
    pull_request_template.md
    workflows/
        pr-notify.yml
.gitignore
app/
    __init__.py
    __pycache__/
    .env
    .env.example
    api/
        dependencies/
        errors/
        routes/
            projects.py
    api_models/
        __init__.py
        __pycache__/
        projects.py
    core/
        __init__.py
        __pycache__/
        config.py
        events.py
        logging.py
        settings/
    db_models/
        __init__.py
        __pycache__/
        base.py
        crud.py
        session.py
    main.py
Dockerfile
docs/
    Architecture.md
    Constraints.md
    Dependencies.md
    Deployment.md
    Design.md
    Project Documentation.md
    Requirements.md
    Testing.md
LICENSE
README.md
requirements.txt
venv/
    bin/
    include/
    lib/
    pyvenv.cfg
```

#### Key Components

1. **FastAPI**: The main web framework used to create the API endpoints and handle HTTP requests.
2. **SQLAlchemy**: The ORM (Object-Relational Mapping) library used for database interactions, including defining models and performing CRUD operations.
3. **SQLite**: The database used to store project and ticket data.
4. **Pydantic**: Used for data validation and settings management.
5. **Loguru**: Used for logging within the application.

#### API Endpoints

- **Create a Project**: `POST /projects/`
- **Retrieve a Project**: `GET /projects/{project_id}`
- **Update a Project**: `PUT /projects/{project_id}`
- **Delete a Project**: `DELETE /projects/{project_id}`

#### Example Code Snippets

**Creating a Project**

```python
@router.post('', response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.create_project(db, project.name, project.description)
    return db_project
```

**Reading a Project**

```python
@router.get('/{project_id}', response_model=ProjectResponse)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")
    return db_project
```

**Updating a Project**

```python
@router.put('/{project_id}', response_model=ProjectResponse)
async def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.update_project(db, project_id, project.name, project.description)
    if db_project is None:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")
    return db_project
```

**Deleting a Project**

```python
@router.delete('/{project_id}')
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")
    crud.delete_project(db, project_id)
    return {'message': f'Project with id {project_id} deleted'}
```

#### Running the Application

To run the application locally:

1. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

2. **Run the Application**:

   ```sh
   uvicorn app.main:app --reload
   ```

3. **Access the Application**:
   - Navigate to `http://localhost:8000` to view the application.

#### Docker Support

The project includes a Dockerfile for containerization. To build and run the Docker image:

1. **Build the Docker Image**:

   ```sh
   docker build -t project-management-api .
   ```

2. **Run the Docker Container**:

   ```sh
   docker run --env-file app/.env -p 8000:8000 project-management-api
   ```

3. **Access the Application**:
   - Navigate to `http://localhost:8000` to view the application.

#### Environment Variables

The project uses environment variables for configuration. An example configuration is provided in the `.env.example` file. You can create a `.env` file based on this example.

**Example `.env` File**

```example
APP_ENV=prod
DATABASE_URL=sqlite:///./project_management.db
```

#### Testing

To ensure the functionality, reliability, and stability of the Project Management API, the project includes unit tests and integration tests.

**Running Tests**:

```sh
pytest
```

**Generating Coverage Report**:

```sh
pytest --cov=app tests/
```

#### Deployment

The project can be deployed using Docker or directly on a server.

**Docker Deployment**:

1. **Build the Docker Image**:
   ```sh
   docker build -t project-management-api .
   ```
2. **Run the Docker Container**:
   ```sh
   docker run --env-file app/.env -p 8000:8000 project-management-api
   ```

**Direct Deployment**:

1. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the Application**:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

#### License

This project is licensed under the MIT License. See the LICENSE file for more details.

#### Contributing

Please refer to the [pull request template](.github/pull_request_template.md) for guidelines on how to contribute to this project.

#### Summary

This documentation provides an overview of the Project Management API, including its features, folder structure, key components, API endpoints, and instructions for running, testing, and deploying the application. For more details, refer to the source code and the project documentation files.
