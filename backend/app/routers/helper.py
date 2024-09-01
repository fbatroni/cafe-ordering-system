from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.core import security
from app.dependencies import get_db
from typing import List

def get_current_user_with_role(required_role: str, db: Session = Depends(get_db)):
    def role_check(current_user: models.User = Depends(get_current_user)):
        user_role = db.query(models.Role).join(models.UserRole).filter(
            models.UserRole.user_id == current_user.user_id,
            models.Role.role_name == required_role
        ).first()
        if not user_role:
            raise HTTPException(status_code=403, detail="Insufficient privileges")
        return current_user
    return role_check

# FastAPI dependency to get the current user
def get_current_user(request: Request, db: Session = Depends(get_db)):
    try:
        authorization_header = request.headers.get('Authorization')
        token = security.extract_token_from_header(authorization_header)
        email = security.verify_token(token)
        if email is None:
            raise security.AuthenticationError("Could not validate credentials")
         # Fetch user with all related fields (roles, profile, addresses)
        user = db.query(models.User).filter(models.User.email == email).first()
        if user is None:
            raise security.AuthenticationError("User not found")
        return user
    except security.AuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )