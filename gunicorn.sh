#!/bin/bash

. /venv/bin/activate
cd /app 

python3 manage.py makemigrations
python3 manage.py migrate

exec gunicorn --bind 0.0.0.0:8000 bookmanagement.wsgi