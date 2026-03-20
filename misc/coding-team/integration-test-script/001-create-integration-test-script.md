# Task: Create integration test script

## Context

The project builds a Docker image via `earthly +deploy`. There are no integration tests. The file `backend/test_main.http` lists 5 endpoints to test. The app is a FastAPI service that serves quotes.

## Objective

Create a bash script `test-integration.sh` at the repo root that:
1. Builds the image using `earthly +deploy`
2. Runs the image in Docker
3. Tests all 5 endpoints with curl
4. Cleans up and reports pass/fail

## Scope

Create one new file: `test-integration.sh`

## Key details

### Build
- Run `earthly +deploy` to validate the full multi-platform build pipeline.
- The image tag uses the git short hash: `ghcr.io/mortenlj/quotes:<hash>`. Derive the tag the same way Earthly does (inspect the `Earthfile` root target for the pattern — it uses `EARTHLY_GIT_PROJECT_NAME` and `EARTHLY_GIT_SHORT_HASH`). Use `git rev-parse --short HEAD` with the appropriate length (Earthly uses 8 chars by default: `git rev-parse --short=8 HEAD`). The project name comes from the git remote — but for simplicity, just hardcode `ghcr.io/mortenlj/quotes` since that's what the Earthfile resolves to, or better yet, derive it from the remote URL the same way Earthly does. Hardcoding is fine here.

### Docker run
- The app defaults to `BIND_ADDRESS=127.0.0.1` and `PORT=3000`. Override `BIND_ADDRESS=0.0.0.0` via env var so it's reachable from the host.
- Map container port 3000 to a host port. Pick a fixed port (e.g., 13000) or use a random available port — either is fine.
- Run the container in detached mode.
- Use a trap to ensure the container is stopped and removed on script exit (success or failure).

### Health check / startup wait
- Poll `/_/healthy` in a loop until it returns 200, with a timeout (e.g., 30 seconds). Fail if the app doesn't start in time.

### Endpoint tests (from `backend/test_main.http`)
For each test, assert the HTTP status code. Use `curl -s -o /dev/null -w '%{http_code}'` (or similar) to capture status codes. Don't follow redirects (`-L` must NOT be used for redirect tests; you may want to omit it globally or use `--max-redirs 0`).

1. `GET /` — expect 303 (redirects to a random quote)
2. `GET /_/healthy` — expect 200
3. `GET /_/ready` — expect 200
4. `GET /api/v1/quotes/` — expect 303 (redirects to a random quote)
5. `GET /api/v1/quotes/1` — expect 200, response body should be JSON containing `"id":1` and a `"quote"` field

### Output
- Print clear pass/fail for each test.
- Exit 0 if all pass, non-zero if any fail.

## Non-goals
- Don't modify any application code.
- Don't test every quote or every edge case (e.g., 404 for missing quotes). Just the 5 endpoints listed.
- Don't add this to CI (that's a separate decision).

## Constraints
- Pure bash. Dependencies: `curl`, `docker`, `earthly`, `git` (all already available in this project's dev environment).
- Make the script executable (`chmod +x`).
- Use `set -euo pipefail` but handle test failures gracefully (don't let `set -e` abort before cleanup).
