---
name: solution-work:start
description: Guided walkthrough — tell me what you're working on and I'll run the right commands in order
allowed-tools: Read, Glob, Grep, Write, Bash, Agent
user-invocable: true
---

# Start

Single entry point for the entire toolkit. Figures out where you are, picks the right workflow, and runs each step in sequence — prompting between steps so you stay in control.

## Steps

1. **Load context** — Read `references/team-context.md` and check for existing artifacts (`solution_state.md`, `synthesis/`, `discovery/`, `data-model/`, `requirements/`, `api-contracts/`, `event-specs/`, `review/`, `brainstorm/`). This tells us what's already been done.

2. **Ask what they're working on** — Present the situation and ask a simple question:

   ```
   What are you working on?

   1. Exploring a new problem (not sure what to build yet)
   2. We have user research to process (interviews, surveys, feedback)
   3. We have an existing codebase to map
   4. We need someone to explain what code does (non-technical)
   5. We need to define the solution (data models, APIs, events, NFRs)
   6. We need to review what we've built so far
   7. We're preparing for PI Planning

   Or just describe what you're doing and I'll figure out where to start.
   ```

3. **Map to workflow** — Based on their answer, select the right sequence:

   | Starting point | Workflow |
   |---------------|----------|
   | Exploring a new problem | `brainstorm` → `generate-requirements` → `review` |
   | Have user research | `synthesize-research` → `generate-requirements` → `review` |
   | Have an existing codebase | `discover` → `datamodel` → `apicontract` → `review` |
   | Need code explained (non-technical) | `explain-code` |
   | Need to define the solution | `datamodel` → `apicontract` → `eventspec` → `nfr` → `review` |
   | Need to review | `review` |
   | Preparing for PI Planning | `review` → `architecture` → `piplan` |

   If they describe something freeform, map it to the closest workflow. If unclear, start with `brainstorm`.

4. **Run each step in sequence** — For each command in the workflow:
   - Announce what you're about to do and why it's next
   - Execute the command's full process (follow that command's steps exactly)
   - Show the user what was produced
   - Ask: "Ready for the next step, or want to pause here?"
   - If they pause, tell them what to run next and update `solution_state.md`

5. **Skip steps that are already done** — If artifacts from a prior run exist (e.g., `discovery/` already has files), tell the user and ask if they want to redo it or skip to the next step.

6. **Wrap up** — After the final step (or when they pause), show:
   - What was produced (list of output directories/files)
   - What's left in the workflow
   - The exact command to resume: `/solution-work:start` (it will pick up where they left off)

## Important

- This command is a router, not a replacement. It runs the actual commands — don't duplicate their logic.
- Always let the user pause between steps. Don't run the full chain without checking in.
- If `solution_state.md` exists, use it to determine what's already been done.
- If no artifacts exist and the user seems unsure, default to `brainstorm`.
- Keep announcements between steps to 2-3 lines. Don't over-explain.
