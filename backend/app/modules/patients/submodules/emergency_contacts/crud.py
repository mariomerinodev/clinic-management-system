from sqlalchemy.orm import Session
from . import schemas, models
from ...models import Patient

# Función para crear un nuevo contacto de emergencia
def contact_create(db: Session, new_contact: schemas.EmergencyContactCreate, patient_id: int):
    # 0. Comprobar si el paciente existe
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not db_patient:
        return "PATIENT_NOT_FOUND"


    # 1. Comprobar si el paciente ya tiene registrado este contacto
    db_contact = db.query(models.EmergencyContact).filter(
        models.EmergencyContact.patient_id == patient_id,
        models.EmergencyContact.phone_number == new_contact.phone_number
    ).first()

    if db_contact:
        return "CONTACT_ALREADY_EXISTS"

    # 2. Crear el contacto
    new_contact = models.EmergencyContact(
        **new_contact.model_dump(),
        patient_id=patient_id
    )

    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

# Función para obtener todos los contactos de emergencia
def contact_get_list(db: Session, patient_id: int):
    db_contacts = db.query(models.EmergencyContact).filter(
        models.EmergencyContact.patient_id == patient_id
    ).all()
    return db_contacts

# Función para obtener un contacto de emergencia
def contact_get(db: Session, patient_id: int, contact_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe el contacto de emergencia
    db_contact = db.query(models.EmergencyContact).filter(
        models.EmergencyContact.id == contact_id,
        models.EmergencyContact.patient_id == patient_id
    ).first()

    if not db_contact:
        return "CONTACT_NOT_FOUND"
    return db_contact

# Función para actualizar datos de un contacto
def contact_update(db: Session, patient_id: int, contact_id: int, new_data_contact: schemas.EmergencyContactUpdate):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe el contacto de emergencia
    db_contact = db.query(models.EmergencyContact).filter(
        models.EmergencyContact.id == contact_id,
        models.EmergencyContact.patient_id == patient_id
    ).first()

    if not db_contact:
        return "CONTACT_NOT_FOUND"

    # 3. Convertir los datos enviados a diccionario
    update_data = new_data_contact.model_dump(exclude_unset=True)
    
    # 4. Actualizar solo los datos que se hayan actualizado
    for key, value in update_data.items():
        setattr(db_contact, key, value)

    db.commit()
    db.refresh(db_contact)
    return db_contact

# Función para eliminar un contacto
def contact_delete(db: Session, patient_id: int, contact_id: int):
    # 1. Comprobar si existe el paciente
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not db_patient:
        return "PATIENT_NOT_FOUND"
    
    # 2. Comprobar si existe el contacto de emergencia
    db_contact = db.query(models.EmergencyContact).filter(
        models.EmergencyContact.id == contact_id,
        models.EmergencyContact.patient_id == patient_id
    ).first()

    if not db_contact:
        return "CONTACT_NOT_FOUND"

    # 3. Eliminar el contacto
    db.delete(db_contact)
    db.commit()
    return {"message": f"Contacto con ID: {contact_id} eliminado correctamente"}