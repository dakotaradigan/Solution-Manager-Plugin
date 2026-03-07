---
title: "Claude Code Plugin Not Loading — Silent Failure"
category: integration-issues
tags: [claude-code, plugin, configuration, silent-failure]
component: plugin-system
symptoms:
  - "Slash commands don't appear in autocomplete"
  - "Skills from plugin not listed in system prompt"
  - "Plugin appears enabled in settings but has no effect"
  - "Typing /plugin-name shows no matching commands"
root_cause: "Mismatch between installed_plugins.json registry key and settings.json enabledPlugins key"
severity: high
date_solved: 2026-03-06
---

# Claude Code Plugin Not Loading — Silent Failure

## Problem

A locally installed Claude Code plugin (`solution-work`) was enabled in settings but none of its commands, skills, or agents loaded. Typing `/solutions` in the CLI showed no matching commands. The plugin was completely invisible despite being "installed."

No error messages were shown — it failed silently.

## Symptoms

- Slash commands from the plugin don't appear in autocomplete
- Skills not listed when Claude describes available skills
- Plugin directory exists at `~/.claude/plugins/local/solution-work/`
- `settings.json` shows `"solution-work@local": true`
- Restarting Claude Code repeatedly does not help

## Investigation Steps

1. **Verified directory structure** — Commands, skills, agents all present and correctly structured. Matched compound-engineering's layout exactly. *(Not the issue.)*

2. **Verified plugin.json** — Located at `.claude-plugin/plugin.json`, correct format, name field set to `"solution-work"`. *(Not the issue.)*

3. **Verified symlink resolution** — `~/.claude/plugins/local/solution-work` symlink resolves to valid target directory. All files accessible through symlink. *(Not the issue.)*

4. **Checked `installed_plugins.json`** — **Found the root cause.** The registry had a completely different key than what settings expected:

   | File | Key | Path |
   |------|-----|------|
   | `settings.json` | `solution-work@local` | N/A |
   | `installed_plugins.json` | `solution-manager-toolkit@pm-tools` | `~/.claude/plugins/local/solution-manager-toolkit` |

   Two problems: the registry key didn't match settings, AND the install path pointed to a directory that had been renamed.

## Root Cause

Claude Code resolves plugins through a **three-way alignment**:

```
settings.json (enabledPlugins key)
        ↕ must match exactly
installed_plugins.json (registry key)
        ↕ must point to valid path
actual directory on disk
```

All three were mismatched:
- **Settings**: `solution-work@local`
- **Registry**: `solution-manager-toolkit@pm-tools` → `/.../.claude/plugins/local/solution-manager-toolkit`
- **Directory**: `~/.claude/plugins/local/solution-work` (renamed in a previous fix attempt)

This happened because:
1. The plugin was originally installed with directory name `solution-manager-toolkit`
2. The `plugin.json` name field was `solution-work` (different from directory name)
3. A previous fix renamed the directory from `solution-manager-toolkit` to `solution-work`
4. Nobody updated `installed_plugins.json` to match

## Solution

Edit `~/.claude/plugins/installed_plugins.json` to align the registry entry:

**Before:**
```json
"solution-manager-toolkit@pm-tools": [
  {
    "scope": "user",
    "installPath": "/Users/dakotaradigan/.claude/plugins/local/solution-manager-toolkit",
    "version": "0.1.0"
  }
]
```

**After:**
```json
"solution-work@local": [
  {
    "scope": "user",
    "installPath": "/Users/dakotaradigan/.claude/plugins/local/solution-work",
    "version": "0.1.0"
  }
]
```

Then restart Claude Code.

## Prevention

When working with Claude Code plugins:

1. **The plugin name in `plugin.json` should match the directory name.** If `plugin.json` says `"name": "solution-work"`, the directory should be `solution-work/`.

2. **Never rename plugin directories without updating `installed_plugins.json`.** The registry path must point to the actual directory.

3. **Three things must always align:**
   - `settings.json` → `enabledPlugins` key (e.g., `solution-work@local`)
   - `installed_plugins.json` → registry key (e.g., `solution-work@local`)
   - `installed_plugins.json` → `installPath` (must exist on disk)

4. **If a plugin silently fails to load**, check `installed_plugins.json` first — not the directory structure.

## Plugin Loading Reference

| Source Type | Settings Key | Registry Key | Install Path |
|-------------|-------------|-------------|-------------|
| Marketplace | `{name}@{marketplace}` | `{name}@{marketplace}` | `~/.claude/plugins/cache/{marketplace}/{name}/{version}` |
| Local | `{name}@local` | `{name}@local` | `~/.claude/plugins/local/{name}` |
