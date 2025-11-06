# GitHub Copilot Instructions

## Project Context
- **Type**: [API REST/Web App/CLI Tool/Library/Microservice]
- **Stack**: [Python 3.x, FastAPI, PostgreSQL, etc.]
- **Architecture**: [Brief description: Monolithic/Microservices/Serverless/Layered]
- **Package Manager**: [uv/pip/poetry/pipenv]
- **Primary Language**: [Python/TypeScript/Go/etc.]

## Complete Documentation
> This file is the **operational reference** for AI assistants. For strategic context, see:
> - **Objective:** `docs/agent/00_OBJECTIVE.md` - What the system does and why
> - **Architecture:** `docs/agent/01_ARCHITECTURE.md` - System structure and components
> - **Roadmap:** `docs/agent/02_ROADMAP.md` - Development phases and priorities
> - **Conventions:** `docs/agent/03_CONVENTIONS.md` - Technical specifications and calculations
> - **Changelog:** `docs/agent/04_CHANGELOG.md` - **⚠️ Update after significant changes**
> - **Services:** `docs/services/*.md` - Service-specific usage tutorials

---

## Code Standards

### Language-Specific Standards

#### Python
- **Version**: [3.11+/3.12+]
- **Type Hints**: Required in all function signatures and class attributes
- **Style Guide**: PEP 8 compliance
- **Line Length**: [88/120] characters (enforced by formatter)
- **Docstrings**: [Google/NumPy/Sphinx] style
- **String Quotes**: [Single/Double] quotes for strings, """ for docstrings
- **Imports**: Absolute imports preferred, relative only within same package

#### [Additional Language - TypeScript/Go/etc.]
- [Language-specific standards if applicable]

### Code Quality Rules

#### Function Design
- Maximum function length: [50/75/100] lines
- Maximum function parameters: [5/7] parameters (use dataclasses/models for more)
- Maximum cyclomatic complexity: [10/15]
- Single Responsibility Principle: One function = one clear purpose

#### Class Design
- Maximum class length: [300/500] lines
- One class per file (except small utility/exception classes)
- Prefer composition over inheritance
- Use dataclasses for data containers
- Use ABC for interfaces/protocols

#### Error Handling
- ✅ Use specific exceptions (ValueError, TypeError, etc.)
- ✅ Custom exceptions inherit from appropriate base
- ✅ Always provide meaningful error messages
- ❌ Never use bare `except:` clauses
- ❌ Don't silence exceptions without logging

#### Configuration Management
- ✅ Environment variables via [pydantic-settings/python-dotenv]
- ✅ Configuration classes/models for validation
- ✅ Separate configs per environment (dev/staging/prod)
- ❌ No hardcoded credentials or secrets
- ❌ No magic numbers (use named constants)

---

## Project Structure & File Organization

### WHERE to Work

#### Allowed Directories
```
project/
├── src/[app/core]/          # ✅ Main application code HERE
├── tests/                    # ✅ All test files HERE
├── docs/                     # ✅ Documentation updates HERE
├── scripts/                  # ✅ Utility scripts HERE (optional)
└── [migrations/alembic]/     # ✅ Database migrations HERE (if applicable)
```

#### Restricted/Protected Directories
- ❌ **NEVER** create files in project root (except config files)
- ❌ **NEVER** modify files in `.git/`
- ❌ **NEVER** modify files in `[venv/.venv/node_modules]`
- ❌ **NEVER** modify generated files (e.g., `*_pb2.py`, compiled binaries)

#### Files to Ignore
```
# Never read or modify these patterns:
**/__pycache__/
**/*.pyc
**/*.pyo
**/*.pyd
**/.pytest_cache/
**/.mypy_cache/
**/.ruff_cache/
**/htmlcov/
**/.coverage
**/*.log
**/.env*
!.env.example
**/.DS_Store
**/Thumbs.db
```

### Naming Conventions

#### Files & Directories
- Python modules: `snake_case.py`
- Python packages: `snake_case/`
- Test files: `test_*.py` or `*_test.py`
- Config files: `[lowercase-with-dashes.yaml]`

#### Code Elements
- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`
- Protected attributes: `_single_underscore`
- Really private: `__double_underscore` (name mangling)

#### Database/API
- Database tables: `[snake_case/lowercase]`
- API endpoints: `[kebab-case/snake_case]`
- Environment variables: `UPPER_SNAKE_CASE`

---

## Dependency Management

### Import Order (strictly enforced)
```python
# 1. Standard library imports
import os
import sys
from typing import Optional

# 2. Third-party imports
import pandas as pd
from fastapi import FastAPI

# 3. Local application imports
from src.core.models import User
from src.utils.helpers import format_date
```

### Package Installation Rules
- ✅ Use `[uv add/pip install/poetry add]` [package-name]
- ✅ Pin major versions in production: `fastapi==0.104.*`
- ✅ Update `requirements.txt` or `pyproject.toml` immediately
- ❌ Never commit `requirements.txt` and `poetry.lock` conflicts
- ❌ Don't install packages globally (use virtual environments)

---

## Testing Standards

### Test Organization
```
tests/
├── unit/           # Pure logic tests, no external dependencies
├── integration/    # Tests with database, APIs, etc.
├── e2e/           # End-to-end workflow tests
└── fixtures/      # Shared test data and fixtures
```

### Testing Requirements
- **Coverage Minimum**: [80/90]%
- **Framework**: [pytest/unittest]
- **Fixtures**: Use pytest fixtures for reusable test data
- **Mocking**: Use [unittest.mock/pytest-mock] for external dependencies
- **Assertions**: Prefer specific assertions (`assert x == 5` over `assert x`)

### Test Naming
```python
def test_[function_name]_[scenario]_[expected_result]:
    """
    Example: test_calculate_discount_with_valid_coupon_returns_reduced_price
    """
    pass
```

### Test Patterns
```python
# ✅ GOOD: Arrange-Act-Assert pattern
def test_user_creation_with_valid_data_creates_user():
    # Arrange
    user_data = {"name": "John", "email": "john@example.com"}
    
    # Act
    user = create_user(user_data)
    
    # Assert
    assert user.name == "John"
    assert user.email == "john@example.com"
```

---

## Code Patterns & Examples

### Preferred Patterns

#### API Endpoint Structure (FastAPI example)
```python
@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> UserResponse:
    """
    Create a new user account.
    
    Args:
        user_data: User creation data
        db: Database session
        current_user: Authenticated user making the request
        
    Returns:
        Created user data
        
    Raises:
        HTTPException: If email already exists
    """
    # Implementation
    pass
```

#### Service Layer Pattern
```python
class UserService:
    """Business logic for user operations."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)
    
    async def create_user(self, user_data: UserCreate) -> User:
        # Validation
        if await self.repository.get_by_email(user_data.email):
            raise ValueError("Email already exists")
        
        # Business logic
        user = User(**user_data.dict())
        return await self.repository.create(user)
