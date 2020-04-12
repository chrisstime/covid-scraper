import os
import traceback
from flask import Flask
from .index import INDEX_BLUEPRINT

APP = Flask(__name__)
APP.register_blueprint(INDEX_BLUEPRINT)