from app.routers.helper import get_current_user_with_role
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from typing import List
from app.dependencies import get_db

categories_router = APIRouter(prefix="/v1/categories", tags=["Categories"])

# Get all categories
@categories_router.get("/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Category).offset(skip).limit(limit).all()

# Get a specific category by ID
@categories_router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

categories_admin_router = APIRouter(prefix="/v1/admin/categories", tags=["Admin"])

# Create a new category
@categories_admin_router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate,
                    db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# Update a category
@categories_admin_router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in category.dict(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

# Delete a category
@categories_admin_router.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return db_category