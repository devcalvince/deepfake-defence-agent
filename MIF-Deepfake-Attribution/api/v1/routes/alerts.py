from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.connection import get_db
from database import models
from api.v1.schemas.response import PipelineAnalysisResponse

router = APIRouter(tags=["Alerts"])

@router.get("/health", tags=["Alerts"])
def health():
    return {
        "service": "Alert Engine Router API",
        "status": "healthy"
    }

@router.get("/critical", response_model=List[PipelineAnalysisResponse])
def get_critical_forensic_alerts(db: Session = Depends(get_db)):
    """
    Queries the database logs for highly critical or suspicious deepfake 
    detections with a confidence rating exceeding a 0.80 risk score.
    """
    try:
        # Querying forensic_detection_logs for critical records
        critical_alerts = db.query(models.ForensicDetectionLog).filter(
            models.ForensicDetectionLog.overall_verdict == "SUSPICIOUS",
            models.ForensicDetectionLog.confidence_score >= 0.80
        ).order_by(models.ForensicDetectionLog.created_at.desc()).all()
        
        return critical_alerts
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to query system alerts: {str(e)}"
        )
