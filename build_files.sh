#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Ensure psycopg2-binary is installed instead of psycopg2
pip install psycopg2-binary

# Run collectstatic to handle static files
python manage.py collectstatic --noinput
