from src.core.db import engine, Base
from src.models.fruit import Fruit
from sqlalchemy.orm import Session

def seed_data():
    # Create a new session
    with Session(engine) as session:
        # Check if data already exists to avoid duplicates
        existing_fruit = session.query(Fruit).filter(Fruit.name == "Apple").first()
        if not existing_fruit:
            print("Seeding data into the database...")
            fruit1 = Fruit(name="Apple", description="A sweet red fruit", price=1.5, stock=100)
            fruit2 = Fruit(name="Banana", description="A yellow tropical fruit", price=0.8, stock=150)
            fruit3 = Fruit(name="Dragonfruit", description="Exotic pitaya", price=5.0, stock=20)
            
            session.add_all([fruit1, fruit2, fruit3])
            session.commit()
            print("Seeding completed successfully!")
        else:
            print("Data already exists. Skipping seed.")

if __name__ == "__main__":
    seed_data()
