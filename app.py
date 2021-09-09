import Adafruit_DHT
from flask import Flask, render_template

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 18


app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    return render_template('index.html',temp = temperature,humi = humidity)


app.run(debug=False,host='192.168.53.166')
