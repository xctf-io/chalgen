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

    users = [{'name': 'BossMan', 'password': 'password1'}, {'name': 'Educator1', 'password': 'password2'}]
    for user in users:
        add_user(user["name"], user["password"])


deploy()
