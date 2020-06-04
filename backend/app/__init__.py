from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from setting import config

app_setting = config["development"]

db = SQLAlchemy()
migrate = Migrate()
api = Api()


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_setting)

    CORS(app, origins='*')

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # from app.models.blog import Blog
    # # Init tables. Need the next two lines one time only. Run app after uncommenting once. Or use flask db init
    # # db.create_all()
    # # db.session.commit()
    with app.app_context():
        from app.views import views
        views.register_view(api)

        # Register the blueprints here

    return app


