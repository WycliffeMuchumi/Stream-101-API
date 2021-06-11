from flask import jsonify, request
from flask.helpers import make_response
from flask_restful import Api, Resource
from app.api.admin import blueprint

""" Pass Our Admin Blueprint in Api module.
    Our Admin Blueprint already has the app instance.
"""

api = Api(blueprint)

@blueprint.route('/', methods=['GET'])
def index():
    make_response = {
        "Message": "Hello There, Welcome to STREAM-101-API admin page !",
        "Status": "Successful"
    }
    return jsonify(make_response), 200

"""
    Admin Resource
"""
class Admin(Resource):
    def get(self, id=None):
        return 'This is another route!'

    def post(self):
        pass



api.add_resource(Admin, '/anotherroute')