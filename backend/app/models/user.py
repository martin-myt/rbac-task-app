from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    auth0_id = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, nullable=False)  # admin, manager, user

    tasks = relationship("Task", back_populates="assigned_user") 