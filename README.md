# Tool Kit

AI-assisted solution management tools built as Claude Code skills and plugins. These tools accelerate the solution management workflow — user research synthesis, requirements generation, and workshop preparation — while keeping human judgment at the center.

## Contents

### Skills (standalone)

| Skill | Description |
|-------|-------------|
| [user-research-synthesizer](skills/user-research-synthesizer/) | Synthesize raw user research into structured problem statements, personas, and themes |

### Plugins (full packages)

| Plugin | Description | Components |
|--------|-------------|------------|
| [solution-manager-toolkit](plugins/solution-manager-toolkit/) | End-to-end solution management workflow | 3 commands, 3 skills, 2 agents |

### Sample Data

| Dataset | Description |
|---------|-------------|
| [Market Data Platform Research](sample-data/) | Synthetic interview notes, workshop transcripts, and survey results for a market data platform discovery |

---

## How Claude Code Skills and Plugins Work

If you're new to Claude Code extensibility, this section explains the building blocks and how they fit together.

### The Building Blocks

There are four types of components. Each does something different:

| Component | What It Is | How It Activates | Lives Where |
|-----------|-----------|-------------------|-------------|
| **Skill** | Domain knowledge — teaches Claude *how to think* about a topic | Automatically, when Claude matches your request to the skill's description | `skills/<name>/SKILL.md` |
| **Command** | A step-by-step workflow with explicit instructions | Manually, when you type a slash command like `/synthesize-research` | `commands/<name>.md` |
| **Agent** | A subtask worker that runs in a separate process | Called by a command or skill when parallel/isolated work is needed | `agents/<name>.md` |
| **Plugin** | A package that bundles commands, skills, and agents together | Installed once, then all its components are available | `.claude-plugin/plugin.json` + everything above |

### Skills — Domain Knowledge That Activates Automatically

A skill is a single `SKILL.md` file that teaches Claude domain expertise. Once installed, Claude draws on it whenever relevant — no slash command needed.

**Example:** You install the `user-research-synthesizer` skill. Now you can just say:

```
You: "I just finished 3 user interviews, can you help me
      pull out the key themes and build personas?"
```

Claude reads your request, matches it to the skill's description ("synthesize raw user research into structured problem statements, personas, and themes"), and activates the skill. It now knows the full process — how to extract observations, cluster themes, build persona cards, generate problem statements with HMW questions, and check its own work for quality.

You didn't type a slash command. Claude just recognized this was its area.

**What a SKILL.md file looks like:**

```markdown
---
name: user-research-synthesizer
description: This skill should be used when synthesizing raw user
  research into structured problem statements, personas, and themes.
user-invocable: true
---

# User Research Synthesizer

## Supported Input Types
- Interview notes
- Workshop transcripts
- Survey responses

## Core Process
### Phase 1: Intake & Inventory
[Steps Claude follows...]

### Phase 2: Theme Extraction
[How to extract and tag observations...]

### Phase 3: Persona Synthesis
[Persona card format and rules...]
```

The `description` field in the YAML header is the trigger — it tells Claude when this skill is relevant. The rest is the playbook Claude follows.

### Commands — Explicit Workflows You Call With `/`

A command is a step-by-step recipe that runs when you type a slash command. Commands can reference skills for domain knowledge and launch agents for subtasks.

**Example:**

```
You: /synthesize-research
```

Claude loads the `synthesize-research.md` command file and follows its steps:
1. Ask where your research files are
2. Inventory what it finds
3. Launch theme-extractor agents (one per file, in parallel)
4. Merge results across all sources
5. Generate personas, problem statements, theme matrix
6. Run the institutional knowledge review
7. Present results

**The difference from a skill:** A command is a specific, structured workflow you explicitly invoke. A skill is ambient knowledge that Claude draws on whenever it's relevant. Commands are rigid ("do step 1, then step 2"). Skills are flexible ("here's how to think about this").

### Agents — Parallel Workers for Subtasks

An agent is a worker that gets spawned as a separate subprocess. It receives a focused task, does its work in isolation, and returns results. The main use case is parallel processing.

**Example:** The `/synthesize-research` command finds 5 research files. Instead of processing them one at a time (slow, fills up context), it launches 5 `theme-extractor` agents in parallel:

```
/synthesize-research kicks off:

  Step 3: Launch theme-extractor agents in parallel
    ├── Agent 1 → processes interview-portfolio-manager-a.md
    ├── Agent 2 → processes interview-ops-manager-b.md
    ├── Agent 3 → processes interview-quant-c.md
    ├── Agent 4 → processes workshop-notes.md
    └── Agent 5 → processes survey-responses.md

  (all 5 run simultaneously)

  Step 4: Merge all agent results into unified themes
```

Each agent gets the `theme-extractor.md` file as its instructions (like a system prompt), processes its assigned file, and returns structured observations. The command then merges everything.

**Agents can also do review passes.** The `institutional-knowledge-check` agent runs after synthesis is complete — it reviews the output for coverage gaps, blind spots, and missing data points, acting as a senior reviewer.

### How They All Connect

Here's the full picture of how a single workflow flows through all the components:

