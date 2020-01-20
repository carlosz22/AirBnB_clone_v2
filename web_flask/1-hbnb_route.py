#!/usr/bin/python3
"""
Simple Flask application with two routes
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """Hello function"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """HBTN route"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
