from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class Role(BaseModel):
    role_id: int
    role_name: str


    class Config:
        from_attributes = True


class UserRole(BaseModel):
    user_role_id: int
    user_id: int
    role_id: int


    class Config:
        from_attributes = True


class UserProfile(BaseModel):
    profile_id: int
    user_id: int
    date_of_birth: Optional[datetime] = None
    profile_picture_url: Optional[str] = None


    class Config:
        from_attributes = True


class UserAddress(BaseModel):
    address_id: int
    user_id: int
    address_type_id: int
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    created_at: datetime


    class Config:
        from_attributes = True


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    user_id: int
    is_active: bool
    created_at: datetime
    roles: Optional[list[Role]] = []
    profile: Optional[UserProfile] = None
    addresses: Optional[list[UserAddress]] = []


    class Config:
        from_attributes = True

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
