from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

# Esquema para crear un paciente
class PatientCreate(BaseModel):
    # Datos personales
    name: str
    birthdate: date
    gender: str
    phone_number: Optional[str] = None
    email: Optional[str] = None
    cp: Optional[str] = None

    # Datos legales
    legal_identifier: str

    # Información médica básica
    blood_group: Optional[str] = None

# Esquema para la respuesta de la API
class PatientResponse(PatientCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config():
        from_attributes=True

# Esquema para actualizar datos de un paciente
class PatientUpdate(BaseModel):
    # Datos personales
    name: Optional[str] = None
    birthdate: Optional[date] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    cp: Optional[str] = None

    # Datos legales
    legal_identifier: Optional[str] = None

    # Información médica básica
    blood_group: Optional[str] = None