#!/usr/bin/env bash
set -euo pipefail

# Integration test script for the quotes service.
# Builds the Docker image, runs it, tests all 5 endpoints, then cleans up.

IMAGE="ttl.sh/mortenlj-quotes:1h"
HOST_PORT=13000
BASE_URL="http://localhost:${HOST_PORT}"
CONTAINER_NAME="quotes-integration-test-$$"
STARTUP_TIMEOUT=30

PASS=0
FAIL=0

# ---------------------------------------------------------------------------
# Cleanup — always runs on exit
# ---------------------------------------------------------------------------
cleanup() {
    echo ""
    echo "==> Cleaning up container '${CONTAINER_NAME}' ..."
    docker rm -f "${CONTAINER_NAME}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
echo "==> Building image ..."
mise run docker-build

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
echo "==> Starting container '${CONTAINER_NAME}' (image: ${IMAGE}) ..."
docker run -d \
    --name "${CONTAINER_NAME}" \
    -e BIND_ADDRESS=0.0.0.0 \
    -p "${HOST_PORT}:3000" \
    "${IMAGE}"

# ---------------------------------------------------------------------------
# Wait for the app to become healthy
# ---------------------------------------------------------------------------
echo "==> Waiting for app to become healthy (timeout: ${STARTUP_TIMEOUT}s) ..."
deadline=$(( $(date +%s) + STARTUP_TIMEOUT ))
while true; do
    status=$(curl -s -o /dev/null -w '%{http_code}' "${BASE_URL}/_/healthy" 2>/dev/null || true)
    if [[ "${status}" == "200" ]]; then
        echo "    App is healthy."
        break
    fi
    if [[ $(date +%s) -ge ${deadline} ]]; then
        echo "ERROR: App did not become healthy within ${STARTUP_TIMEOUT} seconds."
        exit 1
    fi
    sleep 1
done

# ---------------------------------------------------------------------------
# Helper: run a single test
# ---------------------------------------------------------------------------
# Usage: run_test <description> <expected_status> <url> [<body_pattern> ...]
#
# body_pattern arguments are extended-regex patterns; ALL must match the body.
run_test() {
    local description="$1"
    local expected_status="$2"
    local url="$3"
    shift 3
    local body_patterns=("$@")

    # Write body to a temp file; capture status code via -w; do NOT follow redirects.
    local tmpfile
    tmpfile=$(mktemp)
    local actual_status
    actual_status=$(curl -s --max-redirs 0 -o "${tmpfile}" -w '%{http_code}' "${url}" 2>/dev/null || true)

    local ok=true

    if [[ "${actual_status}" != "${expected_status}" ]]; then
        ok=false
    fi

    for pattern in "${body_patterns[@]+"${body_patterns[@]}"}"; do
        if ! grep -qE "${pattern}" "${tmpfile}"; then
            ok=false
        fi
    done

    if ${ok}; then
        echo "  PASS: ${description}"
        (( PASS++ )) || true
    else
        echo "  FAIL: ${description}"
        echo "        expected status=${expected_status}, got status=${actual_status}"
        for pattern in "${body_patterns[@]+"${body_patterns[@]}"}"; do
            if ! grep -qE "${pattern}" "${tmpfile}"; then
                echo "        body pattern '${pattern}' not matched"
            fi
        done
        echo "        body: $(cat "${tmpfile}")"
        (( FAIL++ )) || true
    fi

    rm -f "${tmpfile}"
}

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
echo ""
echo "==> Running endpoint tests ..."

# 1. GET / — expect 303
run_test "GET / returns 303" "303" "${BASE_URL}/"

# 2. GET / — expect 200
run_test "GET /1 returns 200" "200" "${BASE_URL}/1"

# 3. GET /_/healthy — expect 200
run_test "GET /_/healthy returns 200" "200" "${BASE_URL}/_/healthy"

# 4. GET /_/ready — expect 200
run_test "GET /_/ready returns 200" "200" "${BASE_URL}/_/ready"

# 5. GET /api/v1/quotes/ — expect 303
run_test "GET /api/v1/quotes/ returns 303" "303" "${BASE_URL}/api/v1/quotes/"

# 6. GET /api/v1/quotes/1 — expect 200 with JSON body containing "id":1 and "quote" key
run_test "GET /api/v1/quotes/1 returns 200 with JSON" "200" "${BASE_URL}/api/v1/quotes/1" \
    '"id"\s*:\s*1' \
    '"quote"\s*:'

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
echo ""
echo "==> Results: ${PASS} passed, ${FAIL} failed."

if [[ ${FAIL} -gt 0 ]]; then
    exit 1
fi

exit 0
