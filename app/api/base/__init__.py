from flask import Blueprint

"""
    Base Blueprint
"""
blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix = '/',
    template_folder='templates',
    static_folder='static'
)


from app.api.base.views import base