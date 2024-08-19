FROM python:3.12.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir virtualenv

COPY . /app/

RUN virtualenv /venv

COPY ./requirements.txt /app/
RUN /venv/bin/pip install -r requirements.txt