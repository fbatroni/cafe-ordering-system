from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.core import security
from app.dependencies import get_db

router = APIRouter(prefix="/v1/users", tags=["Users"])


@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
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


@router.post("/login", response_model=schemas.Token)
def login(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_login.email).first()
    if not user or not security.verify_password(user_login.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


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

@router.get("/me", response_model=schemas.UserResponse)
def get_me(current_user: models.User = Depends(get_current_user)):
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

