from app.routers.helper import get_current_user_with_role
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db
from typing import List
from datetime import datetime

menu_items_router = APIRouter(prefix="/v1/menu-items", tags=["MenuItems"])

# Get all menu items
@menu_items_router.get("/")
def read_menu_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = (
        db.query(models.MenuItem, models.Category, models.LocationMenuItem, models.Location)
        .join(models.LocationMenuItem, models.MenuItem.item_id == models.LocationMenuItem.item_id)
        .join(models.Category, models.MenuItem.category_id == models.Category.category_id)
        .join(models.Location, models.Location.location_id == models.LocationMenuItem.location_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

    # Dictionary to hold items and their locations
    item_data = {}

    # Process the results and group by item_id
    for item, category, location_menu_item, location in results:
        if item.item_id not in item_data:
            item_data[item.item_id] = {
                'item_id': item.item_id,
                'item_name': item.item_name,
                'description': item.description,
                'price': item.price,
                'image_url': item.image_url,
                'is_available': location_menu_item.is_available,
                'category_name': category.category_name,
                'category_id': category.category_id,
                'category_description': category.description,
                'locations': [location.location_name.replace("Corner Bakery Cafe - ", "")]
            }
        else:
            # Append additional locations to the existing item
            item_data[item.item_id]['locations'].append(location.location_name.replace("Corner Bakery Cafe - ", ""))

    # Convert the dictionary to a list and format the locations as a string
    return [
        schemas.LocationMenuItemFlat(
            location_id=None,  # No need to return individual location ID
            location_name=", ".join(item_data['locations']),  # Join locations with commas
            item_id=item_data['item_id'],
            item_name=item_data['item_name'],
            description=item_data['description'],
            price=item_data['price'],
            image_url=item_data['image_url'],
            is_available=item_data['is_available'],
            category_name=item_data['category_name'],
            category_description=item_data['category_description'],
            category_id=item_data["category_id"],
        )
        for item_data in item_data.values()
    ]

# Get a specific menu item by ID
@menu_items_router.get("/{item_id}", response_model=schemas.MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_menu_item = db.query(models.MenuItem).filter(models.MenuItem.item_id == item_id).first()
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_menu_item

menu_items_admin_router = APIRouter(prefix="/v1/admin/menu-items", tags=["Admin"])

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