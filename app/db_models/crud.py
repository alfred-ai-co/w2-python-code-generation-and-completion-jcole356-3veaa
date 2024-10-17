from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket
from typing import Optional
from app.db_models.base import Ticket


# CRUD operations for Project
def create_ticket(db: Session, ticket_id: int, title: str, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None) -> Ticket:
    new_ticket = Ticket(
        id=ticket_id,
        title=title,
        description=description,
        status=status,
        priority=priority
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket
    
def get_ticket(db: Session, ticket_id: int) -> Optional[Ticket]:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()
