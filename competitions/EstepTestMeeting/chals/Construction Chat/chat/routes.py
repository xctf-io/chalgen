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
chat_messages = [{'name': 'BossMan', 'messages': ["Educator1, I've been hearing some complaints from our students about the smell of the roofing material we've been using. Can you tell me what's going on?"]}, {'name': 'Educator1', 'messages': ["Yes, BossMan. The roofing material we've been using contains toxic chemicals that emit a strong odor. Prolonged exposure to these chemicals can have negative effects on the health of our students."]}, {'name': 'BossMan', 'messages': ["I understand your concern, but we need to get the job done. Can't we just provide our students with masks or something to protect them?"]}, {'name': 'Educator1', 'messages': ['Masks may provide some level of protection, but they are not a solution to the problem. The odor is a clear indication that the chemicals are being released into the air, which means that the students are still being exposed to them. In addition, the odor itself can cause nausea and headaches, which can affect the productivity and well-being of our students.']}, {'name': 'BossMan', 'messages': ["I see your point, but we have a tight deadline to meet. We can't afford to delay the project or use a different roofing material. Can't we just ask our students to tough it out for a little longer?", "droco cdenoxdc kbo mywzvksxsxq dyy wemr...s'vv cryg drow...dro myxmbodo wsh sxmvenoc k vsddvo bknsy-kmdsfo wkdobskv...droi gyx'd uxyg exdsv droi rkfo mrsvnbox pvkq{k_fobi_lkcsm_mkockb_mszrob}"], 'chal': 'Caesar Challenge'}, {'name': 'Educator1', 'messages': ['I understand that we have a deadline to meet, but we cannot compromise the health and safety of our students. The negative effects of prolonged exposure to these toxic chemicals can be serious and long-lasting. As a responsible institution, it is our duty to provide a safe learning environment for our students.']}, {'name': 'BossMan', 'messages': ["I see your point, Educator1. I don't want to put our students in harm's way. Let's find a way to address this issue immediately. Can you recommend a safer roofing material that we can switch to?"]}, {'name': 'Educator1', 'messages': ['Yes, I can recommend several roofing materials that are free from toxic chemicals and do not emit strong odors. I will provide you with a list of options, and we can discuss which one would be the best fit for our project.']}, {'name': 'BossMan', 'messages': ["Thank you, Educator1. I appreciate your expertise and your commitment to our students' health and safety. Let's make sure that we take the necessary steps to address this issue as soon as possible.", 'http://chal-host.chals.mcpshsf.com/construction.jpg'], 'chal': 'Exif Challenge'}, {'name': 'Educator1', 'messages': ["You're welcome, BossMan. It's important to prioritize the well-being of our students."]}, {'name': 'BossMan', 'messages': ['Bye!']}, {'name': 'Educator1', 'messages': ['Goodbye, BossMan.']}]

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
                               chat_name="PHS Bickering about Smells"
                               )
    else:
        return render_template("index.html", title="PHS Bickering about Smells", chat_messages=chat_messages)


@ app.route("/logout")
@ login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
