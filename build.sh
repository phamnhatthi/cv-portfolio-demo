#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Note: Skip migrations since we're deploying with existing database
# python manage.py migrate

echo "Build completed successfully!"
