import datetime
import os

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('_config.py')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

def abort_ro(*args,**kwargs):
    ''' the terrible consequences for trying 
        to flush to the db '''
    print("No writing allowed, tsk!  We're telling mom!")
    return 

if os.getenv('READ_ONLY'):
    db.session.commit = abort_ro
    db.session.flush = abort_ro

from project.users.views import users_blueprint
from project.tweets.views import tweets_blueprint
from project.dms.views import dms_blueprint

# registering blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(tweets_blueprint)
app.register_blueprint(dms_blueprint)


# error handlers
@app.errorhandler(404)
def not_found(e):
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            f.write("\n404 error at {}: {}".format(current_timestamp, r))
    return render_template('404.html'), 404


# cannot test this in development
@app.errorhandler(500) # pragma: no cover
def internal_error(e):
    db.session.rollback()
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            f.write("\n500 error at {}: {}".format(current_timestamp, r))
    return render_template('500.html'), 500
