from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.models.fruit import Fruit
from src.schemas.fruit import Fruit as FruitSchema, FruitCreate, FruitUpdate
from src.crud import crud_fruit
from src.core.db import get_db

router = APIRouter()

@router.post("/", response_model=FruitSchema, status_code=status.HTTP_201_CREATED)
def create_fruit(fruit: FruitCreate, db: Session = Depends(get_db)):
    """Create a new fruit."""
    # Check if fruit with same name already exists
    existing_fruit = crud_fruit.get_fruit_by_name(db, name=fruit.name)
    if existing_fruit:
        raise HTTPException(
            status_code=400, 
            detail=f"Fruit with name '{fruit.name}' already exists"
        )
    return crud_fruit.create_fruit(db, fruit=fruit)

@router.get("/{fruit_id}", response_model=FruitSchema)
def read_fruit(fruit_id: int, db: Session = Depends(get_db)):
    """Get a fruit by its ID."""
    db_fruit = crud_fruit.get_fruit(db, fruit_id=fruit_id)
    if db_fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return db_fruit

@router.get("/", response_model=List[FruitSchema])
def read_fruits(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all fruits with pagination."""
    return crud_fruit.get_fruits(db, skip=skip, limit=limit)

@router.put("/{fruit_id}", response_model=FruitSchema)
def update_fruit(fruit_id: int, fruit_update: FruitUpdate, db: Session = Depends(get_db)):
    """Update an existing fruit."""
    db_fruit = crud_fruit.get_fruit(db, fruit_id=fruit_id)
    if db_fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    updated_fruit = crud_fruit.update_fruit(db, fruit_id=fruit_id, fruit_update=fruit_update)
    return updated_fruit

@router.delete("/{fruit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fruit(fruit_id: int, db: Session = Depends(get_db)):
    """Delete a fruit."""
    db_fruit = crud_fruit.get_fruit(db, fruit_id=fruit_id)
    if db_fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    crud_fruit.delete_fruit(db, fruit_id=fruit_id)
    return None
