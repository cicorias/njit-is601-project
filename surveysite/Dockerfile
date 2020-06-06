FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code/
COPY pyproject.toml poetry.lock /code/
RUN pip install poetry \
    && poetry install

COPY . /code/
