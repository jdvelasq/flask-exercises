# coding:utf-8

from flask import Flask, render_template, flash, request
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/', methods=('GET', 'POST')) 
@app.route('/index', methods=('GET', 'POST'))
def index():
    data = 'data-original'

    if request.method == 'POST':
        data = request.form['fname']
        flash(data)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)