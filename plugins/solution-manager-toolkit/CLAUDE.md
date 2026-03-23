# Solution Manager Toolkit

AI-assisted Solution Management Assistant for investment management firms — tools for the full solution lifecycle.

Plugin name: `solution-work` — commands invoked as `/solution-work:<command>`.

## Architecture Principles

1. **Checklists over opinions** — prompt for completeness, don't make decisions
2. **Everything traceable** — every artifact references its source
3. **Canonical thinking by default** — check data elements against registry
4. **NFRs never optional** — every capability prompts for NFRs
5. **Cross-reference across artifacts** — surface inconsistencies
6. **Domain context from references** — domain defaults come from `references/domain-knowledge.md`; team-specific systems, custodians, and org context come from `references/team-context.md`
7. **WHO > WHAT > HOW > WHO OWNS IT** — default sequence for any definition work

## Six-Phase Solution Management Lifecycle

| Phase | Name | What Happens | Key Commands |
|-------|------|-------------|--------------|
| 0 | Prioritization | Decide WHAT to work on (MoSCoW, WSJF, Impact vs Effort) | `piplan`, `review` |
| 1 | Discovery (Solution Vision) | Workshops, interviews, personas, problem statements | `brainstorm`, `synthesize-research`, `discover`, `workshop-prep`, `generate-requirements` |
| 2 | Solution Intent | Define technical artifacts: data model, API contract, event spec, NFRs, operating model, migration path | `define` |
| 3 | PI Planning | Present vision, teams plan sprints, map dependencies | `architecture`, `piplan` |
| 4 | Execution | Teams build, SM validates against contracts | `review` |
| 5 | Review | System demo, inspect & adapt, update roadmap | `review` |

## Domain & Team Knowledge Architecture

| File | Purpose | Action |
|------|---------|--------|
| `references/domain-knowledge-base.md` | Generic checklists, NFR format, review patterns | Stable — extend but don't remove |
| `references/domain-knowledge.md` | Investment management domain knowledge (instruments, regulations, failure modes) | Review and extend for your firm's specifics |
| `references/team-context.md` | Your team's systems, custodians, org structure, codebase conventions | **Fill in for your team** |

Commands reference `base` and `domain-knowledge` by section heading. Required sections in domain-knowledge: Domain Identifiers, NFR Defaults, Regulatory Requirements, Common Failure Modes, Domain Validation Flags. Missing sections degrade gracefully (commands skip domain checks, don't crash). Team context is optional but enriches discover, piplan, architecture, and review.

## Command Registry (11 commands, 14 skills, 5 agents)

### Start Here
| Command | Description |
|---------|-------------|
| `start` | Guided walkthrough — picks the right commands based on what you're working on |

### Research & Discovery (Phase 1)
| Command | Description |
|---------|-------------|
| `brainstorm` | Interactive exploration of a problem space before formal definition |
| `synthesize-research` | Synthesize raw user research into themes, personas, problem statements |
| `discover` | Analyze a codebase: technical inventory, business explainer, or both |
| `workshop-prep` | Generate workshop agendas and facilitation materials |
| `generate-requirements` | Generate user stories, AC from problem statements |

### Definition (Phase 2)
| Command | Description |
|---------|-------------|
| `define` | Define solution artifacts: data models, API contracts, event specs, NFRs, operating model, migration path |

### Planning & Architecture (Phase 3)
| Command | Description |
|---------|-------------|
| `architecture` | Facilitate architecture decisions with tradeoff matrices |
| `piplan` | Prepare for SAFe PI Planning ceremony |

### Review (Any Phase)
| Command | Description |
|---------|-------------|
| `review` | Quick status, deep completeness/cross-reference, or multi-perspective stakeholder review |
| `help` | Display command registry and workflow guidance |

## Workflow Chain

```
brainstorm → synthesize-research → discover → generate-requirements → define → review → architecture → piplan
```

## Skills (14)

research-synthesizer, requirements-generator, workshop-prep, codebase-discovery, code-explainer, nfr-definition, canonical-data, api-contracts, event-integration, operating-model, migration-path, pi-planning, market-sizing, win-loss-analysis

## Agents (5)

| Agent | Role |
|-------|------|
| `theme-extractor` | Parallel theme extraction from research sources |
| `institutional-knowledge-check` | Senior review for gaps and blind spots |
| `completeness-checker` | Single artifact review against checklists + domain flags |
| `cross-reference-checker` | Cross-artifact consistency and traceability |
| `perspective-reviewer` | Multi-perspective stakeholder review (CTO, UX, Sales, Executive, Devil's Advocate) |

## Operating Rules

- Commands that create artifacts update `solution_state.md` if it exists
- Commands suggest the next logical command in the workflow chain
- `review` launches completeness-checker + cross-reference-checker in parallel, or perspective-reviewer agents for stakeholder review
- Skills are domain knowledge (~30 lines), not workflows
- All NFRs follow the format: Quality + Target + Conditions + Measurement
- The `define` command enforces: ASKS FOR = API, HAPPENS = event
- NFRs without measurable targets are rejected and rewritten

## Directory Structure

```
.claude-plugin/plugin.json
references/
  domain-knowledge-base.md       # generic checklists (stable)
  domain-knowledge.md            # investment management domain knowledge
  team-context.md                # your team's systems, custodians, org (fill in)
  solution-state-template.md
commands/        (11 command files)
skills/          (14 skill directories)
agents/          (5 agent files)
```

## Installation

```bash
claude plugin marketplace add https://github.com/dakotaradigan/Solution-Manager-Plugin
claude plugin install solution-work@solution-manager-plugin
claude plugin enable solution-work@solution-manager-plugin
```

Restart Claude Code after installing.

## Versioning

Update on every change:
1. `.claude-plugin/plugin.json` — bump version (semver)
2. `CHANGELOG.md` — document changes
3. `README.md` — update component counts
