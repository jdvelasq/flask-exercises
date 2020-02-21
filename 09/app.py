# coding:utf-8
import os
os.environ['FLASK_ENV'] = 'development' 

from flask import Flask, render_template, flash
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
def index():

    flash( 'msg 1')
    flash( 'msg 2')
    flash( 'msg 3')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')