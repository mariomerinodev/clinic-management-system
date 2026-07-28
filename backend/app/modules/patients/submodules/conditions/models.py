from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Date, Text
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from .....core.database import Base

# Modelo de Condición
class Condition(Base):
    __tablename__ = "conditions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"), nullable=False)

    # Datos de la condición
    condition_name = Column(String, nullable= False)
    status = Column(String, default="active")
    diagnosed_date = Column(Date)
    notes = Column(Text)

    # Información sobre el registro de la condición
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Paciente (relación del modelo de paciente)
    patient = relationship("Patient", back_populates="conditions")