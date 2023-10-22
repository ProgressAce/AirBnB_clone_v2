#!/usr/bin/python3
"""Starts a Flask wep app server, listening on 0.0.0.0, port 5000.

Route:
    /: display 'Hello HBNB!'
    /hbnb: display 'HBNB'
    /c/<text>: display “C ” followed by the value of the text variable.
    /python/<text>: display “Python ”, followed by the value of the
    text variable.
    /number/<n>: display '<n> is a number' only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
    /number_odd_or_even/<n>: display a HTML page only if n is an integer
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


def is_number(num):
    """Returns True if the passed argument is an integer.
    Otherwise False is returned."""

    if '-' == num[0]:  # checks for negative <n>
        if num[1:].isdigit():
            return True
    else:
        if num.isdigit():
            return True


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """Returns '<n> is a number', only if <n> is an integer."""

    if is_number(n):
        return '{} is a number'.format(escape(n))
    else:
        return render_template('404.html')


@app.route('/number_template/<n>', strict_slashes=False)
def number_template_route(n):
    """Returns an HTML page only if <n> is an integer:

    H1 tag: 'Number: <n>' inside the tag BODY."""

    if is_number(n):
        return render_template('5-number.html', num=n)
    else:
        return render_template('404.html')


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even(n):
    """Renders a HTML page only if n is an integer:

    H1 tag: 'Number: n is even|odd' inside the tag BODY"""

    check = 'odd'
    if is_number(n):
        if int(n) % 2 == 0:
            check = 'even'
        return render_template('6-number_odd_or_even.html', num=n, check=check)
    else:
        return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
