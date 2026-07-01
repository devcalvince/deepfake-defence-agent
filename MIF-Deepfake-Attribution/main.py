from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

# Import your database session connection helper
from database.connection import get_db

from api.v1.routes import (
    authentication,
    detection,
    attribution,
    alerts
)

app = FastAPI(
    title="Multi-Agent Intelligence Framework",
    description="Real-Time Deepfake Detection and Forensic Source Attribution",
    version="1.0.0"
)

# 1. Enable Cross-Origin Resource Sharing (CORS) for your Streamlit/Frontend Dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your frontend components to connect securely
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Register Your Versioned Router Blocks
app.include_router(authentication.router, prefix="/api/v1/auth")
app.include_router(detection.router, prefix="/api/v1/detection")
app.include_router(attribution.router, prefix="/api/v1/attribution")
app.include_router(alerts.router, prefix="/api/v1/alerts")


@app.get("/")
def home():
    return {
        "system": "MIF",
        "status": "Running",
        "version": "1.0.0"
    }

# 3. Add an Operational System Health Check Endpoint
@app.get("/health", tags=["System Maintenance"])
def health_check(db: Session = Depends(get_db)):
    try:
        # Perform a quick, native connectivity query against PostgreSQL
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "system": "Multi-Agent Intelligence Framework Engine"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503, 
            detail=f"System Unhealthy: Database unreachable. Error: {str(e)}"
        )
