# Prompt: Generate 00_OBJECTIVE.md

I need you to generate a complete `00_OBJECTIVE.md` file for my project that explains **WHAT the system does and WHY it exists**. This file will be used by AI assistants (like GitHub Copilot, Claude Code) and team members to understand the project's strategic context.

---

## 📋 Project Information

### Basic Details
- **Project Name**: [Full project name]
- **Project Type**: [API REST / Web Application / CLI Tool / Microservice / Library / Full-Stack App / Data Pipeline]
- **Main Purpose**: [Describe in 2-3 sentences what this system does and why it exists]

**Example:**
> This is a user authentication API that provides secure token-based authentication for enterprise applications. It handles user registration, login, role management, and integrates with third-party identity providers to simplify authentication for development teams.

---

## 👥 Users and Stakeholders

### Primary Users
**Who are the main users?**
- [User Type 1: e.g., "Backend developers integrating auth into their apps"]
- [User Type 2: e.g., "Mobile app developers needing secure authentication"]

**What do they need to accomplish?**
- [Need 1: e.g., "Authenticate users without building custom auth logic"]
- [Need 2: e.g., "Manage user permissions and roles"]

**How will they interact with the system?**
- [Interaction 1: e.g., "Via REST API endpoints"]
- [Interaction 2: e.g., "Through client SDKs (Python, JavaScript)"]

### Secondary Users
**Who else will use this indirectly?**
- [User Type 3: e.g., "System administrators monitoring auth metrics"]
- [User Type 4: e.g., "Security team auditing access logs"]

### Stakeholders
**Who cares about this project's success but doesn't directly use it?**
- [Stakeholder 1: e.g., "Product managers - track adoption rates"]
- [Stakeholder 2: e.g., "CTO - ensure security compliance"]

---

## ⚙️ Core Functionality

### Function 1: [Name the first major capability]
- **What it does**: [Detailed description]
- **Why it matters**: [Business value it provides]
- **How it works**: [High-level process in 2-3 sentences]

**Example:**
- **What**: User registration with email verification
- **Why**: Ensures only legitimate users access the system
- **How**: User submits email/password → System hashes password and creates account → Sends verification email → User clicks link → Account activated

### Function 2: [Name the second major capability]
- **What it does**: [Description]
- **Why it matters**: [Value]
- **How it works**: [Process]

### Function 3: [Name the third major capability]
- **What it does**: [Description]
- **Why it matters**: [Value]
- **How it works**: [Process]

### Function 4: [Optional - Add if needed]
- **What it does**: [Description]
- **Why it matters**: [Value]
- **How it works**: [Process]

### Function 5: [Optional - Add if needed]
- **What it does**: [Description]
- **Why it matters**: [Value]
- **How it works**: [Process]

---

## 💼 Business Context

### Problem It Solves
**What pain points exist without this system?**
1. [Problem 1: e.g., "Teams spend 2-3 weeks building custom authentication"]
2. [Problem 2: e.g., "Inconsistent security implementations across applications"]
3. [Problem 3: e.g., "No centralized user management"]

**What's the impact of these problems?**
- [Impact 1: e.g., "Delayed product launches"]
- [Impact 2: e.g., "Increased security vulnerabilities"]

### Value Proposition
**What value does this system provide?**
1. [Value 1: e.g., "Reduces time-to-market by 2-3 weeks per application"]
2. [Value 2: e.g., "Provides battle-tested, secure authentication"]
3. [Value 3: e.g., "Centralizes user management for easier compliance"]

**What makes it better than alternatives?**
- [Advantage 1: e.g., "10x faster integration than Auth0"]
- [Advantage 2: e.g., "Self-hosted for data sovereignty"]

### Success Metrics
**How will you measure if this project is successful?**
1. [Metric 1: e.g., "Integration time < 2 hours for new apps"]
2. [Metric 2: e.g., "99.9% uptime for authentication requests"]
3. [Metric 3: e.g., "Zero security incidents in production"]
4. [Metric 4: e.g., "50+ applications using the service within 6 months"]

---

## 🎯 Scope

### In Scope - What IS included

#### Phase 1 (MVP - Must Have)
List the core features for the first release:
1. [Feature 1: e.g., "Email/password authentication"]
2. [Feature 2: e.g., "JWT token generation"]
3. [Feature 3: e.g., "Basic role-based access control"]
4. [Feature 4]
5. [Feature 5]

#### Phase 2 (Future - Should Have)
List features for later releases:
1. [Feature 6: e.g., "OAuth 2.0 integration (Google, GitHub)"]
2. [Feature 7: e.g., "Multi-factor authentication"]
3. [Feature 8: e.g., "Session management"]

