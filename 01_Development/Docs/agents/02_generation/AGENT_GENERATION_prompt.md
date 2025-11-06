# Meta-Prompt: Generate Technical Documentation from Objective

You are an experienced software architect and technical lead. I need you to analyze my project's `00_OBJECTIVE.md` file and generate three technical documentation files that define HOW the system will be built.

---

## 📋 Your Task

Based on my `00_OBJECTIVE.md`, you will:

1. **ANALYZE** the objective document thoroughly
2. **ASK QUESTIONS** about any unclear or missing technical details
3. **PROPOSE** architectural solutions with rationale
4. **GENERATE** three complete documentation files:
   - `01_ARCHITECTURE.md` - System structure and components
   - `02_ROADMAP.md` - Development phases and priorities
   - `03_CONVENTIONS.md` - Technical specifications and calculations

---

## 📖 Context: What You Have

I have already defined:
- ✅ **00_OBJECTIVE.md** - WHAT the system does and WHY (attached below)
- ✅ **copilot-instructions.md** - Coding standards and operational rules

What you need to create:
- ❓ **01_ARCHITECTURE.md** - HOW the system is structured
- ❓ **02_ROADMAP.md** - WHEN features will be implemented
- ❓ **03_CONVENTIONS.md** - Technical details and specifications

---

## 🎯 Phase 1: Analysis & Questions

### Step 1: Read and Understand

First, carefully read the attached `00_OBJECTIVE.md` file. Understand:
- What problem we're solving
- Who the users are
- What functionality is required
- What constraints exist
- What success criteria we have

### Step 2: Identify Gaps

After reading, identify what technical details are missing or unclear. Consider:

**Architecture Questions:**
- What's the overall system architecture style? (Layered? Hexagonal? Event-driven?)
- How many services/components are needed?
- What are the main system boundaries?
- How do components communicate?
- What data storage strategy? (Database per service? Shared database?)
- What external integrations are needed?
- How will we handle authentication/authorization flow?
- What's the deployment architecture?

**Technology Stack Questions:**
- Which specific framework version? (e.g., FastAPI 0.104 vs 0.110?)
- Database choice fully justified? (PostgreSQL vs MySQL vs other?)
- Caching layer needed? (Redis? Memcached? None?)
- Message queue needed? (RabbitMQ? Kafka? SQS?)
- Which specific libraries for key functions?
- Infrastructure choices? (Kubernetes? ECS? Lambda?)

**Roadmap Questions:**
- What's the MVP (absolute minimum for launch)?
- How should features be prioritized?
- What are critical dependencies between features?
- What's the realistic timeline given constraints?
- What can be parallelized vs sequential?
- What are the key milestones?

**Technical Specifications Questions:**
- Specific algorithms or calculation logic needed?
- Data validation rules?
- Business rule specifications?
- Performance optimization strategies?
- Security implementation details?
- Error handling strategies?

### Step 3: Ask Your Questions

**CRITICAL**: Before proposing solutions, ask me clarifying questions in this format:

```markdown
## 🤔 Questions Before I Proceed

### Critical Questions (Must Answer)
These are blocking questions - I cannot proceed without answers:

1. **[Category]**: [Specific question]?
   - Why I'm asking: [Explanation]
   - Options I'm considering: [A, B, C]
   
2. **[Category]**: [Specific question]?
   - Why I'm asking: [Explanation]
   - Impact: [What depends on this decision]

### Optional Questions (Nice to Have)
These would help but I can make reasonable assumptions:

1. **[Category]**: [Question]?
   - My assumption if you don't answer: [Default assumption]
   - Why it matters: [Explanation]
```

**Wait for my answers before proceeding to Phase 2.**

---

## 🏗️ Phase 2: Propose Solutions

Once you have answers to your questions, propose architectural solutions:

### Architecture Proposal

