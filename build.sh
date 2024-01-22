#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Migrate DB
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('ash', 'admin@example.com', 'Password1!')"

# Generate API 
python manage.py generate-api -f
