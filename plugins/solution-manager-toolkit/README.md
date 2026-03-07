# Solution Manager Toolkit

A Claude Code plugin for AI-assisted solution management — accelerating user research synthesis, requirements generation, and workshop preparation.

## What This Does

This plugin automates the repetitive parts of the solution management workflow while keeping human judgment at the center:

| Command | What It Does |
|---------|-------------|
| `/solution-work:synthesize-research` | Takes raw interview notes, survey responses, and workshop transcripts → outputs structured problem statements, persona cards, and theme matrices |
| `/solution-work:generate-requirements` | Takes synthesized problem statements → outputs user stories, acceptance criteria, and NFRs |
| `/solution-work:workshop-prep` | Takes a workshop goal and participant list → outputs timed agenda, discussion prompts, and pre-read materials |

Type `/solution-work` in Claude Code to see all available commands.

## Components

- **3 Commands** — User-invocable slash commands for each workflow step
- **3 Skills** — Domain knowledge for research synthesis, requirements, and workshop design
- **2 Agents** — Theme extractor for parallel processing + institutional knowledge reviewer for gap analysis

## Installation

### 1. Add the marketplace (one time)

```bash
claude plugin marketplace add https://github.com/dakotaradigan/PM-Tools
```

### 2. Install the plugin

```bash
claude plugin install solution-work@pm-tools
```

### 3. Enable the plugin

```bash
claude plugin enable solution-work@pm-tools
```

### 4. Restart Claude Code

Type `/solution-work` to see all available commands.

### Uninstall

```bash
claude plugin uninstall solution-work@pm-tools
```

## Usage

### Synthesize Research

Place your research files (markdown) in a directory, then:

```
/solution-work:synthesize-research
```

The command will find your files, extract themes in parallel, and generate:
- `synthesis/research-summary.md`
- `synthesis/personas.md`
- `synthesis/problem-statements.md`
- `synthesis/theme-matrix.md`

### Generate Requirements

After synthesis, run:

```
/solution-work:generate-requirements
```

Generates:
- `requirements/user-stories.md`
- `requirements/acceptance-criteria.md`
- `requirements/nfrs.md`

### Workshop Prep

```
/solution-work:workshop-prep
```

Generates:
- `workshop/agenda.md`
- `workshop/discussion-prompts.md`
- `workshop/pre-read.md`

## MCP Server Integrations (Optional)

This plugin works standalone with local files. For pushing artifacts to external tools, configure these MCP servers:

| Tool | MCP Server | What It Enables |
|------|-----------|----------------|
| Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) | Push workshop structures, persona boards, theme clusters to Miro |
| Confluence | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Publish requirements docs, research summaries to Confluence |
| Jira | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Create epics and stories from generated requirements |

## Sample Data

See `sample-data/` for synthetic market data platform research that demonstrates the full workflow.

## License

MIT
