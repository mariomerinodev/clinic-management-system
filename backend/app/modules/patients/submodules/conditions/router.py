from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....core.database import get_db
from . import schemas, crud

router = APIRouter(prefix="/{patient_id}/conditions", tags=["Conditions"])

# POST -> Crear una condición nueva
@router.post("/", response_model=schemas.ConditionResponse)
def condition_create(patient_id: int, new_condition: schemas.ConditionCreate, db: Session = Depends(get_db)):
    db_condition = crud.condition_create(db=db, new_condition=new_condition, patient_id=patient_id)

    match db_condition:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "CONDITION_ALREADY_EXISTS":
            raise HTTPException(status_code=400, detail="El paciente ya tiene esta condición registrada")
        case _:
            return db_condition


# GET -> Obtener todas las condiciones de un paciente
@router.get("/", response_model=List[schemas.ConditionResponse])
def contact_get_list(patient_id: int, db: Session = Depends(get_db)):
    return crud.condition_get_list(db=db, patient_id=patient_id)


# GET -> Obtener una única condición
@router.get("/{condition_id}", response_model=schemas.ConditionResponse)
def condition_get(patient_id: int, condition_id: int, db: Session = Depends(get_db)):
    db_condition = crud.condition_get(db=db, patient_id=patient_id, condition_id=condition_id)

    match db_condition:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "CONDITION_NOT_FOUND":
            raise HTTPException(status_code=404, detail="La condición no existe")
        case _:
            return db_condition


# PATCH -> Actualizar datos de una condición
@router.patch("/{condition_id}", response_model=schemas.ConditionResponse)
def condition_update(patient_id: int, condition_id: int, new_data_condition: schemas.ConditionUpdate, db: Session = Depends(get_db)):
    db_condition = crud.condition_update(db=db, patient_id=patient_id, condition_id=condition_id, new_data_condition=new_data_condition)

    match db_condition:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "CONDITION_NOT_FOUND":
            raise HTTPException(status_code=404, detail="La condición no existe")
        case _:
            return db_condition


# DELETE -> Eliminar una condición
@router.delete("/{condition_id}", status_code=200)
def condition_delete(patient_id: int, condition_id: int, db: Session = Depends(get_db)):
    db_condition = crud.condition_delete(db=db, patient_id=patient_id, condition_id=condition_id)

    match db_condition:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "CONDITION_NOT_FOUND":
            raise HTTPException(status_code=404, detail="La condición no existe")
        case _:
            return db_condition
