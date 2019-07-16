from flask_restplus import Resource, Api
from tim.web.controllers import api

@api.route('/hello','/hiroy')
class Hello(Resource):
    def get(self):
        return { 'hello': 'World' }