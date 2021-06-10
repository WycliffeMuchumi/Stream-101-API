from flask import Blueprint

"""
    Channels Blueprint
"""
blueprint = Blueprint(
    'channels_blueprint',
    __name__,
    url_prefix = '/channels',
    template_folder='templates',
    static_folder='static'
)


from app.api.channels.views import channels