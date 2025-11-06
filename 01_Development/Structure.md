proyecto/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile (si es necesario)
│
├── .github/
│   └── copilot-instructions.md  # Instrucciones específicas para Copilot
│
├── docs/                         # Renombrado de "Doc"
│   ├── agent/                   
│   │   ├── 00_OBJECTIVE.md      # Objetivo del proyecto
│   │   ├── 01_ARCHITECTURE.md   # Arquitectura y decisiones
│   │   ├── 02_ROADMAP.md        # Roadmap de desarrollo
│   │   ├── 03_CONVENTIONS.md    # Convenciones y estándares
│   │   └── 04_CHANGELOG.md      # Log de cambios importantes
│   │
│   └── api/                     # Documentación técnica
│       └── README.md
│
├── src/
│   ├── __init__.py
│   ├── api/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml              # Configuración moderna de Python
└── README.md