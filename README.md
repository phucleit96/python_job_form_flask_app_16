# Job Application Form
![DEMO](https://i.imgur.com/isrocMU.gif)

This project is a simple job application form built with Flask, SQLAlchemy, and Flask-Mail. It allows users to submit their job application details, which are then stored in a SQLite database and a confirmation email is sent to the user.

## Features

- Form submission with validation
- Data persistence with SQLAlchemy and SQLite
- Email confirmation with Flask-Mail

## Installation

To install the project, follow these steps:

1. Clone the repository:

2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Set your email password as an environment variable:
```bash
export PASSWORD=yourpassword
```
## Usage

To run the project, use the following command:
```bash
python app.py
```
Then, open your web browser and navigate to `http://localhost:5001`.
## Project Structure
- `app.py`: This is the main file where the Flask application is created and configured. It also defines the database model and the route for the form.
- `templates/index.html`: This is the HTML template for the form.
- `data.db`: This is the SQLite database where the form data is stored.


