from flask import Flask
from flask_restful import Resource, Api
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(Config)

api = Api(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

CORS(app, origins='*')

from app import routes, models
from app import views

views.register_view(app, api)

