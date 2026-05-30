FROM ghcr.io/astral-sh/uv:python3.14-bookworm
WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN useradd --uid 1000 app && uv sync --frozen
USER app
COPY . /app
ARG VERSION
LABEL org.opencontainers.image.version=$VERSION
CMD ["uv", "run", "--frozen", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
