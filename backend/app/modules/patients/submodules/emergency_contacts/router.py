from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....core.database import get_db
from . import schemas, crud

router = APIRouter(prefix="/{patient_id}/emergency_contacts", tags=["Emergency Contacts"])

# POST -> Crear un contacto de emergencia nuevo
@router.post("/", response_model=schemas.EmergencyContactResponse)
def contact_create(patient_id: int, new_contact: schemas.EmergencyContactCreate, db: Session = Depends(get_db)):
    db_contact = crud.contact_create(db=db, new_contact=new_contact, patient_id=patient_id)

    match db_contact:
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case "CONTACT_ALREADY_EXISTS":
            raise HTTPException(status_code=400, detail="El paciente ya tiene este teléfono registrado")
        case _:
            return db_contact


# GET -> Obtener todos los contactos de un paciente
@router.get("/", response_model=List[schemas.EmergencyContactResponse])
def contact_get_list(patient_id: int, db: Session = Depends(get_db)):
    return crud.contact_get_list(db=db, patient_id=patient_id)


# GET -> Obtener un único contacto
@router.get("/{contact_id}", response_model=schemas.EmergencyContactResponse)
def contact_get(patient_id: int, contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.contact_get(db=db, patient_id=patient_id, contact_id=contact_id)

    match db_contact:
        case "CONTACT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El contacto no existe")
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case _:
            return db_contact


# PATCH -> Actualizar datos de un contacto
@router.patch("/{contact_id}", response_model=schemas.EmergencyContactResponse)
def contact_update(patient_id: int, contact_id: int, new_data_contact: schemas.EmergencyContactUpdate, db: Session = Depends(get_db)):
    db_contact = crud.contact_update(db=db, patient_id=patient_id, contact_id=contact_id, new_data_contact=new_data_contact)

    match db_contact:
        case "CONTACT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El contacto no existe")
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case _:
            return db_contact


# DELETE -> Eliminar un contacto
@router.delete("/{contact_id}", status_code=200)
def contact_delete(patient_id: int, contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.contact_delete(db=db, patient_id=patient_id, contact_id=contact_id)

    match db_contact:
        case "CONTACT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El contacto no existe")
        case "PATIENT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="El paciente no existe")
        case _:
            return db_contact
