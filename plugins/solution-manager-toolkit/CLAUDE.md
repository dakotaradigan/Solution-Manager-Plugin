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

## Installation (for Claude Code agents)

To install this plugin for a user:

1. Clone the repo to a local directory
2. Create symlink: `ln -s <repo-path>/plugins/solution-manager-toolkit ~/.claude/plugins/local/solution-work`
3. Add `"solution-work@local"` entry to `~/.claude/plugins/installed_plugins.json`
4. Add `"solution-work@local": true` to `enabledPlugins` in `~/.claude/settings.json`
5. User must restart Claude Code

The symlink name MUST be `solution-work` (matching the `name` in `plugin.json`).

## Versioning

Update all three on every change:
1. `.claude-plugin/plugin.json` — bump version (semver)
2. `CHANGELOG.md` — document changes
3. `README.md` — update component counts
