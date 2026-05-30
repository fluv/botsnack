FROM ghcr.io/astral-sh/uv:python3.14-bookworm
WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen
COPY . /app
CMD [ "uv", "run", "fastapi", "run", "--proxy-headers" ]