```

#### Error Response Pattern
```python
# ✅ GOOD: Structured error responses
class ErrorResponse(BaseModel):
    error_code: str
    message: str
    details: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# Usage
raise HTTPException(
    status_code=400,
    detail=ErrorResponse(
        error_code="INVALID_EMAIL",
        message="The provided email is not valid",
        details={"email": user_email}
    ).dict()
)
```

---

## Anti-patterns to Avoid

### Code Smells
- ❌ **God Classes**: Classes > [300/500] lines doing too many things
- ❌ **Long Methods**: Functions > [50/75] lines - break them down
- ❌ **Deep Nesting**: Indentation > 3 levels - extract functions
- ❌ **Primitive Obsession**: Using primitives instead of domain objects
- ❌ **Magic Numbers**: Hardcoded values without named constants

### Common Mistakes
- ❌ **Mutable Default Arguments**: `def func(items=[]):`  → Use `None`
- ❌ **Catching All Exceptions**: `except Exception:` without re-raising
- ❌ **Print Debugging**: `print()` statements → Use proper logging
- ❌ **String Concatenation in Loops**: Use `"".join()` or f-strings
- ❌ **Blocking Operations in Async**: `time.sleep()` in async → Use `asyncio.sleep()`

### Database Anti-patterns
- ❌ **N+1 Queries**: Load relations eagerly or use `selectinload`
- ❌ **Missing Indexes**: Add indexes for frequently queried columns
- ❌ **Raw SQL Without Parameters**: Use parameterized queries always
- ❌ **Committing in Loops**: Batch operations instead

---

## Documentation Standards

### Code Documentation
- All public functions/classes **MUST** have docstrings
- Include type hints (don't duplicate in docstring)
- Document exceptions that can be raised
- Include usage examples for complex functions

### Service Documentation (docs/services/)
Each service MUST have a tutorial explaining:
1. **Purpose**: What problem it solves
2. **Prerequisites**: Required setup/configuration
3. **Step-by-Step Guide**: Code examples with explanations
4. **Common Use Cases**: Real-world scenarios
5. **Troubleshooting**: Common errors and solutions
6. **API Reference**: Available methods and parameters

Template: `docs/services/README.md`

---

## Useful Commands

### Development Workflow
```bash
# Setup
[uv venv / python -m venv .venv]  # Create virtual environment
[uv pip install / pip install -r requirements.txt]  # Install dependencies

