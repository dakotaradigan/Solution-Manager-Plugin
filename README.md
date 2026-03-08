# Solution Manager Toolkit

Turn vague product problems into spec'd, reviewed, ready-to-build solution artifacts — without leaving your terminal.

This is an AI plugin for investment management teams. You type slash commands, it walks you through structured workflows and writes the output as markdown files you can version, share, and build from. Backed by 16 commands, 4 agents, and 10 skills that handle everything from messy problem intake to ready-to-build artifacts. Don't know slash commands? Just describe what you need — the plugin picks the right skill and runs it automatically.

## Quick Start

```bash
# Install (one time)
claude plugin marketplace add https://github.com/dakotaradigan/Solution-Manager-Plugin
claude plugin install solution-work@solution-manager-plugin
claude plugin enable solution-work@solution-manager-plugin
# Restart Claude Code
```

Then run:

```
/solution-work:start
```

It asks what you're working on, picks the right workflow, and walks you through each step. That's the only command you need to remember. Don't have your own data yet? [Try it with the sample data below.](#try-it)

If you already know what you want, jump straight to any command:

```
/solution-work:brainstorm       # "We have a problem but haven't scoped it yet"
/solution-work:discover         # "We have a codebase — what's in it?"
/solution-work:synthesize-research  # "We have interview notes / survey data"
/solution-work:help             # "Show me everything"
```

Type `/solution` and the command palette shows every available command with descriptions:

```
> /solution

  /solution-work:start              Guided walkthrough — tell me what you're working on and I'll run the right commands
  /solution-work:brainstorm         Interactive exploration of a problem space before formal definition
  /solution-work:discover           Analyze an existing codebase to extract data models, API endpoints, dependencies
  /solution-work:explain-code       Explain what code does in plain, non-technical language
  /solution-work:synthesize-research  Synthesize raw user research into themes, personas, problem statements
  /solution-work:generate-requirements  Generate user stories, acceptance criteria from problem statements
  /solution-work:datamodel          Define canonical data models with governance
  /solution-work:apicontract        Define contract-first API specifications
  /solution-work:eventspec          Define event schemas with delivery guarantees
  /solution-work:nfr                Define non-functional requirements with measurable targets
  /solution-work:architecture       Facilitate architecture decisions with tradeoff matrices
  /solution-work:piplan             Prepare for SAFe PI Planning with WSJF prioritization
  /solution-work:workshop-prep      Generate workshop agendas and facilitation materials
  /solution-work:review             Run completeness and cross-reference checks across all artifacts
  /solution-work:status             Generate solution progress report
  /solution-work:help               Display command registry and workflow guidance
```

You describe a problem. The toolkit walks you through defining it. Every output is a markdown file. Nothing is locked in a tool — you own the artifacts.

## Team Setup

The toolkit ships with investment management domain knowledge (instruments, regulations, failure modes). To get the most out of it, fill in your team's specific context.

| File | What It Contains | Action |
|------|-----------------|--------|
| `references/domain-knowledge-base.md` | Generic checklists, NFR format, review patterns | Keep as-is |
| `references/domain-knowledge.md` | Investment management domain knowledge | Review and extend for your firm |
| `references/team-context.md` | **Your team's systems, org structure** | **Fill in for your team** |

Commands still work without team context — you just get more grounded outputs the more you fill in.

## Updating

```bash
claude plugin marketplace update solution-manager-plugin
claude plugin update solution-work@solution-manager-plugin
# Restart Claude Code
```

## Uninstall

```bash
claude plugin uninstall solution-work@solution-manager-plugin
```

## Try It

The repo includes sample data so you can test the plugin without your own files. Clone it and pick a path:

```bash
git clone https://github.com/dakotaradigan/Solution-Manager-Plugin.git
cd Solution-Manager-Plugin/sample-data
```

### Option 1: Brainstorm a problem

There's a messy intake — a forwarded email about a bad fill from stale pricing, plus a Slack thread where three people notice Bloomberg, Refinitiv, and the internal system all show different prices.

```bash
cd brainstorm
# Open Claude Code, then:
/solution-work:brainstorm
# When asked what you're exploring, point it at problem-brief.md
```

### Option 2: Discover a codebase

There's a Python portfolio management app with data models, 15 API endpoints, custodian recon, and drift calculation.

```bash
cd codebase
# Open Claude Code, then:
/solution-work:discover
```

### Option 3: Synthesize user research

There are 5 research files — 3 interviews (trader, ops manager, quant), a 34-person survey, and workshop notes — all from a market data platform discovery.

```bash
cd research
# Open Claude Code, then:
/solution-work:synthesize-research
```

Each command produces output files and suggests what to run next. Or just run `/solution-work:start` and it will figure out which sample data to use.

## Optional: MCP Server Integrations

The plugin works standalone with local markdown files. To push outputs to external tools, configure these MCP servers:

| Tool | MCP Server | What It Enables |
|------|-----------|----------------|
| Jira | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Create epics and stories from generated requirements |
| Confluence | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Publish research summaries and requirements docs |
| Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) | Push persona boards, theme clusters, and workshop structures |

## License

MIT
