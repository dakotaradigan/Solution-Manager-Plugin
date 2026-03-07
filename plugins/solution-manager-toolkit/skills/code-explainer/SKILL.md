---
name: code-explainer
description: This skill should be used when translating code into plain, non-technical language for business stakeholders who don't read code.
---

# Code Explainer

Domain knowledge for translating technical codebases into business-friendly explanations.

## When to Use

- User asks to "explain", "describe", or "walk through" what code does
- A non-technical stakeholder needs to understand a system
- Preparing for a meeting where code decisions need business context

## Translation Rules

1. **No jargon** — say "the system lets you look up X" not "the GET endpoint returns X"
2. **Roles, not actors** — say "traders" or "operations team" not "API consumers" or "authenticated users"
3. **Domain language first** — say "portfolio" not "holdings collection", "price" not "quote object"
4. **Concrete over abstract** — "pulls prices from Bloomberg every morning" not "integrates with external data providers"
5. **Workflows, not architecture** — describe what happens from a business perspective, not how the code is structured

## What to Surface

1. **Business purpose** — what problem does this solve, who benefits
2. **Key workflows** — the 3-5 most important things the system does, described as business processes
3. **Data in business terms** — what information the system tracks and why it matters
4. **Integrations as relationships** — where information comes from and goes to, and why
5. **Gaps** — things the system doesn't do that a stakeholder might expect
6. **Manual workarounds** — places where humans fill gaps the code doesn't cover

## Key Principles

- Explain what the code does, not how it's written.
- If something is confusing in the code, say so — "this area is hard to follow" is useful information.
- A VP should be able to read the output and understand the system without asking follow-up questions.
- Keep it short. Business readers stop reading after one page.
