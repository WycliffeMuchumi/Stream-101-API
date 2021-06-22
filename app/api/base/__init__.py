from flask import Blueprint

"""
    Base Blueprint
"""
blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix = '/'
)


from app.api.base.views import base