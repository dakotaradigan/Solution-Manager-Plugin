---
name: workshop-prep
description: Generate workshop agenda, discussion prompts, and structured preparation materials
allowed-tools: Read, Glob, Grep, Write, Bash
user-invocable: true
---

# Workshop Prep

Prepare structured materials for a user research or discovery workshop.

## Steps

1. **Gather inputs** — Ask the user for:
   - Workshop goal (discovery, validation, prioritization, design)
   - Participant list or roles (e.g., "2 traders, 1 ops lead, 1 quant, 1 compliance")
   - Duration (default: 90 minutes)
   - Any context documents to review beforehand
   - Prior research (link to synthesis outputs if available)

2. **Generate agenda** — Based on goal and duration, create a timed agenda:
   - Intro & ground rules (5 min)
   - Context setting (5-10 min)
   - Core activities (chosen based on workshop type)
   - Dot voting / prioritization (10 min)
   - Wrap-up & next steps (5 min)

3. **Select activities based on workshop type:**

   **Discovery workshops:**
   - Open card sorting (participants write pain points → cluster together)
   - "Day in the life" walkthrough per role
   - Stakeholder mapping exercise

   **Validation workshops:**
   - Present problem statements → thumbs up/down/sideways
   - Priority ranking (forced rank or dot voting)
   - "What's missing?" gap analysis

   **Prioritization workshops:**
   - Impact vs. Effort matrix
   - MoSCoW classification
   - Buy-a-feature game

   **Design workshops:**
   - Crazy 8s sketching
   - User journey mapping
   - "How might we" generation

4. **Generate discussion prompts** — 8-12 open-ended questions tailored to the goal and participant roles. Prompts should surface disagreements, not seek consensus prematurely.

5. **Create pre-read materials** — Brief summary doc for participants covering:
   - Workshop purpose and what we'll accomplish
   - What to prepare (bring examples, think about X)
   - Key findings from prior research (if available)

6. **Write outputs:**
   - `workshop/agenda.md` — Timed agenda with activity descriptions
   - `workshop/discussion-prompts.md` — Facilitation questions
   - `workshop/pre-read.md` — Participant preparation materials

## Important

- Design prompts to surface tension between roles — disagreement is signal.
- Include facilitator notes with each agenda item (what to watch for, how to redirect).
- Keep pre-read materials under 1 page — participants won't read more than that.
