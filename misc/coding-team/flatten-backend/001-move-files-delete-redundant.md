# Task: Move files from backend/ to repo root, delete redundant files

## Context

The `backend/` directory is being eliminated. Its contents move to the repo root. Some files in `backend/` are redundant with root-level equivalents and should just be deleted.

## Objective

Move all meaningful files from `backend/` to the repo root. Delete redundant files. Remove the now-empty `backend/` directory.

## What to move (use `git mv`)

All of these move from `backend/` to the repo root:

- `backend/ibidem/` → `ibidem/`
- `backend/templates/` → `templates/`
- `backend/pyproject.toml` → `pyproject.toml`
- `backend/uv.lock` → `uv.lock`
- `backend/.prospector.yaml` → `.prospector.yaml`
- `backend/http-client.env.json` → `http-client.env.json`
- `backend/test_main.http` → `test_main.http`

## What to delete (use `git rm`)

- `backend/mise.toml` — fully redundant with `.config/mise/config.toml` (identical content)
- `backend/.earthignore` — strict subset of root `.earthignore`
- `backend/Earthfile` — will be merged into root Earthfile in a separate task

## After moves and deletes

The `backend/` directory should be empty and can be removed (`rmdir` or `git rm -r`).

## Non-goals

- Do NOT modify the root `Earthfile` yet (that's a separate task).
- Do NOT modify any file contents — this task is purely about moving/deleting files.
- Do NOT touch `.config/mise/config.toml`, `.github/workflows/main.yaml`, or `test-integration.sh`.

## Constraints

- Use `git mv` for all moves so git tracks renames.
- Use `git rm` for deletions.
