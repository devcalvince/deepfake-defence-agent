from typing import Optional

from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):

    username: str = Field(..., min_length=4)

    password: str = Field(..., min_length=8)


class LoginRequest(BaseModel):

    username: str

    password: str


class AnalysisTriggerRequest(BaseModel):

    file_path: str

    file_type: str

    source_ip: Optional[str] = None

    requested_by: Optional[str] = None


class BlockchainVerificationRequest(BaseModel):

    media_hash: str


class AlertFilterRequest(BaseModel):

    minimum_confidence: float = 0.80

    verdict: Optional[str] = "SUSPICIOUS"