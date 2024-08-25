#!/bin/bash
echo "Present working Directory is: "
echo $PWD
. /venv/bin/activate

cd /app 

# running migrations and collecting the static files
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input

# running application via gunicorn service
gunicorn jktechnologies.wsgi:application --bind 0.0.0.0:8000