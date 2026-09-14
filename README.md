# Gemini API Production-Ready Starter Kit

<img width="1377" height="768" alt="image" src="https://github.com/user-attachments/assets/d7bcbe72-c1ec-48e6-b4e3-2ea5d34011cb" />


A production-grade, asynchronous backend boilerplate built with **FastAPI** and integrated with the **Google Gemini API** using the official, modern `google-genai` SDK. This repository serves as a robust foundation for building scalable AI-powered applications, complete with route security, structured configurations, and Docker containerization.

## 🚀 Features

- **Google Gemini Integration**: Native support for advanced models like `gemini-1.5-pro` using the latest Google GenAI SDK.
- **Asynchronous Inference**: Built-in support for standard JSON responses and live token streaming via Server-Sent Events (SSE).
- **Production-Ready Architecture**: Clean separation of concerns (routes, services, configurations, and core security middleware).
- **API Security**: Middleware-driven endpoint protection using an encrypted or secure custom API Key header header.
- **System Monitoring**: Public health check endpoint for container orchestration liveness/readiness probes (Kubernetes, AWS ECS, etc.).
- **Dockerized Environment**: Multi-stage `Dockerfile` optimized for fast caching layers and isolated dependency execution.

---

## 📂 Project Structure

```text
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── chat.py      # AI Inference & Streaming routes
│   │   │   │   │   └── health.py    # System monitoring health check
│   │   │   │   └── api.py           # Main API router
│   │   ├── core/
│   │   │   ├── config.py            # Pydantic settings & environment validation
│   │   │   └── security.py          # API Key Authentication middleware
│   │   ├── services/
│   │   │   └── ai_service.py        # Google Gemini SDK service wrapper
│   │   └── main.py                  # FastAPI application entrypoint
│   ├── Dockerfile                   # Optimized container setup
│   ├── requirements.txt             # Python application dependencies
│   └── .env.example                 # Template for environment variables
└── .gitignore                       # Safeguard against committing credentials
```

---

## 🛠️ Getting Started

### Prerequisites
Make sure you have the following installed on your machine:
- [Python 3.11+](https://python.org) or [Docker](https://docker.com)
- A Google AI Studio API Key (Get one from [Google AI Studio](https://google.com))

### 1. Environment Setup
Clone the repository and navigate to the backend directory:
```bash
cd backend
```

Copy the environment template file to create your local configurations:
```bash
cp .env.example .env
```

Open the newly created `.env` file and fill in your actual credentials:
```ini
PROJECT_NAME="Gemini Production Starter Kit"
GEMINI_API_KEY="AIzaSyYourActualGeminiKeyHere..."
GEMINI_MODEL="gemini-1.5-pro"
SECRET_API_KEY="choose_a_secure_token_to_protect_your_endpoints"
```

---

## 🐳 Running with Docker

The easiest way to run the application in a clean, isolated environment is using Docker.

1. **Build the Docker Image:**
   ```bash
   docker build -t gemini-fastapi-backend .
   ```

2. **Run the Container:**
   Pass your local environment variables into the container during runtime:
   ```bash
   docker run -d -p 8000:8000 --env-file .env --name gemini-backend gemini-fastapi-backend
   ```

3. **Verify it works:**
   Open your browser and visit `http://localhost:8000/api/v1/health`. You should receive an `{"status": "online"}` response.

---

## 🐍 Running Locally (Without Docker)

If you prefer to run and develop the application directly on your local Python environment:

1. **Create a virtual environment and activate it:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the development server:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## 🔌 API Endpoints & Testing

Once the server is running, you can access the interactive Swagger documentation at:  
👉 **`http://localhost:8000/docs`**

### Authenticating Requests
All endpoints under `/chat` require an authorization header matching the `SECRET_API_KEY` defined in your `.env` file.  
Include this header in your HTTP requests:
- **Header Name**: `access_token`
- **Header Value**: *Your configured backend token*

### Example: Standard Text Generation (`/api/v1/chat/generate`)
**Request:**
```bash
curl -X POST http://localhost:8000/api/v1/chat/generate \
     -H "access_token: your_secure_backend_access_token_here" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Explain Quantum Computing in one short sentence."}'
```

**Response:**
```json
{
  "response": "Quantum computing is a type of computing that uses qubits to process complex data exponentially faster than standard computers by exploiting quantum mechanics."
}
```

### Example: Live Streaming Response (`/api/v1/chat/stream`)
This endpoint utilizes **Server-Sent Events (SSE)** to stream chunks of text back to the client as they are generated by Gemini.
```bash
curl -X POST http://localhost:8000/api/v1/chat/stream \
     -H "access_token: your_secure_backend_access_token_here" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Write a short poem about coding."}'
```

---

## 🔒 Security Notice
The `.env` file contains highly sensitive keys. **Never commit your actual `.env` file to public source control.** The system includes a pre-configured `.gitignore` file to safeguard against accidental exposure. Always use secret management engines (like AWS Secrets Manager, GitHub Secrets, or Doppler) when deploying to live environments.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