```markdown
## 🏗️ Proposed Architecture

### Architecture Style
I recommend [Layered/Hexagonal/Microservices/etc.] because:
- [Reason 1 based on OBJECTIVE constraints]
- [Reason 2 based on OBJECTIVE scale/complexity]
- [Reason 3 based on team size/expertise]

### System Components
Based on the core functionality in OBJECTIVE, the system needs:

1. **[Component Name]**
   - **Purpose**: [What it does]
   - **Responsibilities**: [Specific duties]
   - **Technology**: [Proposed tech stack]
   - **Rationale**: [Why this choice]

2. **[Component Name]**
   - [Same structure]

### Data Flow
[Explain how data flows through the system]

### Technology Justification
[For each major tech choice, explain WHY based on OBJECTIVE constraints]

### Trade-offs
**Benefits of this approach**:
- [Benefit 1]

**Drawbacks**:
- [Drawback 1]

**Alternatives considered**:
- [Alternative 1]: Rejected because [reason]
```

### Roadmap Proposal

```markdown
## 🗺️ Proposed Development Roadmap

### Phase Breakdown Strategy
I'm organizing phases based on:
- [Principle 1: e.g., "Value delivery - highest ROI first"]
- [Principle 2: e.g., "Technical dependencies - foundation first"]
- [Principle 3: e.g., "Risk reduction - validate assumptions early"]

### Proposed Phases

**Phase 1: MVP (Months 1-X)**
- Duration: [X months] | Team: [Y people]
- Goal: [What makes this MVP successful]
- Features from OBJECTIVE:
  - [Feature from scope]
  - [Feature from scope]
- Exit Criteria:
  - [Measurable criterion from SUCCESS_CRITERIA]

**Phase 2: [Name] (Months X-Y)**
- [Same structure]

### Dependencies & Risks
[What could block progress]

### Milestones
[Key checkpoints]
```

### Technical Conventions Proposal

```markdown
## ⚙️ Proposed Technical Conventions

### Domain-Specific Logic
Based on the business logic in OBJECTIVE:

**[Business Rule 1]**:
- Implementation approach: [How we'll code this]
- Validation: [How we'll validate]
- Edge cases: [How we'll handle them]

### Data Models
Based on core functionality:

**[Entity 1]**:
```python
class [EntityName]:
    # Fields based on OBJECTIVE requirements
    [field]: [type]  # Because [reason from OBJECTIVE]
```

### Algorithms & Calculations
If OBJECTIVE mentions specific calculations:

**[Calculation Name]**:
- Formula: [Specific formula]
- Implementation: [Code approach]
- Performance: [Complexity, optimization strategy]

### API Contracts
Based on integrations mentioned in OBJECTIVE:

**[Endpoint Name]**:
- Request: [Schema]
- Response: [Schema]
- Error codes: [List]
```

**Ask me**: Do these proposals align with your vision? Any adjustments needed?

---

## 📝 Phase 3: Generate Documentation

Once you have my approval on proposals, generate three complete files:

### File 1: 01_ARCHITECTURE.md

**Structure** (~300 lines):
```markdown
# System Architecture

## Overview
[2-3 paragraphs explaining the architecture]

## Architecture Diagram
[ASCII or description of system diagram]

## System Components

### [Component 1]
- **Purpose**: 
- **Responsibilities**:
- **Technology Stack**:
- **API Contract**:
- **Data Models**:

### [Component 2]
[Same structure for each component]

## Data Flow

### [Use Case 1 from OBJECTIVE]
[Step-by-step data flow]

## Infrastructure Architecture

### Development Environment
### Staging Environment  
### Production Environment

## Data Storage Strategy

### Database Schema
### Caching Strategy
### File Storage

## Integration Points

### [External Service 1]
- Purpose:
- Protocol:
- Authentication:
- Error Handling:

## Security Architecture

### Authentication Flow
### Authorization Model
### Data Encryption
### Secret Management

## Scalability & Performance

### Horizontal Scaling Strategy
### Caching Strategy
### Database Optimization
### Load Balancing

## Deployment Architecture

### CI/CD Pipeline
### Deployment Strategy
### Rollback Procedure

## Monitoring & Observability

### Metrics
### Logging
### Alerting
### Tracing

## Disaster Recovery

### Backup Strategy
### Failover Plan
### Recovery Procedures

## Technical Debt & Future Improvements
```

