from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
