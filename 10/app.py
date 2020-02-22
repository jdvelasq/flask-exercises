# coding:utf-8
import os
os.environ['FLASK_ENV'] = 'development' 

from flask import Flask, render_template, flash
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pag')
def pag():
    return render_template('pag.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')