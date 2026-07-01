import os
import uuid
import hashlib
from datetime import datetime

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from database.connection import get_db
from database import models

from api.v1.schemas.request import AnalysisTriggerRequest
from api.v1.schemas.response import PipelineAnalysisResponse

from orchestrator.pipeline import AgentOrchestratorPipeline

router = APIRouter(tags=["Detection"])

orchestrator = AgentOrchestratorPipeline()


# ============================================================
# Health
# ============================================================


@router.get("/health")
def health():

    return {
        "service": "Detection Pipeline",
        "status": "healthy"
    }


# ============================================================
# Detection Endpoint
# ============================================================


@router.post(
    "/",
    response_model=PipelineAnalysisResponse,
    status_code=status.HTTP_202_ACCEPTED
)
def trigger_detection(

    request: AnalysisTriggerRequest,

    background_tasks: BackgroundTasks,

    db: Session = Depends(get_db)

):

    if not os.path.exists(request.file_path):

        raise HTTPException(

            status_code=400,

            detail="Target file does not exist."

        )

    try:

        with open(request.file_path, "rb") as file:

            media_hash = hashlib.sha256(
                file.read()
            ).hexdigest()

        log = models.ForensicDetectionLog(

            request_id=str(uuid.uuid4()),

            timestamp=datetime.utcnow(),

            client_ip=request.client_ip,

            media_sha256=media_hash,

            global_risk_score=0.0,

            final_verdict="PROCESSING",

            raw_agent_telemetry={},

            inferred_generator_source="UNKNOWN",

            metadata_tamper_detected=False,

            blockchain_tx_hash=None,

            blockchain_block_number=None,

            ledger_is_anchored=False

        )

        db.add(log)

        db.commit()

        db.refresh(log)

        background_tasks.add_task(

            orchestrator.process_forensic_pipeline,

            log.id,

            request.file_path

        )

        return log

    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )