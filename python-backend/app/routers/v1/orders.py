from app.routers.helper import get_current_user_with_role
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.core import security
from app.dependencies import get_db
from typing import List


orders_router = APIRouter(prefix="/v1/orders", tags=["Orders"])

# User can create an order
@orders_router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@orders_router.put("/{order_id}")
async def submit_order(order_id: int, user_id: int, db: Session = Depends(get_db)):
    # Retrieve the order
    order = db.query(models.Order).filter(models.Order.order_id == order_id, models.Order.user_id == user_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Check if the order is already submitted (i.e., already processed)
    if order.order_status_id != 1:  # Assuming 1 is the "Pending" status
        raise HTTPException(status_code=400, detail="Order already processed or submitted")

    # Retrieve the items in the order
    order_items = db.query(models.OrderItem).filter(models.OrderItem.order_id == order_id).all()

    if not order_items:
        raise HTTPException(status_code=400, detail="No items found in the order")

    # Calculate the total price
    total_price = sum(item.price * item.quantity for item in order_items)

    # Update the order's total_price and status
    order.total_price = total_price
    order.order_status_id = 2  # Assuming 2 represents a "Submitted" status

    # Commit the changes to the database
    db.commit()
    return {"message": "Order submitted successfully", "total_price": total_price}


# User can get their own orders
@orders_router.get("/", response_model=List[schemas.Order])
def read_user_orders(user_id: int, db: Session = Depends(get_db)):
    orders = db.query(models.Order).filter(models.Order.user_id == user_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="Orders not found")
    return orders

# User can view order statuses
@orders_router.get("/statuses", response_model=List[schemas.OrderStatus])
def read_order_statuses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    statuses = db.query(models.OrderStatus).offset(skip).limit(limit).all()
    return statuses

# Create an order item
@orders_router.post("/items", response_model=schemas.OrderItem)
def create_order_item(order_item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    # Validate that the order exists
    order = db.query(models.Order).filter(models.Order.order_id == order_item.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Validate that the menu item exists
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.item_id == order_item.item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    # Calculate the price based on the menu item price
    order_item.price = menu_item.price * order_item.quantity

    db_order_item = models.OrderItem(**order_item.dict())
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

# Get all order items for an order
@orders_router.get("/{order_id}/items", response_model=List[schemas.OrderItem])
def read_order_items(order_id: int, db: Session = Depends(get_db)):
    order_items = db.query(models.OrderItem).filter(models.OrderItem.order_id == order_id).all()
    if not order_items:
        raise HTTPException(status_code=404, detail="No items found for this order")
    return order_items


orders_admin_router = APIRouter(prefix="/v1/admin/orders", tags=["Admin"])

# Admin can view all orders
@orders_admin_router.get("/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    orders = db.query(models.Order).offset(skip).limit(limit).all()
    return orders

# Admin can create a new order status
@orders_admin_router.post("/statuses", response_model=schemas.OrderStatus)
def create_order_status(order_status: schemas.OrderStatusCreate,
                        db: Session = Depends(get_db),
                        current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    db_order_status = models.OrderStatus(order_status_name=order_status.order_status_name)
    db.add(db_order_status)
    db.commit()
    db.refresh(db_order_status)
    return db_order_status

# Admin can update order status
@orders_admin_router.put("/statuses/{order_status_id}", response_model=schemas.OrderStatus)
def update_order_status(order_status_id: int,
                        order_status: schemas.OrderStatusCreate,
                        db: Session = Depends(get_db),
                        current_user: models.User = Depends(get_current_user_with_role("Admin"))):
    db_order_status = db.query(models.OrderStatus).filter(models.OrderStatus.order_status_id == order_status_id).first()
    if db_order_status is None:
        raise HTTPException(status_code=404, detail="Order status not found")
    db_order_status.order_status_name = order_status.order_status_name
    db.commit()
    db.refresh(db_order_status)
    return db_order_status