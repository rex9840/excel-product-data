#!/bin/bash

set -e
python manage.py makemigrations --no-input
python manage.py migrate --no-input 
python manage.py createsuperuseradmin
python manage.py collectstatic --no-input 
honcho start
