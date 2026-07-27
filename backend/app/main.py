from fastapi import FastAPI

app = FastAPI(
    title="CMS API",
    description="Sistema de Gestión de Clínicas sanitarias. Arquitectura modular con FastAPI",
    version="1.0.1",
)

@app.get("/")
def root():
    return {"message": "Bienvenido al backend del CMS. Todo operativo"}