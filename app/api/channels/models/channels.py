from app import db, bcrypt, ma

"""
    Channels Model
"""
class Channels(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key = True)
    channel_username = db.Column(db.Integer, unique = True, nullable = False)
    channel_biography = db.Column(db.Integer, nullable = False)
    my_videos = db.relationship('Video', backref = 'author', lazy = True)
    
