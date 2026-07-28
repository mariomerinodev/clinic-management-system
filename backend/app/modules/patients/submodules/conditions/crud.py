from sqlalchemy.orm import Session
from . import schemas, models
from ...models import Patient

# Función para crear una nueva condición
def condition_create(db: Session, new_condition: schemas.ConditionCreate, patient_id: int):
    # 0. Comprobar si el paciente existe
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not db_patient:
        return "PATIENT_NOT_FOUND"


    # 1. Comprobar si el paciente ya tiene registrado esta condición
    db_condition = db.query(models.Condition).filter(
        models.Condition.patient_id == patient_id,
        models.Condition.condition_name == new_condition.condition_name
    ).first()

    if db_condition:
        return "CONDITION_ALREADY_EXISTS"

    # 2. Crear la condición
    new_condition = models.Condition(
        **new_condition.model_dump(),
        patient_id=patient_id
    )

    db.add(new_condition)
    db.commit()
    db.refresh(new_condition)
    return new_condition

# Función para obtener todos las condiciones
def condition_get_list(db: Session, patient_id: int):
    db_conditions = db.query(models.Condition).filter(
        models.Condition.patient_id == patient_id
    ).all()
    return db_conditions

# Función para obtener una condición de un paciente
def condition_get(db: Session, patient_id: int, condition_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe la condición
    db_condition = db.query(models.Condition).filter(
        models.Condition.id == condition_id,
        models.Condition.patient_id == patient_id
    ).first()

    if not db_condition:
        return "CONDITION_NOT_FOUND"
    return db_condition

# Función para actualizar datos de una condición
def condition_update(db: Session, patient_id: int, condition_id: int, new_data_condition: schemas.ConditionUpdate):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe la condición
    db_condition = db.query(models.Condition).filter(
        models.Condition.id == condition_id,
        models.Condition.patient_id == patient_id
    ).first()

    if not db_condition:
        return "CONDITION_NOT_FOUND"

    # 3. Convertir los datos enviados a diccionario
    update_data = new_data_condition.model_dump(exclude_unset=True)
    
    # 4. Actualizar solo los datos que se hayan actualizado
    for key, value in update_data.items():
        setattr(db_condition, key, value)

    db.commit()
    db.refresh(db_condition)
    return db_condition

# Función para eliminar una condición
def condition_delete(db: Session, patient_id: int, condition_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe la condición
    db_condition = db.query(models.Condition).filter(
        models.Condition.id == condition_id,
        models.Condition.patient_id == patient_id
    ).first()

    if not db_condition:
        return "CONDITION_NOT_FOUND"

    # 3. Eliminar el contacto
    db.delete(db_condition)
    db.commit()
    return {"message": f"Condición con ID: {condition_id} eliminada correctamente"}