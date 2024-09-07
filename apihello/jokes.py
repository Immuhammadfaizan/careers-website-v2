from flask import Flask
import pyjokes

app = Flask(__name__)

@app.route('/')
def onejoke():
    joke = pyjokes.get_joke()
    return f'<h2>{joke}</h2>'

@app.route('/multiplejokes', methods = ['GET'])
def multiplejokes():
    jokes = pyjokes.get_jokes()
    return f'<h2>{jokes}</h2>'

if __name__ == '__main__':
    app.run(debug = True)
