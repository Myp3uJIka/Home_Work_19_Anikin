import calendar
import datetime
import hashlib

import jwt
from flask_restx.errors import abort

from app.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT, SECRET, ALGO
from app.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, name):
        return self.dao.get_one(name)

    def save_data(self, user):
        return self.dao.save_data(user)

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode('utf8', 'ignore')

    def check_user(self, data):
        if 'username' not in data or 'password' not in data:
            abort(400)
        user = UserDAO.get_one(data['username'])
        if user.password == data['password']:
            return True
        else:
            return False

    def create_atoken(self, data):
        data['role'] = data.get('role', 'user')
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        return access_token

    def create_rtoken(self, data):
        data['role'] = data.get('role', 'user')
        days30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data['exp'] = calendar.timegm(days30.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)
        return refresh_token
