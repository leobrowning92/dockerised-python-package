FROM python:3.11-slim as base
WORKDIR /ball-pass

RUN apt-get update && apt-get install -y curl

# Ensure version matches pyproject.toml
ENV POETRY_HOME="/opt/poetry" \
  POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$PATH"

# Install poetry 
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false

COPY  pyproject.toml poetry.lock ./
COPY ball_pass/ ./ball_pass
RUN poetry install --no-dev

ENTRYPOINT [ "python", "./ball_pass" ]

FROM base as test

RUN poetry install

ENTRYPOINT [ "python", "-m", "pytest" ]


