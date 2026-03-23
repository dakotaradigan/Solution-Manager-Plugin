# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-03-22

### Added
- **Multi-perspective stakeholder review** — New review type launching up to 5 parallel perspective-reviewer agents (CTO, UX Lead, Sales, Executive, Devil's Advocate) with inline synthesis. Users can select which perspectives to run. Surfaces agreements, conflicts, and blind spots across perspectives.
- **Market sizing skill** — TAM/SAM/SOM domain knowledge with investment management defaults (fee rates, channels, gatekeepers). Referenced from brainstorm command.
- **Win/loss analysis skill** — Structured post-decision analysis framework for RFPs and competitive outcomes. Referenced from review command at Phase 5.
- New agent: `perspective-reviewer`
- New skills: `market-sizing`, `win-loss-analysis`

### Changed
- `review` command now offers 3 review types: status, deep, stakeholder
- `brainstorm` command references market-sizing skill in approach exploration
- `solution-state-template.md` adds `stakeholder` key under review_findings

## [0.2.0] - 2026-03-07

### Added
- **Domain & team knowledge architecture** — `domain-knowledge-base.md` (generic checklists) + `domain-knowledge.md` (investment management domain) + `team-context.md` (fillable template for team-specific systems, custodians, org structure)
- `solution-state-template.md` — persistent state tracking template
- `references/team-context.md` — fillable template for team-specific operational knowledge (systems, custodians, teams, codebase conventions, vendor integrations, stakeholders)
- 12 new commands:
  - `start` — guided walkthrough that picks the right workflow based on what you're working on
  - `brainstorm` — interactive problem space exploration before formal definition
  - `discover` — codebase comprehension (data models, APIs, dependencies)
  - `datamodel` — canonical data model definition with governance
  - `apicontract` — contract-first API specifications
  - `eventspec` — event schemas with delivery guarantees
  - `nfr` — non-functional requirements with domain-specific defaults
  - `piplan` — SAFe PI Planning preparation
  - `review` — parallel completeness + cross-reference review
  - `architecture` — tradeoff matrices and ADRs
  - `status` — solution progress reports
  - `help` — command registry display
- 6 new skills: codebase-discovery, nfr-definition, canonical-data, api-contracts, event-integration, pi-planning
- 2 new agents: completeness-checker, cross-reference-checker
- Domain knowledge enriched with investment management content (direct indexing, TLH, overlay strategies, SMA/UMA, lot-level tracking, custodian recon)
- Commands reference `team-context.md` for team-specific context (discover, piplan, architecture, review, completeness-checker, institutional-knowledge-check)
- CLAUDE.md rewritten with 6 architecture principles, full 15-command registry, operating rules

### Changed
- Plugin description updated for v0.2.0
- README rewritten with team setup section
- Removed cross-industry portability language — toolkit is focused on investment management with team-level customization

## [0.1.0] - 2026-03-04

### Added
- Initial release
- `synthesize-research` command — research synthesis from raw inputs
- `generate-requirements` command — user stories, AC, and NFRs from problem statements
- `workshop-prep` command — agenda, prompts, and pre-read generation
- `research-synthesizer` skill
- `requirements-generator` skill
- `workshop-prep` skill
- `theme-extractor` agent for parallel source processing
