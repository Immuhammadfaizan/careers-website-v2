from flask import Flask, render_template, request, session
from pymongo import MongoClient
from flask_sessionstore import Session
from flask_session_captcha import FlaskSessionCaptcha
import uuid
import logging

app = Flask(__name__)

# MongoDB Client Setup
mongoclient = MongoClient('localhost', 27017)

# Basic App Config
app.config['SECRET_KEY'] = str(uuid.uuid4())  # Ensure it's a string
app.config['CAPTCHA_ENABLE'] = True

# Captcha Config
app.config['CAPTCHA_LENGTH'] = 5
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60

# MongoDB Session Configuration
app.config['SESSION_MONGODB'] = mongoclient  # MongoClient instance
app.config['SESSION_MONGODB_DB'] = 'captcha_db'  # Database name
app.config['SESSION_MONGODB_COLLECT'] = 'sessions'  # Collection name
app.config['SESSION_TYPE'] = 'mongodb'

# Initialize Server Session
session_store = Session(app)

# Initialize FlaskSessionCaptcha
captcha = FlaskSessionCaptcha(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if captcha.validate():
            return "Success"
        else:
            return "Captcha validation failure!"
    return render_template('form.html')  # Replace with the correct file name

if __name__ == '__main__':
    app.debug = True
    logging.getLogger().setLevel(logging.DEBUG)
    app.run()
