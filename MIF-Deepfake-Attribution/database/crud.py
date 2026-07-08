from sqlalchemy.orm import Session

from database.models import User, ForensicDetectionLog


# ==========================================================
# USER CRUD
# ==========================================================

def get_user_by_username(db: Session, username: str):

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


def create_user(
    db: Session,
    username: str,
    hashed_password: str,
    full_name: str = None,
    email: str = None,
    role: str = "ANALYST"
):

    user = User(
        username=username,
        hashed_password=hashed_password,
        full_name=full_name,
        email=email,
        role=role,
        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# ==========================================================
# DETECTION CRUD
# ==========================================================

def create_detection_log(db: Session, log: ForensicDetectionLog):

    db.add(log)
    db.commit()
    db.refresh(log)

    return log


def get_detection_log(db: Session, log_id: int):

    return (
        db.query(ForensicDetectionLog)
        .filter(ForensicDetectionLog.id == log_id)
        .first()
    )


def get_detection_by_request_id(db: Session, request_id: str):

    return (
        db.query(ForensicDetectionLog)
        .filter(ForensicDetectionLog.request_id == request_id)
        .first()
    )


def update_detection_results(
    db: Session,
    log_id: int,
    **kwargs
):

    log = get_detection_log(db, log_id)

    if log is None:
        return None

    for key, value in kwargs.items():

        if hasattr(log, key):
            setattr(log, key, value)

    db.commit()
    db.refresh(log)

    return log


def delete_detection_log(db: Session, log_id: int):

    log = get_detection_log(db, log_id)

    if log is None:
        return False

    db.delete(log)
    db.commit()

    return True


# ==========================================================
# ALERTS
# ==========================================================

def get_critical_alerts(
    db: Session,
    threshold: float = 0.80
):

    return (
        db.query(ForensicDetectionLog)
        .filter(
            ForensicDetectionLog.final_verdict == "SUSPICIOUS",
            ForensicDetectionLog.detection_confidence >= threshold
        )
        .order_by(
            ForensicDetectionLog.created_at.desc()
        )
        .all()
    )


# ==========================================================
# DASHBOARD
# ==========================================================

def get_recent_detections(
    db: Session,
    limit: int = 20
):

    return (
        db.query(ForensicDetectionLog)
        .order_by(
            ForensicDetectionLog.created_at.desc()
        )
        .limit(limit)
        .all()
    )


def get_dashboard_statistics(db: Session):

    total = db.query(ForensicDetectionLog).count()

    suspicious = (
        db.query(ForensicDetectionLog)
        .filter(
            ForensicDetectionLog.final_verdict == "SUSPICIOUS"
        )
        .count()
    )

    authentic = (
        db.query(ForensicDetectionLog)
        .filter(
            ForensicDetectionLog.final_verdict == "AUTHENTIC"
        )
        .count()
    )

    processing = (
        db.query(ForensicDetectionLog)
        .filter(
            ForensicDetectionLog.processing_status == "PROCESSING"
        )
        .count()
    )

    return {
        "total_cases": total,
        "suspicious_cases": suspicious,
        "authentic_cases": authentic,
        "processing_cases": processing
    }