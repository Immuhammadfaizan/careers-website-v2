from flask import Flask, request, render_template
from datetime import date
import random 
import string

app = Flask(__name__)

# two different timestamp are:
datetoday1 = date.today().strftime('%m_%d_%y')
datetoday2 = date.today().strftime('%d-%B-%Y')

# Functions:
@app.route('/')
def home():
    return render_template('home.html', datetoday2 = datetoday2)

@app.route('/genpassword', methods = ['POST', 'GET'])
def genpassword():
    
    min_length = 8
    max_length = 30
    
    pass_length = int(request.form.get('pass_len'))
    
    if pass_length < min_length:
        return render_template('home.html', todaydate2 = datetoday2, mess = f'Password length should be atleast {min_length}!')
    if pass_length > max_length:
        return render_template('home.html', datetoday2 = datetoday2, mess = f'Password length should be less or equals to {max_length}!')
    
    include_spaces = request.form.get('spaces')
    include_uppercase_letters = request.form.get('uppchars')
    include_digits = request.form.get('digits')
    include_special_characters = request.form.get('specialchars')

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    print(include_spaces, include_uppercase_letters, include_digits, include_special_characters)
    
    char_set = [lowercase]
    
    if include_spaces == 'on':
        char_set.append(' ')
    if include_digits == 'on': 
        char_set.append(digits)
    if include_uppercase_letters == 'on':
        char_set.append(uppercase)
    if include_special_characters == 'on':
        char_set.append(special_characters)
        
    ## join all the character sets
    all_chars = ''.join(char_set)
    
    password = random.choices(all_chars, k=pass_length)
    password = ''.join(password)
    
    return render_template('home.html', datetoday2 = datetoday2, generate_password = password)

if __name__ == '__main__':
    app.run(debug = True)