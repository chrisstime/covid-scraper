import os
import traceback
from flask import Flask
from .index import INDEX_BLUEPRINT
from .about import ABOUT_BLUEPRINT
from .world_cases import WORLDWIDE_BLUEPRINT
from .australia_cases import AUSTRALIA_BLUEPRINT
from db import db

APP = Flask(__name__)
db.init_app(APP)
APP.register_blueprint(INDEX_BLUEPRINT)
APP.register_blueprint(ABOUT_BLUEPRINT)
APP.register_blueprint(WORLDWIDE_BLUEPRINT)
APP.register_blueprint(AUSTRALIA_BLUEPRINT)