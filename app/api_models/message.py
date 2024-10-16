from pydantic import BaseModel

class Message(BaseModel):
    errors: list[str]
    