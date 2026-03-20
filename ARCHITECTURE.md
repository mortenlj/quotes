# Repository Scout Report

_Last updated: 2026-03-20_

---

## Detected Stack

### Languages
- **Python 3.13** — all application code (`backend/pyproject.toml`: `requires-python = "~=3.13.0"`)
- **Jinja2 HTML templates** — `backend/templates/*.html.j2`
- **YAML / Jinja2** — Kubernetes manifests in `deploy/`

### Frameworks and Major Libraries
| Library | Version constraint | Role | Evidence |
|---|---|---|---|
| FastAPI | `>=0.115.2,<1.0.0` | HTTP framework | `backend/pyproject.toml` |
| Uvicorn | `>=0.34.0,<1.0.0` | ASGI server | `backend/pyproject.toml` |
| Pydantic v2 | `>=2.9.2,<3.0.0` | Data models / validation | `backend/pyproject.toml` |
| pydantic-settings | `>=2.6.0,<3.0.0` | Config from env vars | `backend/pyproject.toml` |
| fiaas-logging | `>=0.1.1,<1.0.0` | JSON structured logging | `backend/pyproject.toml` |
| Jinja2 | `>=3.1.6` | HTML templating | `backend/pyproject.toml` |

### Build and Packaging
- **uv** — dependency management and virtualenv (`backend/uv.lock`, `backend/Earthfile`)
- **Earthly** — reproducible build system (`Earthfile`, `backend/Earthfile`)
- **black** (dev) — code formatter (`backend/pyproject.toml`, `backend/Earthfile`)
- **prospector** (dev) — linting aggregator (`backend/pyproject.toml`, `backend/.prospector.yaml`)
- **mise** — tool version manager (`.config/mise/config.toml`: earthly, python 3.13, uv)

### Deployment and Runtime
- **Docker image** — `python:3.13-slim` base, built via `Earthfile` (`+docker` target), pushed to `ghcr.io/<repo>`
- **Kubernetes** — deployed via a custom `yakup.ibidem.no/v1 Application` CRD (`deploy/application.yaml.j2`)
- **GitHub Actions** — CI/CD pipeline (`.github/workflows/main.yaml`)
- **ZeroTier** — VPN used to reach the private k3s cluster during deploy
- **ghcr.io** — container registry

---

## Conventions

### Formatting and Linting
- **black** with `line-length = 120`, `target-version = ["py313"]` (`backend/pyproject.toml` `[tool.black]`)
- **prospector** at `strictness: high`, `max-line-length: 120` (`backend/.prospector.yaml`)
  - pylint, pyroma, frosted, vulture, pep257 are all **disabled**; pep8 (pycodestyle) and mccabe are active
  - `quotes/api/deps.py` is explicitly ignored by prospector (path listed in `ignore-paths`)

### Type Checking
- No mypy or pyright configured. Pydantic v2 models provide runtime type enforcement.

### Testing
- No test framework configured (no pytest, no test files found). The `test` target in `backend/Earthfile` runs only black + prospector (linting, not unit tests).

### Documentation
- `README.rst` — minimal top-level readme
- No docs folder, no changelog, no ADRs

---

## Linting and Testing Commands

**First choice — run everything locally (from `backend/`):**
```bash
uv run black --check . && uv run prospector
```
Source: `backend/Earthfile` → `test` target (runs `LOCALLY`)

**Format (auto-fix):**
```bash
uv run black .
```
Source: `backend/Earthfile` → `black` target

**Via Earthly (containerised, matches CI exactly):**
```bash
earthly ./backend+build
```
Source: `backend/Earthfile` → `build` target (runs black check + prospector inside container)

**Full CI pipeline (build + push + manifests):**
```bash
earthly +deploy
```
Source: root `Earthfile` → `deploy` target

---

## Project Structure Hotspots

```
quotes/                          ← repo root
├── Earthfile                    ← top-level build: docker image, manifests, deploy orchestration
├── backend/                     ← all Python application code
│   ├── pyproject.toml           ← package metadata, deps, black config
│   ├── uv.lock                  ← locked dependency tree
│   ├── Earthfile                ← backend-specific build targets (deps, build, test, black)
│   ├── .prospector.yaml         ← linter configuration
│   ├── quotes/                  ← the Python package (main entry point)
│   │   ├── __init__.py          ← empty (package marker)
│   │   ├── __main__.py          ← `python -m quotes` entry point → calls main()
│   │   ├── main.py              ← FastAPI app construction + uvicorn runner (HIGH CHANGE)
│   │   ├── config.py            ← pydantic-settings Settings singleton
│   │   ├── deps.py              ← in-memory quote database + Jinja2Templates factory (HIGH CHANGE — all quotes live here)
│   │   ├── logger.py            ← logging config dict
│   │   ├── web.py               ← HTML web routes (/, /{id})
│   │   └── api/                 ← REST API sub-package
│   │       ├── __init__.py      ← assembles api.router from v1
│   │       ├── probes.py        ← /_/healthy and /_/ready endpoints
│   │       ├── schemas.py       ← Quote Pydantic model (HIGH CHANGE — shared schema)
│   │       └── v1/
│   │           ├── __init__.py  ← assembles v1.router from quotes sub-router
│   │           └── quotes.py    ← /api/v1/quotes/ REST endpoints
│   └── templates/               ← Jinja2 HTML templates
│       ├── base.html.j2         ← Bootstrap 5 base layout
│       └── quote.html.j2        ← single quote page
├── deploy/                      ← Kubernetes manifests
│   ├── application.yaml.j2      ← yakup Application CRD (image, ports, probes, configmap ref)
│   └── configmap.yaml           ← bind_address and mode env vars
└── .github/workflows/main.yaml  ← CI: build → push → deploy → cleanup
```

