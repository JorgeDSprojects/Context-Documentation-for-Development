# 🐳 Prompt Template: Dev Container Generator

**Copy this prompt, fill in the fields between [brackets], and use it with Claude or any LLM**

---

## 📋 Prompt to Copy and Fill:

```
I need to create a complete Dev Container configuration for a Python project from scratch.

## Project Information

**Project name:** [Project name]
**Language:** Python [Version, e.g.: 3.11]
**Package manager:** uv (https://github.com/astral-sh/uv)
**Project type:** [Briefly describe: REST API, Web App, CLI Tool, Data Science, etc.]

## Technical Requirements

**Main framework:** [FastAPI / Django / Flask / Other]
**Database:** [PostgreSQL / MySQL / MongoDB / SQLite / None]
**Other services:** [Redis / RabbitMQ / None]

**Main dependencies I need:**
- [Example: FastAPI for the API]
- [Example: SQLAlchemy for ORM]
- [Example: Pydantic for validation]
- [Add more as needed]

**Required environment variables:**
- [Example: DATABASE_URL]
- [Example: SECRET_KEY]
- [Example: DEBUG=True]
- [Or indicate: None for now]

## Environment Configuration

**Main port:** [8000 / 3000 / 5000 / other]
**Additional ports:** [If you need more ports]

**Container user:** vscode (UID 1000)
**Working directory:** /workspace

## Development Tools

**Auto-format on save:** [Yes with Black / Yes with Ruff / No]
**Linting:** [Pylint / Ruff / Flake8 / None]
**Type checking:** [mypy / pyright / None]
**Testing:** [pytest / unittest / None]

**Need debugger configured?** [Yes / No]
**Need Jupyter notebooks?** [Yes / No]

## Required VS Code Extensions

**Mandatory:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Additional ones I need:**
- [Check the ones you want]
- [ ] ms-python.black-formatter (Black formatting)
- [ ] charliermarsh.ruff (linting and formatting with Ruff)
- [ ] ms-python.debugpy (debugger)
- [ ] ms-toolsai.jupyter (Jupyter notebooks)
- [ ] ms-azuretools.vscode-docker (Docker support)
- [ ] github.copilot (GitHub Copilot)
- [ ] github.copilot-chat (Copilot Chat)
- [Or list other specific extensions]

## Files to Generate

Please generate the following 4 complete and ready-to-use files:

1. **requirements.txt** - With basic dependencies according to project type
2. **Dockerfile** - Optimized for Python with uv, non-root user
3. **docker-compose.yml** - With bidirectional volumes and command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configured with:
   - Use of docker-compose.yml
   - Automatic venv creation with uv
   - Dependency installation in postCreateCommand
   - Forward of necessary ports
   - Configured VS Code extensions

## Additional Specifications

**Package cache:** Use named volume to cache uv packages
**Virtual environment:** Create .venv with uv in postCreateCommand
**uv installation:** Must be installed in the Dockerfile

## Final Instructions

- All files should have explanatory comments in English
- Include usage instructions at the end
- The environment should be ready for immediate development after opening in VS Code
- Expected structure:
  ```
  [Project-Name]/
  ├── Dockerfile
  ├── docker-compose.yml
  ├── requirements.txt
  ├── .devcontainer/
  │   └── devcontainer.json
  ├── .gitignore
  └── src/
      └── [code files]
  ```

Can you generate the 4 complete files with this configuration?
```

---

## 🎯 Complete Usage Examples:

### Case 1: FastAPI API with Database

