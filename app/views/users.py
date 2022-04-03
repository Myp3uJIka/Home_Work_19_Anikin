from flask.globals import request
from flask_restx.namespace import Namespace
from flask_restx.resource import Resource

from app.dao.model.user import UserSchema
from app.fuctions import admin_required
from app.implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UserViews(Resource):
    @admin_required
    def get(self):
        return UserSchema(many=True).dump(user_service.get_all()), 200

    @admin_required
    def post(self):
        req_json = request.json
        if 'username' not in req_json:
            return {"error": 'Необходимо указать username'}, 400
        if 'password' not in req_json:
            return {"error": 'Необходимо указать password'}, 400
        if 'role' not in req_json:
            req_json['role'] = 'user'
            print(req_json)
        return user_service.create(req_json), 201
