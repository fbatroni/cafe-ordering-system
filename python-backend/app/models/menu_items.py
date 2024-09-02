from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    item_name = Column(String)
    description = Column(String, nullable=True)
    price = Column(DECIMAL(10, 2))
    image_url = Column(String, nullable=True)
    is_available = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)
    description = Column(String, nullable=True)
    parent_category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)

class LocationMenuItem(Base):
    __tablename__ = "location_menu_items"

    location_id = Column(Integer, ForeignKey("locations.location_id"), primary_key=True)
    item_id = Column(Integer, ForeignKey("menu_items.item_id"), primary_key=True)
    is_available = Column(Boolean, default=True)