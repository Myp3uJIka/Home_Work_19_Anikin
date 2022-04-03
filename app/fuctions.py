import jwt

from flask import request
from flask_restx.errors import abort

from app.constants import SECRET, ALGO

from app.implemented import user_service


# def check_auth(func):
#     def wrapper(*args, **kwargs):
#         if user_service.check_user(request.json):
#             return func(*args, **kwargs)
#         else:
#             return False
#     return wrapper()


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, SECRET, algorithms=ALGO)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            u_data = jwt.decode(token, SECRET, algorithms=ALGO)
            if u_data['role'] == 'admin':
                return func(*args, **kwargs)
            else:
                return {"error": "Недостаточно прав"}, 401
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
    return wrapper
