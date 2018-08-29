from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db' : db,
            'User' : User,
            'Post' : Post}

# Tell FLASK how to import it to run by
# setting the environment variable:
# export FLASK_APP=microblog.py
# Alternative, set it in .flaskenv
# then in terminal: flask run