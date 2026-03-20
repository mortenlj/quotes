# Task: Update remaining backend/ references

## Context

The `backend/` directory no longer exists. Files that referenced `backend/` paths need updating.

## Objective

Update `.config/mise/tasks/update-python-version.py` to remove `backend/` path prefixes.

## Changes

In `.config/mise/tasks/update-python-version.py`:

1. Line 24: `"backend/pyproject.toml"` → `"pyproject.toml"`
2. Line 25: `"backend/pyproject.toml"` → `"pyproject.toml"`
3. Line 36: `cwd="backend"` → remove the `cwd` kwarg entirely (uv should run from the repo root now)

## Non-goals

- No other files need changes (verified by grep).
- Do NOT change `pyproject.toml` content (the `name = "quotes-backend"` is intentional).
