from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket
from typing import Optional
from app.db_models.base import Ticket


# CRUD operations for Project
def create_ticket(db: Session, title: str, project_id: int, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None) -> Ticket:
    new_ticket = Ticket(
        title=title,
        description=description,
        status=status,
        priority=priority,
        project_id=project_id
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket
    
def get_ticket(db: Session, ticket_id: int) -> Optional[Ticket]:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, title: str, project_id: int, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None) -> Optional[Ticket]:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        if title is not None:
            ticket.title = title
        if description is not None:
            ticket.description = description
        if status is not None:
            ticket.status = status
        if priority is not None:
            ticket.priority = priority
        if project_id is not None:
            ticket.project_id = project_id
        db.commit()
        db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int) -> bool:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        db.delete(ticket)
        db.commit()
    return ticket
