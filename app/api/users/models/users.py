from app import db, bcrypt, ma
from app.api.videos.models.videos import Video


"""
    Users Model
"""
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable = False)
    lastName = db.Column(db.String(100), nullable = False)
    userName = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(200),unique = True, nullable = False)
    phoneNumber = db.Column(db.String, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    video = db.relationship('Video', backref = 'author', lazy = True)

    def __init__(self, firstName, lastName, userName, email, 
    phoneNumber, password):
        self.firstName = firstName.title()
        self.lastName = lastName.title()
        self.userName = userName.title()
        self.email = email.lower()
        self.phoneNumber = phoneNumber
        self.set_password(password)

    """
        A method that harshes the users' passwords using bcrypt
    """
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    """
        A method that compares the harshed passwords in database 
        to the passwords provided by users during login.
    """
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
        

"""
    Using Marshmallow to serialize our users' schema
"""
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstName', 'lastName', 'userName', 'email', 'phoneNumber')

"""
    Initializing our users' schema
"""
# initializing schema when fetching a single user
user_schema = UserSchema()

# initializing schema when fetching many users
users_schema = UserSchema(many=True)
