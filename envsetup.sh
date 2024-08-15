#!/bin/bash

if [ -d "myenv" ]
then
  echo "Python virtual env exists"
else
  python3 -m venv myenv
fi

echo $USER
echo $PWD
source env/bin/activate

pip3 install -r requirements.txt

if [ -d "logs" ]
then
  echo "Log folder exists"
else
  mkdir logs
  touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs
echo "envsetup finishes"