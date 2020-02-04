# coding:utf-8
import os
os.environ['FLASK_ENV'] = 'development' # development (debug mode) or production?

from flask import Flask
app = Flask(__name__)     # nombre del modulo o paquete

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
def hello():
    return "Hola Mundo Cruel!"

@app.route('/about')
def about():
    return "about page"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# Se ejecuta con python3 app.py