# imports
import datetime
from functools import wraps
from flask import (flash, redirect, render_template,
    request, session, url_for, Blueprint)
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_

from project import db
from project.models import User, Tweet, Follower, DM

# config
dms_blueprint = Blueprint('dms', __name__)

# helper functions

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first')
            return (redirect(url_for('users.login')))
    return wrap


def filtered_dms(user_id):
    user_dms = db.session.query(DM).filter(or_(DM.from_user_id == user_id, DM.to_user_id == user_id))
    groups = {}
    for dm in user_dms:
        group_key = dm.from_user_id if dm.from_user_id != user_id else dm.to_user_id
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(dm)

    return groups

# routes

@dms_blueprint.route('/dms/')
@login_required
def dm():
    return render_template(
        'dms.html',
        all_dms=filtered_dms(session['user_id']),
    )