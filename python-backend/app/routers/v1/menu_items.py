from app.routers.helper import get_current_user_with_role
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db
from typing import List
from datetime import datetime

menu_items_router = APIRouter(prefix="/v1/menu", tags=["MenuItems"])

# Get all menu items
@menu_items_router.get("/", response_model=List[schemas.MenuItem])
def read_menu_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.MenuItem).offset(skip).limit(limit).all()

# Get a specific menu item by ID
@menu_items_router.get("/{item_id}", response_model=schemas.MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_menu_item = db.query(models.MenuItem).filter(models.MenuItem.item_id == item_id).first()
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_menu_item

menu_items_admin_router = APIRouter(prefix="/v1/admin/menu", tags=["Admin"])

# Create a new menu item
@menu_items_admin_router.post("/", response_model=schemas.MenuItem)
def create_menu_item(menu_item: schemas.MenuItemCreate,
                     db: Session = Depends(get_db),
                     current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    db_menu_item = models.MenuItem(**menu_item.dict())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

# Update a menu item
@menu_items_admin_router.put("/{item_id}", response_model=schemas.MenuItem)
def update_menu_item(item_id: int, menu_item: schemas.MenuItemUpdate, db: Session = Depends(get_db)):
    db_menu_item = db.query(models.MenuItem).filter(models.MenuItem.item_id == item_id).first()
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    for key, value in menu_item.dict(exclude_unset=True).items():
        setattr(db_menu_item, key, value)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

# Delete a menu item
@menu_items_admin_router.delete("/{item_id}", response_model=schemas.MenuItem)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_menu_item = db.query(models.MenuItem).filter(models.MenuItem.item_id == item_id).first()
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    db.delete(db_menu_item)
    db.commit()
    return db_menu_item