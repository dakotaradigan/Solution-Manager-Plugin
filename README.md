# Solution Manager Toolkit

Turn vague product problems into spec'd, reviewed, ready-to-build solution artifacts — without leaving your terminal.

This is a Claude Code plugin for investment management teams. You type slash commands, it walks you through structured workflows and writes the output as markdown files you can version, share, and build from.

## Quick Start

```bash
# Install (one time)
claude plugin marketplace add https://github.com/dakotaradigan/PM-Tools
claude plugin install solution-work@pm-tools
claude plugin enable solution-work@pm-tools
# Restart Claude Code
```

Then run:

```
/solution-work:start
```

It asks what you're working on, picks the right workflow, and walks you through each step. That's the only command you need to remember.

If you already know what you want, jump straight to any command:

```
/solution-work:brainstorm       # "We have a problem but haven't scoped it yet"
/solution-work:discover         # "We have a codebase — what's in it?"
/solution-work:synthesize-research  # "We have interview notes / survey data"
/solution-work:help             # "Show me everything"
```

Typing `/solution-work:` shows all available commands in a dropdown.

## What You Get

You describe a problem. The toolkit walks you through defining it:

```
/solution-work:brainstorm           → brainstorm/topic-summary.md
/solution-work:synthesize-research  → synthesis/themes, personas, problem statements
/solution-work:discover             → discovery/entities, APIs, dependencies
/solution-work:generate-requirements → requirements/user stories + acceptance criteria
/solution-work:datamodel            → data-model/canonical entities + governance
/solution-work:apicontract          → api-contracts/endpoints + schemas
/solution-work:eventspec            → event-specs/schemas + delivery guarantees
/solution-work:nfr                  → requirements/NFRs with measurable targets
/solution-work:review               → review/completeness scores + cross-reference gaps
/solution-work:architecture         → architecture/ADRs with tradeoff matrices
/solution-work:piplan               → pi-planning/features, WSJF, dependencies, risks
/solution-work:workshop-prep        → workshop materials + facilitation guides
/solution-work:status               → progress summary across all artifacts
/solution-work:help                 → command reference
```

Every output is a markdown file. Nothing is locked in a tool — you own the artifacts.

## The Workflow

You don't have to run everything. Start wherever you are:

```
brainstorm → synthesize-research → discover → datamodel → apicontract
→ eventspec → nfr → review → architecture → piplan
```

Most teams start with `brainstorm` or `discover`, run 3-4 commands, then `review` to find gaps.

## Team Setup

The toolkit ships with investment management domain knowledge (instruments, regulations, failure modes). To get the most out of it, fill in your team's specific context.

| File | What It Contains | Action |
|------|-----------------|--------|
| `references/domain-knowledge-base.md` | Generic checklists, NFR format, review patterns | Keep as-is |
| `references/domain-knowledge.md` | Investment management domain knowledge | Review and extend for your firm |
| `references/team-context.md` | **Your team's systems, org structure** | **Fill in for your team** |

Commands still work without team context — you just get more grounded outputs the more you fill in.

## Uninstall

```bash
claude plugin uninstall solution-work@pm-tools
```

## Try with Sample Data

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
