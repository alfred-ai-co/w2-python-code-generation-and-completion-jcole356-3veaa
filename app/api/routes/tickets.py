# Ticket Endpoints
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

import app.db_models.crud as crud
from app.api_models.message import Message
from app.api_models.tickets import TicketCreate, TicketResponse
from app.api.dependencies.sqldb import get_db


router = APIRouter()


@router.post('', response_model=TicketResponse)
async def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = crud.create_ticket(db, ticket.title, ticket.description, ticket.project_id, ticket.priority, ticket.status)
    return db_ticket

@router.get('/{ticket_id}', response_model=TicketResponse, responses={404: {"model": Message}})
async def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.put('/{ticket_id}', response_model=TicketResponse, responses={404: {"model": Message}})
async def update_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = crud.update_ticket(db, ticket_id, ticket.title, ticket.description, ticket.project_id, ticket.priority, ticket.status)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.delete('/{ticket_id}', responses={404: {"model": Message}})
async def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.delete_ticket(db, ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {'message': f'Ticket with id {ticket_id} deleted'}
