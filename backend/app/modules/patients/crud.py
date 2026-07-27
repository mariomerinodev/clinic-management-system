from sqlalchemy.orm import Session

from . import schemas
from . import models


# Función para crear un nuevo paciente
def patient_create(db: Session, patient: schemas.PatientCreate):
    # 1. Comprobar si ya existe el paciente en la db
    patient_existing = db.query(models.Patient).filter(models.Patient.legal_identifier == patient.legal_identifier).first()

    if patient_existing:
        return None

    # 2. Crear paciente
    new_patient = models.Patient(
        name=patient.name,
        birthdate=patient.birthdate,
        gender=patient.gender,
        phone_number=patient.phone_number,
        email=patient.email,
        cp=patient.cp,
        legal_identifier=patient.legal_identifier,
        blood_group=patient.blood_group
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