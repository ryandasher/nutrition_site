# Sweepstakes project

Single page webapp where logged in users can earn points to be entered into a drawing. Admin users can run the drawing to determine winners, and then users can log in to claim their prize.

## Project Setup:

Install virtualenv and pip. When you have them installed, create a virtual environment and activate it. Then run:

	$ pip install -r requirements.txt

Start the local webserver with:

	$ python manage.py runserver

Create an admin user with:

	$ python manage.py createsuperuser

Use the admin tool or the shell to create users, drawings, and prizes in order to test the application.

## Project Notes:

Registration templates politely borrowed from https://github.com/macdhuibh/django-registration-templates.
