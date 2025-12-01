from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class FormType(str, enum.Enum):
    INTAKE = "intake"
    CONSENT = "consent"
    MEDICAL_HISTORY = "medical_history"
    INSURANCE = "insurance"
    PAYMENT = "payment"
    HIPAA = "hipaa"


class FormStatus(str, enum.Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    REJECTED = "rejected"


class MedicalForm(Base):
    __tablename__ = "medical_forms"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key to patient
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    
    # Form details
    form_type = Column(Enum(FormType), nullable=False)
    form_title = Column(String(255), nullable=False)
    status = Column(Enum(FormStatus), default=FormStatus.DRAFT)
    
    # Form data (stored as JSON for flexibility)
    form_data = Column(JSON, nullable=False)
    
    # Sensitive data tokens (if form contains payment/SSN)
    sensitive_data_tokens = Column(JSON)  # e.g., {"card": "token_xyz", "ssn": "token_abc"}
    
    # Review info
    reviewed_by = Column(String(200))  # Admin/doctor who reviewed
    reviewed_at = Column(DateTime(timezone=True))
    review_notes = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    submitted_at = Column(DateTime(timezone=True))
    
    # Relationship
    patient = relationship("Patient", backref="medical_forms")