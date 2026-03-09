---
name: solution-work:discover
description: Analyze a codebase — technical inventory, business explainer, or both
allowed-tools: Read, Glob, Grep, Write, Bash, Agent
user-invocable: true
---

# Discover Codebase

Comprehend an existing codebase and produce discovery outputs for solution management context. Can produce a technical inventory, a plain-language business explainer, or both.

## Steps

1. **Find the code** — Check the current directory for source code files and project markers (`package.json`, `requirements.txt`, `Gemfile`, `pom.xml`, `go.mod`, etc.).
   - **If code is found** — Tell the user what you see and confirm: "I see a [language/framework] project here. Should I analyze this?"
   - **If no code is found** — Ask: "I don't see code in the current directory. Point me at a file path, directory, or GitHub repo URL."
   - **If the user provides a GitHub URL** — Clone to a temp directory, then scan.
   - **If a single file** — Scope the analysis to just that file.
   - Wait for confirmation before proceeding.

2. **Ask what they need** — "What kind of output do you want?"
   - **Technical inventory** — Data models, API endpoints, dependencies, event patterns, configuration (for engineering)
   - **Business explainer** — Plain-language explanation of what the system does, for non-technical stakeholders
   - **Both** — Full technical inventory plus business narrative

3. **Load context** — Read `references/team-context.md` for team-specific systems, codebase conventions, and vendor integrations if available. Read `references/domain-knowledge.md` for domain patterns.

4. **Identify project type** — Use Glob and Read to determine the tech stack: language, framework, build tools, package manager.

5. **Scan the codebase** — Use Glob, Grep, and Read to analyze:
   - Data models (ORM definitions, schemas, migrations, entity classes)
   - API endpoints (routes, controllers, OpenAPI specs, GraphQL schemas)
   - Dependencies (external services, vendor integrations, shared libraries)
   - Event patterns (message queues, pub/sub, webhooks, event bus)
   - Configuration (environment variables, feature flags, deployment manifests)

6. **Write outputs** — Write to `discovery/` based on what the user requested:

   **Technical inventory** (reference the codebase-discovery skill):
   - `discovery/codebase-report.md` — Full discovery findings by category
   - `discovery/entity-map.md` — All data entities with attributes and relationships
   - `discovery/api-inventory.md` — All API endpoints with methods and schemas
   - `discovery/dependency-graph.md` — External and internal dependencies

   **Business explainer** (reference the code-explainer skill):
   - `discovery/business-explainer.md` — Plain-language explanation: one-paragraph summary, who uses it, what it does (as workflows), where information flows, what it doesn't do, questions it raises

   For a single file, use simpler formats scoped to that file.

7. **Update solution state** — If `solution_state.md` exists, update the `codebase` section.

8. **Suggest next steps** — Based on findings:
   - If gaps were significant → `brainstorm` to explore the problem space
   - If technical artifacts are needed → `define` to create data models, API contracts, etc.
   - If stakeholders need alignment → `workshop-prep`

## Important

- Discovery is observation, not inference. Report what the code says, not what you think it should say.
- Flag undocumented dependencies as high-risk items.
- If the codebase is very large, ask the user to scope to specific directories or modules.
- For business explainer output: write for a smart person who doesn't code. No jargon. Use domain language from `references/domain-knowledge.md`.
- Always confirm with the user before scanning.
- Reference the codebase-discovery skill for technical analysis and the code-explainer skill for business translation.
