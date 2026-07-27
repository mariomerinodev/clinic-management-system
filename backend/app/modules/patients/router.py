from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...core.database import get_db
from . import schemas, crud

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
@router.patch("/{patient_id}", response_model=schemas.PatientResponse)
def patient_update(patient_id: int, new_data_patient: schemas.PatientUpdate, db: Session = Depends(get_db)):
    db_patient_updated, error = crud.patient_update(db=db, patient_id=patient_id, new_data_patient=new_data_patient)

    match error:
        case "LEGAL_IDENTIFIER_ALREADY_EXISTS":
            raise HTTPException(status_code=400, detail="El identificador legal ya está en uso")
        case "PATIENT_DONT_EXISTS":
            raise HTTPException(status_code=404, detail="El paciente no existe")

    return db_patient_updated

# DELETE -> Eliminar un paciente
@router.delete("/{patient_id}", status_code=200)
def patient_delete(patient_id: int, db: Session = Depends(get_db)):
    db_patient_deleted = crud.patient_delete(db=db, patient_id=patient_id)

    if db_patient_deleted == None:
        raise HTTPException(status_code=404, detail="El paciente no existe")
    
    return db_patient_deleted