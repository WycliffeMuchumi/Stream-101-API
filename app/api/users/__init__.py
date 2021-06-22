from  flask import Blueprint


"""
    Users Blueprint
"""
blueprint = Blueprint(
    'users_blueprint',
    __name__,
    url_prefix = '/users'
)

from app.api.users.views import users