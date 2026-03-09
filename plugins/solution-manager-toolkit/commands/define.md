---
name: solution-work:define
description: Define solution artifacts — data models, API contracts, event specs, NFRs, operating model, or migration path
allowed-tools: Read, Glob, Grep, Write, Bash
user-invocable: true
---

# Define Solution Artifacts

Single entry point for all Phase 2 (Solution Intent) artifact definition. Routes to the right skill based on what the user needs to define.

## Steps

1. **Load references** — Read `references/domain-knowledge-base.md` for completeness checklists. Read `references/domain-knowledge.md` for domain-specific requirements. Read `references/team-context.md` if available.

2. **Check for existing context** — Look for artifacts from prior commands: `discovery/`, `synthesis/`, `requirements/`, `brainstorm/`. These inform what needs to be defined.

3. **Ask what to define** — If the user didn't specify, present options:
   ```
   What are you defining?

   1. Canonical data model — entity definitions, governance, ownership
   2. API contract — endpoints, schemas, error handling, versioning
   3. Event spec — event schemas, delivery guarantees, subscribers
   4. Non-functional requirements — measurable quality targets
   5. Target operating model — how people and processes change
   6. Migration path — staged rollout with rollback options

   Or describe what you need and I'll figure out the right artifact type.
   ```

4. **Follow the WHO > WHAT > HOW > WHO OWNS IT sequence** — Regardless of artifact type:
   - **WHO** consumes this? What do they need? What are downstream dependencies?
   - **WHAT** is the contract or definition? What does "good" look like?
   - **HOW** do we deliver it? What's the structure?
   - **WHO OWNS IT** — Governance. Who approves changes? What's the change process?

5. **Route to the appropriate artifact workflow:**

   ### Canonical Data Model
   Reference the canonical-data skill. For each entity define: name, attributes with types, keys, relationships, ownership, validation rules, enums with governance, versioning, examples. Validate against data model checklist. Write to `data-model/`.

   ### API Contract
   Reference the api-contracts skill. For each endpoint define: method, path, request/response schemas, error codes, auth, rate limits, versioning, pagination, idempotency, examples. Validate against API checklist. Cross-reference with data model.
   - **Flag event-shaped APIs**: If an endpoint handles something that naturally HAPPENS (price updates, index rebalances, corporate actions), flag: "This looks like it should be event-driven. Should this be an event spec instead?"
   Write to `api-contracts/`.

   ### Event Spec
   Reference the event-integration skill. For each event define: name, schema, producer, consumer, trigger, delivery guarantee, ordering, retry/DLQ, schema evolution, versioning, idempotency key, throughput. Validate against event checklist.
   - **Flag lookup-shaped events**: If an event handles something that's naturally an ASK (reference data queries, security lookups), flag: "This looks like a request/response pattern. Should this be an API contract instead?"
   Write to `event-specs/`.

   ### Non-Functional Requirements
   Reference the nfr-definition skill. For each capability, define NFRs covering: latency, availability, throughput, data quality, security, compliance, scalability.
   - **Enforce the formula**: Every NFR must have [Thing you're measuring] + [specific number] + [specific conditions]. Reject vague NFRs ("the system should be fast") and rewrite them: "What's the target latency? Under what conditions? How will you measure it?"
   - The five key NFR types: latency, resiliency, lineage, auditability, explainability.
   Write to `requirements/nfrs.md`.

   ### Target Operating Model
   Define how people and processes change when the system goes live:
   - **Current state** — How people work today (role by role)
   - **Future state** — How people work after deployment
   - **What changes for PEOPLE** — Role by role: new responsibilities, eliminated tasks, training needs
   - **New processes needed** — Monitoring, escalation paths, review cadences
   Write to `operating-model/target-operating-model.md`.

   ### Migration Path
   Define a staged rollout with rollback options at each stage:
   - **Stage 1: Parallel run** — Old and new side by side, old is source of truth. Entry criteria, rollback procedure, success criteria.
   - **Stage 2: Cutover with safety net** — New is primary, old is backup. Entry criteria, rollback procedure, success criteria.
   - **Stage 3: Full migration** — Old retired. Entry criteria, rollback procedure, success criteria.
   Write to `operating-model/migration-path.md`.

6. **Update solution state** — If `solution_state.md` exists, update the relevant artifact status.

7. **Suggest next steps** — Based on what was just defined:
   - After data model → "Define API contracts or event specs that use these entities"
   - After API contract → "Define event specs for async flows, or NFRs for quality targets"
   - After event spec → "Define NFRs for throughput and delivery targets"
   - After NFRs → "Run review to check completeness across all artifacts"
   - After operating model or migration path → "Run review to validate against solution intent"
   - If target operating model or migration path is missing → Flag it: "You've defined the technical solution but not [what's missing]"

## Important

- Contract-first: define specs before code is written.
- Every artifact needs an owner. "TBD" is acceptable temporarily but must be flagged.
- Cross-reference across artifacts — entity names in API schemas must match the data model, event payloads must reference canonical entities.
- The ASKS FOR vs HAPPENS distinction matters: API = someone requests data. Event = something occurred and systems react.
- Target operating model and migration path are not optional — flag if missing when other Phase 2 artifacts exist.
