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

    COPY .config/mise/config.toml mise.toml
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

docker:
    FROM python:3.13-slim

    WORKDIR /app

    COPY --dir +deps/.venv .
    COPY --dir +build/ibidem .
    COPY --dir +build/templates .

    ENV PATH="/bin:/usr/bin:/usr/local/bin:/app/.venv/bin"

    CMD ["/app/.venv/bin/python", "-m", "ibidem.quotes"]

    # builtins must be declared
    ARG EARTHLY_GIT_PROJECT_NAME
    ARG EARTHLY_GIT_SHORT_HASH

    # Override from command-line on CI
    ARG main_image=ghcr.io/$EARTHLY_GIT_PROJECT_NAME
    ARG VERSION=$EARTHLY_GIT_SHORT_HASH

    SAVE IMAGE --push ${main_image}:${VERSION} ${main_image}:latest

manifests:
    # builtins must be declared
    ARG EARTHLY_GIT_PROJECT_NAME
    ARG EARTHLY_GIT_SHORT_HASH

    ARG main_image=ghcr.io/$EARTHLY_GIT_PROJECT_NAME
    ARG VERSION=$EARTHLY_GIT_SHORT_HASH
    DO lib-k8s-commands+ASSEMBLE_MANIFESTS --IMAGE=${main_image} --VERSION=${VERSION}

deploy:
    # builtins must be declared
    ARG EARTHLY_GIT_PROJECT_NAME
    ARG EARTHLY_GIT_SHORT_HASH

    ARG main_image=ghcr.io/$EARTHLY_GIT_PROJECT_NAME
    ARG VERSION=$EARTHLY_GIT_SHORT_HASH

    BUILD --platform=linux/amd64 --platform=linux/arm64 +build
    BUILD --platform=linux/amd64 --platform=linux/arm64 +docker --main_image=${main_image} --VERSION=${VERSION}
    BUILD --platform=linux/amd64 +manifests
