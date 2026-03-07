# Solution Manager Toolkit

AI-assisted tools for the solution management workflow: user research synthesis, requirements generation, and workshop preparation.

Plugin name: `solution-work` — commands are invoked as `/solution-work:<command>`.

## Directory Structure

```
.claude-plugin/
  plugin.json          # Plugin metadata — "name" field sets the /solution-work: prefix

commands/
  synthesize-research.md   # /solution-work:synthesize-research
  generate-requirements.md # /solution-work:generate-requirements
  workshop-prep.md         # /solution-work:workshop-prep

skills/
  research-synthesizer/SKILL.md    # Research synthesis skill
  requirements-generator/SKILL.md  # Requirements generation skill
  workshop-prep/SKILL.md           # Workshop preparation skill

agents/
  theme-extractor.md              # Agent for parallel theme extraction across sources
  institutional-knowledge-check.md # Senior review agent for gap analysis and blind spots
```

## Installation

```bash
claude plugin marketplace add https://github.com/dakotaradigan/PM-Tools
claude plugin install solution-work@pm-tools
claude plugin enable solution-work@pm-tools
```

Restart Claude Code after installing.

## Versioning

Update all three on every change:
1. `.claude-plugin/plugin.json` — bump version (semver)
2. `CHANGELOG.md` — document changes
3. `README.md` — update component counts
