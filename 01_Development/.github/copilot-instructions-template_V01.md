# GitHub Copilot Instructions

## Project Context
- **Type**: [API REST/Web App/CLI Tool]
- **Stack**: [Python 3.x, FastAPI, PostgreSQL, Redis, etc.]
- **Architecture**: [Brief description - e.g., "Microservices with FastAPI and async processing"]

## Complete Documentation
> - **Objective:** `docs/agent/00_OBJECTIVE.md` - What the system does
> - **Architecture:** `docs/agent/01_ARCHITECTURE.md` - System structure and components  
> - **Conventions:** `docs/agent/03_CONVENTIONS.md` - Technical specifications and rules
> - **Roadmap:** `docs/agent/02_ROADMAP.md` - Development phases and milestones
> - **Changelog:** `docs/agent/04_CHANGELOG.md` - **Update after significant changes**
> - **Services:** `docs/services/*.md` - Step-by-step service usage tutorials

---

## 🚨 Critical Rules

### Rule 1: Absolute Imports ONLY
```python
# ✅ CORRECT - Always absolute imports
from app.services.pdf_builder import generate_pdf
from app.models.book import BookConfig
from app.core.margins import calculate_mirror_margins

# ❌ WRONG - Never relative imports
from .pdf_builder import generate_pdf
from ..models import BookConfig
```

**Why:** Prevents import errors in tests, background tasks, and deployment.

---

### Rule 2: Type Hints Required
```python
# ✅ CORRECT
def render_page(page: Page, language: str) -> str:
    """Render a page template with given language."""
    pass

# ❌ WRONG - No type hints
def render_page(page, language):
    pass
```

**Why:** Type safety, better IDE support, catches errors early.

---

### Rule 3: Pydantic for All Data Models
```python
# ✅ CORRECT - Use Pydantic BaseModel
from pydantic import BaseModel, Field

class BookConfig(BaseModel):
    idioma_origen: str = Field(..., description="Source language code")
    languages_real: list[str] = Field(default_factory=list)
    pages: list[Page]

# ❌ WRONG - Plain dicts
book_config = {"idioma_origen": "es", "languages_real": []}
```

**Why:** Automatic validation, clear structure, self-documenting.

---

### Rule 4: File Organization
**ONLY modify files in:**
- ✅ `app/` - Application code (services, models, api)
- ✅ `templates/` - Jinja2 templates and CSS
- ✅ `tests/` - Test files
- ✅ `docs/agent/04_CHANGELOG.md` - After changes
- ✅ `docs/services/` - Service documentation

**DO NOT modify:**
- ❌ `output/` - Generated files (temporary)
- ❌ `assets/` - Temporary uploads
- ❌ `.env` files - Configuration (document changes only)

---

### Rule 5: Logging Standards
```python
import logging

logger = logging.getLogger(__name__)

# ✅ Use appropriate levels
logger.debug("Detailed diagnostic info")
logger.info("Starting PDF generation for: es")
logger.warning(f"Fallback applied - Page 7, de → es")
logger.error(f"Critical: No text for page 7 in es or de")
logger.exception("Unhandled exception occurred")  # Includes traceback
```

**Log Levels:**
- `DEBUG`: Detailed diagnostic information
- `INFO`: General informational messages
- `WARNING`: Warning messages for recoverable issues
- `ERROR`: Error messages for serious problems
- `EXCEPTION`: Error with full traceback

---

## Code Standards

### Python
- **Python Version**: [3.11+]
- **Formatter**: Black (line length: 88)
- **Linter**: Ruff/Flake8
- **Type Checker**: mypy
- **Testing**: pytest with minimum 80% coverage
- **Docstrings**: Google style

```python
def calculate_margin(page_width: float, margin_type: str) -> float:
    """Calculate page margin based on type.
    
    Args:
        page_width: Total width of the page in points
        margin_type: Type of margin ('inner', 'outer', 'top', 'bottom')
    
    Returns:
        Calculated margin value in points
        
    Raises:
        ValueError: If margin_type is not recognized
    """
    pass
```

### Package Manager
- **Use `uv`** for all dependency management
- ❌ Never use `pip install` directly
- ✅ Always use `uv pip install` or `uv add`

### Structure Rules
1. **NEVER** create files outside designated directories
2. **ALWAYS** update `docs/agent/04_CHANGELOG.md` after significant changes
3. **ALWAYS** create/update service documentation in `docs/services/` when adding new services
4. Keep functions under 50 lines
5. One class per file (except small utility classes)
6. Always include `__init__.py` in new packages

### API Routes
- **Prefix**: All API routes must use `/api` prefix
- **Organization**: Define routes in `api/routes.py`, not in `main.py`
- **Versioning**: Use `/api/v1/` for versioned endpoints

```python
# ✅ CORRECT
@router.post("/api/v1/books/generate")
async def generate_book(config: BookConfig):
    pass

# ❌ WRONG - No /api prefix
@router.post("/books/generate")
```

### Testing
- Write tests for every new function
- Minimum coverage: 80%
- Use pytest fixtures for common setups
- Test file naming: `test_*.py`
- Run tests: `pytest tests/ -v`

### Import Order
```python
# 1. Standard library
import os
import sys
from typing import Optional

# 2. Third-party packages
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 3. Local imports (always absolute)
from app.services.renderer import render_template
from app.models.book import BookConfig
from app.core.config import settings
```

---

## ✅ Code Quality Checklist

