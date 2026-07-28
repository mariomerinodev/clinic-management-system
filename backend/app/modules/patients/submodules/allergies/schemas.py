from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

# Esquema para crear una alergia
class AllergyCreate(BaseModel):
    # Datos de la alergia
    allergen: str
    severity: Optional[str] = None
    reaction: Optional[str] = None
    diagnosed_date: Optional[date] = None

# Esquema para la respuesta de la API
class AllergyResponse(AllergyCreate):
    id: int
    patient_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True

# Esquema para actualizar datos de una alergia
class AllergyUpdate(BaseModel):
    # Datos de la alergia
    allergen: Optional[str] = None
    severity: Optional[str] = None
    reaction: Optional[str] = None
    diagnosed_date: Optional[date] = None