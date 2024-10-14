from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket


# CRUD operations for Project
def create_project(db: Session, name: str, description: str) -> Project:
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

# TODO: Get is a hot mess if there is no record
'''Edge Cases: Test edge cases, such as trying to update or delete a project that doesn’t exist,
to see how the API handles such scenarios. This will help you identify if additional error handling is needed.'''
def get_project(db: Session, project_id: int) -> Project:
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
      project.name = name
      project.description = description
      db.commit()
      db.refresh(project)
    return project

def delete_project(db: Session, project_id: int) -> None:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
      db.delete(project)
      db.commit()
