# Solution Manager Toolkit

A Claude Code plugin that turns raw user research into structured deliverables — synthesized themes, personas, requirements docs, and workshop materials — in minutes instead of days.

## What It Does

Three commands that chain together across the solution management workflow:

| Command | What It Does |
|---------|-------------|
| `/solution-work:synthesize-research` | Processes interview notes, survey data, and workshop transcripts into personas, problem statements, and a theme matrix. Runs parallel agents to extract themes from each source simultaneously, then merges and cross-references findings. |
| `/solution-work:generate-requirements` | Takes the synthesized problem statements and generates user stories (with MoSCoW priority), acceptance criteria, and non-functional requirements — all traced back to the original research. |
| `/solution-work:workshop-prep` | Generates a timed agenda, facilitation prompts, and a pre-read doc based on your workshop type (discovery, validation, prioritization, or design) and participant roles. |

Each command also has a matching **skill** that activates automatically when you describe the task in plain language — no slash command needed.

## Example

```
# Drop your raw research files into a research/ folder
mkdir research
cp ~/Downloads/interview-notes-*.md research/
cp ~/Downloads/survey-export.csv research/

# Run synthesis — agents process each file in parallel
> /solution-work:synthesize-research

  Step 1: Found 5 files in research/
  Step 2: Classified — 3 interviews, 1 survey, 1 workshop transcript
  Step 3: Launching 5 theme-extractor agents in parallel...
  Step 4: Merged 47 observations into 8 themes
  Step 5: Generated personas, problem statements, theme matrix
  Step 6: Institutional knowledge review — 2 coverage gaps flagged

  Output written to synthesis/

# Generate requirements from the synthesis
> /solution-work:generate-requirements

  Reading synthesis/problem-statements.md...
  Generated 24 user stories, 68 acceptance criteria, 9 NFRs

  Output written to requirements/

# Prep for next week's validation workshop
> /solution-work:workshop-prep

  Workshop type: validation
  Duration: 90 minutes
  Participants: 2 PMs, 1 trader, 1 compliance officer

  Output written to workshop/
```

Your notes can be messy — raw copy-pastes from meetings, unformatted transcripts, freeform observations. The plugin handles unstructured input.

## Installation

### 1. Add the marketplace

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

### Try with sample data

The repo includes synthetic research data (3 interviews, 1 workshop transcript, 1 survey) for a market data platform discovery:

```bash
git clone https://github.com/dakotaradigan/PM-Tools.git
cd PM-Tools/sample-data
# Open Claude Code and run /solution-work:synthesize-research
```

## Optional: MCP Server Integrations

The plugin works standalone with local markdown files. To push outputs to external tools, configure these MCP servers:

| Tool | MCP Server | What It Enables |
|------|-----------|----------------|
| Jira | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Create epics and stories from generated requirements |
| Confluence | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Publish research summaries and requirements docs |
| Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) | Push persona boards, theme clusters, and workshop structures |

## License

MIT
