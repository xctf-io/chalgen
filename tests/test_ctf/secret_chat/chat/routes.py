from datetime import timedelta
from flask import (
    render_template,
    redirect,
    flash,
    url_for,
    session
)
import bjoern


from flask_bcrypt import check_password_hash

from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required,
)

from app import create_app, login_manager
from models import User
from forms import login_form


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app = create_app()
chat_messages = [{'name': 'Alice', 'messages': ['Hello Bob!', 'How are you?']}, {'name': 'Bob', 'messages': ['Hello Alice!', "I'm fine, thanks!"]}, {'name': 'Alice', 'messages': ['Good to hear!']}, {'name': 'Bob', 'messages': ['Bye!']}, {'name': 'Alice', 'messages': ['Bye!']}]

@ app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)


@ app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    if not current_user.is_authenticated:
        form = login_form()
        if form.validate_on_submit():
            try:
                user = User.query.filter_by(
                    username=form.username.data).first()
                if check_password_hash(user.pwd, form.pwd.data):
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash("Invalid Username or password!", "danger")
            except Exception as e:
                flash(e, "danger")

        return render_template("auth.html",
                               form=form,
                               title="Login",
                               chat_name="Secret Chat"
                               )
    else:
        return render_template("index.html", title="Secret Chat", chat_messages=chat_messages)


@ app.route("/logout")
@ login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    bjoern.run(app, "127.0.0.1", 5000)
