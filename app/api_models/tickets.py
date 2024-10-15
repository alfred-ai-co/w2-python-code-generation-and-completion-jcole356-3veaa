from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class TicketCreate(BaseModel):
  title: str
  description: str
  project_id: int
  status: Literal['open', 'in_progress', 'closed'] = 'open'
  priority: Literal['low', 'medium', 'high'] = 'medium'

class TicketResponse(TicketCreate):
  id: int
  created_at: datetime

  class Config:
    from_attributes = True
