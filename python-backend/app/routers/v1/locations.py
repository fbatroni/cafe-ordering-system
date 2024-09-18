from app.routers.helper import get_current_user_with_role
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db
from typing import List
from datetime import datetime

locations_router = APIRouter(prefix="/v1/locations", tags=["Locations"])

# Get locations by state and/or city
@locations_router.get("/", response_model=List[schemas.Location])
def get_locations(state: str = None, city: str = None, location_type: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Location)
    
    if state:
        query = query.filter(models.Location.state == state)
    if city:
        query = query.filter(models.Location.city == city)
    if location_type:
        query = query.filter(models.Location.location_type == location_type)
    
    return query.all()

# Get a specific location by ID
@locations_router.get("/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

# Get all menu items available at a specific location
@locations_router.get("/{location_id}/menu-items", response_model=List[schemas.LocationMenuItemFlat])
def read_location_menu_items(location_id: int, db: Session = Depends(get_db)):
    results = (
        db.query(models.MenuItem, models.Category, models.LocationMenuItem, models.Location)
        .join(models.LocationMenuItem, models.MenuItem.item_id == models.LocationMenuItem.item_id)
        .join(models.Category, models.MenuItem.category_id == models.Category.category_id)
        .join(models.Location, models.Location.location_id == models.LocationMenuItem.location_id)
        .filter(models.LocationMenuItem.location_id == location_id)
        .all()
    )

    return [
        schemas.LocationMenuItemFlat(
            location_id=location.location_id,
            location_name=location.location_name,
            item_id=item.item_id,
            item_name=item.item_name,
            description=item.description,
            price=item.price,
            image_url=item.image_url,
            is_available=location_menu_item.is_available,
            category_name=category.category_name,
            category_description=category.description,
            category_id=category.category_id
        )
        for item, category, location_menu_item, location in results
    ]




# Get the availability of a specific menu item at a specific location
@locations_router.get("/{location_id}/menu-items/{item_id}", response_model=schemas.LocationMenuItem)
def read_location_menu_item(location_id: int, item_id: int, db: Session = Depends(get_db)):
    db_location_menu_item = db.query(models.LocationMenuItem).filter(
        models.LocationMenuItem.location_id == location_id,
        models.LocationMenuItem.item_id == item_id
    ).first()
    if not db_location_menu_item:
        raise HTTPException(status_code=404, detail="LocationMenuItem not found")
    return db_location_menu_item

# Get currently open locations
@locations_router.get("/open-now", response_model=List[schemas.Location])
def get_open_locations(db: Session = Depends(get_db)):
    current_time = datetime.now().time()
    return db.query(models.Location).filter(models.Location.opening_time <= current_time, models.Location.closing_time >= current_time).all()

locations_admin_router = APIRouter(prefix="/v1/admin/locations", tags=["Admin"])

# Create a new location
@locations_admin_router.post("/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate,
                    db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# Update a location
@locations_admin_router.put("/{location_id}", response_model=schemas.Location)
def update_location(location_id: int,
                    location: schemas.LocationUpdate,
                    db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    db_location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    for key, value in location.dict(exclude_unset=True).items():
        setattr(db_location, key, value)
    db.commit()
    db.refresh(db_location)
    return db_location

# Delete a location
@locations_admin_router.delete("/{location_id}", response_model=schemas.Location)
def delete_location(location_id: int,
                    db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    db_location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(db_location)
    db.commit()
    return db_location

# Create a new location-menu item association
@locations_admin_router.post("/menu-items", response_model=schemas.LocationMenuItem)
def create_location_menu_item(location_menu_item: schemas.LocationMenuItemCreate, db: Session = Depends(get_db)):
    # Ensure location and menu item exist
    location = db.query(models.Location).filter(models.Location.location_id == location_menu_item.location_id).first()
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.item_id == location_menu_item.item_id).first()
    if not location or not menu_item:
        raise HTTPException(status_code=404, detail="Location or Menu Item not found")
    db_location_menu_item = models.LocationMenuItem(**location_menu_item.dict())
    db.add(db_location_menu_item)
    db.commit()
    db.refresh(db_location_menu_item)
    return db_location_menu_item

# Update the availability of a menu item at a specific location
@locations_admin_router.put("/{location_id}/menu-items/{item_id}", response_model=schemas.LocationMenuItem)
def update_location_menu_item(location_id: int, item_id: int, location_menu_item: schemas.LocationMenuItemUpdate, db: Session = Depends(get_db)):
    db_location_menu_item = db.query(models.LocationMenuItem).filter(
        models.LocationMenuItem.location_id == location_id,
        models.LocationMenuItem.item_id == item_id
    ).first()
    if not db_location_menu_item:
        raise HTTPException(status_code=404, detail="LocationMenuItem not found")
    for key, value in location_menu_item.dict(exclude_unset=True).items():
        setattr(db_location_menu_item, key, value)
    db.commit()
    db.refresh(db_location_menu_item)
    return db_location_menu_item

# Delete a location-menu item association
@locations_admin_router.delete("/{location_id}/menu-items/{item_id}", response_model=schemas.LocationMenuItem)
def delete_location_menu_item(location_id: int, item_id: int, db: Session = Depends(get_db)):
    db_location_menu_item = db.query(models.LocationMenuItem).filter(
        models.LocationMenuItem.location_id == location_id,
        models.LocationMenuItem.item_id == item_id
    ).first()
    if not db_location_menu_item:
        raise HTTPException(status_code=404, detail="LocationMenuItem not found")
    db.delete(db_location_menu_item)
    db.commit()
    return db_location_menu_item