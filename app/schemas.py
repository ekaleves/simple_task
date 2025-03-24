from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Schema for creating favicon.ico new task (incoming request body)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


# Schema for reading task data (API response)
class TaskRead(TaskCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Enables compatibility with ORM models (Pydantic v2)


# Schema for updating an existing task (partial update)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
