#!/usr/bin/env python3
""" Route module for the API - Mock logging in"""


from flask import Flask, render_template, g, request
from os import getenv
from flask_babel import Babel
from routes.routes_5 import app_routes

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Setup - Babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config class as configuration for the Flask app
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(app_routes)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 5-index.html
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Determines best match for supported languages """
    # check if there is a locale parameter/query string
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    """ Returns user dict if ID can be found """
    return users.get(user_id)


@app.before_request
def before_request():
    """ Finds user and sets as global on flask.g.user """
    user_id = request.args.get('login_as')

    # Set user as global on flask.g.user
    g.user = get_user(int(user_id)) if user_id else None


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
