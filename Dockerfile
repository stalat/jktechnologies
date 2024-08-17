FROM python:3.12.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir virtualenv
RUN virtualenv /venv

COPY ./requirements.txt /app/
RUN /venv/bin/pip install -r requirements.txt

RUN apt-get update 
