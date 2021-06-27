from datetime import datetime
from app import db, ma


"""
    Videos model
"""
class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(500), unique=True, nullable = False)
    video_content = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    

    def __init__(self, title, description, video_content):
        self.title = title.title()
        self.description = description
        self.video_content = video_content
      
        

"""
    Using Marshmallow to serialize our videos' schema
"""
class VideoSchema(ma.Schema):
    class Meta:
        fields=('id','title','description','video_content') 


"""
    Initializing our videos' schema
"""
# initializing schema when fetching a single video
video_schema = VideoSchema()

# initializing schema when fetching many videos
videos_schema = VideoSchema(many=True)