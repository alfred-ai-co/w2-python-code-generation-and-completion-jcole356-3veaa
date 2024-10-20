from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Pydantic model for creating a new project
class ProjectCreate(BaseModel):
    """
    Pydantic model for creating a new project.

    Attributes:
        name (str): The name of the project.
        description (Optional[str]): The description of the project. Defaults to None.
    """
    name: str
    description: Optional[str] = None

# Pydantic model for the project response
class ProjectResponse(ProjectCreate):
    """
    Pydantic model for the project response, extending ProjectCreate.

    Attributes:
        id (int): The unique identifier of the project.
        created_at (datetime): The timestamp when the project was created.
    """
    id: int
    created_at: datetime
    
    class Config:
        """
        Pydantic configuration class to enable ORM mode.
        """
        from_attributes = True
