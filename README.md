# Django User Profile App

## Overview

This Django project is a simple user profile management application where users can input and save their basic information. The project includes form validation to ensure correct input and uniqueness for email addresses and phone numbers.

## Features

- User profile creation with fields for first name, surname, email, and phone number.
- Validation checks for the correct format of the email address.
- Prevention of duplicate email addresses and phone numbers.
- Clean and responsive UI for an improved user experience.

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone link
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Visit [http://127.0.0.1:8000/profile/create/](http://127.0.0.1:8000/profile/create/) in your browser to access the user profile creation form.

## Project Structure

- `UserProfileProject/`: Django project folder.
  - `user_profile/`: Django app folder.
    - `models.py`: Defines the data model for user profiles.
    - `forms.py`: Contains the form for user input.
    - `views.py`: Implements views for profile creation and success page.
    - `urls.py`: Defines URL patterns for the app.
    - `templates/`: Contains HTML templates.
      - `user_profile/`: Templates specific to the user_profile app.
  - `UserProfileProject/`: Django app folder.
    - `asgi.py`: Manages asynchronous deployment for Django.
    - `settings.py`: Central configuration file for Django settings.
    - `urls.py`: Defines URL patterns for the Django project.
    - `wsgi/`: Configures Django for deployment with web servers.
  - `manage.py/`: Command-line utility for Django tasks.


## Dependencies

- Django: Web framework for building the application.
- SQLite: Default database for development purposes.