from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from datetime import datetime, timezone

from sqlalchemy.orm import relationship
from .....core.database import Base

# Modelo de Contacto de Emegencia
class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"), nullable=False)

    # Datos del contacto
    name = Column(String, nullable= False)
    relationship_type = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    secondary_phone = Column(String)

    # Información sobre el registro del contacto de emergencia
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Paciente (relación del modelo de paciente)
    patient = relationship("Patient", back_populates="emergency_contacts")