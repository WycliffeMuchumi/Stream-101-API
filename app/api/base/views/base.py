from flask import jsonify, make_response, request
from app.api.base import blueprint as home


@home.route('/', methods=['GET'])
def index():
    make_response = {
        "Message": "Hello There, Welcome to STREAM-101-API Home/Base page !",
        "Status": "Successful"
    }
    return jsonify(make_response), 200





