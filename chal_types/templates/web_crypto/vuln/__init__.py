from flask import Flask, render_template, request, redirect, abort, session, jsonify, json as json_mod, url_for
from flask.ext.session import Session
import logging
import os
import sqlalchemy

def create_app(username="", password=""):
    app = Flask("vuln", static_folder="../static", template_folder="../templates")
    with app.app_context():
        app.config.from_object('vuln.config')

        Session(app)

        from vuln.views import init_views
        from vuln.errors import init_errors
        from vuln.utils import init_utils

        init_views(app)
        init_errors(app)
        init_utils(app)

        return app

