from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# OrderStatus Schema
class OrderStatusBase(BaseModel):
    order_status_name: str

class OrderStatusCreate(OrderStatusBase):
    pass

class OrderStatus(OrderStatusBase):
    order_status_id: int

    class Config:
        orm_mode = True

# Order Schema
class OrderBase(BaseModel):
    user_id: Optional[int] = None
    order_status_id: int
    total_price: float

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    order_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# OrderItem Schema
class OrderItemBase(BaseModel):
    order_id: int
    item_id: int
    quantity: int
    price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True
