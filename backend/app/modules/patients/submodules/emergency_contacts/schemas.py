from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# Esquema para crear un contacto de emergencia
class EmergencyContactCreate(BaseModel):
    # Datos del contacto
    name: str
    relationship_type: str
    phone_number: str
    secondary_phone: Optional[str] = None

# Esquema para la respuesta de la API
class EmergencyContactResponse(EmergencyContactCreate):
    id: int
    patient_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True

# Esquema para actualizar datos de un paciente
class EmergencyContactUpdate(BaseModel):
    # Datos del contacto
    name: Optional[str] = None
    relationship_type: Optional[str] = None
    phone_number: Optional[str] = None
    secondary_phone: Optional[str] = None