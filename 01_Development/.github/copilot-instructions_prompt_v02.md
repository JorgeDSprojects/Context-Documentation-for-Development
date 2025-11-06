# Prompt: Generate copilot-instructions.md

I need you to generate a complete, production-ready `copilot-instructions.md` file for my project using the provided template.

---

## 📋 Project Information

### Basic Info
- **Project Type**: [API REST / Web App / CLI Tool / Library / Microservice / Full-Stack App]
- **Primary Language**: [Python / TypeScript / Go / Rust / etc.]
- **Version**: [3.11 / 18.x / 1.21 / etc.]
- **Architecture Style**: [Monolithic / Microservices / Serverless / Layered / Event-Driven / etc.]

### Technology Stack
- **Framework**: [FastAPI / Django / Flask / Express / NestJS / Gin / etc.]
- **Database**: [PostgreSQL / MySQL / MongoDB / Redis / None / etc.]
- **ORM/Query Builder**: [SQLAlchemy / Prisma / GORM / etc.]
- **Package Manager**: [uv / pip / poetry / npm / yarn / pnpm / go mod / cargo / etc.]

### Key Libraries/Dependencies
List the 5-10 most important libraries/frameworks your project uses:
1. [Example: pydantic for data validation]
2. [Example: httpx for async HTTP requests]
3. [Example: celery for background tasks]
4. [Add more...]

---

## ⚙️ Code Standards Configuration

### Formatting & Linting
- **Formatter**: [Black / Ruff / Prettier / gofmt / rustfmt / None]
- **Linter**: [Ruff / Flake8 / ESLint / golangci-lint / clippy / None]
- **Line Length**: [88 / 100 / 120 / 80] characters
- **String Quotes**: [Single / Double / Backticks]

### Type Checking
- **Type Checker**: [mypy / pyright / TypeScript / None]
- **Strictness Level**: [Strict / Normal / Gradual]
- **Type Hints Required**: [Yes / No / Only for public APIs]

### Testing
- **Testing Framework**: [pytest / unittest / Jest / Vitest / testing / etc.]
- **Minimum Coverage**: [80% / 90% / 70% / None]
- **Test Structure**: [Separate directories / Alongside code]
- **Mocking Library**: [unittest.mock / pytest-mock / jest.mock / etc.]

### Documentation Style
- **Docstring Format**: [Google / NumPy / JSDoc / GoDoc / RustDoc / None]
- **API Documentation**: [OpenAPI/Swagger / GraphQL Schema / None]

---

## 📁 Project Structure

### Directory Organization
Provide your project's main directory structure:
```
project/
├── [src / app / lib / cmd / internal] /   # Main code location
├── tests/                                   # Tests location
├── docs/                                    # Documentation location
├── [scripts / tools] /                      # Utility scripts (if any)
└── [Other important directories]
```

### Source Code Location
- **Main Application Code**: [src/ / app/ / lib/ / internal/]
- **Tests**: [tests/ / test/ / __tests__/]
- **Documentation**: [docs/ / documentation/ / wiki/]
- **Configuration Files**: [config/ / conf/ / root directory]

### Files to Ignore
Are there specific files or patterns your project should never modify? Examples:
- Generated code (migrations, protobuf, graphql codegen)
- Build artifacts
- Vendor directories
- [Add project-specific patterns]

---

## 🔧 Project-Specific Rules

### Critical Patterns (What TO DO)
List 3-5 patterns that are critical to your project:
1. [Example: Always use dependency injection for services]
2. [Example: All API responses must use the standardized response wrapper]
3. [Example: Database queries must be async]
4. [Add more specific to your project...]

