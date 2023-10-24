FROM python:3.9-slim

LABEL name=g_challenge_de

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

SHELL ["/bin/bash", "-c"]

# Install poetry and compilation dependencies
RUN apt-get update && apt-get install -y 
RUN pip install --upgrade pip
RUN pip install poetry
RUN groupadd dsuser
RUN useradd --create-home -g dsuser dsuser
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# Install python dependencies in /.venv
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false &&  poetry install --no-root --no-dev

# Create and switch to a new user
WORKDIR /app


# Install application into container
COPY dist/ ./dist
RUN pip install dist/*.whl
RUN rm -rf pyproject.toml poetry.lock dist
USER dsuser

COPY startup.py /app
EXPOSE 8020
CMD python startup.py