```
I need to create a complete Dev Container configuration for a Python project from scratch.

## Project Information

**Project name:** TaskManager API
**Language:** Python 3.11
**Package manager:** uv (https://github.com/astral-sh/uv)
**Project type:** REST API for task management with JWT authentication

## Technical Requirements

**Main framework:** FastAPI
**Database:** PostgreSQL
**Other services:** Redis for caching

**Main dependencies I need:**
- FastAPI for the API
- SQLAlchemy for ORM
- Alembic for migrations
- Pydantic for validation
- python-jose for JWT
- passlib for password hashing
- Redis for caching
- pytest for testing

**Required environment variables:**
- DATABASE_URL=postgresql://user:pass@localhost:5432/taskdb
- REDIS_URL=redis://localhost:6379
- SECRET_KEY=your-secret-key-here
- DEBUG=True

## Environment Configuration

**Main port:** 8000 (FastAPI)
**Additional ports:** 5432 (PostgreSQL), 6379 (Redis)

**Container user:** vscode (UID 1000)
**Working directory:** /workspace

## Development Tools

**Auto-format on save:** Yes with Black
**Linting:** Ruff
**Type checking:** mypy
**Testing:** pytest

**Need debugger configured?** Yes
**Need Jupyter notebooks?** No

## Required VS Code Extensions

**Mandatory:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Additional ones I need:**
- [x] ms-python.black-formatter
- [x] charliermarsh.ruff
- [x] ms-python.debugpy
- [x] ms-azuretools.vscode-docker
- [x] github.copilot
- [x] github.copilot-chat
- [x] mtxr.sqltools (for PostgreSQL)
- [x] mtxr.sqltools-driver-pg

## Files to Generate

Please generate the following 4 complete and ready-to-use files:

1. **requirements.txt** - With basic dependencies according to project type
2. **Dockerfile** - Optimized for Python with uv, non-root user
3. **docker-compose.yml** - With bidirectional volumes and command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configured with:
   - Use of docker-compose.yml
   - Automatic venv creation with uv
   - Dependency installation in postCreateCommand
   - Forward of necessary ports
   - Configured VS Code extensions

## Additional Specifications

**Package cache:** Use named volume to cache uv packages
**Virtual environment:** Create .venv with uv in postCreateCommand
**uv installation:** Must be installed in the Dockerfile

## Final Instructions

- All files should have explanatory comments in English
- Include usage instructions at the end
- The environment should be ready for immediate development after opening in VS Code

Can you generate the 4 complete files with this configuration?
```

---

### Case 2: Data Science Project

```
I need to create a complete Dev Container configuration for a Python project from scratch.

## Project Information

**Project name:** ML Pipeline
**Language:** Python 3.11
**Package manager:** uv (https://github.com/astral-sh/uv)
**Project type:** Machine Learning pipeline for predictive analysis

## Technical Requirements

**Main framework:** None (data science)
**Database:** None
**Other services:** None

**Main dependencies I need:**
- pandas for data analysis
- numpy for numerical computing
- scikit-learn for machine learning
- matplotlib and seaborn for visualization
- jupyter for notebooks
- pytest for testing

**Required environment variables:**
- None for now

## Environment Configuration

**Main port:** 8888 (Jupyter)
**Additional ports:** None

**Container user:** vscode (UID 1000)
**Working directory:** /workspace

## Development Tools

**Auto-format on save:** Yes with Black
**Linting:** Ruff
**Type checking:** mypy
**Testing:** pytest

**Need debugger configured?** Yes
**Need Jupyter notebooks?** Yes

## Required VS Code Extensions

**Mandatory:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Additional ones I need:**
- [x] ms-python.black-formatter
- [x] ms-python.debugpy
- [x] ms-toolsai.jupyter
- [x] github.copilot
- [x] github.copilot-chat

## Files to Generate

Please generate the following 4 complete and ready-to-use files:

1. **requirements.txt** - With basic dependencies according to project type
2. **Dockerfile** - Optimized for Python with uv, non-root user
3. **docker-compose.yml** - With bidirectional volumes and command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configured with:
   - Use of docker-compose.yml
   - Automatic venv creation with uv
   - Dependency installation in postCreateCommand
   - Forward of necessary ports
   - Configured VS Code extensions

## Additional Specifications

**Package cache:** Use named volume to cache uv packages
**Virtual environment:** Create .venv with uv in postCreateCommand
**uv installation:** Must be installed in the Dockerfile

## Final Instructions

- All files should have explanatory comments in English
- Include usage instructions at the end
- The environment should be ready for immediate development after opening in VS Code

Can you generate the 4 complete files with this configuration?
```

---

## 💡 Usage Tips

### 1. **Copy the base prompt** (it's in the first block)

### 2. **Fill only the sections between [brackets]**
```
[Project name] → BookGenerator
[Python 3.11] → Already there, leave it as is
[FastAPI / Django / Flask] → FastAPI
```

