from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...core.database import get_db
from . import schemas
from . import crud

router = APIRouter(prefix="/patients", tags=["Patients"])

# POST -> Crear un paciente nuevo
@router.post("/", response_model=schemas.PatientResponse)
def patient_create(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.patient_create(db=db, patient=patient)

    if db_patient == None:
        raise HTTPException(status_code=400, detail="El paciente ya está registrado ")
    return db_patient

# GET -> Obtener todos los pacientes
@router.get("/", response_model=List[schemas.PatientResponse])
def patient_get_list(db: Session = Depends(get_db)):
    return crud.patient_get_list(db=db)

# GET -> Obtener un paciente
@router.get("/{patient_id}", response_model=schemas.PatientResponse)
def patient_get(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.patient_get(db=db, patient_id=patient_id)

    if db_patient == None:
        raise HTTPException(status_code=404, detail="El paciente no existe")
    return db_patient

# PATCH -> Actualizar datos de un paciente

# DELETE -> Eliminar un paciente