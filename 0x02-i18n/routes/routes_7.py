#!/usr/bin/env python3
"""Basic route task 0"""
from flask import Blueprint, render_template
from flask_babel import _


app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/', methods=["GET"], strict_slashes=False)
def home():
    """ Home page """
    return render_template(
        '7-index.html', title=_('home_title'),
        header=_('home_header')
    )
