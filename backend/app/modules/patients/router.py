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