# Running the application
[uv run python -m src.main / python -m src.main]
[uvicorn src.main:app --reload]  # For FastAPI apps

# Development server
[npm run dev / yarn dev]  # If frontend included
```

### Testing
```bash
# Run all tests
[uv run pytest / pytest]

# Run with coverage
pytest --cov=src --cov-report=html --cov-report=term

# Run specific test file
pytest tests/unit/test_users.py

# Run tests matching pattern
pytest -k "test_user"

# Run with verbose output
pytest -v

# Run only failed tests
pytest --lf
```

### Code Quality
```bash
# Type checking
[mypy src / pyright src]

# Linting
[ruff check src / flake8 src]

# Formatting
[ruff format src / black src]

# Import sorting
[ruff check --select I --fix / isort src]

# Security scan
bandit -r src/

# All checks at once
[your custom command: make lint / pre-commit run --all-files]
```

### Database (if applicable)
```bash
# Create migration
[alembic revision --autogenerate -m "description"]

# Run migrations
[alembic upgrade head]

# Rollback migration
[alembic downgrade -1]

# Database shell
[psql -U user -d database / mysql -u user -p database]
```

### Docker (if applicable)
```bash
# Build image
docker build -t [project-name]:[tag] .

# Run container
docker run -p [8000:8000] [project-name]:[tag]

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down
```

---

## Before Committing (Checklist)

### Required Checks
- [ ] All tests pass: `pytest`
- [ ] Type checking passes: `[mypy/pyright] src`
- [ ] Linting passes: `[ruff check/flake8] src`
- [ ] Formatting applied: `[ruff format/black] src`
- [ ] Coverage meets minimum: `pytest --cov=src --cov-report=term`
- [ ] No debug code (print, console.log, debugger)
- [ ] No commented-out code blocks

### Documentation Checks
- [ ] Updated `docs/agent/04_CHANGELOG.md` if significant changes
- [ ] Updated relevant service documentation if API changed
- [ ] Docstrings added for new public functions/classes
- [ ] README.md updated if setup process changed

### Security Checks
- [ ] No secrets or credentials in code
- [ ] No sensitive data in logs
- [ ] Environment variables used for configuration
- [ ] Dependencies have no known vulnerabilities

### Git Hygiene
- [ ] Commit message follows convention: `[type]: [description]`
  - Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
- [ ] Commits are atomic (one logical change per commit)
- [ ] Branch name follows pattern: `[feature/fix/refactor]/[description]`

---

## Integration & Deployment

### CI/CD (if applicable)
- Pipeline configuration: `[.github/workflows / .gitlab-ci.yml / Jenkinsfile]`
- Required checks: [tests, linting, type-checking, security scan]
- Deployment branches: `[main/master for prod, develop for staging]`

### Environment Variables
```bash
# Required variables (document in .env.example)
DATABASE_URL=[required for database connection]
SECRET_KEY=[required for security]
API_KEY_[SERVICE]=[if external APIs used]

# Optional variables
LOG_LEVEL=[INFO/DEBUG]
ENVIRONMENT=[development/staging/production]
```

### Pre-commit Hooks (if configured)
```yaml
# .pre-commit-config.yaml exists in project
# Runs automatically before commit:
# - Formatting checks
# - Linting
# - Type checking
# - Test suite (optional)
```

---

## Additional Context

### Common Tasks & Recipes

#### Adding a New Endpoint
1. Define Pydantic models in `src/models/schemas.py`
2. Create service logic in `src/services/`
3. Add endpoint in `src/api/routes/`
4. Write tests in `tests/integration/api/`
5. Update API documentation
6. Update CHANGELOG.md

#### Adding a New Service
1. Create service file in `src/services/[service_name].py`
2. Define interface/protocol if needed
3. Write unit tests in `tests/unit/services/`
4. Create tutorial in `docs/services/[service_name].md`
5. Register in dependency injection (if applicable)

---

**Last Updated**: [Date]
**Maintainer**: [Team/Person]
**Questions**: [Contact method or link to discussions]
