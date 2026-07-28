from fastapi import APIRouter
from .patients.router import router as patient_router
from .patients.submodules.emergency_contacts.router import router as emergency_contacts_router
from .patients.submodules.allergies.router import router as allergies_router
from .patients.submodules.conditions.router import router as conditions_router

router = APIRouter()

router.include_router(patient_router)

# Subrouters
router.include_router(emergency_contacts_router)
router.include_router(allergies_router)
router.include_router(conditions_router)