Before committing:
- [ ] All tests pass: `pytest tests/ -v`
- [ ] Type checking passes: `mypy app/`
- [ ] Linting passes: `ruff check .` or `flake8 app/`
- [ ] Formatting applied: `black app/ tests/`
- [ ] Type hints on all public functions
- [ ] Logging at appropriate levels (no print statements)
- [ ] No relative imports
- [ ] Pydantic models for all data structures
- [ ] Error handling with specific exceptions
- [ ] Service documentation updated in `docs/services/` (if applicable)
- [ ] Updated `docs/agent/04_CHANGELOG.md` if significant changes

---

## ❌ Anti-Patterns to Avoid

### Import Anti-Patterns
```python
# ❌ Relative imports
from .services import renderer
from ..models import Book

# ❌ Star imports
from app.models import *

# ❌ Circular imports
# file_a.py imports file_b.py and file_b.py imports file_a.py

# ✅ Correct - Absolute imports
from app.services.renderer import render_template
from app.models.book import BookConfig
```

### Error Handling Anti-Patterns
```python
# ❌ Bare except
try:
    result = risky_operation()
except:
    pass

# ❌ Generic exceptions
raise Exception("Something went wrong")

# ❌ Swallowing errors silently
try:
    result = risky_operation()
except Exception:
    pass  # Error disappears

# ✅ Correct
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise HTTPException(
        status_code=500,
        detail={"error": "Operation failed", "reason": str(e)}
    )
```

### Data Model Anti-Patterns
```python
# ❌ Plain dicts for complex data
config = {"idioma": "es", "pages": [...]}

# ❌ No validation
def process_book(config: dict):
    # Assumes structure is correct - will fail at runtime
    language = config["idioma"]  # KeyError if missing
    pass

# ✅ Correct - Pydantic models with validation
class BookConfig(BaseModel):
    idioma_origen: str = Field(..., min_length=2, max_length=5)
    pages: list[Page]

def process_book(config: BookConfig):
    # Validated automatically, guaranteed structure
    language = config.idioma_origen
    pass
```

### File Organization Anti-Patterns
```python
# ❌ God files (>500 lines)
# main.py with routes, models, services all mixed

# ❌ Logic in wrong layer
@app.post("/generate")
def generate_pdf(config: dict):
    # Business logic directly in endpoint
    pdf_data = complicated_pdf_generation()
    return pdf_data

# ❌ Models in multiple places
# User model defined in both api.py and services.py

# ✅ Correct separation
# api/endpoints.py - Only request/response handling
@router.post("/generate")
async def generate_pdf(config: BookConfig):
    result = await pdf_service.generate(config)
    return result

# services/pdf_service.py - Business logic
async def generate(config: BookConfig) -> PDFResult:
    # All generation logic here
    pass

# models/book.py - Data structures
class BookConfig(BaseModel):
    pass
```

### Performance Anti-Patterns
```python
# ❌ N+1 queries
for user in users:
    profile = db.query(Profile).filter_by(user_id=user.id).first()

# ❌ Loading everything into memory
all_records = db.query(LargeTable).all()  # Could be millions

# ❌ Blocking I/O in async functions
async def fetch_data():
    response = requests.get(url)  # Blocking!
    return response.json()

# ✅ Correct
# Use eager loading
users = db.query(User).options(joinedload(User.profile)).all()

# Use pagination
records = db.query(LargeTable).limit(100).offset(0).all()

# Use async clients
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
```

### Security Anti-Patterns
```python
# ❌ SQL injection vulnerability
query = f"SELECT * FROM users WHERE username = '{username}'"

# ❌ Exposing sensitive data in logs
logger.info(f"User logged in: {username}, password: {password}")

# ❌ No input validation
@app.post("/user")
def create_user(email: str):
    # Accepts any string, including malicious input
    pass

# ✅ Correct
# Use parameterized queries
query = "SELECT * FROM users WHERE username = :username"

# Sanitize logs
logger.info(f"User logged in: {username}")

# Validate with Pydantic
class UserCreate(BaseModel):
    email: EmailStr  # Validates email format
    username: str = Field(..., min_length=3, max_length=50, regex="^[a-zA-Z0-9_]+$")
```

---

## Testing Patterns

### Good Test Structure
```python
# tests/test_pdf_service.py
import pytest
from app.services.pdf_service import PDFService
from app.models.book import BookConfig

@pytest.fixture
def sample_book_config():
    """Fixture providing a valid book configuration."""
    return BookConfig(
        idioma_origen="es",
        languages_real=["en", "fr"],
        pages=[...]
    )

def test_generate_pdf_success(sample_book_config):
    """Test successful PDF generation."""
    # Arrange
    service = PDFService()
    
    # Act
    result = service.generate(sample_book_config)
    
    # Assert
    assert result.success is True
    assert result.file_path.endswith(".pdf")

def test_generate_pdf_missing_language(sample_book_config):
    """Test PDF generation with missing language raises error."""
    # Arrange
    sample_book_config.languages_real = []
    service = PDFService()
    
    # Act & Assert
    with pytest.raises(ValueError, match="At least one language required"):
        service.generate(sample_book_config)
```

---

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

## Useful Commands

```bash
# Development
uv run pytest tests/ -v              # Run tests
uv run mypy app/                     # Type checking
uv run ruff check .                  # Linting
uv run black app/ tests/             # Format code

# Package management
uv pip install package-name          # Install package
uv pip list                          # List packages
uv pip freeze > requirements.txt     # Export dependencies

# API testing
curl -X POST http://localhost:8000/api/v1/endpoint \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

---

## Additional Resources
- Project documentation: `docs/agent/`
- Service tutorials: `docs/services/`
- Architecture diagrams: `docs/diagrams/`
- API documentation: http://localhost:8000/docs (when running)
