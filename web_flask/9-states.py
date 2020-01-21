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


@app.route('/states', strict_slashes=False)
def show_states():
    """Show a list of states"""
    all_states = storage.all('State')
    return render_template('9-states.html', states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def show_states_element(id):
    """Show a list of states"""
    all_states = storage.all('State')
    for state in all_states.values():
        if state.id == id:
            state_found = state
            return render_template('9-states.html', state_cities=state_found)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