### 3. **Delete what you don't need**
```
**Other services:** [Redis / RabbitMQ / None]
                      ↓
**Other services:** None
```

### 4. **Add specific dependencies**
```
**Main dependencies I need:**
- WeasyPrint for PDF generation
- Jinja2 for templates
- Pillow for image processing
```

### 5. **Check the extensions you want**
```
- [ ] ms-python.black-formatter
      ↓
- [x] ms-python.black-formatter  (mark with x)
```

---

## 🚀 For Your Current Project (GenTales)

Here's the pre-filled prompt for the Book Generator:

```
I need to create a complete Dev Container configuration for a Python project from scratch.

## Project Information

**Project name:** GenTales Book Generator
**Language:** Python 3.11
**Package manager:** uv (https://github.com/astral-sh/uv)
**Project type:** REST API for generating illustrated books in PDF/EPUB from JSON

## Technical Requirements

**Main framework:** FastAPI
**Database:** None (stateless system)
**Other services:** None

**Main dependencies I need:**
- FastAPI for REST API
- Uvicorn for ASGI server
- Pydantic for data validation
- Jinja2 for HTML templates
- WeasyPrint for PDF generation (HTML → PDF)
- ebooklib for EPUB generation
- Pillow for image processing
- pytest for testing
- httpx for API tests

**Required environment variables:**
- DEBUG=True
- OUTPUT_DIR=/workspace/output
- ASSETS_DIR=/workspace/assets
- FONTS_DIR=/workspace/fonts

**System dependencies (for WeasyPrint):**
- libcairo2
- libpango-1.0-0
- libpangocairo-1.0-0
- libgdk-pixbuf2.0-0
- libffi-dev
- shared-mime-info

## Environment Configuration

**Main port:** 8057 (FastAPI)
**Additional ports:** None

**Container user:** vscode (UID 1000)
**Working directory:** /workspace

## Development Tools

**Auto-format on save:** Yes with Black
**Linting:** Ruff
**Type checking:** mypy
**Testing:** pytest with coverage

**Need debugger configured?** Yes
**Need Jupyter notebooks?** No

## Required VS Code Extensions

**Mandatory:**
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)

**Additional ones I need:**
- [x] ms-python.black-formatter
- [x] charliermarsh.ruff
- [x] ms-python.debugpy
- [x] ms-azuretools.vscode-docker
- [x] github.copilot
- [x] github.copilot-chat
- [x] redhat.vscode-yaml (for configs)
- [x] yzhang.markdown-all-in-one (for docs)

## Files to Generate

Please generate the following 4 complete and ready-to-use files:

1. **requirements.txt** - With basic dependencies according to project type
2. **Dockerfile** - Optimized for Python with uv, non-root user, IMPORTANT: must install system dependencies for WeasyPrint
3. **docker-compose.yml** - With bidirectional volumes and command: sleep infinity
4. **.devcontainer/devcontainer.json** - Configured with:
   - Use of docker-compose.yml
   - Automatic venv creation with uv
   - Dependency installation in postCreateCommand
   - Forward of port 8057
   - Configured VS Code extensions

## Additional Specifications

**Package cache:** Use named volume to cache uv packages
**Virtual environment:** Create .venv with uv in postCreateCommand
**uv installation:** Must be installed in the Dockerfile

**Project structure:**
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

## Final Instructions

- All files should have explanatory comments in English
- Include usage instructions at the end
- The environment should be ready for immediate development after opening in VS Code
- IMPORTANT: The Dockerfile must install WeasyPrint system dependencies

Can you generate the 4 complete files with this configuration?
```

---

## 📝 Final Notes

**Save this prompt template in:**
```
docs/templates/DEVCONTAINER_PROMPT.md
```

**To use it:**
1. Copy the base prompt
2. Fill in the fields between [brackets]
3. Paste it into Claude/ChatGPT/LLM
4. Get your 4 ready-to-use files

**Advantages:**
- ✅ Consistency across projects
- ✅ Don't forget important configurations
- ✅ Quick setup (5 minutes)
- ✅ Automatically documented

---

Want me to adjust anything in the prompt template or generate the files for your GenTales project right now?
