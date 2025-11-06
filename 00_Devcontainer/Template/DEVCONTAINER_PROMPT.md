# 🐳 Prompt Template: Generador de Dev Container

**Copia este prompt, llena los campos entre [corchetes], y úsalo con Claude o cualquier LLM**

---

## 📋 Prompt para Copiar y Llenar:

```
Necesito crear una configuración de Dev Container completa para un proyecto Python desde cero.

## Información del Proyecto

**Nombre del proyecto:** [Nombre del proyecto]
**Lenguaje:** Python [Versión, ej: 3.11]
**Gestor de paquetes:** uv (https://github.com/astral-sh/uv)
**Tipo de proyecto:** [Describe brevemente: API REST, Web App, CLI Tool, Data Science, etc.]

## Requisitos Técnicos

**Framework principal:** [FastAPI / Django / Flask / Otro]
**Base de datos:** [PostgreSQL / MySQL / MongoDB / SQLite / Ninguna]
**Otros servicios:** [Redis / RabbitMQ / Ninguno]

**Dependencias principales que necesito:**
- [Ejemplo: FastAPI para la API]
- [Ejemplo: SQLAlchemy para ORM]
- [Ejemplo: Pydantic para validación]
- [Agregar más según necesites]

**Variables de entorno necesarias:**
- [Ejemplo: DATABASE_URL]
- [Ejemplo: SECRET_KEY]
- [Ejemplo: DEBUG=True]
- [O indica: Ninguna por ahora]

## Configuración del Entorno

**Puerto principal:** [8000 / 3000 / 5000 / otro]
**Puertos adicionales:** [Si necesitas más puertos]

**Usuario en container:** vscode (UID 1000)
**Directorio de trabajo:** /workspace

## Herramientas de Desarrollo

**Formateo automático al guardar:** [Sí con Black / Sí con Ruff / No]
**Linting:** [Pylint / Ruff / Flake8 / Ninguno]
**Type checking:** [mypy / pyright / Ninguno]
**Testing:** [pytest / unittest / Ninguno]

**¿Necesitas debugger configurado?** [Sí / No]
**¿Necesitas Jupyter notebooks?** [Sí / No]

## Extensiones VS Code Requeridas

**Obligatorias:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Adicionales que necesito:**
- [Marca las que quieras]
- [ ] ms-python.black-formatter (formateo con Black)
- [ ] charliermarsh.ruff (linting y formateo con Ruff)
- [ ] ms-python.debugpy (debugger)
- [ ] ms-toolsai.jupyter (Jupyter notebooks)
- [ ] ms-azuretools.vscode-docker (Docker support)
- [ ] github.copilot (GitHub Copilot)
- [ ] github.copilot-chat (Copilot Chat)
- [O lista otras extensiones específicas]

## Archivos a Generar

Por favor, genera los siguientes 4 archivos completos y listos para usar:

1. **requirements.txt** - Con las dependencias básicas según el tipo de proyecto
2. **Dockerfile** - Optimizado para Python con uv, usuario no-root
3. **docker-compose.yml** - Con volúmenes bidireccionales y command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configurado con:
   - Uso del docker-compose.yml
   - Creación automática de venv con uv
   - Instalación de dependencias en postCreateCommand
   - Forward de puertos necesarios
   - Extensiones de VS Code configuradas

## Especificaciones Adicionales

**Caché de paquetes:** Usar volumen nombrado para cachear paquetes de uv
**Entorno virtual:** Crear .venv con uv en postCreateCommand
**Instalación de uv:** Debe instalarse en el Dockerfile

## Instrucciones Finales

- Todos los archivos deben tener comentarios explicativos en español
- Incluye instrucciones de uso al final
- El entorno debe quedar listo para desarrollo inmediato después de abrir en VS Code
- Estructura esperada:
  ```
  [Nombre-Proyecto]/
  ├── Dockerfile
  ├── docker-compose.yml
  ├── requirements.txt
  ├── .devcontainer/
  │   └── devcontainer.json
  ├── .gitignore
  └── src/
      └── [archivos de código]
  ```

¿Puedes generar los 4 archivos completos con esta configuración?
```

---

## 🎯 Ejemplo de Uso Completo:

### Caso 1: API FastAPI con Base de Datos

