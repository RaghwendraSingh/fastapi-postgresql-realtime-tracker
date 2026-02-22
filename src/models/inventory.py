from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from pydantic import BaseModel
from datetime import datetime

from database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class InventoryBase(BaseModel):
    name: str
    quantiy: int

class InventoryCreate(BaseModel):
    pass

class InventoryUpdate(BaseModel):
    quantity: int

class InventoryResponse(BaseModel):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True
    