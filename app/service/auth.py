import jwt
from flask_restx.errors import abort


from app.constants import SECRET, ALGO
from app.service.user import UserService


class AuthService:
    def __init__(self, user: UserService):
        self.user = user

    def take_tokens_from_udata(self, data):
        return {
            'access_token': self.user.create_atoken(data),
            'refresh_token': self.user.create_rtoken(data),
        }

    def take_tokens_from_rtoken(self, data):
        if data['refresh_token']:
            try:
                user_data = jwt.decode(data['refresh_token'], SECRET, algorithms=ALGO)
                return {
                    'access_token': self.user.create_atoken(user_data),
                    'refresh_token': self.user.create_rtoken(user_data),
                }
            except Exception as e:
                abort(401)
        else:
            abort(401)
