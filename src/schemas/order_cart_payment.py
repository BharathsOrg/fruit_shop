from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# --- Customer Schemas ---
class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int
    class Config:
        from_attributes = True

# --- Order Schemas ---
class OrderItemBase(BaseModel):
    fruit_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    price_at_time: float
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    customer_id: int
    status: str = "pending"
    total_amount: float

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class Order(OrderBase):
    id: int
    created_at: datetime
    order_items: List[OrderItem] = []
    class Config:
        from_attributes = True

# --- Cart Schemas ---
class CartItemBase(BaseModel):
    fruit_id: int
    quantity: int

class CartItemCreate(CartItemBase):
    pass

class CartItem(CartItemBase):
    id: int
    class Config:
        from_attributes = True

class Cart(BaseModel):
    id: int
    customer_id: int
    items: List[CartItem] = []
    class Config:
        from_attributes = True

# --- Payment Schemas ---
class PaymentBase(BaseModel):
    order_id: int
    amount: float
    status: str
    payment_method: str
    transaction_id: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
