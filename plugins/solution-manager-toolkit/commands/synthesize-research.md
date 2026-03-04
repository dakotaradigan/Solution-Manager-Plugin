---
name: synthesize-research
description: Synthesize raw user research into structured problem statements, personas, and theme matrices
allowed-tools: Read, Glob, Grep, Write, Agent, Bash
user-invocable: true
---

# Synthesize Research

Run user research synthesis on a set of input files.

## Steps

1. **Ask for input location** — Prompt the user for the path to their research files (interview notes, survey responses, workshop notes). Default to looking in the current directory.

2. **Inventory sources** — Use Glob to find all markdown/text files in the input path. Present the list and ask the user to confirm which files to include.

3. **Launch parallel theme extraction** — Use the Agent tool with the `theme-extractor` agent to process each source file in parallel. Each agent extracts observations, tags them by segment/sentiment/topic, and returns structured findings.

4. **Synthesize across sources** — Merge the extracted themes, cluster them, identify cross-source patterns, and surface contradictions between segments.

5. **Generate artifacts** — Write the following to a `synthesis/` directory:
   - `research-summary.md` — Executive summary, methodology, top findings, theme matrix
   - `personas.md` — Persona cards derived from the data
   - `problem-statements.md` — Ranked problem statements with HMW questions
   - `theme-matrix.md` — Theme x Source traceability table

6. **Institutional knowledge review** — Launch the `institutional-knowledge-check` agent to review the synthesized outputs. This agent stress-tests the findings for coverage gaps, organizational blind spots, missing data points, and priority challenges. Write the review to `synthesis/institutional-review.md`.

7. **Present results** — Show the user a summary of findings, the institutional review highlights, and where the output files were written.

## Important

- Every finding must trace to a specific source. Do not invent data.
- Flag contradictions between user segments — these are design tensions, not errors.
- If quantitative data (scores, NPS) exists, integrate it with qualitative themes.
