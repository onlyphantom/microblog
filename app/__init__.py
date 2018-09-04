from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Creates the application object as an instance of class Flask
app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# let Flask-Login know which page (function name) handles login
login.login_view = 'login'

# Import at the bottom to workaround circular imports;
# Routes module needs to import the app variable defined in
# this script, so putting the reciprocal imports at the
# bottom avoids the error from mutual references between
# these two files
from app import routes, models, errors
