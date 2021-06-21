from flask import jsonify, request
from flask.helpers import make_response
from flask_restful import Api, Resource
from app.api.users import blueprint
from app.api.users.models.users import User, user_schema, users_schema
from app import db

""" Pass Our Users Blueprint in Api module.
    Our Users Blueprint already has the app instance.
"""

api = Api(blueprint)

@blueprint.route('/gender', methods=['GET'])
def gender():
    gender = {
        1: "Male",
        2: "Female",
        3: "Transgender"
    }
    return jsonify(gender), 200

"""
    Users Resource
"""
class Users(Resource):
    # post method
    def post(self):
        data = request.get_json()
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        userName = data.get('userName')
        email = data.get('email')
        phoneNumber = data.get('phoneNumber')
        password = data.get('password')

        new_user = User(firstName=firstName, lastName=lastName, userName=userName,
                        email=email, phoneNumber = phoneNumber, password=password)
        db.session.add(new_user)
        try:
            db.session.commit()
            return user_schema.dump(new_user), 201
        except:
            db.session.rollback()
            return jsonify({"Message": "error, that user already exists"})
        finally:
            db.session.close()

    # get all users and get user by id method
    def get(self, id=None):
        if id is None:
            users = User.query.all()
            return users_schema.dump(users), 200
        else:
            user = User.query.get(id)
            return user_schema.dump(user), 200



api.add_resource(Users, '/', methods=['GET', 'POST'], endpoint='users_index')
api.add_resource(Users, '/<id>', methods=['GET', 'PUT', 'DELETE'], endpoint='user')