### File 2: 02_ROADMAP.md

**Structure** (~150-200 lines):
```markdown
# Development Roadmap

## Roadmap Overview
[Context about how this roadmap was created]

## Phases Summary
[Table with all phases, timeline, goals]

## Phase 1: MVP

### Overview
- **Duration**: 
- **Team Size**:
- **Goal**:

### Features
1. **[Feature from OBJECTIVE]**
   - Priority: [High/Medium/Low]
   - Effort: [Story points or time estimate]
   - Dependencies: [What must be done first]
   
### Milestones
- **Week 2**: [Milestone]
- **Week 4**: [Milestone]

### Exit Criteria
[From SUCCESS_CRITERIA in OBJECTIVE]

### Risks & Mitigation

## Phase 2: [Name]
[Same structure]

## Phase 3: [Name]
[Same structure]

## Technical Dependencies

### Dependency Graph
[Which features depend on which]

### Critical Path
[What defines the minimum timeline]

## Resource Plan

### Team Composition
### Skill Requirements
### External Dependencies

## Risk Management

### Technical Risks
### Timeline Risks
### Resource Risks

## Success Metrics

### Phase 1 Success Metrics
[How to measure if MVP succeeded]

### Overall Project Success
[From OBJECTIVE]
```

### File 3: 03_CONVENTIONS.md

**Structure** (~400 lines):
```markdown
# Technical Conventions & Specifications

## Purpose
[Why this document exists]

## Domain Models

### [Entity 1]
**Purpose**: [What this represents]

**Attributes**:
```python
class [EntityName]:
    id: UUID
    [field]: [type]  # [Description from business logic]
```

**Validation Rules**:
- [Rule 1 from business requirements]

**Business Rules**:
- [Rule from OBJECTIVE]

## Business Logic Specifications

### [Business Rule 1 from OBJECTIVE]
**Description**: [Detailed explanation]

**Algorithm**:
```python
def [function_name]():
    """
    Implementation of [business rule]
    
    Business logic: [From OBJECTIVE]
    """
    # Step-by-step implementation
```

**Edge Cases**:
- [Case 1]: [How to handle]

**Testing Strategy**:
- [What to test]

## Data Validation Rules

### Input Validation
[For each endpoint/input]

### Business Validation  
[Domain-specific validation]

### Error Messages
[Standardized error messages]

## Calculations & Algorithms

### [Calculation 1]
**Business Context**: [From OBJECTIVE]

**Formula**: 
```
[Mathematical formula]
```

**Implementation**:
```python
def calculate_[name](params):
    """
    [Description]
    
    Args:
        [param]: [description]
    
    Returns:
        [type]: [description]
        
    Examples:
        >>> calculate_[name](...)
        [expected result]
    """
    # Implementation with comments
```

**Performance Considerations**:
- Complexity: [O(...)]
- Optimization: [Strategy]

**Test Cases**:
```python
def test_calculate_[name]():
    # Positive case
    assert calculate_[name](...) == ...
    
    # Edge case
    assert calculate_[name](...) == ...
    
    # Error case
    with pytest.raises(ValueError):
        calculate_[name](...)
```

## API Specifications

### Endpoint: [Name]
**Business Purpose**: [From OBJECTIVE functionality]

**Request**:
```json
{
  "field": "type // description"
}
```

**Response**:
```json
{
  "field": "type // description"
}
```

**Validation Rules**:
- [Rule 1]

**Error Responses**:
- 400: [When this happens]
- 404: [When this happens]

**Examples**:
```bash
curl -X POST [url] \
  -H "Content-Type: application/json" \
  -d '{...}'
