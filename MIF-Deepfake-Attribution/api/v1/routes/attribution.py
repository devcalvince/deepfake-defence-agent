from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from database.connection import get_db
from database import models
from api.v1.schemas.response import PipelineAnalysisResponse

router = APIRouter(tags=["Attribution"])

@router.get("/health", tags=["Attribution"])
def health():
    return {
        "service": "Forensic Attribution Router API",
        "status": "healthy"
    }

@router.get("/report/{log_id}", response_model=PipelineAnalysisResponse)
def get_source_attribution_results(log_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a completed forensic report by its tracking ID to examine 
    the model fingerprinting, source tracing, and metadata analysis.
    """
    # Query your forensic_detection_logs table natively
    db_log = db.query(models.ForensicDetectionLog).filter(models.ForensicDetectionLog.id == log_id).first()
    
    if not db_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="The requested forensic log record does not exist."
        )
        
    if db_log.status == "PROCESSING":
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail="Forensic attribution is still being calculated by the agent engine."
        )
        
    return db_log
