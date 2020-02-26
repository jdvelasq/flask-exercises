# coding:utf-8
# import os
# os.environ['FLASK_ENV'] = 'development' 

from flask import Flask, render_template, flash, request, redirect
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')           # indica que dirección dispara la función
@app.route('/index', methods=('GET', 'POST'))
def index():
    data = 'data-original'

    if request.method == 'POST':
        data = request.form['fname']
        flash(data)

    return render_template('app.html', data=data)


@app.route('/form', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        return redirect("/index")

    return render_template('form.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)