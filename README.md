# MealPlanit

A meal prep and recipe web app, built with Django and React-Native (or similar).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or later
- pip
- virtualenv (or venv)

### Installing

1. Clone the repository to your local machine

git clone https://github.com/jeremykissack/MealPlanit.git


2. Optional: Create a new virtual environment for the project and activate it

python -m venv ~/.virtualenvs/mp_env
source ~/.virtualenvs/mp_env/bin/activate


3. Install the required dependencies

pip install -r requirements.txt


4. Run the development server

python manage.py runserver


5. The project will be running on `http://127.0.0.1:8000/` in your browser

### Running the tests

You can run the test by using the command

python manage.py test


### Creating the database

In case you want to create the database with initial data, you can use the command

python manage.py migrate


### Creating an admin user

You can create an admin user by running the command

python manage.py createsuperuser


### Front-end

To set up the front-end part of the project, please follow the instructions in the `frontend` directory.

## Built With

- [Django](https://www.djangoproject.com/)
- [React-Native](https://reactnative.dev/) (To-do)
- [django-rest-framework](https://www.django-rest-framework.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

# mealPlanit
