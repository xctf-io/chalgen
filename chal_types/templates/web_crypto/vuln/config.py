import os
##### SERVER SETTINGS #####
SECRET_KEY = os.urandom(64)
DB_USERNAME = "root"
DB_PASSWORD = "toor"
CHALLENGE_NAME = "crypto"
PORT = 1337
SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@localhost:{port}/{chal}_vuln'.format(
            user=DB_USERNAME,
            password=DB_PASSWORD,
            port=PORT,
            chal=CHALLENGE_NAME
        )
SESSION_TYPE = "filesystem"
SESSION_FILE_DIR = "/tmp/flask_session"
SESSION_COOKIE_HTTPONLY = True
PERMANENT_SESSION_LIFETIME = 604800 # 7 days in seconds
#HOST = ".ctfd.io"
UPLOAD_FOLDER = os.path.normpath('/tmp/uploads')
