from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    role: str


class UserCreate(UserBase):
    auth0_id: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True 