from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from .models import Note


class BaseUser(BaseModel):
    username: str = Field(title="Username")
    email: EmailStr = Field(title="user@gmail.com")
    password: str
    
class BaseNotes(BaseModel):
    title: str = Field(title="Title")
    content: str 
    
class ResponseUser(BaseModel):
    id: int
    username: str 
    email: EmailStr 
    created_at: datetime
    updated_at: datetime
    
    class Config:
        arbitrary_types_allowed = True  # Allow any type for some_date

class UserWithNotesResponse(ResponseUser):
    notes: Note
    
    class Config:
        arbitrary_types_allowed = True  # Allow any type for some_date