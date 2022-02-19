from flask import jsonify, make_response, request
from app.api.admin import blueprint as admin


@admin.route('/dashboard', methods=['GET'])
def admin():
    make_response = {
        "Message": "Hello There, Welcome to STREAM-101-API admin page !",
        "Status": "Successful"
    }
    return jsonify(make_response), 200

