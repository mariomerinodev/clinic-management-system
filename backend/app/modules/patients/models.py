from sqlalchemy import Column, Date, Integer, String
from ...core.database import Base

# Modelo del Paciente
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    # Datos personales
    name = Column(String, nullable= False, index=True)
    birthdate = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    phone_number = Column(String, index=True)
    email = Column (String, index=True)
    cp = Column(String)

    # Datos legales
    legal_identifier = Column(String, index=True, unique=True, nullable=False)

    # Información médica básica
    blood_group = Column(String)