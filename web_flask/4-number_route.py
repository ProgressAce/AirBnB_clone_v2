#!/usr/bin/python3
"""Starts a Flask wep app server, listening on 0.0.0.0, port 5000.

Route:
    /: display 'Hello HBNB!'
    /hbnb: display 'HBNB'
    /c/<text>: display “C ” followed by the value of the text variable.
    /python/<text>: display “Python ”, followed by the value of the
    text variable.
    /number/<n>: display '<n> is a number' only if n is an integer
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Returns 'Hello HBNB!' to the browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Returns 'HBNB' to the browser"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text_page(text):
    """Returns 'C ' followed by the value of the text variable.
    Replaces underscore _ symbols with a space."""

    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text_page(text='is cool'):
    """Returns 'Python ' followed by the value of the text variable.
    Replaces underscore _ symbols with a space."""

    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """Returns '<n> is a number', only if <n> is an integer."""

    is_int = False
    if '-' == n[0]:  # checks for negative <n>
        if n[1:].isdigit():
            is_int = True
    else:
        if n.isdigit():
            is_int = True

    if is_int:
        return '{} is a number'.format(escape(n))
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
