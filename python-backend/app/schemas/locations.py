from pydantic import BaseModel, Field,  constr
from typing import Optional, List
from datetime import datetime
from datetime import time

class LocationBase(BaseModel):
    location_name: constr(min_length=1, max_length=100)
    address_line1: constr(min_length=1, max_length=255)
    address_line2: Optional[constr(max_length=255)] = None
    city: constr(min_length=1, max_length=100)
    state: constr(min_length=2, max_length=100)
    postal_code: constr(min_length=1, max_length=20)
    phone_number: constr(min_length=10, max_length=20)
    location_type: Optional[constr(max_length=50)] = None  # Optional categorization by type
    opening_time: Optional[time] = None  # Optional opening time
    closing_time: Optional[time] = None  # Optional closing time

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class Location(LocationBase):
    location_id: int = Field(..., description="The unique ID of the location")
    created_at: Optional[str] = None  # Include the created_at timestamp in the response

    class Config:
        orm_mode = True

class LocationMenuItemBase(BaseModel):
    location_id: int
    item_id: int
    is_available: Optional[bool] = True

class LocationMenuItemCreate(LocationMenuItemBase):
    pass

class LocationMenuItemUpdate(LocationMenuItemBase):
    pass

class LocationMenuItem(LocationMenuItemBase):
    class Config:
        orm_mode = True