#### Phase 3 (Nice to Have)
List optional features:
1. [Feature 9: e.g., "SAML SSO for enterprise"]
2. [Feature 10: e.g., "Biometric authentication"]

### Out of Scope - What is NOT included
**Explicitly list what this project will NOT do:**
1. [Excluded 1: e.g., "User profile management beyond auth data"]
2. [Excluded 2: e.g., "Payment processing or billing"]
3. [Excluded 3: e.g., "Email delivery (use external service)"]
4. [Excluded 4: e.g., "Mobile app development"]
5. [Excluded 5: e.g., "Analytics dashboards"]

**Why are these out of scope?**
- [Reason 1: e.g., "Profile management is app-specific"]
- [Reason 2: e.g., "Email delivery better handled by SendGrid/SES"]

---

## 🔄 Typical User Flows

### Flow 1: [Name of primary use case]
**Scenario**: [Describe the scenario - e.g., "A new user registers and authenticates"]  
**Actor**: [Who does this - e.g., "End user via mobile app"]

Describe each step in detail:

**Step 1: [Step Name]**
- **Input**: [What data/actions the user provides]
- **Processing**: [What the system does internally]
- **Output**: [What result the user sees/receives]

**Step 2: [Step Name]**
- **Input**: [What goes in]
- **Processing**: [What happens]
- **Output**: [What comes out]

**Step 3: [Step Name]**
- **Input**: [What goes in]
- **Processing**: [What happens]
- **Output**: [What comes out]

**Step 4: [Step Name]** (if applicable)
- **Input**: [What goes in]
- **Processing**: [What happens]
- **Output**: [What comes out]

### Flow 2: [Name of secondary use case] (Optional)
**Scenario**: [Describe another important scenario]  
**Actor**: [Who performs this]

**Step 1: [Step Name]**
- **Input**: [What goes in]
- **Processing**: [What happens]
- **Output**: [What comes out]

**Step 2: [Step Name]**
- **Input**: [What goes in]
- **Processing**: [What happens]
- **Output**: [What comes out]

---

## 🚧 Constraints

### Technical Constraints
**Technology and architecture limitations:**
1. [Constraint 1: e.g., "Must run in Docker containers"]
2. [Constraint 2: e.g., "Must use Python 3.11+ (no Python 2)"]
3. [Constraint 3: e.g., "Database: PostgreSQL 13+ only"]
4. [Constraint 4: e.g., "API response time: < 200ms (p95)"]
5. [Constraint 5: e.g., "Must support horizontal scaling"]

### Operational Constraints
**Deployment, maintenance, and support limitations:**
1. [Constraint 1: e.g., "Must deploy on AWS (no GCP/Azure)"]
2. [Constraint 2: e.g., "Zero-downtime deployments required"]
3. [Constraint 3: e.g., "Automated backups every 6 hours"]
4. [Constraint 4: e.g., "Monitoring via Prometheus/Grafana"]
5. [Constraint 5: e.g., "99.9% SLA required"]

### Business Constraints
**Budget, timeline, and organizational limitations:**
1. [Constraint 1: e.g., "MVP launch: 3 months maximum"]
2. [Constraint 2: e.g., "Infrastructure budget: $500/month"]
3. [Constraint 3: e.g., "Team size: 2 developers + 1 DevOps"]
4. [Constraint 4: e.g., "Open source only (no paid licenses)"]
5. [Constraint 5: e.g., "Must comply with GDPR and SOC 2"]

### Compliance & Security Constraints
**Legal and regulatory requirements:**
1. [Constraint 1: e.g., "GDPR compliance for EU users"]
2. [Constraint 2: e.g., "Data encryption at rest and in transit"]
3. [Constraint 3: e.g., "Audit logging for all auth events"]
4. [Constraint 4: e.g., "Password policy: min 12 chars, complexity rules"]

---

## ✅ Success Criteria

### Functional Success Criteria
**The system MUST successfully:**
- [ ] [Criterion 1: e.g., "Register users with email verification"]
- [ ] [Criterion 2: e.g., "Authenticate users and issue JWT tokens"]
- [ ] [Criterion 3: e.g., "Support role-based access control (3+ roles)"]
- [ ] [Criterion 4: e.g., "Integrate with 2+ OAuth providers"]
- [ ] [Criterion 5: e.g., "Provide admin API for user management"]

