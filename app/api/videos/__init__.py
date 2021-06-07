from flask import Blueprint


"""
    Videos Blueprint
"""
blueprint = Blueprint(
    'videos_blueprint',
    __name__,
    url_prefix = '/videos',
    template_folder='templates',
    static_folder='static'
)

from app.api.videos.views import videos