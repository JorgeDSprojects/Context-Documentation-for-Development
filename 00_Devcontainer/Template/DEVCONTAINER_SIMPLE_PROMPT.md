# 🚀 Simple Dev Container Generator Prompt

**Quick setup with minimal questions - just copy and fill the basics!**

---

## ⚡ Quick Prompt (Copy This)

```
Generate a complete Dev Container setup for my Python project.

Project: [Project Name]
Type: [API / Web App / CLI / Data Science / Microservice]
Framework: [FastAPI / Django / Flask / None]
Database: [PostgreSQL / MySQL / MongoDB / None]

Generate these 4 files ready to use:
1. requirements.txt (with basic dependencies for my project type)
2. Dockerfile (Python 3.11 + uv package manager)
3. docker-compose.yml (with bidirectional volumes)
4. .devcontainer/devcontainer.json (full VS Code setup)

Use these defaults:
- Python 3.11 with uv package manager
- Non-root user (vscode, UID 1000)
- Auto-format with Black on save
- Include debugger configuration
- Port 8000 for the main service
- Testing with pytest
- Common VS Code extensions for Python

Add comments in English and include setup instructions.
```

---

## 📝 Even Simpler Version (Ultra-Minimal)

```
Create a Dev Container for: [Project Name]

It's a [describe in 5-10 words what your project does]

Stack: Python 3.11 + [framework if any]

Generate the 4 files: Dockerfile, docker-compose.yml, requirements.txt, and devcontainer.json
```

---

## 🎯 Real Examples

### Example 1: FastAPI Project
```
Generate a complete Dev Container setup for my Python project.

Project: TaskManager API
Type: API
Framework: FastAPI
Database: PostgreSQL

Generate these 4 files ready to use:
1. requirements.txt (with basic dependencies for my project type)
2. Dockerfile (Python 3.11 + uv package manager)
3. docker-compose.yml (with bidirectional volumes)
4. .devcontainer/devcontainer.json (full VS Code setup)

Use these defaults:
- Python 3.11 with uv package manager
- Non-root user (vscode, UID 1000)
- Auto-format with Black on save
- Include debugger configuration
- Port 8000 for the main service
- Testing with pytest
- Common VS Code extensions for Python

Add comments in English and include setup instructions.
```

### Example 2: Data Science Project
```
Create a Dev Container for: ML Analysis Pipeline

It's a data science project with pandas, sklearn, and Jupyter notebooks

Stack: Python 3.11

Generate the 4 files: Dockerfile, docker-compose.yml, requirements.txt, and devcontainer.json
```

### Example 3: CLI Tool
```
Generate a complete Dev Container setup for my Python project.

Project: FileOrganizer CLI
Type: CLI
Framework: None
Database: None

Generate these 4 files ready to use:
1. requirements.txt (with basic dependencies for my project type)
2. Dockerfile (Python 3.11 + uv package manager)
3. docker-compose.yml (with bidirectional volumes)
4. .devcontainer/devcontainer.json (full VS Code setup)

Use these defaults:
- Python 3.11 with uv package manager
- Non-root user (vscode, UID 1000)
- Auto-format with Black on save
- Include debugger configuration
- Port 8000 for the main service
- Testing with pytest
- Common VS Code extensions for Python

Add comments in English and include setup instructions.
```

---

## 🎨 For Your GenTales Project

```
Generate a complete Dev Container setup for my Python project.

Project: GenTales Book Generator
Type: API
Framework: FastAPI
Database: None

Additional dependencies needed:
- WeasyPrint (for PDF generation - requires system libs: libcairo2, libpango, libgdk-pixbuf)
- ebooklib (for EPUB)
- Jinja2 (for templates)
- Pillow (for images)

Use port 8057 instead of 8000.

Generate these 4 files ready to use:
1. requirements.txt (with basic dependencies for my project type)
2. Dockerfile (Python 3.11 + uv package manager + WeasyPrint system dependencies)
3. docker-compose.yml (with bidirectional volumes)
4. .devcontainer/devcontainer.json (full VS Code setup)

Use these defaults:
- Python 3.11 with uv package manager
- Non-root user (vscode, UID 1000)
- Auto-format with Black on save
- Include debugger configuration
- Testing with pytest
- Common VS Code extensions for Python

Add comments in English and include setup instructions.
```

---

## 🔧 Optional Add-ons

If you need to customize further, add these lines:

**For specific ports:**
```
Use ports: 8000 (API), 5432 (PostgreSQL), 6379 (Redis)
```

**For additional services:**
```
Include Redis and PostgreSQL in docker-compose.yml
```

**For specific dependencies:**
```
Additional dependencies:
- celery (for async tasks)
- redis (for caching)
- sqlalchemy (for ORM)
```

**For special system packages:**
```
System dependencies needed:
- ffmpeg (for video processing)
- tesseract-ocr (for OCR)
```

**For environment variables:**
```
Environment variables:
- DATABASE_URL=postgresql://user:pass@db:5432/mydb
- SECRET_KEY=dev-secret-key
- DEBUG=True
```

---

## 💡 How It Works

1. **Copy the quick prompt** (first block)
2. **Fill in just 4 fields:**
   - Project name
   - Project type
   - Framework
   - Database
3. **Paste to Claude/ChatGPT**
4. **Get your 4 files** with:
   - Smart defaults
   - Best practices
   - Ready to use
   - Fully commented

---

## ✅ What You Get Automatically

Without specifying anything extra:

- ✅ Python 3.11
- ✅ uv package manager (fast!)
- ✅ Non-root user setup
- ✅ Black formatter on save
- ✅ Pylint + Pylance
- ✅ Debugger configured
- ✅ pytest for testing
- ✅ Docker Compose with proper volumes
- ✅ VS Code extensions bundle
- ✅ Virtual environment auto-created
- ✅ Dependencies auto-installed

---

## 🎯 Comparison

### Old Way (Complex Template)
```
Lines to fill: 30+
Time: 10-15 minutes
Complexity: High
```

### New Way (Simple Prompt)
```
Lines to fill: 4
Time: 1 minute
Complexity: Low
```

**Same result, 10x faster! 🚀**

---

## 📚 Pro Tips

### Tip 1: Start Simple
Use the minimal version first. You can always regenerate with more details.

### Tip 2: Trust the Defaults
The defaults are production-ready. Only customize if you really need to.

### Tip 3: Iterate
Got the files? Try them. Need changes? Just ask:
```
"Add PostgreSQL to the docker-compose"
"Change port to 3000"
"Add Jupyter support"
```

### Tip 4: One Question Rule
If you're unsure about something, just describe your project in plain English:
```
"I'm building a REST API that converts JSON to PDF books"
```

The LLM will figure out what you need!

---

## 🔥 Ultra-Quick Reference

**For APIs:**
```
Project: [Name]
Type: API  
Framework: FastAPI
Database: [PostgreSQL/None]
```

**For Web Apps:**
```
Project: [Name]
Type: Web App
Framework: Django
Database: PostgreSQL
```

**For Data Science:**
```
Project: [Name]
Type: Data Science
Framework: None
Database: None
Additional: Add Jupyter notebooks support
```

**For Microservices:**
```
Project: [Name]
Type: Microservice
Framework: FastAPI
Database: [Your choice]
Additional: Include Redis for caching
```

---

## 🎁 Bonus: One-Liner for Experts

```
DevContainer for Python 3.11 + [framework] + [database] project called [name], generate 4 files with uv and common setup
```

Done! 🎉

---

## 📝 Save This As

```
docs/prompts/devcontainer-quick-setup.md
```

Now you can generate Dev Containers in under 60 seconds! ⚡
