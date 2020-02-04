# coding:utf-8
import os
os.environ['FLASK_ENV'] = 'development' # development (debug mode) or production?

from flask import Flask, render_template
app = Flask(__name__)     # nombre del modulo o paquete

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')