#!/usr/bin/python3
"""
Flask web app to fetch states
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(txt):
    """Restart session with storage"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_state():
    """Show a list of states"""
    all_states = storage.all('State')
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
