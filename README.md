# Cure_connect

A simple Django-based healthcare management demo project with patient, doctor, and appointment views.

## Features
- Custom user model for accounts
- Patient, doctor, and appointment management views
- SQLite database for local development

## Local setup
1. Create and activate a virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Apply migrations:
   python manage.py migrate
4. Start the development server:
   python manage.py runserver

## GitHub-ready notes
- Keep secrets in environment variables instead of hard-coding them.
- The project uses a default development secret key and SQLite database for local use.
- For production, replace the secret key and configure a production database and hosting environment.
