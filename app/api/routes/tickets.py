from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db_models import crud
from app.api_models import tickets
from app.api.dependencies.sqldb import get_db

router = APIRouter()

@router.post("/tickets/", response_model=tickets.Ticket)
def create_ticket(ticket: tickets.TicketCreate, db: Session = Depends(get_db)):
  db_ticket = crud.create_ticket(db=db, ticket=ticket)
  if db_ticket is None:
    raise HTTPException(status_code=400, detail="Ticket could not be created")
  return db_ticket

@router.get("/tickets/{ticket_id}", response_model=tickets.Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
  db_ticket = crud.get_ticket(db, ticket_id=ticket_id)
  if db_ticket is None:
    raise HTTPException(status_code=404, detail="Ticket not found")
  return db_ticket

@router.put("/tickets/{ticket_id}", response_model=tickets.Ticket)
def update_ticket(ticket_id: int, ticket: tickets.TicketCreate, db: Session = Depends(get_db)):
  db_ticket = crud.update_ticket(db=db, ticket_id=ticket_id, ticket=ticket)
  if db_ticket is None:
    raise HTTPException(status_code=404, detail="Ticket not found")
  return db_ticket

@router.delete("/tickets/{ticket_id}", response_model=tickets.Ticket)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
  db_ticket = crud.delete_ticket(db=db, ticket_id=ticket_id)
  if db_ticket is None:
    raise HTTPException(status_code=404, detail="Ticket not found")
  return db_ticket
