#!/usr/bin/python3
"""0x04. AirBnB clone - Web framework, task 8. List of states
"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.teardown_appcontext
def states_list_teardown(self):
    """ Ensures SQLAlchemy session opened to serve dynamic content for HTML
    templates is closed after serving.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Requests list of `State`s ordered by name, which populates HTML
    template served to '/states_list'.
    """
    # session = storage._DBStorage__session
    # states_sorted = session.query(State).order_by(State.name).all()

    # states = storage.all(State).values()
    # states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
