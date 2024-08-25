FROM python:3.12.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# setting up working directory
WORKDIR /app

# updating container packages & installing virtualenv
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir virtualenv

COPY . /app/

# creating virtual environment
RUN virtualenv /venv

# installing required packages
COPY ./requirements.txt /app/
RUN /venv/bin/pip install -r requirements.txt