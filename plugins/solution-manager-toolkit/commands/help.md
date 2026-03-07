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
   Solution Manager Toolkit v0.4.0
   ================================

   START HERE
     /solution-work:start                — Guided walkthrough: tell me what you're working on, I'll run the right commands

   RESEARCH & DISCOVERY
     /solution-work:synthesize-research  — Synthesize raw user research into themes, personas, problem statements
     /solution-work:discover             — Analyze codebase for data models, APIs, dependencies
     /solution-work:explain-code         — Explain what code does in plain, non-technical language
     /solution-work:brainstorm           — Interactive exploration of a problem space before formal definition

   DEFINITION
     /solution-work:generate-requirements — Generate user stories, acceptance criteria from problem statements
     /solution-work:datamodel            — Define canonical data models with governance
     /solution-work:apicontract          — Define contract-first API specifications
     /solution-work:eventspec            — Define event schemas with delivery guarantees
     /solution-work:nfr                  — Define non-functional requirements with measurable targets

   PLANNING & ARCHITECTURE
     /solution-work:workshop-prep        — Generate workshop agendas and facilitation materials
     /solution-work:piplan               — Prepare for SAFe PI Planning ceremony
     /solution-work:architecture         — Facilitate architecture decisions with tradeoff matrices

   REVIEW & STATUS
     /solution-work:review               — Run completeness and cross-reference checks on all artifacts
     /solution-work:status               — Generate solution progress report
     /solution-work:help                 — Show this help
   ```

2. **Show suggested workflow chains:**

   ```
   Typical workflow:
     1. brainstorm → 2. synthesize-research → 3. discover → 4. datamodel →
     5. apicontract → 6. eventspec → 7. nfr → 8. review → 9. architecture → 10. piplan

   Quick start:
     - Exploring a new problem:    /solution-work:brainstorm
     - New project from research:  /solution-work:synthesize-research
     - Existing codebase:          /solution-work:discover
     - Check what's done:          /solution-work:status
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
