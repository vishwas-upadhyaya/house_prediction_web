# house_prediction_web

## Project Overview
A web application providing a user interface for the house price prediction machine learning model.

## What is this Project?
This repository contains a Django-based web application where users can input housing features (like area, bedrooms, location) through a web form, and the backend utilizes a pre-trained machine learning model to estimate the property's value.

## How it was done
The project is built with the Django web framework (`manage.py`, `house_prediction/` core app, `prediction/` app). The front-end uses HTML templates (`templates/`), while the backend processes form submissions and runs the regression model to return the estimated price.

## Why it was done
To deploy a machine learning model into a production-like environment, making the predictive capabilities accessible to end-users via a user-friendly web interface.

## Tech Stack
- Python
- Django (Web Framework)
- HTML/CSS (Templates)
- SQLite (Database)
- Scikit-learn/Pandas (for ML prediction logic)

## Key Features
- Interactive web forms for inputting property details.
- Integration of a machine learning model within a web backend.
- Dynamic rendering of predicted housing prices using Django templates.

## File Structure
- `manage.py`: The Django command-line utility.
- `house_prediction/`: The main Django project configuration folder.
- `prediction/`: The Django app handling user inputs and model inference.
- `templates/`: HTML templates for the front-end interface.
- `db.sqlite3`: The default SQLite database for the application.

## Local Setup (if applicable)
1. Clone the repository.
2. Install Django and required ML libraries: `pip install django scikit-learn pandas numpy`.
3. Run database migrations: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.
5. Access the application in your browser at `http://127.0.0.1:8000/`.