from pydantic import BaseModel
from typing import Optional

class FruitBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

class FruitCreate(FruitBase):
    pass

class FruitUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

class Fruit(FruitBase):
    id: int

    class Config:
        from_attributes = True
