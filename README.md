# chat-app Django 
# create a virtual environment
virtualenv venv
pip install Django
pip install djangorestframework

# command to create Django project

django-admin startproject chat_app_service

# Driver for allowing Django to use MongoDB as the database backend.
pip install djongo

# how to create virtual env
virtualenv venv
python3.6 -m venv venv  (with python 3.6 last venv is the name of virtualenv)

# running the server
python manage.py runserver