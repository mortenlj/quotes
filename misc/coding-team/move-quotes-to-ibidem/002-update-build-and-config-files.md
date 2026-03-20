# Task: Update build and config files for new package path

## Context

The Python package has moved from `backend/quotes/` to `backend/ibidem/quotes/`. Build files and linter config still reference the old path.

## Objective

Update all non-Python files that reference the `quotes` package path to use `ibidem/quotes` (or `ibidem.quotes` for Python module syntax).

## Scope

### `Earthfile` (root — `/home/mortenlj/code/personal/quotes/Earthfile`)
- `COPY --dir ./backend/+build/quotes .` → `COPY --dir ./backend/+build/ibidem .`
- `CMD ["/app/.venv/bin/python", "-m", "quotes"]` → `CMD ["/app/.venv/bin/python", "-m", "ibidem.quotes"]`

### `backend/Earthfile`
- `COPY --dir .prospector.yaml quotes templates .` → `COPY --dir .prospector.yaml ibidem templates .`
- `SAVE ARTIFACT quotes` → `SAVE ARTIFACT ibidem`

### `backend/.prospector.yaml`
- `ignore-paths` entry `quotes/api/deps.py` → `ibidem/quotes/api/deps.py`
  (Note: this path was already stale — the file doesn't exist — but update it to match the new structure for consistency.)

## Non-goals

- Do NOT change `pyproject.toml` package name (stays `quotes`).
- Do NOT change Kubernetes resource names in `deploy/`.
- Do NOT change GitHub workflow references.
- Do NOT touch any Python files.