### Quality Success Criteria
**The system MUST meet quality standards:**
- [ ] [Criterion 1: e.g., "Test coverage ≥ 80%"]
- [ ] [Criterion 2: e.g., "Zero critical security vulnerabilities"]
- [ ] [Criterion 3: e.g., "100% API documentation coverage"]
- [ ] [Criterion 4: e.g., "Code quality score ≥ 8/10"]
- [ ] [Criterion 5: e.g., "All APIs have usage examples"]

### Performance Success Criteria
**The system MUST perform within these limits:**
- [ ] [Criterion 1: e.g., "Authentication: < 100ms (p95)"]
- [ ] [Criterion 2: e.g., "Token validation: < 10ms (p95)"]
- [ ] [Criterion 3: e.g., "Support 1000 concurrent users"]
- [ ] [Criterion 4: e.g., "Database queries: < 50ms average"]
- [ ] [Criterion 5: e.g., "API uptime: 99.9% monthly"]

### Operational Success Criteria
**The system MUST be operable:**
- [ ] [Criterion 1: e.g., "CI/CD pipeline fully automated"]
- [ ] [Criterion 2: e.g., "Monitoring dashboards configured"]
- [ ] [Criterion 3: e.g., "Automated daily backups"]
- [ ] [Criterion 4: e.g., "Disaster recovery plan tested"]
- [ ] [Criterion 5: e.g., "Runbook for common issues"]

### Business Success Criteria
**The project MUST achieve business goals:**
- [ ] [Criterion 1: e.g., "5+ apps migrated in 6 months"]
- [ ] [Criterion 2: e.g., "50% reduction in auth support tickets"]
- [ ] [Criterion 3: e.g., "Developer satisfaction ≥ 4/5"]
- [ ] [Criterion 4: e.g., "Zero security breaches in year 1"]
- [ ] [Criterion 5: e.g., "Integration time < 2 hours"]

---

## 📎 Additional Context (Optional but Recommended)

### Assumptions
**What are we assuming to be true?**
1. [Assumption 1: e.g., "Users have stable internet"]
2. [Assumption 2: e.g., "Apps handle token refresh"]
3. [Assumption 3: e.g., "Email delivery via external service"]

### Dependencies
**What does this project depend on?**
1. [Dependency 1: e.g., "PostgreSQL database (managed)"]
2. [Dependency 2: e.g., "Redis for session storage"]
3. [Dependency 3: e.g., "SMTP server for emails"]

### Related Projects
**What other systems does this integrate with?**
1. [Project 1: e.g., "User Profile Service"]
2. [Project 2: e.g., "Admin Dashboard"]
3. [Project 3: e.g., "Monitoring Stack"]

---

## 📎 Template Reference

**CRITICAL**: Please use the attached template file as the base structure:
- **File**: `00_OBJECTIVE_template.md`
- **Instructions**:
  1. Use the template as your BASE - don't create from scratch
  2. Fill in ALL bracketed placeholders `[like this]` with my specific information provided above
  3. Replace ALL examples with real data from my project
  4. Keep the same section structure and organization from the template
  5. Remove optional sections if they don't apply to my project (mark with "N/A" if unsure)
  6. Expand examples where needed to provide clarity
  7. Ensure the document is ~150-200 lines when complete

---

## 🎯 Deliverable Requirements

Generate a complete `00_OBJECTIVE.md` file that includes:

✅ **Clear Purpose** - Anyone can understand what the system does in 2 minutes  
✅ **Target Users** - Clearly defined primary, secondary users and stakeholders  
✅ **Core Functionality** - 3-5 main functions with "what, why, how"  
✅ **Business Value** - Problems solved, value provided, success metrics  
✅ **Scope** - In-scope features by phase, out-of-scope with rationale  
✅ **User Flows** - At least 1 detailed flow with input/processing/output  
✅ **Constraints** - Technical, operational, business, compliance  
✅ **Success Criteria** - Functional, quality, performance, operational, business  

The file should be:
- **Strategic**: Focuses on WHAT and WHY, not HOW
- **AI-Readable**: Clear structure that AI assistants can parse and understand
- **Comprehensive**: ~150-200 lines covering all essential aspects
- **Actionable**: Team members can use it to make scope decisions

---

## ❓ Questions to Ask Me (If Information is Missing)

If any critical information is unclear or missing from what I provided, ask me:
- What specific problems does this solve for users?
- Who are the primary vs secondary users?
- What are the top 3 things this system MUST do?
- What's explicitly out of scope?
- What are the key performance requirements?
- What compliance/security requirements exist?
- How do you measure success?

---

**Ready to generate?** Provide your answers to all the sections above, attach `00_OBJECTIVE_template.md`, and I'll create your customized `00_OBJECTIVE.md` file.
