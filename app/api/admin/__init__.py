from flask import Blueprint

"""
    Admin Blueprint
"""

blueprint = Blueprint(
    'admin_blueprint',
    __name__,
    url_prefix = '/admin',
    template_folder='templates',
    static_folder='static'
)