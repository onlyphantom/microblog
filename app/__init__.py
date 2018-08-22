from flask import Flask

# Creates the application object as an instance of class Flask
app = Flask(__name__)

# Import at the bottom to workaround circular imports; 
# Routes module needs to import the app variable defined in 
# this script, so putting the reciprocal imports at the
# bottom avoids the error from mutual references between
# these two files
from app import routes