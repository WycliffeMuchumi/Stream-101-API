from utils.validations import validate_users_key_pair_values
from flask import jsonify, request
from flask.helpers import make_response
from app.api.users import blueprint as users
from app.api.users.models.users import User, user_schema, users_schema
from utils.validations import validate_users_key_pair_values, error, check_for_blanks, check_for_non_strings
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
    if user:
        return user_schema.dump(user), 200
    else:
        make_response={
            "msg": "error, that user does not exist"
        }
        return jsonify(make_response), 404


"""
    Create a user
"""
@users.route('/signup', methods=['POST'])
def post():

    if validate_users_key_pair_values(request):
        return error(400, "{} key missing".format(', '.join(validate_users_key_pair_values(request))))

    data = request.get_json()

    if check_for_blanks(data):
        return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

    if check_for_non_strings(data):
        return error(400, "{} must be a string".format(', '.join(check_for_non_strings(data))))

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
            "msg": "error, that user already exists"
        }
        return jsonify(make_response), 409
    finally:
        db.session.close()


"""
    Edit a user
"""
@users.route('/edit_user/<int:id>', methods=['PUT'])
def edit_user(id):
    user = User.query.get(id)

    data = request.get_json()
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    userName = data.get('userName')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    password = data.get('password')

    user.firstName = firstName
    user.lastName = lastName
    user.userName = userName
    user.email = email
    user.phoneNumber = phoneNumber
    user.password = password

    try:
        db.session.commit()
        return user_schema.dump(user), 201
    except:
        db.session.rollback()
        make_response={
            "msg": "error, unable to update this user's record"
        }
        return jsonify(make_response), 400
    finally:
        db.session.close()


"""
    Delete a user
"""
@users.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    try:
        db.session.delete(user)
        make_response={
            "msg": "record deleted successfully"
        }
        return jsonify(make_response), 200
    except:
        db.session.rollback()
        make_response={
            "msg": "error, check your connection"
        }
        return jsonify(make_response), 502
    finally:
        db.session.close()

    
"""
    Searching a user by his/her username
"""
@users.route('/search/<string:userName>', methods=['GET'])
def search_user(userName):
    users = db.session.query(User).filter(User.userName.like(userName+'%'))
    return users_schema.jsonify(users), 200
   