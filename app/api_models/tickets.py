from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class TicketCreate(BaseModel):
  title: str
  description: str
  status: Literal['open', 'in_progress', 'closed'] = 'open'

class TicketResponse(TicketCreate):
  id: int
  created_at: datetime

  class Config:
    from_attributes = True
