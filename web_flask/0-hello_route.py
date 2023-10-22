#!/usr/bin/python3
"""Starts a Flask web application, listening on 0.0.0.0, port 5000.

Routes:
    /: displays 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_route():
    """returns 'Hello HBNB!' to the browser"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
