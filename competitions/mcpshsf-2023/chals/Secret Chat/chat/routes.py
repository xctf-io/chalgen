from datetime import timedelta
from flask import (
    render_template,
    redirect,
    flash,
    url_for,
    session
)

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
chat_messages = [{'name': 'chance', 'messages': ['hello!', 'anyone here?']}, {'name': 'bob', 'messages': ['hey chance!', "how's it going?"]}, {'name': 'nick', 'messages': ['hey guys!', 'wassup?']}, {'name': 'chance', 'messages': ['not much', 'just selling some latkes :)']}, {'name': 'bob', 'messages': ['oh yeah btw', 'you need to up your latkes sales', 'the cartel is LOSING money!!!']}, {'name': 'chance', 'messages': ['yo chill', "i'm doing my best :("]}, {'name': 'bob', 'messages': ['well you better do better', 'or else...']}, {'name': 'chance', 'messages': ['or else what?']}, {'name': 'bob', 'messages': ['you know the rules', 'you break them, you pay the price...']}, {'name': 'nick', 'messages': ['you right bob', "we gotta make sure we're making money"]}, {'name': 'bob', 'messages': ['yeah', "if we don't make money, we're gonna have to sell our souls to the pancake cartel"]}, {'name': 'nick', 'messages': ['*throws up*', 'pancakes are gross', 'chance you better sell more latkes']}, {'name': 'chance', 'messages': ['bruh stop being so mean bob', 'just give me a chance']}, {'name': 'bob', 'messages': ['hey nick', "i got somethin' to tell you"]}, {'name': 'nick', 'messages': ["what's up bob?"]}, {'name': 'bob', 'messages': ["wait i don't want chance to hear this", 'decode this using our secret code', 'Nulla pellentesque dignissim enim sit amet venenatis urna cursus eget. Aliquam purus sit amet luctus venenatis lectus. Pellentesque habitant morbi tristique senectus et netus et. Faucibus a pellentesque sit amet. Aliquet bibendum enim facilisis gravida neque convallis a. Ut placerat orci nulla pellentesque. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Hac habitasse platea dictumst quisque sagittis. Tempor orci dapibus ultrices in iaculis nunc sed. A scelerisque purus semper eget.឵\u180e\u180e឵឵\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵឵឵឵\u180e឵\u180e\u180e឵឵\u180e\u180e\u180e឵\u180e\u180e\u180e\u180e឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e឵឵឵\u180e\u180e឵឵឵឵឵឵\u180e\u180e឵឵឵឵឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e឵\u180e\u180e឵\u180e឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e\u180e឵឵឵឵\u180e឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e\u180e឵឵\u180e\u180e\u180e឵\u180e\u180e឵\u180e឵឵឵឵឵\u180e\u180e឵឵឵឵឵\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e\u180e឵\u180e឵឵឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e឵឵឵\u180e\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e឵឵\u180e឵឵឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e\u180e\u180e\u180e឵឵\u180e឵឵\u180e\u180e឵឵឵឵឵\u180e\u180e\u180e឵\u180e឵\u180e឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵឵\u180e\u180e឵\u180e឵឵឵\u180e\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e\u180e឵\u180e឵឵឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e឵឵\u180e\u180e឵឵\u180e\u180e឵឵\u180e\u180e឵឵\u180e\u180e឵\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e\u180e឵\u180e\u180e឵\u180e឵឵\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e\u180e\u180e\u180e឵\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e឵\u180e឵឵឵឵\u180e\u180e឵឵឵឵\u180e឵\u180e\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e឵឵\u180e឵\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e\u180e឵\u180e឵឵឵\u180e\u180e\u180e឵\u180e឵\u180e឵\u180e\u180e\u180e឵឵឵឵឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e឵឵\u180e឵឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵\u180e\u180e឵\u180e\u180e឵឵឵឵\u180e឵\u180e\u180e\u180e឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵឵឵឵឵\u180e\u180e\u180e឵឵\u180e឵឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵\u180e\u180e឵឵឵\u180e឵឵\u180e\u180e឵឵឵឵\u180e឵\u180e\u180e឵឵឵\u180e឵឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e\u180e\u180e឵឵\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e឵\u180e឵឵឵឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵\u180e\u180e\u180e឵\u180e឵\u180e឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵឵\u180e឵឵឵\u180e\u180e឵\u180e\u180e\u180e឵឵឵\u180e឵឵\u180e\u180e\u180e឵\u180e\u180e\u180e឵\u180e឵឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵឵\u180e឵\u180e឵\u180e\u180e\u180e឵\u180e\u180e឵឵\u180e\u180e឵឵\u180e឵\u180e឵\u180e\u180e឵\u180e\u180e\u180e឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵឵឵\u180e឵឵\u180e\u180e឵឵\u180e឵\u180e឵\u180e\u180e឵឵\u180e឵\u180e឵\u180e\u180e឵\u180e\u180e\u180e឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e឵\u180e\u180e\u180e឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵\u180e឵឵឵\u180e\u180e឵\u180e឵឵឵឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e឵឵឵឵\u180e឵\u180e\u180e\u180e឵឵\u180e឵឵\u180e\u180e\u180e឵\u180e឵឵឵\u180e\u180e឵឵\u180e឵\u180e឵\u180e\u180e឵\u180e\u180e឵឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵\u180e឵឵឵\u180e\u180e឵឵឵\u180e឵឵\u180e\u180e឵\u180e឵឵឵឵឵\u180e឵\u180e\u180e\u180e឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵឵឵\u180e឵឵\u180e\u180e\u180e឵\u180e឵\u180e឵\u180e\u180e\u180e឵\u180e឵឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e឵឵\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e\u180e឵\u180e឵឵឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e឵឵឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵\u180e\u180e\u180e឵\u180e\u180e឵឵\u180e\u180e឵឵\u180e឵\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e឵឵឵឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e឵\u180e\u180e឵\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵឵឵\u180e឵឵\u180e\u180e឵឵឵\u180e\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e឵឵឵឵\u180e\u180e឵឵\u180e឵\u180e឵឵\u180e឵឵\u180e\u180e\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e\u180e឵\u180e\u180e\u180e\u180e឵឵\u180e឵឵឵឵឵឵\u180e\u180e឵\u180e\u180e\u180e឵឵\u180e\u180e឵\u180e឵឵\u180e឵\u180e\u180e឵឵឵\u180e\u180e឵\u180e\u180e឵឵\u180e឵\u180e឵឵\u180e឵឵឵឵឵឵឵\u180e\u180e\u180e\u180e឵឵឵឵\u180e\u180e឵឵\u180e\u180e'], 'chal': 'Invisible Message'}, {'name': 'chance', 'messages': ['this is not cool bob', "why can't you tell me?"]}, {'name': 'bob', 'messages': ["i'm sorry chance", "but it's top secret"]}, {'name': 'nick', 'messages': ['LOL bob', "you're so funny"]}, {'name': 'bob', 'messages': ['IKR', "i'm hilarious"]}, {'name': 'chance', 'messages': ['stop excluding me guys', "i'm your friend too ;("]}, {'name': 'bob', 'messages': ["hey y'all i got a keylogger on corncob's computer", "i'm gonna see what he's up to >:)"]}, {'name': 'nick', 'messages': ['nice job bob!!!', 'let us know what you find']}, {'name': 'bob', 'messages': ['ok got it', 'the keylogger gave me this file', "can y'all help me find what he typed?", 'http://127.0.0.1:8200/keylog.pcap'], 'chal': 'Keyboard Input'}, {'name': 'nick', 'messages': ['i got no clue what this is', 'chance do you know?']}, {'name': 'chance', 'messages': ["i don't know either", "i'm no computer expert LOL"]}, {'name': 'bob', 'messages': ["well i guess we'll never know"]}, {'name': 'nick', 'messages': ["y'all i was drawing something and my computer crashed", 'i managed to get a memory dump of the computer', 'can someone help me recover my drawing?'], 'chal': 'Memory Dump'}, {'name': 'chance', 'messages': ['what were you drawing?']}, {'name': 'nick', 'messages': ["i can't tell you", "it's a surprise for someone", 'anyways, can you help me?']}, {'name': 'chance', 'messages': ["nah i'm not good at that stuff", 'i just sell latkes lol']}, {'name': 'nick', 'messages': ['how about you bob?']}, {'name': 'bob', 'messages': ["i'm not good at that stuff either", 'maybe ask a forensic expert']}, {'name': 'nick', 'messages': ['ok thanks guys']}, {'name': 'bob', 'messages': ["alright i'm gonna go", "i'll talk to you guys later"]}, {'name': 'nick', 'messages': ['bye bob']}, {'name': 'chance', 'messages': ['bye bob', 'have a good day']}, {'name': 'bob', 'messages': ['bye nick']}, {'name': 'chance', 'messages': ['so rude bob', "anyways i'm gonna go too", "i'll see y'all later >:)"]}, {'name': 'nick', 'messages': ['bye chance']}]

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
                               chat_name="Latke Cartel"
                               )
    else:
        return render_template("index.html", title="Latke Cartel", chat_messages=chat_messages)


@ app.route("/logout")
@ login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
