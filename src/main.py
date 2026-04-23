from fastapi import FastAPI
from src.api.v1.endpoints.health import router as health_router
from src.api.v1.endpoints.fruit import router as fruit_router
from src.api.v1.endpoints.customer import router as customer_router

app = FastAPI(
    title="Fruit Shop API",
    description="A modular FastAPI service for managing fruit inventory.",
    version="0.1.0"
)

# Include the health check router
app.include_router(health_router)

# Include the fruit router with a versioned prefix
app.include_router(fruit_router, prefix="/api/v1/fruits", tags=["fruits"])

# Include the customer router with a versioned prefix
app.include_router(customer_router, prefix="/api/v1/customers", tags=["customers"])

@app.get("/")
async def root():
    return {"message": "Welcome to Fruit Shop API. Visit /docs for documentation."}
