# coding:utf-8
import os
os.environ['FLASK_ENV'] = 'development' 

from flask import Flask, render_template, flash, request
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'you-will-never-guess'

data = {'textvalue': 'default'}

@app.route('/')           # indica que dirección dispara la función
@app.route('/index', methods=('GET', 'POST'))
def index():
    global data


    if request.method == 'POST':
        data.textvalue = request.form['fname']
        print(data.textvalue)


    return render_template('app.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')