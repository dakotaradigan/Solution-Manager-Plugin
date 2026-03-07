---
name: solution-work:explain-code
description: Analyze a codebase and explain what it does in plain, non-technical language for business stakeholders
allowed-tools: Read, Glob, Grep, Write, Bash, Agent
user-invocable: true
---

# Explain Code

Read code and produce a plain-language explanation of what it does — written for people who don't read code. Reference the code-explainer skill for translation rules and principles.

## Steps

1. **Find the code** — Determine what to analyze:

   a. **Check the current directory** — Use Glob to look for source code files and project markers (`package.json`, `requirements.txt`, `Gemfile`, `pom.xml`, `go.mod`, etc.).

   b. **If code is found** — Tell the user what you see and confirm:
      - "I see a [language/framework] project here with [brief description]. Should I explain this?"
      - Wait for confirmation before proceeding.

   c. **If no code is found** — Ask the user:
      - "I don't see code in the current directory. Point me at a file path, directory, or GitHub repo URL."

   d. **If the user provides a GitHub URL** — Clone it to a temp directory using Bash, then scan from there.

   e. **If the user provides a single file** — Read that file and scope the explanation to just what that file does.

2. **Load context** — Read `references/team-context.md` and `references/domain-knowledge.md` if available. These help translate technical concepts into the right business language.

3. **Scan and explain** — Use Glob, Grep, and Read to understand the code. Apply the code-explainer skill to translate findings into business language. Identify the business purpose, trace key workflows, map integrations, and surface gaps.

4. **Write the explanation** — Write to `discovery/`:
   - `discovery/business-explainer.md` for a full codebase
   - For a single file, use a simpler format focused on what that file does

   Follow the output structure from the code-explainer skill: one-paragraph summary, who uses it, what it does (as workflows), where information flows, what it doesn't do, and questions it raises.

5. **Update solution state** — If `solution_state.md` exists, note that a business explainer has been produced.

6. **Suggest next steps** — Based on findings:
   - Significant gaps → `brainstorm`
   - Codebase well-understood → `discover` for full technical inventory
   - Stakeholders need alignment → `workshop-prep`

## Important

- Always confirm with the user before scanning — never assume they want the current directory analyzed.
- This is a complement to `discover`, not a replacement. `discover` produces technical inventory; `explain-code` produces business narrative.
- Reference the code-explainer skill for all translation and writing guidance.
