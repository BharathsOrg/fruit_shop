from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    A simple health check endpoint to verify the service is running.
    """
    return {"status": "ok", "message": "Fruit Shop API is healthy"}
