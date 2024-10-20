### Project Documentation

#### Overview

This project is a Project Management API built using FastAPI, SQLAlchemy, and SQLite. It allows users to manage projects and their associated tickets. The API provides endpoints for creating, reading, updating, and deleting projects.

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
LICENSE
README.md
requirements.txt
venv/
    bin/
        activate
        ...
    include/
        ...
    lib/
    pyvenv.cfg
```

#### Key Components

- **Configuration**: Managed in

config.py

. The `get_app_settings` function loads the appropriate settings based on the environment (development or production).

- **Database**: Managed using SQLAlchemy. The database session is created in

session.py

, and CRUD operations are defined in

crud.py

.

- **API Routes**: Defined in

routes

. For example, project-related endpoints are defined in

projects.py

.

- **Error Handling**: Custom error handlers are defined in

errors

.

- **Event Handlers**: Event handlers for application startup and shutdown are defined in

events.py

.

#### API Endpoints

- **Create a new project**: `POST /projects/`
- **Retrieve a project**: `GET /projects/{project_id}`
- **Update a project**: `PUT /projects/{project_id}`
- **Delete a project**: `DELETE /projects/{project_id}`

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

#### License

This project is licensed under the MIT License. See the

LICENSE

file for more details.

#### Contributing

Please refer to the [pull request template](.github/pull_request_template.md) for guidelines on how to contribute to this project.

#### Environment Variables

The project uses environment variables for configuration. An example configuration is provided in the

.env.example

file.

```example
APP_ENV=dev
```

#### Ignored Files

The

.gitignore

file specifies files and directories that should be ignored by Git, including environment files and the SQLite database file.

```gitignore
**.env
dev.env
prod.env
project_management.db
```

This documentation provides an overview of the project structure, key components, API endpoints, database models, CRUD operations, and instructions for running the application. For more details, refer to the source code and the README.md file.
