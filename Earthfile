VERSION 0.7

IMPORT github.com/mortenlj/earthly-lib/kubernetes/commands AS lib-k8s-commands

FROM busybox

manifests:
    # builtins must be declared
    ARG EARTHLY_GIT_PROJECT_NAME
    ARG EARTHLY_GIT_SHORT_HASH

    ARG main_image=ghcr.io/$EARTHLY_GIT_PROJECT_NAME
    ARG VERSION=$EARTHLY_GIT_SHORT_HASH
    DO lib-k8s-commands+ASSEMBLE_MANIFESTS --IMAGE=${main_image} --VERSION=${VERSION}

docker:
    FROM python:3.11-slim

    WORKDIR /app

    COPY --dir ./backend/+deps/.venv .
    COPY --dir ./backend/+build/quotes .
    COPY --dir --platform=linux/amd64 ./frontend/+build/build .

    ENV PATH="/bin:/usr/bin:/usr/local/bin:/app/.venv/bin"

    CMD ["/app/.venv/bin/python", "-m", "quotes"]

    # builtins must be declared
    ARG EARTHLY_GIT_PROJECT_NAME
    ARG EARTHLY_GIT_SHORT_HASH

    # Override from command-line on CI
    ARG main_image=ghcr.io/$EARTHLY_GIT_PROJECT_NAME
    ARG VERSION=$EARTHLY_GIT_SHORT_HASH

    SAVE IMAGE --push ${main_image}:${VERSION} ${main_image}:latest

deploy:
    # builtins must be declared
    ARG EARTHLY_GIT_PROJECT_NAME
    ARG EARTHLY_GIT_SHORT_HASH

    ARG main_image=ghcr.io/$EARTHLY_GIT_PROJECT_NAME
    ARG VERSION=$EARTHLY_GIT_SHORT_HASH

    BUILD --platform=linux/amd64 ./frontend+build
    BUILD --platform=linux/amd64 --platform=linux/arm64 ./backend+build
    BUILD --platform=linux/amd64 --platform=linux/arm64 +docker --main_image=${main_image} --VERSION=${VERSION}
    BUILD --platform=linux/amd64 +manifests
