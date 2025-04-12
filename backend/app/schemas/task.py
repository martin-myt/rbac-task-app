from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: TaskStatus = TaskStatus.TODO
    assigned_user_id: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    title: Optional[str] = None


class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True 