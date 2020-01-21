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


@app.route('/states_list', strict_slashes=False)
def show_states():
    """Show a list of states"""
    all_states = storage.all('State')
    return render_template('7-states_list.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
