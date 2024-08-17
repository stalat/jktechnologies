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
echo "Now listing the content"
ls -lah 
python3 bookmanagement/manage.py makemigrations
python3 bookmanagement/manage.py migrate

echo "Migrations are applied"

# cd /var/lib/jenkins/workspace/Django-jenkins/
cp -rf gunicorn.socket /etc/systemd/system/
cp -rf gunicorn.service /etc/systemd/system/

echo "$USER"
echo "$PWD"

systemctl daemon-reload
systemctl start gunicorn
systemctl enable gunicorn

echo "GUNICORN has been started"

sudo systemctl status gunicorn
sudo systemctl restart gunicorn