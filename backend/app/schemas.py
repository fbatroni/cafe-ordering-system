from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
from datetime import datetime

# Role-related Schemas
class Role(BaseModel):
    """
    Schema for user roles.

    This schema defines the structure for roles that can be assigned to users in the Cafe Ordering System. 
    It includes the role ID and role name.
    """
    role_id: int
    role_name: str

    class Config:
        from_attributes = True


class UserRole(BaseModel):
    """
    Schema for mapping users to roles.

    This schema represents the association between users and their roles, including the user role ID, 
    user ID, and role ID.
    """
    user_role_id: int
    user_id: int
    role_id: int

    class Config:
        from_attributes = True


# User-related Schemas
class UserProfile(BaseModel):
    """
    Schema for user profile.

    This schema defines the structure for storing a user's profile information, including the profile ID, 
    user ID, date of birth, and profile picture URL.
    """
    profile_id: int
    user_id: int
    date_of_birth: Optional[datetime] = None
    profile_picture_url: Optional[str] = None

    class Config:
        from_attributes = True


class UserAddress(BaseModel):
    """
    Schema for user address.

    This schema defines the structure for storing a user's address information in the Cafe Ordering System. 
    It includes address ID, user ID, address type ID, address lines, city, state, postal code, and country.
    """
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
    """
    Base schema for user-related information.

    This base schema includes common fields for users, such as first name, last name, and email. 
    It is extended by other schemas like UserCreate, UserUpdate, and UserResponse.
    """
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Schema for creating a new user.

    This schema is used to define the data required when creating a new user, including their first name, 
    last name, email, and password.
    """
    password: str


class UserUpdate(UserBase):
    """
    Schema for updating an existing user's information.

    This schema is used for updating a user's profile information, such as first name, last name, and email. 
    The password is optional and will only be updated if provided.
    """
    password: Optional[str] = None


class UserPasswordUpdate(BaseModel):
    """
    Schema for updating a user's password.

    This schema is specifically used for updating the user's password. The new password must be at least 
    8 characters long.
    """
    password: constr(min_length=8)  # Ensure the password is at least 8 characters long

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    """
    Schema for user login.

    This schema defines the required data for a user to log in, including their email and password.
    """
    email: EmailStr
    password: str


class UserResponse(UserBase):
    """
    Schema for user response.

    This schema is used to return user data after successful operations such as registration, login, 
    or retrieving user details. It includes user ID, first name, last name, email, active status, 
    creation date, roles, profile, and addresses.
    """
    user_id: int
    is_active: bool
    created_at: datetime
    roles: Optional[List[Role]] = []
    profile: Optional[UserProfile] = None
    addresses: Optional[List[UserAddress]] = []

    class Config:
        from_attributes = True


# Token-related Schemas
class Token(BaseModel):
    """
    Schema for authentication tokens.

    This schema defines the structure of the JWT token returned upon successful authentication. 
    It includes the access token and its type (bearer).
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Schema for token data payload.

    This schema represents the data contained within a JWT token, typically used for validating the 
    user's session or role during API requests.
    """
    email: Optional[str] = None
