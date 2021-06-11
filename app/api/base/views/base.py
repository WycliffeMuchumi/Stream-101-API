from flask import jsonify, request
from flask.helpers import make_response
from flask_restful import Api, Resource
from app.api.base import blueprint

""" Pass Our Base Blueprint in Api module.
    Our Base Blueprint already has the app instance.
"""

api = Api(blueprint)

@blueprint.route('/', methods=['GET'])
def index():
    make_response = {
        "Message": "Hello There, Welcome to STREAM-101-API Home/Base page !",
        "Status": "Successful"
    }
    return jsonify(make_response), 200

"""
    Base Resource
"""
class Base(Resource):
    def get(self, id=None):
        return 'This is another route!'

    def post(self):
        pass



api.add_resource(Base, '/anotherroute')