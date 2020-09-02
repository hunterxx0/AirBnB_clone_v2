#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def stt_list():
    """ Displays states """
    stt = [ st for st in storage.all('State').values()]
    stt = sorted(stt, key=lambda x: x.name)
    return (render_template('7-states_list.html', stt=stt))


@app.teardown_appcontext
def teardown():
    """ Close """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