---

## Do and Don't Patterns

### Do

- **Absolute imports from the package root** — all intra-package imports use `from quotes.X import Y` (not relative `..`), except `__main__.py` which uses `from .main import main` and the `api` sub-package which uses `from . import v1` / `from . import quotes`.
  - Evidence: `backend/quotes/main.py` (`from quotes import api, web`), `backend/quotes/web.py` (`from quotes.deps import get_db, templates`), `backend/quotes/api/v1/quotes.py` (`from quotes.deps import get_db`)

- **FastAPI `Depends()` for dependency injection** — database dict and Jinja2Templates are injected via `Depends(get_db)` / `Depends(templates)`, not imported as globals in route files.
  - Evidence: `backend/quotes/web.py`, `backend/quotes/api/v1/quotes.py`

- **Pydantic v2 models for schemas** — `Quote` uses `BaseModel` with `ConfigDict(from_attributes=True)`.
  - Evidence: `backend/quotes/api/schemas.py`

- **pydantic-settings for configuration** — a single `settings` singleton is created at module load from env vars; no manual `os.getenv` calls in application code.
  - Evidence: `backend/quotes/config.py`

- **Standard library `logging` + fiaas-logging for structured output** — log config is centralised in `logger.py`; supports both plain (dev) and JSON (prod) formats.
  - Evidence: `backend/quotes/logger.py`, `backend/quotes/main.py`

- **Signal handling for graceful shutdown** — SIGTERM and SIGINT are caught and converted to a custom `ExitOnSignal` exception.
  - Evidence: `backend/quotes/main.py`

- **`python -m quotes` as the container entrypoint** — the Earthfile CMD uses `/app/.venv/bin/python -m quotes`.
  - Evidence: root `Earthfile` line 27

### Don't

- **No broad exception swallowing** — only one bare `except Exception` exists in `main.py`, and it prints and sets a non-zero exit code (not silently ignored).
  - Evidence: `backend/quotes/main.py` lines 46–48

- **No database / ORM** — data is a hard-coded in-memory tuple of `Quote` objects in `deps.py`; no SQLAlchemy, no migrations.

- **No test suite** — there are no `test_*.py` files and no pytest configuration anywhere in the repo.

- **No type checker** — mypy and pyright are absent from both `pyproject.toml` and the Earthfile build steps.

- **No relative imports outside the `api` sub-package** — top-level modules (`main.py`, `web.py`, `deps.py`) all use absolute `quotes.*` imports.

---

## References to `quotes` Package in Non-Python Files

| File | Reference | Context |
|---|---|---|
| `Earthfile` (root) | `COPY --dir ./backend/+build/quotes .` | Copies built package into Docker image |
| `Earthfile` (root) | `CMD ["/app/.venv/bin/python", "-m", "quotes"]` | Container entrypoint |
| `Earthfile` (root) | `BUILD --platform=... ./backend+build` | Triggers backend build |
| `backend/Earthfile` | `COPY --dir .prospector.yaml quotes templates .` | Copies source for lint/build |
| `backend/Earthfile` | `SAVE ARTIFACT quotes` | Exports package artifact |
| `backend/.prospector.yaml` | `ignore-paths: - quotes/api/deps.py` | Suppresses linting on that path |
| `deploy/application.yaml.j2` | `name: quotes`, `app: quotes`, `configMap: quotes-config` | K8s resource names |
| `deploy/configmap.yaml` | `name: quotes-config`, `app: quotes` | K8s ConfigMap for the app |
| `.github/workflows/main.yaml` | `package: quotes/cache` | GHCR cache image cleanup |
| `backend/templates/base.html.j2` | `href="https://github.com/mortenlj/quotes"` | Footer link to source repo |

---

## Open Questions

1. **`quotes/api/deps.py` in `.prospector.yaml` ignore-paths** — the file `backend/quotes/api/deps.py` is listed as ignored by prospector, but it does not exist in the repo (the actual deps file is `backend/quotes/deps.py`). This looks like a stale/incorrect path. Clarify whether a `quotes/api/deps.py` is planned or if the ignore entry should be removed.

2. **No tests** — there is no test suite at all. Is this intentional (the app is trivially simple) or is testing planned?

3. **`templates` directory path at runtime** — `deps.py` calls `Jinja2Templates(directory="templates")` with a relative path. This works only if the process CWD is `/app` (which it is in the Docker image, per `WORKDIR /app`). Running locally from a different directory will fail. No open question if always run via `python -m quotes` from `backend/`, but worth noting.
