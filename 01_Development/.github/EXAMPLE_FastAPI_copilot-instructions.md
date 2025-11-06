# GitHub Copilot Instructions

## Project Context
- **Type**: API REST Microservice
- **Stack**: Python 3.11, FastAPI 0.104, PostgreSQL 15, Redis 7
- **Architecture**: Layered architecture with Clean Architecture principles (Domain-Driven Design)
- **Package Manager**: uv (ultra-fast Python package installer)
- **Primary Language**: Python 3.11

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
- **Version**: 3.11+
- **Type Hints**: Required in all function signatures and class attributes
- **Style Guide**: PEP 8 compliance
- **Line Length**: 88 characters (enforced by Black)
- **Docstrings**: Google style
- **String Quotes**: Double quotes for strings, """ for docstrings
- **Imports**: Absolute imports preferred, relative only within same package

### Code Quality Rules

#### Function Design
- Maximum function length: 50 lines
- Maximum function parameters: 5 parameters (use Pydantic models for more)
- Maximum cyclomatic complexity: 10
- Single Responsibility Principle: One function = one clear purpose

#### Class Design
- Maximum class length: 300 lines
- One class per file (except small utility/exception classes)
- Prefer composition over inheritance
- Use Pydantic models for data validation
- Use ABC for interfaces/protocols

#### Error Handling
- ✅ Use specific exceptions (ValueError, HTTPException, etc.)
- ✅ Custom exceptions inherit from BaseException in `src/core/exceptions.py`
- ✅ Always provide meaningful error messages with context
- ❌ Never use bare `except:` clauses
- ❌ Don't silence exceptions without logging

#### Configuration Management
- ✅ Environment variables via pydantic-settings
- ✅ Configuration class in `src/core/config.py`
- ✅ Separate configs per environment (.env.development, .env.production)
- ❌ No hardcoded credentials or secrets
- ❌ No magic numbers (use named constants in `src/core/constants.py`)

---

## Project Structure & File Organization

### WHERE to Work

#### Allowed Directories
```
user-api/
├── src/
│   ├── api/                # ✅ API routes and endpoints HERE
│   ├── core/               # ✅ Core configuration, exceptions, constants
│   ├── domain/             # ✅ Domain models and business logic
│   ├── services/           # ✅ Business logic services
│   ├── repositories/       # ✅ Data access layer
│   └── utils/              # ✅ Helper functions and utilities
├── tests/                  # ✅ All test files HERE
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/                   # ✅ Documentation updates HERE
├── scripts/                # ✅ Utility scripts HERE
└── alembic/                # ✅ Database migrations HERE
```

#### Restricted/Protected Directories
- ❌ **NEVER** create files in project root (except config files like .env.example)
- ❌ **NEVER** modify files in `.git/`
- ❌ **NEVER** modify files in `.venv/` or `__pycache__/`
- ❌ **NEVER** modify Alembic generated migration files directly (create new ones)

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
**/.env
**/.env.local
**/.env.production
!.env.example
**/.DS_Store
```

### Naming Conventions

#### Files & Directories
- Python modules: `snake_case.py` (e.g., `user_service.py`)
- Python packages: `snake_case/` (e.g., `repositories/`)
- Test files: `test_*.py` (e.g., `test_user_service.py`)
- Config files: `lowercase-with-dashes.yaml`

#### Code Elements
- Classes: `PascalCase` (e.g., `UserService`, `UserRepository`)
- Functions/methods: `snake_case` (e.g., `create_user`, `get_user_by_id`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)
- Private methods: `_leading_underscore` (e.g., `_validate_email`)
- Protected attributes: `_single_underscore`

#### Database/API
- Database tables: `snake_case` (e.g., `users`, `user_profiles`)
- API endpoints: `kebab-case` (e.g., `/api/v1/users`, `/api/v1/user-profiles`)
- Environment variables: `UPPER_SNAKE_CASE` (e.g., `DATABASE_URL`, `REDIS_HOST`)

---

## Dependency Management

### Import Order (strictly enforced by Ruff)
```python
# 1. Standard library imports
import os
from datetime import datetime
from typing import Optional, List

# 2. Third-party imports
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

# 3. Local application imports
from src.core.config import settings
from src.core.exceptions import UserNotFoundError
from src.domain.models import User
from src.repositories.user_repository import UserRepository
```

### Package Installation Rules
- ✅ Use `uv add [package-name]` for adding dependencies
- ✅ Use `uv add --dev [package-name]` for dev dependencies
- ✅ Pin major versions in production: `fastapi==0.104.*`
- ✅ Run `uv lock` after adding packages
- ❌ Never commit with outdated `uv.lock`
- ❌ Don't install packages globally (use virtual environments)

---

## Testing Standards

### Test Organization
```
tests/
├── unit/              # Pure logic tests, no external dependencies
│   ├── services/
│   ├── repositories/
│   └── utils/
├── integration/       # Tests with database, Redis, external APIs
│   ├── api/
│   └── repositories/
├── e2e/              # End-to-end user workflows
└── conftest.py       # Shared fixtures
```

### Testing Requirements
- **Coverage Minimum**: 80%
- **Framework**: pytest
- **Fixtures**: Use pytest fixtures in `conftest.py` for reusable test data
- **Mocking**: Use `pytest-mock` for external dependencies
- **Assertions**: Prefer specific assertions with clear messages

### Test Naming
```python
def test_[function_name]_[scenario]_[expected_result]:
    """
    Example: test_create_user_with_valid_data_returns_created_user
    """
    pass
```

### Test Patterns
```python
# ✅ GOOD: Arrange-Act-Assert pattern
def test_create_user_with_valid_data_returns_created_user():
    # Arrange
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="SecurePass123!"
    )
    user_service = UserService(db=mock_db)
    
    # Act
    created_user = user_service.create_user(user_data)
    
    # Assert
    assert created_user.email == "test@example.com"
    assert created_user.username == "testuser"
    assert created_user.id is not None
```

---

## Code Patterns & Examples

### Preferred Patterns

#### API Endpoint Structure (FastAPI)
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.dependencies import get_db, get_current_user
from src.domain.schemas import UserCreate, UserResponse
from src.services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create new user"
)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> UserResponse:
    """
    Create a new user account with the provided information.
    
    Args:
        user_data: User creation data including email, username, password
        db: Database session dependency
        current_user: Authenticated user making the request
        
    Returns:
        Created user data with generated ID
        
    Raises:
        HTTPException 400: If email or username already exists
        HTTPException 422: If validation fails
    """
    service = UserService(db)
    
    try:
        user = await service.create_user(user_data)
        return UserResponse.from_orm(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
```

#### Service Layer Pattern
```python
from typing import Optional
from sqlalchemy.orm import Session

from src.core.exceptions import UserNotFoundError, EmailAlreadyExistsError
from src.domain.models import User
from src.domain.schemas import UserCreate, UserUpdate
from src.repositories.user_repository import UserRepository
from src.utils.security import hash_password

class UserService:
    """Business logic for user operations."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)
    
    async def create_user(self, user_data: UserCreate) -> User:
        """
        Create a new user with validation and password hashing.
        
        Args:
            user_data: User creation data
            
        Returns:
            Created user instance
            
        Raises:
            EmailAlreadyExistsError: If email is already registered
        """
        # Validation
        existing = await self.repository.get_by_email(user_data.email)
        if existing:
            raise EmailAlreadyExistsError(f"Email {user_data.email} already exists")
        
        # Business logic
        hashed_password = hash_password(user_data.password)
        user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=hashed_password
        )
        
        return await self.repository.create(user)
    
    async def get_user(self, user_id: int) -> User:
        """Get user by ID."""
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        return user
```

#### Repository Pattern
```python
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import select

