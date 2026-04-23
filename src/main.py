from fastapi import FastAPI
from src.api.v1.endpoints.health import router as health_router
from src.api.v1.endpoints.fruit import router as fruit_router

app = FastAPI(
    title="Fruit Shop API",
    description="A modular FastAPI service for managing fruit inventory.",
    version="0.1.0"
)

# Include the health check router
app.include_router(health_router)

# Include the fruit router with a versioned prefix
app.include_router(fruit_router, prefix="/api/v1/fruits", tags=["fruits"])

@app.get("/")
async def root():
    return {"message": "Welcome to Fruit Shop API. Visit /docs for documentation."}
