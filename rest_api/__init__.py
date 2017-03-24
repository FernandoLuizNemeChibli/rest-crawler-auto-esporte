from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import base_dir

flask_application = Flask(__name__)
flask_application.config.from_object('config')
db = SQLAlchemy(flask_application)

from rest_api import url_access
