# database/models.py

import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    JSON,
    Boolean,
    Text
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ForensicDetectionLog(Base):
    """
    Core forensic intelligence ledger.

    Stores:
    - Multi-agent telemetry
    - Deepfake detection results
    - Forensic attribution findings
    - Blockchain verification records
    - Security audit information
    """

    __tablename__ = "forensic_detection_logs"

    # ==================================================
    # PRIMARY IDENTIFIERS
    # ==================================================

    id = Column(Integer, primary_key=True, autoincrement=True)

    request_id = Column(
        String(36),
        unique=True,
        nullable=False,
        index=True
    )

    timestamp = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False,
        index=True
    )

    client_ip = Column(
        String(45),
        nullable=False,
        index=True
    )

    # ==================================================
    # MEDIA FINGERPRINTING
    # ==================================================

    media_sha256 = Column(
        String(64),
        nullable=False,
        index=True
    )

    evidence_path = Column(
        String(255),
        nullable=True
    )

    # ==================================================
    # AGENT SCORES
    # ==================================================

    visual_score = Column(
        Float,
        nullable=False,
        default=0.0
    )

    biometric_score = Column(
        Float,
        nullable=False,
        default=0.0
    )

    audio_score = Column(
        Float,
        nullable=False,
        default=0.0
    )

    forensic_score = Column(
        Float,
        nullable=False,
        default=0.0
    )

    semantic_score = Column(
        Float,
        nullable=False,
        default=0.0
    )

    # ==================================================
    # CONSENSUS ENGINE OUTPUT
    # ==================================================

    global_risk_score = Column(
        Float,
        nullable=False
    )

    detection_confidence = Column(
        Float,
        nullable=False
    )

    final_verdict = Column(
        String(30),
        nullable=False,
        index=True
    )

    # ==================================================
    # RAW AGENT TELEMETRY
    # ==================================================

    raw_agent_telemetry = Column(
        JSON,
        nullable=False
    )

    # ==================================================
    # FORENSIC ATTRIBUTION
    # ==================================================

    inferred_generator_source = Column(
        String(150),
        nullable=True
    )

    suspected_ai_model = Column(
        String(150),
        nullable=True
    )

    metadata_tamper_detected = Column(
        Boolean,
        nullable=False,
        default=False
    )

    semantic_anomaly_detected = Column(
        Boolean,
        nullable=False,
        default=False
    )

    # ==================================================
    # REAL-TIME ALERTING
    # ==================================================

    alert_generated = Column(
        Boolean,
        nullable=False,
        default=False
    )

    alert_timestamp = Column(
        DateTime,
        nullable=True
    )

    # ==================================================
    # BLOCKCHAIN VERIFICATION
    # ==================================================

    blockchain_tx_hash = Column(
        String(100),
        nullable=True
    )

    blockchain_block_number = Column(
        String(50),
        nullable=True
    )

    ledger_is_anchored = Column(
        Boolean,
        nullable=False,
        default=False
    )

    # ==================================================
    # SECURITY CONTROLS
    # ==================================================

    is_encrypted = Column(
        Boolean,
        nullable=False,
        default=True
    )

    # ==================================================
    # OPTIONAL INVESTIGATION NOTES
    # ==================================================

    analyst_notes = Column(
        Text,
        nullable=True
    )

    # ==================================================
    # RECORD STATUS
    # ==================================================

    record_status = Column(
        String(30),
        nullable=False,
        default="ACTIVE"
    )

    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )