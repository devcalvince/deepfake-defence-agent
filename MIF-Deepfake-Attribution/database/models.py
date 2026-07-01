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
    Text,
    ForeignKey
)

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# ==========================================================
# USER MODEL
# ==========================================================

class User(Base):
    """
    System users (Forensic Analysts / Administrators)
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String(255),
        nullable=False
    )

    full_name = Column(
        String(150),
        nullable=True
    )

    email = Column(
        String(150),
        unique=True,
        nullable=True
    )

    role = Column(
        String(30),
        default="ANALYST"
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

    investigations = relationship(
        "ForensicDetectionLog",
        back_populates="analyst"
    )


# ==========================================================
# FORENSIC DETECTION LOG
# ==========================================================

class ForensicDetectionLog(Base):

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

    analyst_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    analyst = relationship(
        "User",
        back_populates="investigations"
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
    # MEDIA INFORMATION
    # ==================================================

    original_filename = Column(
        String(255),
        nullable=True
    )

    media_type = Column(
        String(30),
        nullable=True
    )

    evidence_path = Column(
        String(255),
        nullable=True
    )

    media_sha256 = Column(
        String(64),
        nullable=False,
        index=True
    )

    # ==================================================
    # AGENT SCORES
    # ==================================================

    visual_score = Column(
        Float,
        default=0.0,
        nullable=False
    )

    biometric_score = Column(
        Float,
        default=0.0,
        nullable=False
    )

    audio_score = Column(
        Float,
        default=0.0,
        nullable=False
    )

    forensic_score = Column(
        Float,
        default=0.0,
        nullable=False
    )

    semantic_score = Column(
        Float,
        default=0.0,
        nullable=False
    )

    # ==================================================
    # CONSENSUS ENGINE
    # ==================================================

    global_risk_score = Column(
        Float,
        default=0.0,
        nullable=False
    )

    detection_confidence = Column(
        Float,
        default=0.0,
        nullable=False
    )

    final_verdict = Column(
        String(30),
        default="PROCESSING",
        nullable=False,
        index=True
    )

    processing_status = Column(
        String(30),
        default="PENDING",
        nullable=False,
        index=True
    )

    # ==================================================
    # RAW AGENT OUTPUTS
    # ==================================================

    raw_agent_telemetry = Column(
        JSON,
        default=dict,
        nullable=False
    )

    # ==================================================
    # FORENSIC ATTRIBUTION
    # ==================================================

    inferred_generator_source = Column(
        String(150)
    )

    suspected_ai_model = Column(
        String(150)
    )

    metadata_tamper_detected = Column(
        Boolean,
        default=False,
        nullable=False
    )

    semantic_anomaly_detected = Column(
        Boolean,
        default=False,
        nullable=False
    )

    # ==================================================
    # ALERTING
    # ==================================================

    alert_generated = Column(
        Boolean,
        default=False,
        nullable=False
    )

    alert_timestamp = Column(
        DateTime,
        nullable=True
    )

    # ==================================================
    # BLOCKCHAIN
    # ==================================================

    blockchain_tx_hash = Column(
        String(100)
    )

    blockchain_block_number = Column(
        String(50)
    )

    ledger_is_anchored = Column(
        Boolean,
        default=False,
        nullable=False
    )

    # ==================================================
    # SECURITY
    # ==================================================

    is_encrypted = Column(
        Boolean,
        default=True,
        nullable=False
    )

    # ==================================================
    # ANALYST NOTES
    # ==================================================

    analyst_notes = Column(
        Text
    )

    # ==================================================
    # RECORD STATUS
    # ==================================================

    record_status = Column(
        String(30),
        default="ACTIVE",
        nullable=False
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