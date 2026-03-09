---
name: solution-work:review
description: Check solution progress — quick status or deep completeness and cross-reference review
allowed-tools: Read, Glob, Grep, Write, Agent, Bash
user-invocable: true
---

# Review

Check solution progress. Can run as a quick status check or a deep completeness and cross-reference review.

## Steps

1. **Inventory artifacts** — Use Glob to find all solution artifacts across known directories: `synthesis/`, `brainstorm/`, `data-model/`, `api-contracts/`, `event-specs/`, `requirements/`, `operating-model/`, `pi-planning/`, `discovery/`, `architecture/`, `review/`, `workshop/`. Note which exist and their last modified dates.

2. **Read solution state** — If `solution_state.md` exists, read it for context on project phase, open questions, risks, and decisions.

3. **Ask what kind of review** — If the user didn't specify:
   ```
   What kind of review?

   1. Status — Quick progress summary (what exists, what's missing, next steps)
   2. Deep review — Completeness checks + cross-reference consistency across all artifacts
   ```

4. **Status review (light pass):**
   - For each artifact category, determine status: Complete / In progress / Not started
   - Identify which lifecycle phase the project is in (Phase 0-5)
   - Pull open questions, risks, and unresolved findings from solution state
   - Generate a progress summary with recommended next steps
   - Write to `status-report.md`

5. **Deep review (full pass):**

   a. **Launch completeness checks in parallel** — For each artifact found, launch a `completeness-checker` agent. Each agent reviews one artifact against the structural checklist from `references/domain-knowledge-base.md` and domain flags from `references/domain-knowledge.md`.

   b. **Launch cross-reference check** — Launch a `cross-reference-checker` agent to check consistency across all artifacts: naming mismatches, orphan references, CRUD gaps, NFR gaps, contradictions.

   c. **Phase-aware checks** — Based on current phase:
      - **Phase 1 (Discovery/Vision):** Do we have personas, journeys, problem statement?
      - **Phase 2 (Solution Intent):** Do we have all six artifacts? Flag missing target operating model or migration path: "You've defined the technical solution but not how people and processes change."
      - **Phase 3+ (PI Planning and beyond):** Are PI objectives traceable to solution vision? Are NFRs being validated?

   d. **Collect results** — Merge findings into a single review report.

   e. **Write review outputs:**
      - `review/completeness-report.md` — Per-artifact scores and gaps
      - `review/cross-reference-report.md` — Cross-artifact consistency findings
      - `review/action-items.md` — Prioritized gaps sorted by severity

6. **Update solution state** — If `solution_state.md` exists, update `review_findings` and phase tracker.

7. **Present summary** — Show: overall progress, critical issues, and top action items with specific commands to address them (e.g., "run `/solution-work:define` to add missing NFRs").

## Important

- Review is non-destructive — it reports findings but does not modify artifacts.
- Contradictions (from cross-reference) are higher severity than gaps (from completeness).
- Run completeness and cross-reference checks in parallel for speed.
- Flag stale artifacts (not updated in > 2 weeks) as needing refresh.
- The review should make the author say "good catch."
- Always recommend the next command to run based on what's missing.
- If no `solution_state.md` exists, suggest creating one from the template.