```

## Database Specifications

### Table: [name]
**Purpose**: [What data this stores from OBJECTIVE]

**Schema**:
```sql
CREATE TABLE [name] (
    id UUID PRIMARY KEY,
    [field] [type] [constraints],  -- [Business reason]
    created_at TIMESTAMP DEFAULT NOW()
);
```

**Indexes**:
```sql
CREATE INDEX idx_[name] ON [table]([field]);  -- Because [query pattern]
```

**Constraints**:
- [Constraint 1]: [Business rule it enforces]

## Security Specifications

### Authentication
[Specific implementation based on OBJECTIVE]

### Authorization
[RBAC rules from OBJECTIVE]

### Data Encryption
[What, how, when]

## Performance Specifications

### Response Time Targets
[From OBJECTIVE constraints]

### Optimization Strategies
[Specific to this domain]

### Caching Rules
[What to cache, TTL, invalidation]

## Integration Specifications

### [External Service 1]
**Integration Pattern**: [Request/Response, Event-driven, etc.]

**Authentication**: [How]

**Data Mapping**:
[Their format → Our format]

**Error Handling**:
[Retry strategy, fallback, circuit breaker]

**Rate Limiting**:
[Constraints, strategy]

## Multi-language/Localization
[If applicable from OBJECTIVE]

## Compliance Specifications

### GDPR
[Specific requirements from OBJECTIVE]

### SOC 2
[Specific controls]

### Data Retention
[Rules from business/legal requirements]

## Testing Specifications

### Unit Test Requirements
[Coverage, patterns]

### Integration Test Strategy
[What to test]

### Performance Test Criteria
[From OBJECTIVE performance criteria]

## Deployment Specifications

### Environment Configuration
[Dev, staging, prod differences]

### Feature Flags
[Strategy]

### Migration Strategy
[Database, breaking changes]

## Monitoring Specifications

### Key Metrics
[From OBJECTIVE success criteria]

### Alerting Thresholds
[When to alert]

### Logging Standards
[What to log, format]
```

---

## 🎯 Deliverables Summary

At the end, I expect:

1. ✅ **Questions Document** - Your clarifying questions (Phase 1)
2. ✅ **Proposals Document** - Your architectural proposals (Phase 2)
3. ✅ **01_ARCHITECTURE.md** - Complete architecture documentation (~300 lines)
4. ✅ **02_ROADMAP.md** - Complete roadmap documentation (~150-200 lines)
5. ✅ **03_CONVENTIONS.md** - Complete technical specifications (~400 lines)

All documents should:
- Reference the `00_OBJECTIVE.md` explicitly
- Use consistent terminology
- Be AI-assistant friendly (clear structure, examples)
- Follow the same format as copilot-instructions and OBJECTIVE
- Include "How to Use This Document" sections

---

## 📎 Required Input from User

Please provide:

1. **Your 00_OBJECTIVE.md file** (attach or paste below)
2. **Your copilot-instructions.md file** (optional but helpful for coding standards)
3. **Any additional context**: existing codebase, team expertise, infrastructure constraints

---

## 🚀 Process Flow

```
1. You provide OBJECTIVE.md
   ↓
2. I read and analyze it
   ↓
3. I ask clarifying questions
   ↓
4. You answer questions
   ↓
5. I propose architectural solutions
   ↓
6. You review and approve/adjust
   ↓
7. I generate three complete documentation files
   ↓
8. You review and iterate if needed
```

---

## ⚡ Quick Start

To begin, paste your `00_OBJECTIVE.md` content below and say: **"Generate technical documentation"**

I will then:
1. Ask you questions (you answer them)
2. Propose solutions (you approve/adjust)
3. Generate all three files

---

**Ready when you are!** 

Attach your `00_OBJECTIVE.md` and let's build the technical foundation for your project. 🚀
