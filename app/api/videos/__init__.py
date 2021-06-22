from flask import Blueprint


"""
    Videos Blueprint
"""
blueprint = Blueprint(
    'videos_blueprint',
    __name__,
    url_prefix = '/videos'
)


from app.api.videos.views import videos