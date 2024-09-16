from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database import Base

class OrderStatus(Base):
    __tablename__ = "order_statuses"

    order_status_id = Column(Integer, primary_key=True, index=True)
    order_status_name = Column(String, unique=True, index=True)
    orders = relationship("Order", back_populates="order_status")

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    order_status_id = Column(Integer, ForeignKey("order_statuses.order_status_id"))
    total_price = Column(DECIMAL(10, 2))
    created_at = Column(TIMESTAMP, default=func.now())

    order_status = relationship("OrderStatus", back_populates="orders")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE"))
    item_id = Column(Integer, ForeignKey("menu_items.item_id", ondelete="CASCADE"))
    quantity = Column(Integer)
    price = Column(DECIMAL(10, 2))