```
Necesito crear una configuración de Dev Container completa para un proyecto Python desde cero.

## Información del Proyecto

**Nombre del proyecto:** TaskManager API
**Lenguaje:** Python 3.11
**Gestor de paquetes:** uv (https://github.com/astral-sh/uv)
**Tipo de proyecto:** API REST para gestión de tareas con autenticación JWT

## Requisitos Técnicos

**Framework principal:** FastAPI
**Base de datos:** PostgreSQL
**Otros servicios:** Redis para caché

**Dependencias principales que necesito:**
- FastAPI para la API
- SQLAlchemy para ORM
- Alembic para migraciones
- Pydantic para validación
- python-jose para JWT
- passlib para hashing de passwords
- Redis para caché
- pytest para testing

**Variables de entorno necesarias:**
- DATABASE_URL=postgresql://user:pass@localhost:5432/taskdb
- REDIS_URL=redis://localhost:6379
- SECRET_KEY=your-secret-key-here
- DEBUG=True

## Configuración del Entorno

**Puerto principal:** 8000 (FastAPI)
**Puertos adicionales:** 5432 (PostgreSQL), 6379 (Redis)

**Usuario en container:** vscode (UID 1000)
**Directorio de trabajo:** /workspace

## Herramientas de Desarrollo

**Formateo automático al guardar:** Sí con Black
**Linting:** Ruff
**Type checking:** mypy
**Testing:** pytest

**¿Necesitas debugger configurado?** Sí
**¿Necesitas Jupyter notebooks?** No

## Extensiones VS Code Requeridas

**Obligatorias:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Adicionales que necesito:**
- [x] ms-python.black-formatter
- [x] charliermarsh.ruff
- [x] ms-python.debugpy
- [x] ms-azuretools.vscode-docker
- [x] github.copilot
- [x] github.copilot-chat
- [x] mtxr.sqltools (para PostgreSQL)
- [x] mtxr.sqltools-driver-pg

## Archivos a Generar

Por favor, genera los siguientes 4 archivos completos y listos para usar:

1. **requirements.txt** - Con las dependencias básicas según el tipo de proyecto
2. **Dockerfile** - Optimizado para Python con uv, usuario no-root
3. **docker-compose.yml** - Con volúmenes bidireccionales y command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configurado con:
   - Uso del docker-compose.yml
   - Creación automática de venv con uv
   - Instalación de dependencias en postCreateCommand
   - Forward de puertos necesarios
   - Extensiones de VS Code configuradas

## Especificaciones Adicionales

**Caché de paquetes:** Usar volumen nombrado para cachear paquetes de uv
**Entorno virtual:** Crear .venv con uv en postCreateCommand
**Instalación de uv:** Debe instalarse en el Dockerfile

## Instrucciones Finales

- Todos los archivos deben tener comentarios explicativos en español
- Incluye instrucciones de uso al final
- El entorno debe quedar listo para desarrollo inmediato después de abrir en VS Code

¿Puedes generar los 4 archivos completos con esta configuración?
```

---

### Caso 2: Proyecto de Data Science

```
Necesito crear una configuración de Dev Container completa para un proyecto Python desde cero.

## Información del Proyecto

**Nombre del proyecto:** ML Pipeline
**Lenguaje:** Python 3.11
**Gestor de paquetes:** uv (https://github.com/astral-sh/uv)
**Tipo de proyecto:** Pipeline de Machine Learning para análisis predictivo

## Requisitos Técnicos

**Framework principal:** Ninguno (data science)
**Base de datos:** Ninguna
**Otros servicios:** Ninguno

**Dependencias principales que necesito:**
- pandas para análisis de datos
- numpy para computación numérica
- scikit-learn para machine learning
- matplotlib y seaborn para visualización
- jupyter para notebooks
- pytest para testing

**Variables de entorno necesarias:**
- Ninguna por ahora

## Configuración del Entorno

**Puerto principal:** 8888 (Jupyter)
**Puertos adicionales:** Ninguno

**Usuario en container:** vscode (UID 1000)
**Directorio de trabajo:** /workspace

## Herramientas de Desarrollo

**Formateo automático al guardar:** Sí con Black
**Linting:** Ruff
**Type checking:** mypy
**Testing:** pytest

**¿Necesitas debugger configurado?** Sí
**¿Necesitas Jupyter notebooks?** Sí

## Extensiones VS Code Requeridas

**Obligatorias:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Adicionales que necesito:**
- [x] ms-python.black-formatter
- [x] ms-python.debugpy
- [x] ms-toolsai.jupyter
- [x] github.copilot
- [x] github.copilot-chat

## Archivos a Generar

Por favor, genera los siguientes 4 archivos completos y listos para usar:

1. **requirements.txt** - Con las dependencias básicas según el tipo de proyecto
2. **Dockerfile** - Optimizado para Python con uv, usuario no-root
3. **docker-compose.yml** - Con volúmenes bidireccionales y command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configurado con:
   - Uso del docker-compose.yml
   - Creación automática de venv con uv
   - Instalación de dependencias en postCreateCommand
   - Forward de puertos necesarios
   - Extensiones de VS Code configuradas

## Especificaciones Adicionales

**Caché de paquetes:** Usar volumen nombrado para cachear paquetes de uv
**Entorno virtual:** Crear .venv con uv en postCreateCommand
**Instalación de uv:** Debe instalarse en el Dockerfile

## Instrucciones Finales

- Todos los archivos deben tener comentarios explicativos en español
- Incluye instrucciones de uso al final
- El entorno debe quedar listo para desarrollo inmediato después de abrir en VS Code

¿Puedes generar los 4 archivos completos con esta configuración?
```

---

## 💡 Tips de Uso

### 1. **Copia el prompt base** (está en el primer bloque)

### 2. **Llena solo las secciones entre [corchetes]**
```
[Nombre del proyecto] → BookGenerator
[Python 3.11] → Ya está, déjalo así
[FastAPI / Django / Flask] → FastAPI
```

