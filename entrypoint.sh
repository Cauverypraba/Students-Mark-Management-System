#!/bin/sh

# Migrate django models
python manage.py migrate

# Collect static files from docker-compose volumn
python manage.py collectstatic

# Run development server
gunicorn Marks_Management_System.wsgi:application --bind 0.0.0.0:8000
