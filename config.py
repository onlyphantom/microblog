import os

# /Users/Samuel/Dropbox/Projects/Python/Microblog
basedir = os.path.abspath(os.path.dirname(__file__))

# create the configuration class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
    'you-will-never-guess'

    #sqlite:////Users/Samuel/Dropbox/Projects/Python/Microblog/app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