### 3. **Borra lo que no necesites**
```
**Otros servicios:** [Redis / RabbitMQ / Ninguno]
                      ↓
**Otros servicios:** Ninguno
```

### 4. **Agrega dependencias específicas**
```
**Dependencias principales que necesito:**
- WeasyPrint para generar PDFs
- Jinja2 para templates
- Pillow para procesamiento de imágenes
```

### 5. **Marca las extensiones que quieras**
```
- [ ] ms-python.black-formatter
      ↓
- [x] ms-python.black-formatter  (marca con x)
```

---

## 🚀 Para tu Proyecto Actual (GenTales)

Aquí tienes el prompt pre-llenado para el Book Generator:

```
Necesito crear una configuración de Dev Container completa para un proyecto Python desde cero.

## Información del Proyecto

**Nombre del proyecto:** GenTales Book Generator
**Lenguaje:** Python 3.11
**Gestor de paquetes:** uv (https://github.com/astral-sh/uv)
**Tipo de proyecto:** API REST para generación de libros ilustrados en PDF/EPUB a partir de JSON

## Requisitos Técnicos

**Framework principal:** FastAPI
**Base de datos:** Ninguna (sistema stateless)
**Otros servicios:** Ninguno

**Dependencias principales que necesito:**
- FastAPI para la API REST
- Uvicorn para el servidor ASGI
- Pydantic para validación de datos
- Jinja2 para templates HTML
- WeasyPrint para generación de PDFs (HTML → PDF)
- ebooklib para generación de EPUB
- Pillow para procesamiento de imágenes
- pytest para testing
- httpx para tests de API

**Variables de entorno necesarias:**
- DEBUG=True
- OUTPUT_DIR=/workspace/output
- ASSETS_DIR=/workspace/assets
- FONTS_DIR=/workspace/fonts

**Dependencias del sistema (para WeasyPrint):**
- libcairo2
- libpango-1.0-0
- libpangocairo-1.0-0
- libgdk-pixbuf2.0-0
- libffi-dev
- shared-mime-info

## Configuración del Entorno

**Puerto principal:** 8057 (FastAPI)
**Puertos adicionales:** Ninguno

**Usuario en container:** vscode (UID 1000)
**Directorio de trabajo:** /workspace

## Herramientas de Desarrollo

**Formateo automático al guardar:** Sí con Black
**Linting:** Ruff
**Type checking:** mypy
**Testing:** pytest con coverage

**¿Necesitas debugger configurado?** Sí
**¿Necesitas Jupyter notebooks?** No

## Extensiones VS Code Requeridas

**Obligatorias:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Adicionales que necesito:**
- [x] ms-python.black-formatter
- [x] charliermarsh.ruff
- [x] ms-python.debugpy
- [x] ms-azuretools.vscode-docker
- [x] github.copilot
- [x] github.copilot-chat
- [x] redhat.vscode-yaml (para configs)
- [x] yzhang.markdown-all-in-one (para docs)

## Archivos a Generar

Por favor, genera los siguientes 4 archivos completos y listos para usar:

1. **requirements.txt** - Con las dependencias básicas según el tipo de proyecto
2. **Dockerfile** - Optimizado para Python con uv, usuario no-root, IMPORTANTE: debe instalar las dependencias del sistema para WeasyPrint
3. **docker-compose.yml** - Con volúmenes bidireccionales y command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configurado con:
   - Uso del docker-compose.yml
   - Creación automática de venv con uv
   - Instalación de dependencias en postCreateCommand
   - Forward del puerto 8057
   - Extensiones de VS Code configuradas

## Especificaciones Adicionales

**Caché de paquetes:** Usar volumen nombrado para cachear paquetes de uv
**Entorno virtual:** Crear .venv con uv en postCreateCommand
**Instalación de uv:** Debe instalarse en el Dockerfile

**Estructura del proyecto:**
```
book-generator/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .devcontainer/
│   └── devcontainer.json
├── .gitignore
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── utils/
├── templates/
│   ├── base.html
│   ├── pages/
│   └── styles/
├── tests/
├── assets/
├── fonts/
└── output/
```

## Instrucciones Finales

- Todos los archivos deben tener comentarios explicativos en español
- Incluye instrucciones de uso al final
- El entorno debe quedar listo para desarrollo inmediato después de abrir en VS Code
- IMPORTANTE: El Dockerfile debe instalar las dependencias del sistema de WeasyPrint

¿Puedes generar los 4 archivos completos con esta configuración?
```

---

## 📝 Notas Finales

**Guarda este prompt template en:**
```
docs/templates/DEVCONTAINER_PROMPT.md
```

**Para usarlo:**
1. Copia el prompt base
2. Llena los campos entre [corchetes]
3. Pégalo en Claude/ChatGPT/LLM
4. Obtienes tus 4 archivos listos

**Ventajas:**
- ✅ Consistencia entre proyectos
- ✅ No olvidas configuraciones importantes
- ✅ Setup rápido (5 minutos)
- ✅ Documentado automáticamente

---

¿Quieres que ajuste algo del prompt template o te genero los archivos para tu proyecto GenTales ahora mismo?
