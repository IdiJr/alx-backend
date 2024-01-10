#!/usr/bin/env python3
""" 3-app module """
from flask import Flask, render_template, request
from flask_babel import Babel, _
from routes.routes_3 import app_routes


app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


class Config:
    """ Config class for configuring available
    languages, default locale, and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.register_blueprint(app_routes)


def get_locale():
    """ get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
