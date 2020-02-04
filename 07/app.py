import os
os.environ['FLASK_ENV'] = 'development' # development (debug mode) or production?

from flask import Flask, render_template, g, request
app = Flask(__name__)     # nombre del modulo o paquete

import pandas as pd

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
def myapp():
    if 'df' not in g:
        g.df = pd.read_csv('data.csv')

    selection = request.form['regions']


    return render_template('dashboard.html', listvalues=g.df.columns[1:], selection=selection)

if __name__ == "__main__":
    app.run(host='0.0.0.0')