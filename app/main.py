# Entry point for the Task Tracker backend.
# Creates the FastAPI application instance and defines the /health endpoint.

from datetime import datetime, timezone
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

# Load environment variables from .env (falls back to defaults if not present)
load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
PORT = int(os.getenv("PORT", 8000))

# Create the FastAPI app instance
app = FastAPI(
    title="Task Tracker API",
    description="A learning-focused backend built with FastAPI and JSON file storage.",
    version="0.1.0",
)

# Pydantic model defining the shape of the /health response
class HealthResponse(BaseModel):
    status: str
    timestamp: str

@app.get("/health", response_model=HealthResponse, status_code=200)
def health_check() -> HealthResponse:
    """Returns API health status and the current UTC timestamp in ISO 8601 format."""
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=(APP_ENV == "development"))