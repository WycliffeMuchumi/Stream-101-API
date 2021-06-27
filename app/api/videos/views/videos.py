from flask import jsonify, request
from flask.helpers import make_response
from app.api.videos import blueprint as videos
from app.api.videos.models.videos import Video, video_schema, videos_schema
from app import db

"""
    Get all videos
"""
@videos.route('/', methods = ['GET'])
def get():
    videos = Video.query.all()
    return videos_schema.jsonify(videos), 200

"""
    Get a single video
"""
@videos.route('/video/<int:id>', methods = ['GET'])
def get_video(id):
    video = Video.query.get(id)
    if video:
        return video_schema.dump(video), 200
    else:
        make_response={
            "msg": "error, that video does not exist"
        }
        return jsonify(make_response), 404

"""
    Post a video
"""
@videos.route('/post_video', methods = ['POST'])
def post():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    video_content = data.get('video_content')

    new_video = Video(title = title, description = description, video_content=video_content)
    db.session.add(new_video)
    try:
        db.session.commit()
        return video_schema.dump(new_video), 201
    except:
        db.session.rollback()
        make_response={
            "msg": "error, a video by that description already exists"
        }
        return jsonify(make_response), 409
    finally:
        db.session.close()

"""
    Edit a video
"""
@videos.route('/edit_video/<int:id>', methods=['PUT'])
def edit_video(id):
    video = Video.query.get(id)

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    video_content = data.get('video_content')

    video.title = title
    video.description = description
    video.video_content = video_content

    try:
        db.session.commit()
        return video_schema.dump(video), 201
    except:
        db.session.rollback()
        make_response={
            "msg": "error, unable to update this record"
        }
        return jsonify(make_response), 400
    finally:
        db.session.close()
