---
name: solution-work:brainstorm
description: Interactive exploration of a problem space — stakeholders, approaches, constraints, and tradeoffs — before formal definition begins
allowed-tools: Read, Glob, Grep, Write, Bash
user-invocable: true
---

# Brainstorm

Facilitate early-stage exploration of a problem before committing to formal artifacts. Helps teams think through what they're solving, who cares, what's been tried, and what constraints apply.

## Steps

1. **Load context** — Read `references/domain-knowledge.md` for domain patterns and terminology. Read `references/team-context.md` for team-specific systems, custodians, and org context if available. Check for existing artifacts in `synthesis/`, `discovery/`, or `requirements/` that provide prior context.

2. **Frame the problem** — Ask the user to describe what they're exploring. Prompt with:
   - What problem or opportunity are we looking at?
   - Who first raised this? What triggered this exploration?
   - Is there an existing system or process this relates to?

3. **Identify stakeholders** — Using domain knowledge and team context, help the user map who cares about this problem:
   - Who experiences the pain directly?
   - Who owns the current process or system?
   - Who would need to approve or fund a solution?
   - Who downstream would be affected by changes?
   - Are there regulatory or compliance stakeholders?

4. **Explore approaches** — Generate 3-5 possible approaches ranging from incremental to ambitious. For each:
   - What would this look like concretely?
   - What are the tradeoffs?
   - What's the rough effort level?
   - What assumptions does it make?
   - Has something like this been tried before?
   - What's the addressable market or opportunity size? Reference the `market-sizing` skill for TAM/SAM/SOM framework if relevant.

5. **Surface constraints** — Prompt for constraints the team might not have articulated:
   - Regulatory (reference domain knowledge for applicable regulations)
   - Technical (existing system limitations, vendor dependencies)
   - Organizational (team capacity, budget cycles, competing priorities)
   - Timeline (hard deadlines, market windows, regulatory dates)

6. **Capture decisions and open questions** — As the conversation progresses, track:
   - Decisions made (even tentative ones)
   - Open questions that need answers before proceeding
   - Assumptions that need validation
   - Risks identified

7. **Write brainstorm summary** — Write to `brainstorm/`:
   - `brainstorm/[topic-slug]-summary.md` containing:
     ```
     # Brainstorm: [Topic]
     Date: [date]

     ## Problem Statement (Draft)
     [1-2 sentences capturing the problem as understood]

     ## Stakeholders Identified
     | Stakeholder | Interest | Priority |
     |------------|----------|----------|

     ## Approaches Considered
     ### [Approach Name]
     - Description: ...
     - Tradeoffs: ...
     - Effort: ...

     ## Constraints
     - [constraint list]

     ## Market Opportunity (Draft)
     [If market sizing was explored — rough TAM/SAM/SOM or skip if not applicable]

     ## Decisions Made
     - [decision list]

     ## Open Questions
     - [question list]

     ## Suggested Next Steps
     - [which commands to run next and why]
     ```

8. **Suggest next steps** — Based on the conversation, recommend the logical next command:
   - If the problem is well-understood → `generate-requirements`
   - If the existing system needs mapping → `discover`
   - If more research is needed → `synthesize-research`
   - If architecture questions dominate → `architecture`
   - If the team needs alignment → `workshop-prep`

## Important

- This is exploration, not definition. Keep the conversation open-ended and avoid premature closure.
- Use domain knowledge to ask informed questions, not to prescribe answers.
- Capture everything — even ideas that get rejected. They're valuable context for later decisions.
- Don't push for resolution. The goal is clarity about what's known, unknown, and contested.
- If team context is available, reference it to ground the conversation in the team's actual systems and constraints.
