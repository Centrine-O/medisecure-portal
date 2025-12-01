from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class AppointmentStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    NO_SHOW = "no_show"


class AppointmentType(str, enum.Enum):
    GENERAL = "general"
    FOLLOWUP = "followup"
    EMERGENCY = "emergency"
    CONSULTATION = "consultation"
    LAB_WORK = "lab_work"


class Appointment(Base):
    __tablename__ = "appointments"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key to patient
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    
    # Appointment details
    appointment_date = Column(DateTime, nullable=False, index=True)
    appointment_type = Column(Enum(AppointmentType), default=AppointmentType.GENERAL)
    status = Column(Enum(AppointmentStatus), default=AppointmentStatus.PENDING)
    
    # Doctor/Provider info
    doctor_name = Column(String(200))
    department = Column(String(100))
    
    # Reason and notes
    reason = Column(Text, nullable=False)
    notes = Column(Text)
    admin_notes = Column(Text)  # Only visible to staff
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship
    patient = relationship("Patient", backref="appointments")