# Importing necessary modules from Flask, SQLAlchemy, Flask-Mail, os and datetime
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
from datetime import datetime

# Creating a new Flask web server from the Flask module
app = Flask(__name__)

# Configuring the Flask app with various parameters for secret key, database, mail server, mail port, mail SSL usage, mail username and password
app.config["SECRET_KEY"] = "letranhuyenminh1108@"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "badboy27796@gmail.com"
app.config['MAIL_PASSWORD'] = os.getenv("PASSWORD")

# Creating a SQLAlchemy ORM instance for our Flask app
db = SQLAlchemy(app)

# Creating a Flask-Mail instance for our Flask app
mail = Mail(app)

# Defining a new model 'Form' for our database with fields id, first_name, last_name, email, date, occupation
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

# Defining a route for our web server at '/' and allowing both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    # If the request method is POST, we process the form data
    if request.method == "POST":
        # Extracting form data for first_name, last_name, email, date, occupation
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        # Converting the date string into a datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form['occupation']

        # Creating a new Form instance with the extracted form data
        form = Form(first_name=first_name, last_name=last_name, email=email, date=date_obj, occupation=occupation)
        # Adding the new Form instance to our database session
        db.session.add(form)
        # Committing (saving) our database session changes
        db.session.commit()

        # Creating a message body for the email
        message_body = f"""
        Thank you for your job submission, {first_name}
        Here are your data: \n{first_name}\n{last_name}\n{date}\n
        Thank you very much!
        """
        # Creating a new Mail Message instance with the subject, sender, recipients and body
        message = Message(subject="New form submission",
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[email],
                          body=message_body)
        # Sending the email through our Flask-Mail instance
        mail.send(message)
        # Flashing a success message to the user
        flash(f"{first_name}, your form was submitted successfully!", "success")
    # If the request method is not POST, we render the index.html template
    return render_template("index.html")

# If this file is being run directly, we start our Flask app
if __name__ == "__main__":
    # Creating all database tables according to the models
    with app.app_context():
        db.create_all()
    # Running our Flask app with debug mode on and on port 5001
    app.run(debug=True, port=5001)