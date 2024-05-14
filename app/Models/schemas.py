from datetime import datetime
from pydantic import BaseModel, Field, EmailStr 
from .models import Note
from typing import Optional


class BaseUser(BaseModel):
    username: str = Field(title="Username")
    email: EmailStr = Field(title="user@gmail.com")
    password: str
    
class BaseNotes(BaseModel):
    title: str = Field(description="Title")
    content: str 
    
class ResponseUser(BaseModel):
    id: int
    username: str 
    email: EmailStr 
    created_at: datetime
    updated_at: datetime
    
    class Config:
        arbitrary_types_allowed = True  # Allow any type for some_date

class ResponseNote(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        arbitrary_types_allowed = True
        
        
        
class UpdateNote(BaseNotes):
    # updated_at: Optional[datetime]
    
    # class Config:
    #     arbitrary_types_allowed = True
    pass