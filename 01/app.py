# coding:utf-8
import os
os.environ['FLASK_ENV'] = 'development' # development (debug mode) or production?

from flask import Flask
app = Flask(__name__)     # nombre del modulo o paquete

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
def hello():
    return "Hola Mundo Cruel!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Se ejecuta con python3 app.py