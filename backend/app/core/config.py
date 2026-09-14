from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gemini Production Starter Kit"
    API_V1_STR: str = "/api/v1"
    
    # Gemini Configuration
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-1.5-pro"
    
    # Security
    API_KEY_NAME: str = "access_token"
    SECRET_API_KEY: str = "secure_fallback_development_key_12345"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
