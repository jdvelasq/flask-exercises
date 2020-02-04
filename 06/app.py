import os
os.environ['FLASK_ENV'] = 'development' # development (debug mode) or production?

from flask import Flask, request
app = Flask(__name__)     # nombre del modulo o paquete

@app.route('/')           # indica que dirección dispara la función
@app.route('/index')
@app.route('/login', methods=['POST', 'GET'])
def hello():
error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0')