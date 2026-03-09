---
name: solution-work:help
description: Display the complete command registry with descriptions, suggested workflows, and quick-start guidance
allowed-tools: Read, Glob, Bash
user-invocable: true
---

# Solution Manager Help

Display the complete command registry and usage guidance.

## Steps

1. **Display command registry:**

   ```
   Solution Manager Toolkit v1.0.0
   ================================

   START HERE
     /solution-work:start                — Guided walkthrough: tell me what you're working on, I'll run the right commands

   RESEARCH & DISCOVERY (Phase 1 — Solution Vision)
     /solution-work:brainstorm           — Interactive exploration of a problem space before formal definition
     /solution-work:synthesize-research  — Synthesize raw user research into themes, personas, problem statements
     /solution-work:discover             — Analyze a codebase: technical inventory, business explainer, or both
     /solution-work:workshop-prep        — Generate workshop agendas and facilitation materials
     /solution-work:generate-requirements — Generate user stories, acceptance criteria from problem statements

   DEFINITION (Phase 2 — Solution Intent)
     /solution-work:define               — Define solution artifacts: data models, API contracts, event specs, NFRs, operating model, migration path

   PLANNING & ARCHITECTURE (Phase 3)
     /solution-work:architecture         — Facilitate architecture decisions with tradeoff matrices
     /solution-work:piplan               — Prepare for SAFe PI Planning with WSJF prioritization

   REVIEW (Any Phase)
     /solution-work:review               — Quick status check or deep completeness and cross-reference review
     /solution-work:help                 — Show this help
   ```

2. **Show suggested workflow chains:**

   ```
   Typical workflow:
     Phase 1: brainstorm → synthesize-research → discover → generate-requirements
     Phase 2: define (data model → API contract → event spec → NFRs → operating model → migration path)
     Phase 3: architecture → piplan
     Review:  review (run at any point to check progress)

   Quick start:
     - Exploring a new problem:    /solution-work:brainstorm
     - New project from research:  /solution-work:synthesize-research
     - Existing codebase:          /solution-work:discover
     - Define technical artifacts: /solution-work:define
     - Check what's done:          /solution-work:review
   ```

3. **Show team setup note:**

   ```
   Team Setup:
     Fill in references/team-context.md with your team's specifics:
       - Systems (OMS, portfolio management, rebalancer, data warehouse)
       - Custodians (file formats, recon cadence, SLAs)
       - Teams & ownership areas
       - Codebase conventions
       - Vendor integrations
       - Stakeholders & decision-making

     Domain knowledge (references/domain-knowledge.md) ships with investment
     management content. Review and extend for your firm's specifics.
   ```

## Important

- This command only displays information. It does not modify any files.
- Keep the output concise — users want a quick reference, not documentation.
- If `solution_state.md` exists, also show current project status summary at the top.
