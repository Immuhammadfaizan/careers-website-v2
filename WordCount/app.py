from flask import Flask, request, render_template
from datetime import date

app = Flask(__name__)

# here we'll set two different times
time1 = date.today().strftime('%m_%d_%y')
time2 = date.today().strftime('%d-%B-%Y')

def replace_lines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

# routing functions
@app.route('/')
def home():
    return render_template('home.html', timetoday2 = time2)

@app.route('/count', methods=['POST', 'GET'])
def count():
    text = request.form['text']
    
    words = len(text.split())
    paras = replace_lines(text)
    
    text = text.replace('\r', ' ').replace('\n', ' ')
    
    chars = len(text)
    return render_template('home.html', paras = paras,  words = words, chars = chars, timetoday2 = time2)

if __name__ == '__main__':
    app.run(debug = True)