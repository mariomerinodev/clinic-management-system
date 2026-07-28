from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

# Esquema para crear una condición
class ConditionCreate(BaseModel):
    # Datos de la condición
    condition_name: str
    status: Optional[str] = "active"
    diagnosed_date: Optional[date] = None
    notes: Optional[str] = None

# Esquema para la respuesta de la API
class ConditionResponse(ConditionCreate):
    id: int
    patient_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True

# Esquema para actualizar datos de una condición
class ConditionUpdate(BaseModel):
    # Datos de la condición
    condition_name: Optional[str] = None
    status: Optional[str] = None
    diagnosed_date: Optional[date] = None
    notes: Optional[str] = None