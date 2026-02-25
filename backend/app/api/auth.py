from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Patient, User
from app.services.auth import auth_service
from app.api.schemas import (
    PatientRegisterRequest,
    UserRegisterRequest,
    LoginRequest,
    TokenResponse,
    PatientResponse,
    UserResponse
)
from datetime import datetime

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/patient/register", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def register_patient(request: PatientRegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new patient account.
    """
    # Check if email already exists
    existing_patient = db.query(Patient).filter(Patient.email == request.email).first()
    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash password
    hashed_password = auth_service.hash_password(request.password)
    
    # Create new patient
    new_patient = Patient(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        phone=request.phone,
        date_of_birth=request.date_of_birth,
        hashed_password=hashed_password,
        is_active=True,
        is_verified=False
    )
    
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    
    return new_patient


@router.post("/user/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(request: UserRegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new staff/admin user.
    (In production, this should require admin authentication)
    """
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Check if username already exists
    existing_username = db.query(User).filter(User.username == request.username).first()
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    
    # Hash password
    hashed_password = auth_service.hash_password(request.password)
    
    # Create new user
    new_user = User(
        email=request.email,
        username=request.username,
        first_name=request.first_name,
        last_name=request.last_name,
        role=request.role,
        phone=request.phone,
        department=request.department,
        hashed_password=hashed_password,
        is_active=True
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/patient/login", response_model=TokenResponse)
def login_patient(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Patient login - returns JWT token.
    """
    # Find patient by email
    patient = db.query(Patient).filter(Patient.email == request.email).first()
    
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Verify password
    if not auth_service.verify_password(request.password, patient.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Check if account is active
    if not patient.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is deactivated"
        )
    
    # Update last login
    patient.last_login = datetime.utcnow()
    db.commit()
    
    # Create JWT token
    access_token = auth_service.create_patient_token(patient.id, patient.email)
    
    return TokenResponse(
        access_token=access_token,
        user_type="patient",
        user_id=patient.id,
        email=patient.email
    )


@router.post("/user/login", response_model=TokenResponse)
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Staff/Admin login - returns JWT token.
    """
    # Find user by email
    user = db.query(User).filter(User.email == request.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Verify password
    if not auth_service.verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Check if account is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is deactivated"
        )
    
    # Update last login
    user.last_login = datetime.utcnow()
    db.commit()
    
    # Create JWT token
    access_token = auth_service.create_user_token(user.id, user.email, user.role.value)
    
    return TokenResponse(
        access_token=access_token,
        user_type="user",
        user_id=user.id,
        email=user.email,
        role=user.role.value
    )