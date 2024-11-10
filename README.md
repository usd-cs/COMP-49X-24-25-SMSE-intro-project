# SMSE Team Intro Project

Description:

Table of Contents:
  1. Features
  2. Requirments
  3. Dependencies:
  4. Database Setup
  5. Testing: 

Features:

Requirements: 
  - Python (version 3.10 or higher)
  - PostgreSQL (latest version)
  - pip

Dependencies:
  - pip install -r requirements.txt (installs Django, psycopg2, and other required Python packages)

Database Setup:
  1. bash# psql -U postgres (login to postgresql, i used username:postgres and password: password) 
  2. sql# CREATE DATABASE intro_project_db;
  3. sql# CREATE USER postgres WITH PASSWORD password; (this is the username and password we're all using) 
  4. sql# GRANT ALL PRIVILEGES ON DATABASE intro_project_db TO postgres;

        The database settings under settings.py should look like this: 
        DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'intro_project_db',
              'USER': 'postgres',
              'PASSWORD': 'password',
              'HOST': 'localhost',
              'PORT': '5432',
          }
        }

  5. bash# python manage.py makemigrations (then make sure to set up the database model objects )
  6. bash# python manage.py migrate
  7. python manage.py createsuperuser (made a superuser)
       - username: admin
       - email address: admin@gmail.com
       - password: password
  8. python manage.py runserver  (runs the app)

Testing:
python manage.py test  (runs the tests) 
