from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone_number = Column(String(50))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    roles = relationship("UserRole", back_populates="user")
    profile = relationship("UserProfile", uselist=False, back_populates="user")
    addresses = relationship("UserAddress", back_populates="user")


class Role(Base):
    __tablename__ = "roles"


    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), nullable=False)


class UserRole(Base):
    __tablename__ = "user_roles"


    user_role_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.role_id"), nullable=False)
    
    user = relationship("User", back_populates="roles")
    role = relationship("Role")


class UserProfile(Base):
    __tablename__ = "user_profiles"


    profile_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    date_of_birth = Column(DateTime)
    profile_picture_url = Column(String(255))
    
    user = relationship("User", back_populates="profile")


class UserAddress(Base):
    __tablename__ = "user_addresses"


    address_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    address_type_id = Column(Integer, ForeignKey("address_types.address_type_id"), nullable=False)
    address_line1 = Column(String(255))
    address_line2 = Column(String(255))
    city = Column(String(100))
    state = Column(String(100))
    postal_code = Column(String(20))
    country = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="addresses")







# CREATE TABLE inventory (
#     inventory_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#     item_id INT,
#     quantity_available INT,
#     reorder_level INT,
#     last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE
# );

class inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True,index=True)
    item_id =  Column(Integer, ForeignKey("menu_item.item_id"), nullable=False)
    quantity_available = Column(Integer)
    reorder_level = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)
    menu_item = relationship("item", back_populates="inventory")
    

# CREATE TABLE locations (
#     location_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#     location_name VARCHAR(100),
#     address_line1 VARCHAR(255),
#     address_line2 VARCHAR(255),
#     city VARCHAR(100),
#     state VARCHAR(100),
#     postal_code VARCHAR(20),
#     phone_number VARCHAR(20),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

class location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String(100))
    address_line1 = Column(String(255))
    address_line2 = Column(String(255))
    city = Column(String(100))
    state = Column(String(100))
    postal_code = Column(String(20))
    phone_number = Column(String(20))
    create_at = Column(DateTime, default=datetime.utcnow)


# CREATE TABLE discount_types (
#     discount_type_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#     discount_type_name VARCHAR(50) UNIQUE
# );


class discount_type(Base):
    __tablename__ = "discount_types"
    
    discount_type_id = Column(Integer, primary_key=True,nullable=True)
    discount_type_name = Column(String(100), unique=True)

