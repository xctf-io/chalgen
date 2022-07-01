import yaml
import datetime
import os

from forum.database import db
from forum.database import User, Post, Subforum, Comment

os.system("rm forum/database.db")

db.create_all()
db.session.commit()

with open('forum_contents.yaml') as f:
    data = yaml.safe_load(f)

users = data['users']
subforums = data['subforums']
posts = data['posts']

user_objs = {}
for user in users:
    user_obj = User(user['name'], user['name'] + "@a.com", "aaaaaa")
    db.session.add(user_obj)
    user_objs[user['name']] = user_obj
db.session.commit()

def add_subforum(title, description, parent=None):
    sub = Subforum(title, description)
    if parent:
        for subforum in parent.subforums:
            if subforum.title == title:
                return
        parent.subforums.append(sub)
    else:
        subforums = Subforum.query.filter(Subforum.parent_id == None).all()
        for subforum in subforums:
            if subforum.title == title:
                return
        db.session.add(sub)
    print("adding " + title)
    db.session.commit()
    return sub

subforum_objs = {}
for subforum in subforums:
    subforum_objs[subforum['name']] = add_subforum(subforum['name'], subforum['desc'])

for post in posts:
    user = user_objs[post['user']]
    subforum = subforum_objs[post['subforum']]
    post_obj = Post(post['title'], post['text'], datetime.datetime.now())

    user.posts.append(post_obj)
    subforum.posts.append(post_obj)

    db.session.commit()

    # Add comments
    if post['comments'] is None:
        post['comments'] = []

    for comment in post['comments']:
        comment_obj = Comment(comment['text'], datetime.datetime.now())

        user = user_objs[comment['user']]

        user.comments.append(comment_obj)
        post_obj.comments.append(comment_obj)

        db.session.commit()
