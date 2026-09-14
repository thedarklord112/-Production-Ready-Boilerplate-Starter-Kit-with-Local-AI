from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.endpoints import chat, health
from app.core.security import validate_api_key

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Application Routing
# Protect chat routes with the security dependency
app.include_router(
    chat.router, 
    prefix=f"{settings.API_V1_STR}/chat", 
    tags=["AI Inference"],
    dependencies=[Depends(validate_api_key)]
)

# Keep health check public for load balancers (AWS ALB, Kubernetes liveness probes)
app.include_router(
    health.router, 
    prefix=f"{settings.API_V1_STR}/health", 
    tags=["System Monitor"]
)
