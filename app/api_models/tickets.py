from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TicketCreate(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = Field(..., default=None, description="The date with which the ticket is due and can be flagged if current dates are past this")
    status: Optional[str] = Field(..., default="open", description="The status of the ticket")
    priority: Optional[str] = None

class TicketResponse(TicketCreate):
	id: int
	created_at: datetime
