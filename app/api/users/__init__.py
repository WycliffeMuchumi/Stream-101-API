from  flask import Blueprint


"""
    Users Blueprint
"""
blueprint = Blueprint(
    'users_blueprint',
    __name__,
    url_prefix = '/users',
    template_folder='templates',
    static_folder='static'
)

from app.api.users.views import users