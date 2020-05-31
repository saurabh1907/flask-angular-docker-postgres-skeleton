"""
    Main application
"""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
# from server.settings import config
# instantiate the db
from setting import config

app = Flask(__name__)

app_settings = config["development"]
app.config.from_object(app_settings)

api = Api(app)

db = SQLAlchemy(app)


migrate = Migrate(app, db)

CORS(app, origins='*')

from app import models
from app.views import views, default

views.register_view(app, api)

