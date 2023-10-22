#!/usr/bin/python3
"""Starts a Flask web app server, listening on 0.0.0.0 port 5000.

Route:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Returns 'Hello HBNB!' to the browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Returns 'HBNB' to the browser"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