from src.domain.models import User

class UserRepository:
    """Data access layer for User model."""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def create(self, user: User) -> User:
        """Create a new user."""
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
```

---

## Anti-patterns to Avoid

### Code Smells
- ❌ **God Classes**: Classes > 300 lines - break into smaller classes
- ❌ **Long Methods**: Functions > 50 lines - extract into smaller functions
- ❌ **Deep Nesting**: Indentation > 3 levels - use early returns or extract functions
- ❌ **Primitive Obsession**: Using dict/tuple instead of Pydantic models
- ❌ **Magic Numbers**: Hardcoded values like `if age > 18:` → use `MINIMUM_AGE = 18`

### Common Mistakes
- ❌ **Mutable Default Arguments**: `def func(items=[]):` → Use `def func(items=None):`
- ❌ **Catching All Exceptions**: `except Exception:` without logging or re-raising
- ❌ **Print Debugging**: `print(user)` → Use `logger.debug(f"User: {user}")`
- ❌ **Blocking Operations in Async**: `time.sleep(1)` → Use `await asyncio.sleep(1)`
- ❌ **Direct Database Access from Routes**: Always use service layer

### Database Anti-patterns
- ❌ **N+1 Queries**: Use `selectinload()` or `joinedload()` for relationships
- ❌ **Missing Indexes**: Add indexes for frequently queried columns (email, username)
- ❌ **Raw SQL Without Parameters**: Always use parameterized queries
- ❌ **Committing in Loops**: Batch operations with bulk insert/update

### FastAPI-Specific Anti-patterns
- ❌ **Missing Response Models**: Always define `response_model` in endpoints
- ❌ **Not Using Dependency Injection**: Don't instantiate services directly in routes
- ❌ **Ignoring Status Codes**: Use appropriate HTTP status codes (201, 204, etc.)
- ❌ **No Input Validation**: Always use Pydantic models for request bodies

---

## Documentation Standards

### Code Documentation
- All public functions/classes **MUST** have docstrings (Google style)
- Include type hints (don't duplicate types in docstring)
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
uv venv                              # Create virtual environment
source .venv/bin/activate            # Activate (Linux/Mac)
.venv\Scripts\activate               # Activate (Windows)
uv pip install -e ".[dev]"           # Install with dev dependencies

# Running the application
uv run uvicorn src.main:app --reload --port 8000

# Development with auto-reload
uv run uvicorn src.main:app --reload --log-level debug
```

