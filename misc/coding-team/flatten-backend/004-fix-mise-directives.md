# Task: Fix mise comment directives in update-python-version.py

## Context

The previous task's auto-formatter changed `#MISE` to `# MISE` and `#USAGE` to `# USAGE` in `.config/mise/tasks/update-python-version.py`. Mise intentionally ignores `# MISE` (with space) — only `#MISE` (no space) is recognized as a directive. This broke the task's description and argument parsing.

## Objective

Restore the original mise directive format (no space after `#`).

## Changes

In `.config/mise/tasks/update-python-version.py`:

- Line 2: `# MISE description=` → `#MISE description=`
- Line 3: `# USAGE arg` → `#USAGE arg`

## Non-goals

- No other changes to this file or any other file.
