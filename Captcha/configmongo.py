import uuid 
import logging 
from flask import Flask, request, render_template 
from flask_sessionstore import Session 
from flask_session_captcha import FlaskSessionCaptcha 
from pymongo import MongoClient 

app = Flask(__name__) 

# Database Config 
# If your mongodb runs on a different port 
# change 27017 to that port number 
mongoClient = MongoClient('localhost', 27017) 

# Captcha Configuration 
app.config["SECRET_KEY"] = uuid.uuid4() 
app.config['CAPTCHA_ENABLE'] = True

# Set 5 as character length in captcha 
app.config['CAPTCHA_LENGTH'] = 5

# Set the captcha height and width 
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['SESSION_MONGODB'] = mongoClient 
app.config['SESSION_TYPE'] = 'mongodb'

# Enables server session 
Session(app) 

# Initialize FlaskSessionCaptcha 
captcha = FlaskSessionCaptcha(app) 

@app.route('/', methods=['POST', 'GET']) 
def index(): 
	if request.method == "POST": 
		if captcha.validate(): 
			return "success"
		else: 
			return "fail"

	return render_template("form.html") 


if __name__ == "__main__": 
	app.debug = True
	logging.getLogger().setLevel("DEBUG") 
	app.run() 