### Testing
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=html --cov-report=term-missing

# Run specific test file
uv run pytest tests/unit/services/test_user_service.py

# Run tests matching pattern
uv run pytest -k "test_create_user"

# Run with verbose output
uv run pytest -v -s

# Run only failed tests
uv run pytest --lf

# Run tests in parallel (with pytest-xdist)
uv run pytest -n auto
```

### Code Quality
```bash
# Type checking
uv run mypy src/

# Linting
uv run ruff check src/

# Formatting
uv run ruff format src/

# Import sorting (part of ruff)
uv run ruff check --select I --fix src/

# Security scan
uv run bandit -r src/

# All checks at once
uv run pre-commit run --all-files
```

### Database
```bash
# Create migration
uv run alembic revision --autogenerate -m "Add user table"

# Run migrations
uv run alembic upgrade head

# Rollback migration
uv run alembic downgrade -1

# Check migration status
uv run alembic current

# Database shell
psql -U postgres -d user_api_db
```

### Docker
```bash
# Build image
docker build -t user-api:latest .

# Run container
docker run -p 8000:8000 --env-file .env user-api:latest

# Docker Compose
docker-compose up -d              # Start services
docker-compose logs -f api        # Follow logs
docker-compose down               # Stop services
docker-compose exec api bash      # Enter container shell
```

---

## Before Committing (Checklist)

### Required Checks
- [ ] All tests pass: `uv run pytest`
- [ ] Type checking passes: `uv run mypy src/`
- [ ] Linting passes: `uv run ruff check src/`
- [ ] Formatting applied: `uv run ruff format src/`
- [ ] Coverage ≥ 80%: `uv run pytest --cov=src --cov-report=term`
- [ ] No debug code (print, pdb, breakpoint)
- [ ] No commented-out code blocks

### Documentation Checks
- [ ] Updated `docs/agent/04_CHANGELOG.md` for significant changes
- [ ] Updated service docs if API endpoints changed
- [ ] Docstrings added for new public functions/classes
- [ ] OpenAPI schema reflects changes (check /docs endpoint)

### Security Checks
- [ ] No secrets or API keys in code
- [ ] No sensitive data logged
- [ ] Environment variables used for all config
- [ ] Dependencies scanned: `uv run bandit -r src/`

### Git Hygiene
- [ ] Commit message format: `feat: add user authentication endpoint`
  - Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`
- [ ] Commits are atomic (one logical change per commit)
- [ ] Branch name: `feature/user-authentication` or `fix/email-validation`

---

## Integration & Deployment

### CI/CD
- **Platform**: GitHub Actions
- **Pipeline**: `.github/workflows/ci.yml`
- **Required Checks**: tests, mypy, ruff, coverage report
- **Deployment Branches**: 
  - `main` → Production (auto-deploy)
  - `develop` → Staging (auto-deploy)
  - `feature/*` → No deployment (CI only)

### Environment Variables
```bash
# Required (document in .env.example)
DATABASE_URL=postgresql://user:pass@localhost:5432/user_api_db
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key-min-32-chars
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Optional
LOG_LEVEL=INFO
ENVIRONMENT=development
SENTRY_DSN=https://...
CORS_ORIGINS=["http://localhost:3000"]
```

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml is configured
# Runs automatically before commit:
# - Ruff formatting and linting
# - mypy type checking
# - pytest (unit tests only, fast)
```

---

## Additional Context

### Common Tasks & Recipes

#### Adding a New Endpoint
1. Define Pydantic schemas in `src/domain/schemas.py`
2. Create/update service in `src/services/`
3. Add endpoint in `src/api/routes/`
4. Write integration tests in `tests/integration/api/`
5. Update OpenAPI docs (automatic via FastAPI)
6. Update `docs/agent/04_CHANGELOG.md`

#### Adding a New Model
1. Create SQLAlchemy model in `src/domain/models.py`
2. Create Alembic migration: `alembic revision --autogenerate -m "description"`
3. Review and adjust migration file
4. Apply migration: `alembic upgrade head`
5. Create Pydantic schemas in `src/domain/schemas.py`
6. Create repository in `src/repositories/`
7. Write unit tests

#### Troubleshooting Database Issues
```bash
# Check current migration
uv run alembic current

# View migration history
uv run alembic history

# Rollback to specific revision
uv run alembic downgrade <revision>

# Reset database (DESTRUCTIVE)
uv run alembic downgrade base
uv run alembic upgrade head
```

---

**Last Updated**: 2025-11-06  
**Maintainer**: Backend Team  
**Questions**: #backend-support on Slack or backend-team@company.com
