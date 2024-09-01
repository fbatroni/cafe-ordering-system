from app.routers.helper import get_current_user_with_role
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.core import security
from app.dependencies import get_db
from typing import List

admin_router = APIRouter(prefix="/v1/admin", tags=["Admin"])

@admin_router.get("/users", response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    """
    Retrieve a list of all users.

    This endpoint allows an admin user to retrieve a list of all registered users.
    The response includes user details such as user ID, first name, last name, email, and roles.

    Only users with the "Admin" role can access this endpoint. If the current user
    does not have the required role, an HTTP 403 error will be raised.

    If no users are found in the database, an HTTP 404 error will be raised.
    """
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

@admin_router.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    """
    Retrieve a single user's details.

    This endpoint allows an admin user to retrieve the details of a specific user by their user ID.
    The response includes user details such as user ID, first name, last name, email, roles, and profile information.

    Only users with the "Admin" role can access this endpoint. If the current user
    does not have the required role, an HTTP 403 error will be raised.

    If the user is not found in the database, an HTTP 404 error will be raised.
    """
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@admin_router.delete("/users/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    """
    Delete a user from the system.

    This endpoint allows an admin user to delete a specific user by their user ID.
    The user's data will be permanently removed from the database.

    Only users with the "Admin" role can access this endpoint. If the current user
    does not have the required role, an HTTP 403 error will be raised.

    If the user is not found in the database, an HTTP 404 error will be raised.
    """
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return db_user