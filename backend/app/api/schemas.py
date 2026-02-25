from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime
from app.models.user import UserRole
from app.models.appointment import AppointmentStatus, AppointmentType
from app.models.medical_form import FormType, FormStatus


# ==================== AUTH SCHEMAS ====================

class PatientRegisterRequest(BaseModel):
    """Patient registration request"""
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    phone: Optional[str] = None
    date_of_birth: Optional[datetime] = None


class UserRegisterRequest(BaseModel):
    """Staff/Admin registration request"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=8)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    role: UserRole
    phone: Optional[str] = None
    department: Optional[str] = None


class LoginRequest(BaseModel):
    """Login request (works for both patients and users)"""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """JWT token response"""
    access_token: str
    token_type: str = "bearer"
    user_type: str  # "patient" or "user"
    user_id: int
    email: str
    role: Optional[str] = None  # Only for staff/admin


# ==================== PATIENT SCHEMAS ====================

class PatientResponse(BaseModel):
    """Patient data response (without sensitive info)"""
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str]
    date_of_birth: Optional[datetime]
    address_line1: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    blood_type: Optional[str]
    is_active: bool
    is_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class PatientUpdateRequest(BaseModel):
    """Update patient profile"""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    blood_type: Optional[str] = None
    allergies: Optional[str] = None
    medical_conditions: Optional[str] = None


class SensitiveDataRequest(BaseModel):
    """Request to add/update sensitive data (SSN, insurance, payment)"""
    ssn: Optional[str] = None
    insurance_number: Optional[str] = None
    card_number: Optional[str] = None


# ==================== APPOINTMENT SCHEMAS ====================

class AppointmentCreateRequest(BaseModel):
    """Create new appointment"""
    appointment_date: datetime
    appointment_type: AppointmentType
    reason: str = Field(..., min_length=10)
    doctor_name: Optional[str] = None
    department: Optional[str] = None
    notes: Optional[str] = None


class AppointmentResponse(BaseModel):
    """Appointment data response"""
    id: int
    patient_id: int
    appointment_date: datetime
    appointment_type: AppointmentType
    status: AppointmentStatus
    doctor_name: Optional[str]
    department: Optional[str]
    reason: str
    notes: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


class AppointmentUpdateRequest(BaseModel):
    """Update appointment (staff only)"""
    appointment_date: Optional[datetime] = None
    status: Optional[AppointmentStatus] = None
    doctor_name: Optional[str] = None
    admin_notes: Optional[str] = None


# ==================== MEDICAL FORM SCHEMAS ====================

class MedicalFormCreateRequest(BaseModel):
    """Create/submit medical form"""
    form_type: FormType
    form_title: str
    form_data: dict  # Flexible JSON data
    sensitive_fields: Optional[dict] = None  # Fields to tokenize


class MedicalFormResponse(BaseModel):
    """Medical form response"""
    id: int
    patient_id: int
    form_type: FormType
    form_title: str
    status: FormStatus
    form_data: dict
    created_at: datetime
    submitted_at: Optional[datetime]
    
    class Config:
        from_attributes = True


# ==================== USER SCHEMAS ====================

class UserResponse(BaseModel):
    """Staff/Admin user response"""
    id: int
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    role: UserRole
    phone: Optional[str]
    department: Optional[str]
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True