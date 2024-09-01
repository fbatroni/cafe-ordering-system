from app.routers.helper import get_current_user
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.core import security
from app.dependencies import get_db
from typing import List

users_router = APIRouter(prefix="/v1/users", tags=["Users"])

@users_router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.

    This endpoint allows a new user to be registered by providing their
    first name, last name, email, and password. The password will be hashed
    before being stored in the database.

    If the email is already registered, an HTTP 400 error will be raised.
    """
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    password_hash = security.get_password_hash(user.password)
    new_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password_hash=password_hash
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@users_router.post("/login", response_model=schemas.Token)
def login(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate a user and return a token.

    This endpoint allows a user to log in by providing their email and password.
    If the credentials are correct, a JWT token is returned that can be used
    for authenticated requests.

    If the credentials are incorrect, an HTTP 400 error will be raised.
    """
    user = db.query(models.User).filter(models.User.email == user_login.email).first()
    if not user or not security.verify_password(user_login.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@users_router.get("/me", response_model=schemas.UserResponse)
def get_me(current_user: models.User = Depends(get_current_user)):
    """
    Retrieve the current authenticated user's profile.

    This endpoint returns the profile of the currently authenticated user,
    including personal details, roles, profile information, and addresses.
    """
    user_response = schemas.UserResponse(
        user_id=current_user.user_id,
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        email=current_user.email,
        is_active=current_user.is_active,
        created_at=current_user.created_at,
        roles=[schemas.Role(role_id=role.role_id, role_name=role.role_name) for role in current_user.roles],
        profile=schemas.UserProfile(
            profile_id=current_user.profile.profile_id,
            user_id=current_user.profile.user_id,
            date_of_birth=current_user.profile.date_of_birth,
            profile_picture_url=current_user.profile.profile_picture_url,
        ) if current_user.profile else None,
        addresses=[
            schemas.UserAddress(
                address_id=address.address_id,
                user_id=address.user_id,
                address_type_id=address.address_type_id,
                address_line1=address.address_line1,
                address_line2=address.address_line2,
                city=address.city,
                state=address.state,
                postal_code=address.postal_code,
                country=address.country,
                created_at=address.created_at,
            ) for address in current_user.addresses
        ]
    )
    return user_response

@users_router.put("/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int, 
    user: schemas.UserUpdate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    """
    Update an existing user's details.

    This endpoint allows the currently authenticated user to update their
    profile information. The user can update fields like first name, last name,
    and email. If a new password is provided, it will be hashed before being stored.

    If the user ID does not match the authenticated user's ID, an HTTP 403 error
    will be raised. If the user is not found, an HTTP 404 error will be raised.
    """
    if current_user.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this user")

    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.password:
        password_hash = security.get_password_hash(user.password)
        user_data = user.dict(exclude_unset=True)
        user_data['password_hash'] = password_hash
        del user_data['password']
    else:
        user_data = user.dict(exclude_unset=True)

    for key, value in user_data.items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

@users_router.patch("/{user_id}/password", response_model=schemas.UserResponse)
def update_user_password(
    user_id: int, 
    password_data: schemas.UserPasswordUpdate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    """
    Update the password for the authenticated user.

    This endpoint allows the currently authenticated user to update their
    password. The new password will be hashed before being stored.

    If the user ID does not match the authenticated user's ID, an HTTP 403 error
    will be raised. If the user is not found, an HTTP 404 error will be raised.
    """
    if current_user.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this user's password")

    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    password_hash = security.get_password_hash(password_data.password)
    db_user.password_hash = password_hash
    
    db.commit()
    db.refresh(db_user)
    return db_user

@users_router.delete("/{user_id}", response_model=schemas.UserResponse)
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    """
    Delete the authenticated user's account.

    This endpoint allows the currently authenticated user to delete their
    account. The user's data will be permanently removed from the database.

    If the user ID does not match the authenticated user's ID, an HTTP 403 error
    will be raised. If the user is not found, an HTTP 404 error will be raised.
    """
    if current_user.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this user")

    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return db_user