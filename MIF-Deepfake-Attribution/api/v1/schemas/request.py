from typing import Optional

from pydantic import BaseModel, Field


# ==========================================================
# Authentication
# ==========================================================

class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=4, max_length=100)
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = None
    email: Optional[str] = None


class LoginRequest(BaseModel):
    username: str
    password: str


# ==========================================================
# Detection Pipeline
# ==========================================================

class AnalysisTriggerRequest(BaseModel):
    file_path: str
    file_type: str
    client_ip: str
    requested_by: Optional[str] = None


# ==========================================================
# Blockchain
# ==========================================================

class BlockchainVerificationRequest(BaseModel):
    media_hash: str


# ==========================================================
# Alerts
# ==========================================================

class AlertFilterRequest(BaseModel):
    minimum_confidence: float = 0.80
    verdict: str = "SUSPICIOUS"


# ==========================================================
# Analyst Notes
# ==========================================================

class AnalystNotesRequest(BaseModel):
    analyst_notes: str