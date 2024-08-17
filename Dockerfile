FROM python:3.12.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update 

COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
