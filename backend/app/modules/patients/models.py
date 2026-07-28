from sqlalchemy import Column, Date, DateTime, Integer, String
from datetime import datetime, timezone

from sqlalchemy.orm import relationship
from ...core.database import Base

# Modelo del Paciente
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    # Datos personales
    name = Column(String, nullable= False, index=True)
    birthdate = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    phone_number = Column(String, index=True)
    email = Column (String, index=True)
    cp = Column(String)

    # Datos legales
    legal_identifier = Column(String, index=True, unique=True, nullable=False)

    # Información médica básica
    blood_group = Column(String)

    # Información sobre el registro del paciente
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relaciones con otras tablas
    emergency_contacts =  relationship("EmergencyContact", back_populates="patient", cascade="all, delete-orphan")