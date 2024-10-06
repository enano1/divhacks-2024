#!/bin/bash
# Create and activate a virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
venv/bin/pip install -r requirements.txt

# Ensure psycopg2-binary is installed instead of psycopg2
venv/bin/pip install psycopg2-binary

# Run collectstatic to handle static files
venv/bin/python manage.py collectstatic --noinput
