# coding:utf-8
# import os
# os.environ['FLASK_ENV'] = 'development' 

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') 
@app.route('/index')
def hello():
    user = {'username': 'YO'} # use a dictionary 
    mylist = [1, 2, 3, 4, 5, 6]
    return render_template('hello.html', user=user, mylist=mylist)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)