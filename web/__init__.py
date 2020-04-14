import os
import traceback
from flask import Flask
from .index import INDEX_BLUEPRINT, ABOUT_BLUEPRINT

APP = Flask(__name__)
APP.register_blueprint(INDEX_BLUEPRINT)
APP.register_blueprint(ABOUT_BLUEPRINT)