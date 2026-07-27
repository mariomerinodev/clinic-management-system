# 🏥 HealthClinic API - Sistema de Gestión Clínica

> Sistema backend modular y escalable para la gestión integral de clínicas médicas, desarrollado con un enfoque en arquitectura limpia, seguridad y rendimiento.

---

## 🚀 Características Principales (Features)

- **Control de Acceso Basado en Roles (RBAC):** Gestión diferenciada de permisos para Administradores, Médicos y Pacientes.
- **Gestión Inteligente de Citas:** Sistema de agendamiento en tiempo real con validación automática para evitar solapamientos de horarios.
- **Historiales Clínicos (EHR):** Registro seguro de antecedentes, diagnósticos y recetas médicas asociadas a cada paciente.
- **Documentación Interactiva:** API completamente documentada y lista para probar mediante Swagger UI y ReDoc.

---

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.10+
- **Framework Web:** FastAPI (Asíncrono y de alto rendimiento)
- **Base de Datos:** PostgreSQL
- **ORM y Migraciones:** SQLAlchemy & Alembic
- **Validación de Datos:** Pydantic (v2)
- **Seguridad:** OAuth2 con tokens JWT y cifrado de contraseñas con Passlib (Bcrypt)
- **Contenedorización:** Docker & Docker Compose

---

## 📁 Arquitectura del Proyecto

clinic-management-system/
│
├── app/
│ ├── api/ # Endpoints y enrutadores de la API
│ ├── core/ # Configuración central, seguridad y base de datos
│ ├── crud/ # Lógica de acceso a base de datos
│ ├── models/ # Modelos ORM de SQLAlchemy
│ ├── schemas/ # Modelos de validación Pydantic
│ └── main.py # Punto de entrada de la aplicación FastAPI
│
├── alembic/ # Control de migraciones de la base de datos
├── .gitignore # Archivos excluidos del control de versiones
└── README.md # Documentación del proyecto
