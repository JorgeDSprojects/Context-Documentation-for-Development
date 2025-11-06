# GitHub Copilot Instructions

## Project Context
- **Type**: [API REST/Web App/CLI Tool]
- **Stack**: Python 3.x, FastAPI, etc.
- **Architecture**: [Descripción breve]


## Complete Documentation:
> - **Objective:** `docs/agent/00_OBJECTIVE.md` - What the system does
> - **Architecture:** `docs/agent/01_ARCHITECTURE.md` - System structure and components
> - **Conventions:** `docs/agent/03_CONVENTIONS.md` - Technical specifications (margins, bleed, multi-language)
> - **Changelog:** `docs/agent/04_CHANGELOG.md` - **Update after significant changes**
> - **Services:** `docs/services/*.md` - Step-by-step service usage tutorials

## Documentation Standards

### Service Documentation (docs/services/)
Each service MUST have a tutorial file explaining:
1. **What it does** - Brief description
2. **Input requirements** - What data/parameters needed
3. **Step-by-step usage** - Concrete examples
4. **Output explanation** - What you get back
5. **Common errors** - Troubleshooting

See: `docs/services/README.md` for template
---

## Code Standards

### Python
- Use type hints in all functions
- Follow PEP 8
- Maximum line length: 88 (Black formatter)
- Docstrings: Google style

### Structure Rules
1. **NEVER** create files outside of `src/` or `tests/`
2. **ALWAYS** update `docs/agent/04_CHANGELOG.md` after significant changes
3. Keep functions under 50 lines
4. One class per file (except small utility classes)

### Testing
- Write tests for every new function
- Minimum coverage: 80%
- Use pytest fixtures

### Import Order
1. Standard library
2. Third-party packages
3. Local imports

## Anti-patterns to Avoid
- ❌ God classes (>300 lines)
- ❌ Nested functions >2 levels
- ❌ Hardcoded values (use config)
- ❌ Print statements (use logging)

## Before Committing
- [ ] Tests pass
- [ ] Type checking passes (mypy)
- [ ] Linting passes (ruff/flake8)
- [ ] CHANGELOG updated
```
