from urlparse import urlparse, urljoin
from functools import wraps
from flask import current_app as app, g, request, redirect, url_for, session

def init_utils(app):
    app.jinja_env.globals.update(challenge_name=challenge_name)

def challenge_name():
    return "crypto"

