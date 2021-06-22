from flask import jsonify, request
from flask.helpers import make_response
from app.api.base import blueprint as home


@home.route('/', methods=['GET'])
def index():
    make_response = {
        "Message": "Hello There, Welcome to STREAM-101-API Home/Base page !",
        "Status": "Successful"
    }
    return jsonify(make_response), 200





