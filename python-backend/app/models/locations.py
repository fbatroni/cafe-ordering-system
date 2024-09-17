from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database import Base

class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String)
    address_line1 = Column(String)
    address_line2 = Column(String)
    phone_number = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    created_at = Column(TIMESTAMP, default=func.now())
