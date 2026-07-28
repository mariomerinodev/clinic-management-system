from sqlalchemy.orm import Session
from . import schemas, models
from ...models import Patient

# Función para crear una nueva alergia
def allergy_create(db: Session, new_allergy: schemas.AllergyCreate, patient_id: int):
    # 0. Comprobar si el paciente existe
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not db_patient:
        return "PATIENT_NOT_FOUND"


    # 1. Comprobar si el paciente ya tiene registrado esta alergia
    db_allergy = db.query(models.Allergy).filter(
        models.Allergy.patient_id == patient_id,
        models.Allergy.allergen == new_allergy.allergen
    ).first()

    if db_allergy:
        return "ALLERGY_ALREADY_EXISTS"

    # 2. Crear la alergia
    new_allergy = models.Allergy(
        **new_allergy.model_dump(),
        patient_id=patient_id
    )

    db.add(new_allergy)
    db.commit()
    db.refresh(new_allergy)
    return new_allergy

# Función para obtener todos las alergias
def allergy_get_list(db: Session, patient_id: int):
    db_allergies = db.query(models.Allergy).filter(
        models.Allergy.patient_id == patient_id
    ).all()
    return db_allergies

# Función para obtener una alergia de un paciente
def allergy_get(db: Session, patient_id: int, allergy_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe la alergia
    db_allergy = db.query(models.Allergy).filter(
        models.Allergy.id == allergy_id,
        models.Allergy.patient_id == patient_id
    ).first()

    if not db_allergy:
        return "ALLERGY_NOT_FOUND"
    return db_allergy

# Función para actualizar datos de una alergia
def allergy_update(db: Session, patient_id: int, allergy_id: int, new_data_allergy: schemas.AllergyUpdate):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe la alergia
    db_allergy = db.query(models.Allergy).filter(
        models.Allergy.id == allergy_id,
        models.Allergy.patient_id == patient_id
    ).first()

    if not db_allergy:
        return "ALLERGY_NOT_FOUND"

    # 3. Convertir los datos enviados a diccionario
    update_data = new_data_allergy.model_dump(exclude_unset=True)
    
    # 4. Actualizar solo los datos que se hayan actualizado
    for key, value in update_data.items():
        setattr(db_allergy, key, value)

    db.commit()
    db.refresh(db_allergy)
    return db_allergy

# Función para eliminar una alergia
def allergy_delete(db: Session, patient_id: int, allergy_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe la alergia
    db_allergy = db.query(models.Allergy).filter(
        models.Allergy.id == allergy_id,
        models.Allergy.patient_id == patient_id
    ).first()

    if not db_allergy:
        return "ALLERGY_NOT_FOUND"

    # 3. Eliminar el contacto
    db.delete(db_allergy)
    db.commit()
    return {"message": f"Alergia con ID: {allergy_id} eliminada correctamente"}