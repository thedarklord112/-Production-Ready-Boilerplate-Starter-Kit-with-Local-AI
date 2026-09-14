from google import genai
from app.core.config import settings
from fastapi import HTTPException

class AIService:
    def __init__(self):
        # The Client automatically picks up GEMINI_API_KEY from the environment settings
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.GEMINI_MODEL  # e.g., "gemini-1.5-pro"

    async def generate_response(self, prompt: str) -> dict:
        """Standard non-streaming generation using Google Gemini SDK."""
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return {"response": response.text}
        except Exception as e:
            raise HTTPException(
                status_code=500, 
                detail=f"Gemini API Error: {str(e)}"
            )

    async def stream_response(self, prompt: str):
        """Asynchronous generator for streaming tokens to the client via Server-Sent Events (SSE)."""
        try:
            response_stream = self.client.models.generate_content_stream(
                model=self.model,
                contents=prompt,
            )
            for chunk in response_stream:
                if chunk.text:
                    yield f"data: {chunk.text}\n\n"
        except Exception as e:
            yield f"data: [ERROR: Gemini streaming failed - {str(e)}]\n\n"
