# Task: Move quotes package into ibidem namespace and update imports

## Context

The Python package lives at `backend/quotes/`. It needs to be nested under a new `ibidem` package so the import path becomes `ibidem.quotes.*`.

## Objective

1. Create `backend/ibidem/__init__.py` (empty file).
2. Move `backend/quotes/` to `backend/ibidem/quotes/` (the directory, all contents).
3. Update **every** Python import across the codebase from `quotes.*` to `ibidem.quotes.*`.
4. Replace the single relative import in `__main__.py` (`from .main import main`) with an absolute import (`from ibidem.quotes.main import main`).
5. Keep relative imports within sub-packages (`api/__init__.py`, `api/v1/__init__.py`) as-is — they reference siblings, not the top-level package, so they still work.

## Scope

Python files only. The following files contain `quotes.*` imports that need updating:

- `backend/ibidem/quotes/__main__.py` — `from .main import main` → `from ibidem.quotes.main import main`
- `backend/ibidem/quotes/main.py` — `from quotes import api, web` and three other `quotes.*` imports
- `backend/ibidem/quotes/web.py` — `from quotes.deps import ...`
- `backend/ibidem/quotes/deps.py` — `from quotes.api.schemas import Quote`
- `backend/ibidem/quotes/api/v1/quotes.py` — two `quotes.*` imports

Files with only relative imports (`api/__init__.py`, `api/v1/__init__.py`) need no changes.

## Non-goals

- Do NOT touch Earthfiles, `.prospector.yaml`, `pyproject.toml`, deploy files, or any non-Python files. That's a separate task.
- Do NOT rename the package in `pyproject.toml`.
- Do NOT move `backend/templates/`.

## Constraints

- Use `git mv` to move the directory so git tracks the rename.
- All imports must be absolute `ibidem.quotes.*` form.
