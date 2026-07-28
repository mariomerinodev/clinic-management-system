from sqlalchemy.orm import Session
from . import schemas, models

# Función para crear un nuevo paciente
def patient_create(db: Session, patient: schemas.PatientCreate):
    # 1. Comprobar si ya existe el paciente en la db
    db_patient = db.query(models.Patient).filter(models.Patient.legal_identifier == patient.legal_identifier).first()

    if db_patient:
        return None

    # 2. Crear paciente
    new_patient = models.Patient(
        **patient.model_dump()
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


# Función para obtener todos los pacientes
def patient_get_list(db: Session):
    db_patients = db.query(models.Patient).all()
    return db_patients

# Función para obtener un paciente
def patient_get(db: Session, patient_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    
    if not db_patient:
        return None
    return db_patient


# Función para actualizar datos de un paciente
def patient_update(db: Session, patient_id: int, new_data_patient: schemas.PatientUpdate):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    
    if not db_patient:
        return None, "PATIENT_NOT_FOUND"
    
    # 2. Convertir los datos enviados a diccionario
    update_data = new_data_patient.model_dump(exclude_unset=True) # Excluye los que no se hayan rellenado

    # 3. Comprobar que los parametros únicos no se repitan
    if "legal_identifier" in update_data:
        existing_identifier = db.query(models.Patient).filter(
            models.Patient.legal_identifier == update_data["legal_identifier"],
            models.Patient.id != patient_id
        ).first()
        if existing_identifier:
            return None, "LEGAL_IDENTIFIER_ALREADY_EXISTS"
    
    # 4. Actualizar solo los datos que se hayan actualizado
    for key, value in update_data.items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)
    return db_patient, None


# Función para eliminar un paciente
def patient_delete(db: Session, patient_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not db_patient:
        return None

    db.delete(db_patient)
    db.commit()
    return {"message": f"Paciente con ID: {patient_id} eliminado correctamente"}