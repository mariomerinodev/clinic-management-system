from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .modules.patients.router import router as patient_router
from .core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CMS API",
    description="Sistema de Gestión de Clínicas sanitarias. Arquitectura modular con FastAPI",
    version="1.0.1",
)

# Middleware para gestionar las rutas
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://192.168.0.27:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los routers
app.include_router(patient_router)

@app.get("/")
def root():
    return {"message": "Bienvenido al backend del CMS. Todo operativo"}