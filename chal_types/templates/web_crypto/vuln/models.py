from passlib.hash import bcrypt_sha256

import datetime
import hashlib

def sha512(string):
    return hashlib.sha512(string).hexdigest()
