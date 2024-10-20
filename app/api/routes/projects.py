# Project Endpoints
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

import app.db_models.crud as crud
from app.api_models.projects import ProjectCreate, ProjectResponse
from app.api.dependencies.sqldb import get_db

# Initialize the API router
router = APIRouter()

# Endpoint to create a new project
@router.post('', response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    """
    Create a new project.

    Args:
        project (ProjectCreate): The project data to create.
        db (Session): The database session.

    Returns:
        ProjectResponse: The created project.
    """
    db_project = crud.create_project(db, project.name, project.description)
    return db_project

# Endpoint to read a project by its ID
@router.get('/{project_id}', response_model=ProjectResponse)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a project by its ID.

    Args:
        project_id (int): The ID of the project to retrieve.
        db (Session): The database session.

    Returns:
        ProjectResponse: The retrieved project.
    """
    db_project = crud.get_project(db, project_id)
    return db_project

# Endpoint to update an existing project by its ID
@router.put('/{project_id}', response_model=ProjectResponse)
async def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    """
    Update an existing project by its ID.

    Args:
        project_id (int): The ID of the project to update.
        project (ProjectCreate): The updated project data.
        db (Session): The database session.

    Returns:
        ProjectResponse: The updated project.
    """
    db_project = crud.update_project(db, project_id, project.name, project.description)
    return db_project

# Endpoint to delete a project by its ID
@router.delete('/{project_id}')
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    """
    Delete a project by its ID.

    Args:
        project_id (int): The ID of the project to delete.
        db (Session): The database session.

    Returns:
        dict: A message indicating the project was deleted.
    """
    crud.delete_project(db, project_id)
    return {'message': f'Project with id {project_id} deleted'}
