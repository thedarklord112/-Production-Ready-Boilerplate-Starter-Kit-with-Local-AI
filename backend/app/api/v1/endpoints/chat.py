from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.services.ai_service import AIService
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_text(payload: ChatRequest, ai_service: AIService = Depends()):
    """Sends a prompt to Gemini and returns the complete text response."""
    try:
        data = await ai_service.generate_response(payload.prompt)
        return {"response": data.get("response")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stream")
async def stream_text(payload: ChatRequest, ai_service: AIService = Depends()):
    """Sends a prompt to Gemini and streams back the response tokens in real-time."""
    return StreamingResponse(
        ai_service.stream_response(payload.prompt), 
        media_type="text/event-stream"
    )
