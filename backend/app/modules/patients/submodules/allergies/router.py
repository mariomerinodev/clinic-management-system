from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....core.database import get_db
from . import schemas, crud

router = APIRouter(prefix="/{patient_id}/allergies", tags=["Allergies"])

# POST -> Crear una alergia nueva
@router.post("/", response_model=schemas.AllergyResponse)
def allergy_create(patient_id: int, new_allergy: schemas.AllergyCreate, db: Session = Depends(get_db)):
    db_allergy = crud.allergy_create(db=db, new_allergy=new_allergy, patient_id=patient_id)

    match db_allergy:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "ALLERGY_ALREADY_EXISTS":
            raise HTTPException(status_code=400, detail="El paciente ya tiene esta alergia registrada")
        case _:
            return db_allergy


# GET -> Obtener todas las alergias de un paciente
@router.get("/", response_model=List[schemas.AllergyResponse])
def contact_get_list(patient_id: int, db: Session = Depends(get_db)):
    return crud.allergy_get_list(db=db, patient_id=patient_id)


# GET -> Obtener una única alergia
@router.get("/{allergy_id}", response_model=schemas.AllergyResponse)
def allergy_get(patient_id: int, allergy_id: int, db: Session = Depends(get_db)):
    db_allergy = crud.allergy_get(db=db, patient_id=patient_id, allergy_id=allergy_id)

    match db_allergy:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "ALLERGY_NOT_FOUND":
            raise HTTPException(status_code=404, detail="La alergia no existe")
        case _:
            return db_allergy


# PATCH -> Actualizar datos de una alergia
@router.patch("/{allergy_id}", response_model=schemas.AllergyResponse)
def allergy_update(patient_id: int, allergy_id: int, new_data_allergy: schemas.AllergyUpdate, db: Session = Depends(get_db)):
    db_allergy = crud.allergy_update(db=db, patient_id=patient_id, allergy_id=allergy_id, new_data_allergy=new_data_allergy)

    match db_allergy:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "ALLERGY_NOT_FOUND":
            raise HTTPException(status_code=404, detail="La alergia no existe")
        case _:
            return db_allergy


# DELETE -> Eliminar un contacto
@router.delete("/{allergy_id}", status_code=200)
def allergy_delete(patient_id: int, allergy_id: int, db: Session = Depends(get_db)):
    db_allergy = crud.allergy_delete(db=db, patient_id=patient_id, allergy_id=allergy_id)

    match db_allergy:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "ALLERGY_NOT_FOUND":
            raise HTTPException(status_code=404, detail="La alergia no existe")
        case _:
            return db_allergy
