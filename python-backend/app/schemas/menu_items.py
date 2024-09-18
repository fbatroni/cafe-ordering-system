# app/schemas/menu_items.py

from pydantic import BaseModel, constr, condecimal
from typing import Optional

class MenuItemBase(BaseModel):
    category_id: int
    item_name: constr(min_length=1, max_length=100)
    description: Optional[str] = None
    price: condecimal(max_digits=10, decimal_places=2)
    image_url: Optional[str] = None
    is_available: Optional[bool] = True

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    item_id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    category_name: constr(min_length=1, max_length=100)
    description: Optional[str] = None
    parent_category_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True

class CategoryDetails(BaseModel):
    category_name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class MenuItemDetails(BaseModel):
    item_id: int
    item_name: constr(min_length=1, max_length=100)
    description: Optional[str] = None
    price: condecimal(max_digits=10, decimal_places=2)
    image_url: Optional[str] = None
    is_available: Optional[bool] = True
    category: CategoryDetails

    class Config:
        orm_mode = True

class LocationMenuItemDetails(BaseModel):
    location_id: int
    item: MenuItemDetails
    is_available: Optional[bool] = True

    class Config:
        orm_mode = True