import os
from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database.connection import get_db
from database import models
from api.v1.schemas.request import RegisterRequest, LoginRequest

router = APIRouter(tags=["Authentication"])

# ============================================================
# Security Configuration
# ============================================================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "CHANGE_THIS_SECRET_IN_PRODUCTION"
)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)

# ============================================================
# Password Helpers
# ============================================================


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ============================================================
# Health
# ============================================================


@router.get("/health")
def health():

    return {
        "service": "Authentication API",
        "status": "healthy"
    }


# ============================================================
# Register
# ============================================================


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register_user(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing = (
        db.query(models.User)
        .filter(models.User.username == request.username)
        .first()
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )

    user = models.User(

        username=request.username,

        hashed_password=hash_password(request.password),

        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully.",
        "username": user.username
    }


# ============================================================
# Login
# ============================================================


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(models.User)
        .filter(models.User.username == request.username)
        .first()
    )

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )

    if not verify_password(
        request.password,
        user.hashed_password
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )

    token = create_access_token(
        {"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }