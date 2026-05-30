FROM ghcr.io/astral-sh/uv:python3.14-bookworm
# https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

# install dependencies:
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    useradd --uid 1000 app && \
    uv sync --frozen --no-install-project
COPY . /app
# install our app as separate layer
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

USER app
ARG VERSION
LABEL org.opencontainers.image.version=$VERSION

ENTRYPOINT []
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
