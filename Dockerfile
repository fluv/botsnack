FROM ghcr.io/astral-sh/uv:python3.14-bookworm
WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN useradd --uid 1000 app && uv sync --frozen
USER app
COPY . /app
ARG VERSION
LABEL org.opencontainers.image.version=$VERSION
CMD [ "uv", "run", "fastapi", "run", "--proxy-headers" ]
