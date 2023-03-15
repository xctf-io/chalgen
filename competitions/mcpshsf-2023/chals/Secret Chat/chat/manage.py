from app import create_app, db
from flask_migrate import upgrade, migrate, init, stamp
from models import User
from flask_bcrypt import generate_password_hash

def add_user(username, password):
    newuser = User(
        username=username,
        pwd=generate_password_hash(password),
    )
    db.session.add(newuser)
    db.session.commit()

def deploy():
    """Run deployment tasks."""

    app = create_app()
    app.app_context().push()
    db.create_all()

    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()

    users = [{'name': 'chance', 'password': 'mhm_p0t4t0es'}, {'name': 'bob', 'password': 'l4tk3c4rt3lforever'}, {'name': 'nick', 'password': 'eatm0r3l4tk3s!!!'}]
    for user in users:
        add_user(user["name"], user["password"])


deploy()
