# coding:utf-8
import os
os.environ['FLASK_ENV'] = 'development' # development (debug mode) or production?

from flask import Flask
from flask import escape
app = Flask(__name__)     # nombre del modulo o paquete

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
def hello():
    return "Hola Mundo Cruel!"

@app.route('/about')
def about():
    return "about page"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
    # example: http://0.0.0.0:5000/user/jdvelsq

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    # example: http://0.0.0.0:5000/post/12


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
    # example: http://0.0.0.0:5000/path/directory

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# Se ejecuta con python3 app.py