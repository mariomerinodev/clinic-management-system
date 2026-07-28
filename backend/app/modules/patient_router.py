from fastapi import APIRouter
from .patients.router import router as patient_router
from .patients.submodules.emergency_contacts.router import router as emergency_contact_router

router = APIRouter()

router.include_router(patient_router)

# Subrouters
router.include_router(emergency_contact_router)