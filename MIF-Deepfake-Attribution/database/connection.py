# database/connection.py

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base


# ==========================================================
# DATABASE CONFIGURATION
# ==========================================================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/mif_deepfake_db"
)


# ==========================================================
# DATABASE ENGINE
# ==========================================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    echo=False
)


# ==========================================================
# SESSION FACTORY
# ==========================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==========================================================
# FASTAPI DATABASE DEPENDENCY
# ==========================================================

def get_db():
    """
    Creates a database session for each request.

    Used by FastAPI dependency injection.

    Example:
        @router.post("/detect")
        def detect_media(
            payload: DetectionRequest,
            db: Session = Depends(get_db)
        ):
            ...
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

def initialize_database_tables():
    """
    Creates all database tables defined in models.py.

    Safe to execute multiple times because
    SQLAlchemy only creates missing tables.
    """

    Base.metadata.create_all(bind=engine)


# ==========================================================
# DATABASE HEALTH CHECK
# ==========================================================

def check_database_connection():
    """
    Verifies that the PostgreSQL database
    is reachable and operational.

    Returns:
        bool: True if connection succeeds,
              False otherwise.
    """

    try:

        with engine.connect() as connection:
            connection.execute("SELECT 1")

        return True

    except Exception as error:

        print(f"[DATABASE ERROR] {error}")

        return False