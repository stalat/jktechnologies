#!/bin/bash

cd /app 
. /venv/bin/activate

python3 manage.py makemigrations
python3 manage.py migrate

exec gunicorn --bind 0.0.0.0:8000 bookmanagement.wsgi