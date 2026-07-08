from datetime import datetime
from typing import List, Optional, Dict, Any

from pydantic import BaseModel, ConfigDict


# ==========================================================
# Individual Agent Results
# ==========================================================

class VisualAgentResult(BaseModel):
    confidence: float
    artifacts: List[str]
    is_fake: bool


class AudioAgentResult(BaseModel):
    confidence: float
    artifacts: List[str]
    is_fake: bool


class BiometricAgentResult(BaseModel):
    confidence: float
    artifacts: List[str]
    is_fake: bool


class SemanticAgentResult(BaseModel):
    confidence: float
    artifacts: List[str]
    is_fake: bool


class ForensicAgentResult(BaseModel):
    confidence: float
    artifacts: List[str]
    detected_generator: Optional[str]
    suspected_ai_model: Optional[str]
    is_fake: bool


# ==========================================================
# Consensus Engine
# ==========================================================

class ConsensusResult(BaseModel):
    final_score: float
    overall_verdict: str
    aggregated_artifacts: List[str]


# ==========================================================
# Blockchain
# ==========================================================

class BlockchainReceipt(BaseModel):
    transaction_hash: Optional[str]
    block_number: Optional[str]
    anchored: bool


# ==========================================================
# Pipeline Response
# ==========================================================

class PipelineAnalysisResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int

    request_id: str

    timestamp: datetime

    client_ip: str

    original_filename: Optional[str]

    media_type: Optional[str]

    media_sha256: str

    visual_score: float

    biometric_score: float

    audio_score: float

    forensic_score: float

    semantic_score: float

    global_risk_score: float

    detection_confidence: float

    final_verdict: str

    processing_status: str

    inferred_generator_source: Optional[str]

    suspected_ai_model: Optional[str]

    metadata_tamper_detected: bool

    semantic_anomaly_detected: bool

    blockchain_tx_hash: Optional[str]

    blockchain_block_number: Optional[str]

    ledger_is_anchored: bool

    created_at: datetime

    updated_at: datetime


# ==========================================================
# Authentication Response
# ==========================================================

class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    full_name: Optional[str]
    email: Optional[str]
    role: str
    is_active: bool