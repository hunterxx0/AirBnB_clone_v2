#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)



@app.route('/hbnb_filters', strict_slashes=False)
def filt():
    """ Displays filters """
    stt = storage.all('State').values()
    ame = storage.all('Amenity').values()
    return (render_template('10-hbnb_filters.html', stt=stt, ame=ame))


@app.teardown_appcontext
def teardown(exception):
    """ Close """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
