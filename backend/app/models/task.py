from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

from app.db.base_class import Base


class TaskStatus(str, enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(DateTime)
    status = Column(Enum(TaskStatus), default=TaskStatus.TODO)
    assigned_user_id = Column(Integer, ForeignKey("users.id"))

    assigned_user = relationship("User", back_populates="tasks") 