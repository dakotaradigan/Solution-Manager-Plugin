---
name: synthesize-research
description: Synthesize raw user research into structured problem statements, personas, and theme matrices
allowed-tools: Read, Glob, Grep, Write, Agent, Bash
user-invocable: true
---

# Synthesize Research

Run user research synthesis on raw notes dropped into a research folder.

## Input folder

Look for a `research/` directory in the current working directory. This is the default location where users drop their raw notes — meeting transcripts, interview notes, survey exports, workshop captures, or any other unstructured text. If `research/` does not exist, ask the user where their notes are.

Users should not need to format, rename, or structure their files. The notes may be messy copy-pastes from meetings, transcripts, or freeform observations. Accept any `.md`, `.txt`, or `.csv` file found in `research/` (including subdirectories).

## Steps

1. **Discover source files** — Use Glob to find all files matching `research/**/*.md`, `research/**/*.txt`, and `research/**/*.csv`. If no files are found, tell the user to create a `research/` folder and drop their notes in.

2. **Classify each source** — Read each file and determine its type based on content (not filename). Classify as one of:
   - **Interview / 1:1** — conversation with a single participant
   - **Survey** — quantitative responses, ratings, or structured feedback
   - **Workshop / group session** — multi-participant discussion or exercise
   - **Meeting notes** — general meeting notes, standups, or status updates
   - **Other** — anything that doesn't fit the above

   Present the classified file list to the user and ask them to confirm or correct before proceeding.

3. **Launch parallel theme extraction** — Use the Agent tool with the `theme-extractor` agent to process each source file in parallel. Each agent reads the raw content, extracts observations, identifies the participant role/segment where possible, tags findings by topic and sentiment, and returns structured results. The agent should handle messy, unstructured input gracefully.

4. **Synthesize across sources** — Merge the extracted themes, cluster them, identify cross-source patterns, and surface contradictions between segments.

5. **Generate artifacts** — Write the following to a `synthesis/` directory:
   - `research-summary.md` — Executive summary, methodology, top findings, theme matrix
   - `personas.md` — Persona cards derived from the data
   - `problem-statements.md` — Ranked problem statements with HMW questions
   - `theme-matrix.md` — Theme x Source traceability table

6. **Institutional knowledge review** — Launch the `institutional-knowledge-check` agent to review the synthesized outputs. This agent stress-tests the findings for coverage gaps, organizational blind spots, missing data points, and priority challenges. Write the review to `synthesis/institutional-review.md`.

7. **Present results** — Show the user a summary of findings, the institutional review highlights, and where the output files were written.

## Important

- Every finding must trace to a specific source file. Do not invent data.
- Flag contradictions between user segments — these are design tensions, not errors.
- If quantitative data (scores, NPS) exists, integrate it with qualitative themes.
- Do not require users to format or structure their input files. Handle raw, unstructured notes.
