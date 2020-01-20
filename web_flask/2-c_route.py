#!/usr/bin/python3
"""
Simple Flask application with three routes
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

@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """C route"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
