from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket

# CRUD operations for Project

def create_project(db: Session, name: str, description: str) -> Project:
    """
    Create a new project in the database.

    Args:
      db (Session): The database session to use for the operation.
      name (str): The name of the project.
      description (str): The description of the project.

    Returns:
      Project: The newly created project instance.
    """
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project(db: Session, project_id: int) -> Project:
    """
    Retrieve a project by its ID from the database.

    Args:
      db (Session): The database session to use for the query.
      project_id (int): The ID of the project to retrieve.

    Returns:
      Project: The retrieved project object, or None if the project was not found.
    """
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    """
    Update the details of an existing project in the database.

    Args:
      db (Session): The database session to use for the query.
      project_id (int): The ID of the project to update.
      name (str): The new name for the project. If None, the name will not be updated.
      description (str): The new description for the project. If None, the description will not be updated.

    Returns:
      Project: The updated project object, or None if the project was not found.
    """
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
      project.name = name or project.name
      project.description = description or project.description
      db.commit()
      db.refresh(project)
    return project

def delete_project(db: Session, project_id: int) -> None:
    """
    Delete a project by its ID from the database.

    Args:
      db (Session): The database session to use for the query.
      project_id (int): The ID of the project to delete.

    Returns:
      None: If the project was successfully deleted or not found.
    """
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
      db.delete(project)
      db.commit()
    return project
