import jwt
from flask_restx.errors import abort

from app.implemented import user_service
from app.constants import SECRET, ALGO


class AuthService:
    def __init__(self):
        pass

    def take_tokens_from_udata(self, data):
        if user_service.check_user(data):
            return {
                'access_token': user_service.create_atoken(data),
                'refresh_token': user_service.create_rtoken(),
            }

    def take_tokens_from_rtoken(self, data):
        if data['refresh_token']:
            try:
                user_data = jwt.decode(data['refresh_token'], SECRET, algorithms=ALGO)
                return {
                    'access_token': user_service.create_atoken(data),
                    'refresh_token': user_service.create_rtoken(),
                }
            except Exception as e:
                abort(400)
