from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Date
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from .....core.database import Base

# Modelo de Alergia
class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"), nullable=False)

    # Datos del alérgenos
    allergen = Column(String, nullable= False)
    severity = Column(String)
    reaction = Column(String)
    diagnosed_date = Column(Date)

    # Información sobre el registro del contacto de emergencia
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Paciente (relación del modelo de paciente)
    patient = relationship("Patient", back_populates="allergies")