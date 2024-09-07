from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'Bahawalnagar'

    api = '4ea81429628aee36da9c748307efcabe'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'

    try:
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)
    except Exception as e:
        list_of_data = {'error': str(e)}

    data = {
        "country_code": str(list_of_data['sys']['country']),
        "cityname": city,
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'K',
        "temp_cel": str(round(list_of_data['main']['temp'] - 273.15, 2)) + 'C', 
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }

    print(data)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
