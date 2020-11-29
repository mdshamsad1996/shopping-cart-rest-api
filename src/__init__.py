"""
Contained the common setting and obj which is used by most of other module
"""
import flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True

from src import routes
