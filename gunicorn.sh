#!/bin/bash

if [ -d "venv" ]
then
  echo "Python virtual env exists"
else
  python3 -m venv venv
fi

. /app/venv/bin/activate

# . venv/bin/
# cd /var/lib/jenkins/workspace/Django-jenkins/bookmanagement
cd /app

python3 bookmamagement/manage.py makemigrations
python3 bookmamagement/manage.py migrate

echo "Migrations are applied"

# cd /var/lib/jenkins/workspace/Django-jenkins/
sudo cp -rf gunicorn.socket /etc/systemd/system/
sudo cp -rf gunicorn.service /etc/systemd/system/

echo "$USER"
echo "$PWD"

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

echo "GUNICORN has been started"

sudo systemctl status gunicorn
sudo systemctl restart gunicorn