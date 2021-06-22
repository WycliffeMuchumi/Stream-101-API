from flask import jsonify, request
from flask.helpers import make_response
from app.api.users import blueprint as users
from app.api.users.models.users import User, user_schema, users_schema
from app import db

"""
    Get all users
"""
@users.route('/', methods=['GET'])
def get():
    users = User.query.all()
    return users_schema.jsonify(users), 200
        
"""
    Get a single user by id
"""
@users.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.dump(user), 200  
        
"""
    Create a user
"""
@users.route('/signup', methods=['POST'])
def post():
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
        make_response = {
            "Message": "error, that user already exists"
        }
        return jsonify(make_response), 409
    finally:
        db.session.close()

"""
    Searching a user by his/her username
"""
@users.route('/search/<string:userName>', methods=['GET'])
def search_user(userName):
    try:
        users = db.session.query(User).filter(User.userName.like(userName+'%'))
        return users_schema.jsonify(users), 200
    except:
        make_response={
            "msg": "A user by that username does not exist"
        }
        return jsonify(make_response), 404