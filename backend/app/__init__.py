"""
    Main application
"""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from setting import config

app = Flask(__name__)

app_setting = config["development"]
app.config.from_object(app_setting)

api = Api(app)

CORS(app, origins='*')

from app import models
db = SQLAlchemy(app)

# Init tables. Need the next three lines one time only.
from app.models.blog import Blog
db.create_all()
db.session.commit()

migrate = Migrate(app, db)

from app.views import views, default

views.register_view(api)



