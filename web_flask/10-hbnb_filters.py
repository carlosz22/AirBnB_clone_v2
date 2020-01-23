#!/usr/bin/python3
"""
Flask web app to fetch filters for AirBnB
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(txt):
    """Restart session with storage"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def show_filters():
    """Show AirBnB filters (states, amenities)"""
    all_states = storage.all('State')
    all_amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=all_states,
                           amenities=all_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
