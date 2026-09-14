from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from app.core.config import settings

api_key_header = APIKeyHeader(name=settings.API_KEY_NAME, auto_error=False)

async def validate_api_key(api_key: str = Security(api_key_header)):
    """
    Validates the incoming API key against the configured secure token.
    Raises a 403 Forbidden exception if validation fails.
    """
    if api_key == settings.SECRET_API_KEY:
        return api_key
        
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate credentials. Invalid or missing API Key.",
    )
