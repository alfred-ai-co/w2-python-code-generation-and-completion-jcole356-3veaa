### Project Architecture

#### Overview

This project is a Project Management API built using FastAPI, SQLAlchemy, and SQLite. It allows users to manage projects and their associated tickets. The architecture is designed to be modular, scalable, and maintainable, leveraging the strengths of each technology to provide a robust API.

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
    Dependencies.md
    Project Documentation.md
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

#### Modules and Their Responsibilities

1. **app/**: Main application directory.

   - **api/**: Contains API-related code.
     - **dependencies/**: Manages dependencies for the API.
     - **errors/**: Handles HTTP and validation errors.
     - **routes/**: Defines API routes.
       - **projects.py**: Contains endpoints for managing projects.
   - **api_models/**: Contains Pydantic models for request and response validation.
     - **projects.py**: Defines the `ProjectCreate` and `ProjectResponse` models.
   - **core/**: Core application settings and configurations.
     - **config.py**: Configuration settings for the application.
     - **events.py**: Event handlers for application startup and shutdown.
     - **logging.py**: Logging configuration.
     - **settings/**: Additional settings.
   - **db_models/**: Database models and CRUD operations.
     - **base.py**: Base database models.
     - **crud.py**: CRUD operations for database models.
     - **session.py**: Database session management.
   - **main.py**: Entry point for the FastAPI application.

2. **docs/**: Documentation files.

   - **Dependencies.md**: Documentation for project dependencies.
   - **Project Documentation.md**: General project documentation.

3. **venv/**: Virtual environment directory.

#### Database Models

**Project Model**

```python
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    tickets = relationship("Ticket", back_populates="project")
```

#### CRUD Operations

**Create Project**

```python
def create_project(db: Session, name: str, description: str) -> Project:
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project
```

**Get Project**

```python
def get_project(db: Session, project_id: int) -> Project:
    return db.query(Project).filter(Project.id == project_id).first()
```

**Update Project**

```python
def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        project.name = name or project.name
        project.description = description or project.description
        db.commit()
        db.refresh(project)
    return project
```

**Delete Project**

```python
def delete_project(db: Session, project_id: int) -> None:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()
    return project
```

#### API Endpoints

**Create a Project**

```python
@router.post('', response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.create_project(db, project.name, project.description)
    return db_project
```

**Read a Project**

```python
@router.get('/{project_id}', response_model=ProjectResponse)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")
    return db_project
```

**Update a Project**

```python
@router.put('/{project_id}', response_model=ProjectResponse)
async def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.update_project(db, project_id, project.name, project.description)
    if db_project is None:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")
    return db_project
```

**Delete a Project**

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

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the application:
   ```sh
   uvicorn app.main:app --reload
   ```
3. Navigate to `http://localhost:8000` to view the application.

#### Docker Support

The project includes a Dockerfile for containerization. To build and run the Docker image:

1. Build the Docker image:
   ```sh
   docker build -t <image_name> .
   ```
2. Run the Docker container:
   ```sh
   docker run --env-file app/.env -p 8000:8000 <image_name>
   ```

#### Environment Variables

The project uses environment variables for configuration. An example configuration is provided in the [.env.example](../.env.example) file.

```example
APP_ENV=dev
```

#### Summary

This documentation provides an overview of the project architecture, including the folder structure, key components, database models, CRUD operations, and API endpoints. It also includes instructions for running the application locally and using Docker for containerization. For more details, refer to the source code and the file:///Users/joshuacole/projects/app_academy/gen_ai/w2-python-code-generation-and-completion-jcole356-3veaa/README.md file.
