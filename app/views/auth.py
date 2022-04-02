from flask.globals import request
from flask_restx.namespace import Namespace
from flask_restx.resource import Resource

from app.implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        return auth_service.take_tokens_from_udata(req_json)

    def put(self):
        req_json = request.json
        return auth_service.take_tokens_from_rtoken(req_json)


