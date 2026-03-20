# Task: Merge backend Earthfile targets into root Earthfile

## Context

The `backend/Earthfile` has been deleted (task 001), but its targets (`INSTALL_MISE`, `deps`, `build`, `test`, `black`) need to be incorporated into the root `Earthfile`. All source files now live at the repo root.

## Objective

Rewrite the root `Earthfile` to include all targets from both the old root and old backend Earthfiles, adjusted for the new flat directory structure.

## The old backend Earthfile (now deleted) contained

```
VERSION 0.8

IMPORT github.com/mortenlj/earthly-lib/kubernetes/commands AS lib-k8s-commands

FROM busybox

INSTALL_MISE:
    FUNCTION
    ENV MISE_DATA_DIR="/mise"
    ENV MISE_CONFIG_DIR="/mise"
    ENV MISE_CACHE_DIR="/mise/cache"
    ENV MISE_INSTALL_PATH="/usr/local/bin/mise"
    ENV PATH="/mise/shims:$PATH"

    COPY mise.toml .
    RUN curl https://mise.run | sh && \
        mise trust /app/mise.toml

deps:
    FROM python:3.13

    WORKDIR /app

    DO +INSTALL_MISE
    RUN mise install uv

    COPY pyproject.toml uv.lock .
    RUN uv sync --no-install-workspace --locked --compile-bytecode

    SAVE ARTIFACT .venv
    SAVE IMAGE --cache-hint


build:
    FROM +deps

    RUN uv sync --locked --compile-bytecode --group=dev

    COPY --dir .prospector.yaml ibidem templates .
    RUN uv run black --check . && \
        uv run prospector

    SAVE ARTIFACT ibidem
    SAVE ARTIFACT templates
    SAVE IMAGE --cache-hint

test:
    LOCALLY
    RUN uv sync --locked --compile-bytecode && \
        uv run black --check . && \
        uv run prospector

black:
    LOCALLY
    RUN uv sync --locked --compile-bytecode && \
        uv run black .
```

## Changes needed in the merged Earthfile

1. **VERSION**: Bump from `0.7` to `0.8` (the backend was already on 0.8).

2. **IMPORT**: Keep the single `IMPORT` line (both files had the same one). The backend's `IMPORT` was unused there (only `manifests` target uses it), so just keep the root's.

3. **Add targets from backend**: `INSTALL_MISE` (function), `deps`, `build`, `test`, `black` — paste them in before the existing `docker` target.

4. **INSTALL_MISE function**: The `COPY mise.toml .` line needs updating. The file is now at `.config/mise/config.toml`. Change to: `COPY .config/mise/config.toml mise.toml`
   (This copies it into the container as `mise.toml` which is what `mise trust /app/mise.toml` expects.)

5. **`docker` target**: Update the three COPY lines that referenced `./backend/+deps` and `./backend/+build`:
   - `COPY --dir ./backend/+deps/.venv .` → `COPY --dir +deps/.venv .`
   - `COPY --dir ./backend/+build/ibidem .` → `COPY --dir +build/ibidem .`
   - `COPY --dir ./backend/+build/templates .` → `COPY --dir +build/templates .`

6. **`deploy` target**: Update the cross-reference:
   - `BUILD --platform=linux/amd64 --platform=linux/arm64 ./backend+build` → `BUILD --platform=linux/amd64 --platform=linux/arm64 +build`

7. **Target ordering**: Use this order for readability:
   `INSTALL_MISE`, `deps`, `build`, `test`, `black`, `docker`, `manifests`, `deploy`

## Non-goals

- Do NOT touch any other files.
- Do NOT change the logic of any target beyond the path adjustments described above.

## Constraints

- The `INSTALL_MISE` function must copy `.config/mise/config.toml` as `mise.toml` into the container (mise expects `mise.toml` at `/app/mise.toml`).
