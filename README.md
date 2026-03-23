# Solution Manager Toolkit

Turn vague product problems into spec'd, reviewed, ready-to-build solution artifacts — without leaving your terminal.

An AI plugin for [Claude Code](https://claude.com/claude-code) built for investment management teams. It walks you through structured PM workflows and writes the output as markdown files you own.

## One Command to Remember

```
/solution-work:start
```

It asks what you're working on and runs the right workflow. That's it.

## When Would I Use This?

**"We got a new client request and I need to think it through."**
Run `/solution-work:start` → "Exploring a new problem" → It asks about the problem, stakeholders, constraints, and market opportunity. Outputs a brainstorm summary with approaches, tradeoffs, and open questions.

**"I have 5 interview transcripts and need to make sense of them."**
Run `/solution-work:synthesize-research` → It reads all files in parallel, extracts themes, builds personas, writes problem statements. Every finding traces back to its source.

**"We need to define the data model and APIs before the team starts building."**
Run `/solution-work:define` → Pick what to define (data model, API contract, event spec, NFRs, operating model, migration path). It walks you through each one with investment management defaults baked in.

**"Is our solution complete? What are we missing?"**
Run `/solution-work:review` → Pick your review type:
- **Status** — quick progress check
- **Deep** — parallel agents check every artifact against checklists
- **Stakeholder** — 5 AI agents simultaneously review your work as CTO, UX Lead, Sales, Executive, and Devil's Advocate. Surfaces where they agree, where they conflict, and what everyone missed.

**"We have PI Planning next week."**
Run `/solution-work:piplan` → Breaks features into sprint-sized work, scores priorities with WSJF, maps cross-team dependencies, drafts PI objectives.

**"We lost that RFP — what happened?"**
Run `/solution-work:review` at Phase 5 → It uses the win/loss analysis framework: decision factors, competitive positioning, what worked, what didn't, actionable changes.

## How It Works

```
You describe a problem
    ↓
The toolkit asks structured questions
    ↓
It writes markdown files as output
    ↓
It suggests what to run next
```

Each command produces files and tells you the next step. The natural flow:

```
brainstorm → synthesize-research → generate-requirements → define → review → piplan
```

You don't have to follow the chain. Jump to any command directly if you know what you need.

## Install

```bash
claude plugin marketplace add https://github.com/dakotaradigan/Solution-Manager-Plugin
claude plugin install solution-work@solution-manager-plugin
claude plugin enable solution-work@solution-manager-plugin
# Restart Claude Code
```

## All Commands

| When you need to... | Run this |
|---------------------|----------|
| Figure out where to start | `/solution-work:start` |
| Explore a problem before committing | `/solution-work:brainstorm` |
| Make sense of interviews or surveys | `/solution-work:synthesize-research` |
| Understand an existing codebase | `/solution-work:discover` |
| Prepare workshop materials | `/solution-work:workshop-prep` |
| Write user stories and acceptance criteria | `/solution-work:generate-requirements` |
| Define data models, APIs, events, NFRs | `/solution-work:define` |
| Make architecture decisions with tradeoffs | `/solution-work:architecture` |
| Prepare for SAFe PI Planning | `/solution-work:piplan` |
| Check completeness or get stakeholder perspectives | `/solution-work:review` |
| See all commands | `/solution-work:help` |

Or just type `/solution` in Claude Code and browse the command palette.

## What Are Skills and Agents?

You never need to invoke these directly — they work behind the scenes.

**Skills** are domain knowledge (~30 lines each). When a command needs to know about TAM/SAM/SOM market sizing or NFR formats, it references the right skill automatically. There are 14 skills covering everything from API contracts to win/loss analysis.

**Agents** are parallel workers. When you run a stakeholder review, the plugin launches 5 agents simultaneously — one per perspective. When you run a deep review, it launches completeness checkers in parallel for every artifact. There are 5 agents that handle the heavy lifting.

## Team Setup

The toolkit ships with investment management domain knowledge. To get the most out of it, fill in your team's context.

| File | What It Contains | Action |
|------|-----------------|--------|
| `references/domain-knowledge.md` | Investment management domain knowledge | Review and extend for your firm |
| `references/team-context.md` | **Your team's systems, org structure** | **Fill in for your team** |
| `references/domain-knowledge-base.md` | Generic checklists and review patterns | Keep as-is |

Commands still work without team context — you just get more specific outputs the more you fill in.

## Try It

The repo includes sample data so you can test without your own files.

```bash
git clone https://github.com/dakotaradigan/Solution-Manager-Plugin.git
cd Solution-Manager-Plugin/sample-data
```

**Brainstorm a problem** — A forwarded email from an RM about a $50M prospect transitioning into direct indexing, plus a Slack thread debating tax budgets and wash sales.
```bash
cd brainstorm && /solution-work:brainstorm
```

**Discover a codebase** — A Python transition analysis platform with data models, API endpoints, and a tax calculator.
```bash
cd codebase && /solution-work:discover
```

**Synthesize research** — 3 interviews, a 31-person survey, and workshop notes from a transition analysis workflow discovery.
```bash
cd research && /solution-work:synthesize-research
```

Each command produces output files and suggests what to run next.

## Updating

```bash
claude plugin marketplace update solution-manager-plugin
claude plugin update solution-work@solution-manager-plugin
# Restart Claude Code
```

## Optional: MCP Server Integrations

The plugin works standalone with local markdown files. To push outputs to external tools:

| Tool | MCP Server | What It Enables |
|------|-----------|----------------|
| Jira | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Create epics and stories from generated requirements |
| Confluence | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Publish research summaries and requirements docs |
| Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) | Push persona boards, theme clusters, and workshop structures |

## License

MIT
