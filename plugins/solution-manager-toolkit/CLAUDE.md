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

## Domain & Team Knowledge Architecture

| File | Purpose | Action |
|------|---------|--------|
| `references/domain-knowledge-base.md` | Generic checklists, NFR format, review patterns | Stable — extend but don't remove |
| `references/domain-knowledge.md` | Investment management domain knowledge (instruments, regulations, failure modes) | Review and extend for your firm's specifics |
| `references/team-context.md` | Your team's systems, custodians, org structure, codebase conventions | **Fill in for your team** |

Commands reference `base` and `domain-knowledge` by section heading. Required sections in domain-knowledge: Domain Identifiers, NFR Defaults, Regulatory Requirements, Common Failure Modes, Domain Validation Flags. Missing sections degrade gracefully (commands skip domain checks, don't crash). Team context is optional but enriches discover, piplan, architecture, and review.

## Command Registry (16 commands)

### Start Here
| Command | Description |
|---------|-------------|
| `start` | Guided walkthrough — picks the right commands based on what you're working on |

### Research & Discovery
| Command | Description |
|---------|-------------|
| `synthesize-research` | Synthesize raw user research into themes, personas, problem statements |
| `discover` | Analyze codebase for data models, APIs, dependencies |
| `explain-code` | Explain what code does in plain, non-technical language |
| `brainstorm` | Interactive exploration of a problem space before formal definition |

### Definition
| Command | Description |
|---------|-------------|
| `generate-requirements` | Generate user stories, AC from problem statements |
| `datamodel` | Define canonical data models with governance |
| `apicontract` | Define contract-first API specifications |
| `eventspec` | Define event schemas with delivery guarantees |
| `nfr` | Define non-functional requirements with measurable targets |

### Planning & Architecture
| Command | Description |
|---------|-------------|
| `workshop-prep` | Generate workshop agendas and facilitation materials |
| `piplan` | Prepare for SAFe PI Planning ceremony |
| `architecture` | Facilitate architecture decisions with tradeoff matrices |

### Review & Status
| Command | Description |
|---------|-------------|
| `review` | Run completeness and cross-reference checks on all artifacts |
| `status` | Generate solution progress report |
| `help` | Display command registry and workflow guidance |

## Workflow Chain

```
brainstorm → synthesize-research → discover → datamodel → apicontract → eventspec → nfr → review → architecture → piplan
```

## Skills (10)

research-synthesizer, requirements-generator, workshop-prep, codebase-discovery, code-explainer, nfr-definition, canonical-data, api-contracts, event-integration, pi-planning

## Agents (4)

| Agent | Role |
|-------|------|
| `theme-extractor` | Parallel theme extraction from research sources |
| `institutional-knowledge-check` | Senior review for gaps and blind spots |
| `completeness-checker` | Single artifact review against checklists + domain flags |
| `cross-reference-checker` | Cross-artifact consistency and traceability |

## Operating Rules

- Commands that create artifacts update `solution_state.md` if it exists
- Commands suggest the next logical command in the workflow chain
- `review` launches completeness-checker + cross-reference-checker in parallel
- Skills are domain knowledge (~30 lines), not workflows
- All NFRs follow the format: Quality + Target + Conditions + Measurement

## Directory Structure

```
.claude-plugin/plugin.json
references/
  domain-knowledge-base.md       # generic checklists (stable)
  domain-knowledge.md            # investment management domain knowledge
  team-context.md                # your team's systems, custodians, org (fill in)
  solution-state-template.md
commands/        (16 command files)
skills/          (10 skill directories)
agents/          (4 agent files)
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
