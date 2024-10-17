from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket


# CRUD operations for Project
def create_project(db: Session, name: str, description: str) -> Project:
    description = description or name
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project(db: Session, project_id: int) -> Project:
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
      project.name = name or project.name
      project.description = description or project.description
      db.commit()
      db.refresh(project)
    return project

def delete_project(db: Session, project_id: int) -> None:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
      db.delete(project)
      db.commit()
    return project

# CRUD operations for Ticket
def create_ticket(
    db: Session,
    title: str,
    description: str,
    project_id: int,
    priority: str,
    status: str
) -> Ticket:
    ticket = Ticket(title=title, description=description, project_id=project_id, priority=priority, status=status)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_ticket(db: Session, ticket_id: int) -> Ticket:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, title: str, description: str, project_id: int, priority: str, status: str) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
      ticket.title = title or ticket.title
      ticket.description = description or ticket.description
      ticket.project_id = project_id or ticket.project_id
      ticket.priority = priority or ticket.priority
      ticket.status = status or ticket.status
      db.commit()
      db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int) -> None:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
      db.delete(ticket)
      db.commit()
    return ticket
