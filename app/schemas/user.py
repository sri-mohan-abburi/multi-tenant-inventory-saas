from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: str = "staff"  # admin, manager, staff


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    tenant_id: int

    model_config = ConfigDict(from_attributes=True)
