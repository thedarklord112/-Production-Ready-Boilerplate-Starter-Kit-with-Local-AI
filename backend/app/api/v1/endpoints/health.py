from fastapi import APIRouter, status

router = APIRouter()

@router.get("", status_code=status.HTTP_200_OK)
async def health_check():
    """
    Simple public health check endpoint.
    Used by infrastructure, load balancers, or monitoring tools to verify the backend is live.
    """
    return {
        "status": "online",
        "services": {
            "api": "healthy"
        }
    }
