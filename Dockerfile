FROM python:3.12.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir virtualenv
RUN virtualenv venv
RUN . venv/bin/activate

RUN apt-get update 

COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
