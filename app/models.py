from app import db

# inherits from db.Model class, a base class for all models
# from Flask-SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # __repr__ is a built-in function to compute the official 
    # string representation of an object
    def __repr__(self):
        return '<User {}>'.format(self.username)
    # in REPL: 
    # >>> from app.models import User
    # >>> u = User(username = 'susan', email='susan@example.com')
    # >>> u 
    # <User susan>

