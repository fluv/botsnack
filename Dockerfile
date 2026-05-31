FROM ghcr.io/astral-sh/uv:python3.14-bookworm AS builder
# https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
WORKDIR /app

# install dependencies:
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project
COPY . /app
# install our app as separate layer
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

FROM python:3.14-slim-bookworm
RUN useradd --uid 1000 --create-home app
WORKDIR /app
COPY --from=builder /app /app
RUN chown --recursive app:root /app
USER app
ENV PATH="/app/.venv/bin:$PATH"
ARG VERSION
LABEL org.opencontainers.image.version=$VERSION

ENTRYPOINT []
CMD ["/app/.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
