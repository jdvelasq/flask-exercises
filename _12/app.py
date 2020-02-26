import os
# os.environ['FLASK_ENV'] = 'development' # development (debug mode) or production?

from flask import Flask, request, render_template
app = Flask(__name__)     # nombre del modulo o paquete

@app.route('/')           # indica que dirección dispara la función
@app.route('/index', methods=['POST', 'GET'])
def hello():

    seleccion="ninguna"

    if request.method == 'GET':
        seleccion='helloooooooo'


    return render_template('app.html', text="texto de prueba", seleccion=seleccion)

if __name__ == "__main__":
    app.run(host='0.0.0.0')