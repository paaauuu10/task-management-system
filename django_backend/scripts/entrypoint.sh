#!/bin/bash

# exit if something fails
set -e

# waiting for the DB
echo " Waiting for the DB... " 
sleep 3


echo "Migrating..."
python manage.py migrate

echo "Running Django server..."
exec python manage.py runserver 0.0.0.0:8000