### Anti-patterns (What NOT TO DO)
List 3-5 anti-patterns specific to your project:
1. [Example: Never access the database directly from controllers]
2. [Example: Don't use ORM relationships for reporting queries]
3. [Example: Avoid circular imports between modules]
4. [Add more specific to your project...]

### Business Logic Rules
Any domain-specific rules or calculations the AI should know:
- [Example: Prices must always be stored in cents (integers)]
- [Example: User roles: admin > manager > user (hierarchy)]
- [Example: All dates must be in UTC]
- [Add more...]

---

## 🔌 Integrations & Services

### External Services
Does your project integrate with external services?
- [ ] AWS (S3, Lambda, SQS, etc.)
- [ ] Google Cloud (Storage, Pub/Sub, etc.)
- [ ] Payment Gateways (Stripe, PayPal, etc.)
- [ ] Email Services (SendGrid, SES, etc.)
- [ ] Analytics (Google Analytics, Mixpanel, etc.)
- [ ] Monitoring (Sentry, DataDog, etc.)
- [ ] Other: [Specify]

### APIs & Protocols
- **REST API**: [Yes / No]
- **GraphQL**: [Yes / No]
- **WebSockets**: [Yes / No]
- **gRPC**: [Yes / No]
- **Message Queue**: [RabbitMQ / Kafka / Redis / None]

---

## 🐳 Infrastructure & Deployment

### Containerization
- **Docker**: [Yes / No]
- **Docker Compose**: [Yes / No]
- **Kubernetes**: [Yes / No]

### CI/CD
- **Platform**: [GitHub Actions / GitLab CI / Jenkins / CircleCI / None]
- **Pipeline Location**: [.github/workflows / .gitlab-ci.yml / Jenkinsfile / etc.]
- **Deployment Targets**: [AWS / GCP / Azure / Heroku / Vercel / On-premise / etc.]

### Environment Variables
List critical environment variables the AI should know about:
1. `[DATABASE_URL]` - [Description]
2. `[API_KEY]` - [Description]
3. `[SECRET_KEY]` - [Description]
4. [Add more...]

---

## 🎯 Development Workflow

### Common Commands
What commands do developers run frequently?

**Setup:**
```bash
[Example: uv venv && uv pip install -e .]
```

**Development Server:**
```bash
[Example: uvicorn app.main:app --reload]
```

**Run Tests:**
```bash
[Example: pytest -v]
```

**Code Quality:**
```bash
[Example: ruff check . && mypy .]
```

**Database:**
```bash
[Example: alembic upgrade head]
```

### Git Workflow
- **Branch Naming**: [feature/* / feat/* / custom pattern]
- **Commit Convention**: [Conventional Commits / Custom / None]
- **PR Requirements**: [Tests pass / Review approval / CI green / etc.]

---

## 📚 Additional Context

### Team Preferences
- **Code Review Focus**: [Security / Performance / Readability / All]
- **Communication Style**: [Detailed comments / Self-documenting code / Both]
- **Breaking Changes**: [Require RFC / Team discussion / Just document / etc.]

### Special Considerations
Any unique aspects of your project:
- [Example: Legacy code sections that need careful handling]
- [Example: Performance-critical modules requiring optimization]
- [Example: Multi-tenant architecture with data isolation requirements]
- [Add more...]

---

## 📎 Template Reference

Please use the attached template file as the base structure:
- **File**: `copilot-instructions_template.md`
- **Instructions**: 
  1. Fill in ALL bracketed placeholders `[like this]` with my specific information
  2. Remove sections that don't apply to my project (mark with N/A if unsure)
  3. Expand examples to match my tech stack
  4. Add project-specific commands in the "Useful Commands" section
  5. Ensure all file paths match my project structure
  6. Keep the same section structure and organization

---

## 🎯 Deliverable Requirements

Generate a complete `copilot-instructions.md` file that includes:

✅ **Project Context** - Fully customized to my stack and architecture
✅ **Code Standards** - Specific to my language, tools, and conventions
✅ **File Organization** - Exact paths and structure from my project
✅ **Useful Commands** - All commands with my actual tool names (uv/pip/npm/etc.)
✅ **Testing Patterns** - Examples using my testing framework
✅ **Anti-patterns** - Both general and project-specific
✅ **Integration Details** - External services, APIs, deployment info
✅ **Before Committing Checklist** - Customized to my pipeline

The file should be:
- **Production-ready**: Can be committed directly to the repository
- **Actionable**: AI assistants can immediately follow the instructions
- **Comprehensive**: ~200-250 lines covering all essential aspects
- **Accurate**: All commands and paths work in my environment

---

## ❓ Questions Before Generation (Ask me if any info is missing)

If any critical information is unclear or missing, ask me to clarify:
- Database schema patterns
- Authentication/authorization approach
- Specific performance requirements
- Legacy code constraints
- Team size and structure

---

**Ready to generate?** Provide your answers to the sections above, and I'll create your customized `copilot-instructions.md` file.
