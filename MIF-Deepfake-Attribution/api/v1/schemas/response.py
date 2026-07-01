from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional, Dict, Any

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


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

    is_fake: bool


class ConsensusResult(BaseModel):

    final_score: float

    overall_verdict: str

    aggregated_artifacts: List[str]


class BlockchainReceipt(BaseModel):

    transaction_hash: Optional[str]

    block_number: Optional[int]

    anchored: bool


class PipelineAnalysisResponse(BaseModel):

    id: int

    request_id: str

    timestamp: datetime

    file_name: Optional[str]

    file_type: Optional[str]

    confidence_score: float

    overall_verdict: str

    status: str

    class Config:

        from_attributes = True