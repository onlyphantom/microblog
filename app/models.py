from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

# inherits from db.Model class, a base class for all models
# from Flask-SQLAlchemy

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # a relationship; posts is not an actual column in the table
    # allow us to do things like:
    # posts = Post.query.all()
    # for p in posts:
    #   print(p.id, p.author.username, p.author.email, p.body)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # __repr__ is a built-in function to compute the official
    # string representation of an object
    def __repr__(self):
        return '<User {}>'.format(self.username)
    # in REPL:
    # >>> from app.models import User
    # >>> u = User(username = 'susan', email='susan@example.com')
    # >>> u
    # <User susan>
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size
        )

class Post(db.Model):
    """Model for posts.
    :param db.Model: Create Posts
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # datetime.utcnow() returns: 2018-08-26 08:29:16.511177
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
