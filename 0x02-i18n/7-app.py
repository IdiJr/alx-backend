#!/usr/bin/env python3
"""
App module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_locale
from routes.routes_7 import app_routes
import pytz


app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


class Config(object):
    """ Class config app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)
app.register_blueprint(app_routes)

def get_user(user_id):
    """get_user function to return a user dictionary
    or None if the ID cannot be found or if login_as
    was not passed """
    return users.get(user_id)


@babel.localeselector
def get_locale():
    """ get locale
    """
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ get timezone """
    if 'timezone' in request.args:
        try:
            pytz.timezone(request.args['timezone'])
            return request.args['timezone']
        except pytz.UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass
        # Resort to the default timezone if no valid timezone is found
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """ before request
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/')
def index() -> str:
    """ index
    """
    return render_template(
        '7-index.html', title=_('home_title'),
        header=_('home_header')
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
