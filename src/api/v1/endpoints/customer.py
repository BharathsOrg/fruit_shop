from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.db import get_db
from src.schemas.customer import Customer, CustomerCreate, CustomerUpdate
from src.crud import customer as crud_customer

router = APIRouter()

@router.post("/", response_model=Customer)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return crud_customer.create_customer(db=db, customer=customer)

@router.get("/{customer_id}", response_model=Customer)
async def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud_customer.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.get("/", response_model=List[Customer])
async def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_customer.get_customers(db, skip=skip, limit=limit)

@router.put("/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, customer_data: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = crud_customer.update_customer(db, customer_id=customer_id, customer_data=customer_data)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.delete("/{customer_id}")
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    success = crud_customer.delete_customer(db, customer_id=customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}
