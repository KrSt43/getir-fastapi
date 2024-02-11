from .database import Base
from sqlalchemy import Column, Integer, String, Double, DateTime
from sqlalchemy import func


class Driver(Base):
    __tablename__ = 'driver_driver'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    driving_score = Column(Double)
    age = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
