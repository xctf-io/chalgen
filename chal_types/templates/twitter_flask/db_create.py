import yaml
import datetime
import os

from project import db, bcrypt
from project.models import Tweet, User, Follower, DM

os.system("rm project/database.db")

db.create_all()
db.session.commit()

with open('twitter_contents.yaml') as f:
    data = yaml.safe_load(f)

users = data['users']
messages = data['messages']
followers = data['followers'] if data['followers'] is not None else []
dms = data['dms']

for user in users:
    if user.get('email') and user.get('password'):
        db.session.add(
            User(
                user['name'],
                user['email'],
                bcrypt.generate_password_hash(user['password'].encode("utf-8")),
                "character"
                )
            )
    else:
        password = user['name'].encode("utf-8") + "$up3rsecret"
        db.session.add(User(user['name'], user['name'] + "@a.com", bcrypt.generate_password_hash(password), "character"))
db.session.commit()

user_objs = {}
users = User.query.all()
for user in users:
    user_objs[user.name] = user

for message in messages:
    if message.get('date'):
        date = datetime.datetime.strptime(message['date'], '%m/%d/%y')
    else:
        date = datetime.datetime.now()
    db.session.add(Tweet(message['text'], date, user_objs[message['user']].id))
db.session.commit()

for dm in dms:
    db.session.add(DM(user_objs[dm['from_user']].id, user_objs[dm['to_user']].id, datetime.datetime.now(), dm['text']))
db.session.commit()

for follow in followers:
    db.session.add(Follower(user_objs[follow['name1']].id, user_objs[follow['name2']].id))
db.session.commit()

