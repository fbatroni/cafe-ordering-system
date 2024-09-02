from pydantic import BaseModel, constr
from typing import Optional

class CategoryBase(BaseModel):
    category_name: constr(min_length=1, max_length=100)
    description: Optional[str] = None
    parent_category_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True