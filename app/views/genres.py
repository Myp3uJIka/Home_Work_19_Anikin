from flask.globals import request
from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return '', 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        req_json = request.json
        req_json['id'] = rid
        genre_service.update(req_json)
        return '', 201

    def delete(self, rid):
        genre_service.delete(rid)
        return '', 204
