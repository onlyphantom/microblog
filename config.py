import os

# /Users/Samuel/Dropbox/Projects/Python/Microblog
basedir = os.path.abspath(os.path.dirname(__file__))

# create the configuration class


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'you-will-never-guess'

    # sqlite:////Users/Samuel/Dropbox/Projects/Python/Microblog/app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['samuel@algorit.ma']

    # pagination configuration
    POSTS_PER_PAGE = 3
