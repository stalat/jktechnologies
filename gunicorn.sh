#!/bin/bash
echo "Present working Directory is: "
echo $PWD
. /venv/bin/activate
echo "Listing all the files"
ls -lah
cd /app 

python3 manage.py makemigrations
python3 manage.py migrate

exec gunicorn --bind 0.0.0.0:8000 jktechnologies.wsgi:application