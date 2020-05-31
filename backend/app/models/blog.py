from app import db
from app.models.base import BaseModel
from sqlalchemy.sql import func
import json


class Blog(BaseModel, db.Model, dict):
    """Model for blogs table"""
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=func.now())

    #     password_hash = db.Column(db.String(128)

    def __init__(self, title, description):
        super().__init__()
        self.title = title
        self.description = description
        dict.__init__(self, title=self.title, description=self.description, blog_id=self.id)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


db.create_all()
db.session.commit()