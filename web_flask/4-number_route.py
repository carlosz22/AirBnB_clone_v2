#!/usr/bin/python3
"""
Simple Flask application with five routes
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

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Python route"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """Number route"""
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
