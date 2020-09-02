#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<st_>', strict_slashes=False)
def stt_id(st_=None):
    """ Displays states """
    stt = storage.all('State')
    if st_:
        st_ = "State.{}".format(st_)
    return (render_template('9-states.html', stt=stt, st_=st_))


@app.teardown_appcontext
def teardown(exception):
    """ Close """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
