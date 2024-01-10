#!/usr/bin/env python3
"""Basic route task 0"""
from flask import Blueprint, render_template


app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/', methods=["GET"], strict_slashes=False)
def home():
    """
    Route for the main page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template(
        '0-index.html', title='Welcome to Holberton',
        header='Hello world'
    )
