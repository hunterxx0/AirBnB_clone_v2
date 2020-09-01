#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Displays “Hello HBNB!” """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays "HBNB" """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays "C" followed by text """
    return ('C ' + text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    """ Displays "Python" followed by text """
    return ('Python ' + text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def int_num(n):
    """ Displays n if it(s an integer """
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_templ(n):
    """ display a HTML page """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ display a HTML page """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, ev_od='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, ev_od='odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