```
You say: /synthesize-research
         │
         ▼
┌─────────────────────────────────┐
│  COMMAND: synthesize-research   │  ← Step-by-step orchestrator
│                                 │
│  Step 1: Find research files    │
│  Step 2: Inventory sources      │
│  Step 3: Launch agents ─────────┼──► AGENT: theme-extractor (x5)
│  Step 4: Merge results          │       Each processes one file
│  Step 5: Generate artifacts     │       in parallel, returns
│          (uses SKILL knowledge) │       structured themes
│  Step 6: Launch review ─────────┼──► AGENT: institutional-knowledge-check
│  Step 7: Present results        │       Reviews for gaps and
│                                 │       blind spots
└─────────────────────────────────┘
         │
         ▼
    Output files:
    synthesis/research-summary.md
    synthesis/personas.md
    synthesis/problem-statements.md
    synthesis/theme-matrix.md
    synthesis/institutional-review.md
```

Or without the slash command:

```
You say: "I have some interview notes, can you
          synthesize the key findings?"
         │
         ▼
┌─────────────────────────────────┐
│  SKILL: research-synthesizer    │  ← Claude works directly
│                                 │     in the main conversation
│  Knows: how to extract themes,  │
│  build personas, write problem  │
│  statements, check quality      │
│                                 │
│  (No agents, no parallel work   │
│   — Claude does it all inline)  │
└─────────────────────────────────┘
         │
         ▼
    Claude responds with the
    synthesis in the conversation
    (or writes output files)
```

### Plugins — Bundling It All Together

A plugin is a package that bundles commands, skills, and agents into one installable unit. The directory structure:

```
solution-manager-toolkit/
├── .claude-plugin/
│   └── plugin.json              ← Metadata: name, version, author
├── CLAUDE.md                    ← Instructions for Claude about this plugin
├── commands/
│   ├── synthesize-research.md   ← /synthesize-research
│   ├── generate-requirements.md ← /generate-requirements
│   └── workshop-prep.md         ← /workshop-prep
├── skills/
│   ├── research-synthesizer/
│   │   └── SKILL.md             ← Domain knowledge: research synthesis
│   ├── requirements-generator/
│   │   └── SKILL.md             ← Domain knowledge: requirements
│   └── workshop-prep/
│       └── SKILL.md             ← Domain knowledge: workshop design
├── agents/
│   ├── theme-extractor.md       ← Parallel worker: process one source
│   └── institutional-knowledge-check.md  ← Review agent: senior lens
├── README.md
└── CHANGELOG.md
```

When someone installs the plugin, they get all the commands, skills, and agents at once.

---

## Skill vs. Plugin — When to Use Which

**Build a skill when:**
- You want to teach Claude one domain area
- No multi-step orchestration needed
- Maximum portability — one file, copy and go
- Someone should get value just by talking to Claude naturally

**Build a plugin when:**
- You have multiple related workflows
- You want slash commands for structured execution
- You need agents for parallel processing or specialized review passes
- You want to distribute a cohesive toolkit

---

## Real-World Workflow Example

Here's how these tools chain together across a real project:

```
Week 1 — Prep
  You: "I have a discovery workshop next Tuesday with 2 PMs,
        a trader, and a compliance officer. Help me prep."
  → workshop-prep skill activates automatically
  → Generates: agenda, discussion prompts, pre-read

Week 1 — Run the workshop
  (You facilitate using the generated materials)
  (You take notes during the session)

Week 2 — Synthesize
  You: /synthesize-research
  → Command finds your interview notes, workshop notes, survey
  → Theme-extractor agents process each file in parallel
  → Institutional-knowledge-check agent reviews for gaps
  → Outputs: personas, problem statements, theme matrix, review

Week 2 — Generate requirements
  You: /generate-requirements
  → Reads the problem statements from synthesis
  → Outputs: user stories, acceptance criteria, NFRs
  → Every requirement traces back to the research

Week 3 — Push to tools (with MCP servers configured)
  → Requirements → Jira (epics and stories)
  → Research summary → Confluence (structured page)
  → Personas and themes → Miro (visual board)
```

Each step builds on the previous one's output files.

---

## Installation

### Install the plugin (recommended)

In Claude Code, run:

```
/plugin marketplace add https://github.com/dakotaradigan/PM-Tools.git
/plugin install solution-work
```

Type `/solution-work` to see all commands.

### Install the standalone skill only

```bash
git clone https://github.com/dakotaradigan/PM-Tools.git
cp -r PM-Tools/skills/user-research-synthesizer ~/.claude/skills/
```

### Try it with sample data

The `sample-data/` directory contains synthetic market data platform research:
- 3 interviews (Portfolio Manager, Data Ops Manager, Quant Analyst)
- 1 workshop transcript (8-person discovery session with card sorting)
- 1 survey (34 respondents, quantitative scores + verbatims)

```bash
cd tool-kit/sample-data
# Then run /synthesize-research in Claude Code
```

---

## Optional: MCP Server Integrations

The plugin works standalone with local markdown files. To push artifacts to external tools, configure these MCP servers:

| Tool | MCP Server | What It Enables |
|------|-----------|----------------|
| Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) | Push workshop structures, persona boards, theme clusters to Miro |
| Confluence | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Publish requirements docs, research summaries to Confluence |
| Jira | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Create epics and stories from generated requirements |

These are official first-party MCP servers maintained by Miro and Atlassian.

---

## License

MIT
