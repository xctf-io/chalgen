import os

SITE_LOCKDOWN = True

SECRET_KEY = os.environ['SECRET_KEY']

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'database.db'
DATABASE_PATH = os.path.join(BASE_DIR, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

SITE_NAME = "Forknite Forums"
SITE_DESCRIPTION = "Discuss the latest and greatest of Forknite!"
