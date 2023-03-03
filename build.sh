#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Migrate DB
python manage.py makemigrations
python manage.py migrate

# Generate API 
python manage.py generate-api -f
