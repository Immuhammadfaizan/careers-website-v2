from flask import Flask, render_template, request
from pymongo import MongoClient
from flask_session import Session
from flask_session_captcha import FlaskSessionCaptcha
import uuid
import logging

# Create Flask application
app = Flask(__name__)

# Setup MongoDB client
mongoclient = MongoClient('localhost', 27017)

# Basic application configuration
app.config['SECRET_KEY'] = str(uuid.uuid4())  # Generate a random secret key
app.config['CAPTCHA_ENABLE'] = True

# Captcha configuration
app.config['CAPTCHA_LENGTH'] = 5
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60

# Session configuration for MongoDB
app.config['SESSION_TYPE'] = 'mongodb'
app.config['SESSION_MONGODB'] = mongoclient
app.config['SESSION_MONGODB_DB'] = 'captcha_db'  # Database name
app.config['SESSION_MONGODB_COLLECT'] = 'sessions'  # Collection name

# Initialize server-side session management
Session(app)

# Initialize FlaskSessionCaptcha
captcha = FlaskSessionCaptcha(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Validate CAPTCHA
        if captcha.validate():
            return "Success"
        else:
            return "Captcha validation failure!"
    return render_template('form.html')  # Render the form template

if __name__ == '__main__':
    app.debug = True
    logging.getLogger().setLevel(logging.DEBUG)
    app.run()
