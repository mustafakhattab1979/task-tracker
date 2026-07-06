# Entry point for the Task Tracker backend.
# Creates the FastAPI application instance and registers all routers.

from datetime import datetime, timezone
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.routers import tasks

# Load environment variables from .env
load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
PORT = int(os.getenv("PORT", 8000))

# Create the FastAPI app instance
app = FastAPI(
    title="Task Tracker API",
    description="A learning-focused backend built with FastAPI and JSON file storage.",
    version="0.1.0",
)

# Allow the frontend (opened locally, e.g. via file:// or a local static
# server on a different port) to call this API from the browser.
# Without this, the browser blocks the requests with a CORS error even
# though the backend itself is running and reachable via curl.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(tasks.router)


# Pydantic model for health response
class HealthResponse(BaseModel):
    status: str
    timestamp: str


@app.get("/health", response_model=HealthResponse, status_code=200)
def health_check() -> HealthResponse:
    """Returns API health status and current UTC timestamp."""
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=(APP_ENV == "development"))