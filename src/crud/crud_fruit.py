from sqlalchemy.orm import Session
from src.models.fruit import Fruit
from src.schemas.fruit import FruitCreate, FruitUpdate

def get_fruit(db: Session, fruit_id: int):
    return db.query(Fruit).filter(Fruit.id == fruit_id).first()

def get_fruit_by_name(db: Session, name: str):
    return db.query(Fruit).filter(Fruit.name == name).first()

def get_fruits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Fruit).offset(skip).limit(limit).all()

def create_fruit(db: Session, fruit: FruitCreate):
    db_fruit = Fruit(
        name=fruit.name,
        description=fruit.description,
        price=fruit.price,
        stock=fruit.stock
    )
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

def update_fruit(db: Session, fruit_id: int, fruit_update: FruitUpdate):
    db_fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if not db_fruit:
        return None
    
    update_data = fruit_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_fruit, key, value)
    
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

def delete_fruit(db: Session, fruit_id: int):
    db_fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if db_fruit:
        db.delete(db_fruit)
        db.commit()
    return db_fruit
