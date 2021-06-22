from flask import Blueprint

"""
    Channels Blueprint
"""
blueprint = Blueprint(
    'channels_blueprint',
    __name__,
    url_prefix = '/channels'
)


from app.api.channels.views import channels