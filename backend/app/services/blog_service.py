from app.models.blog import Blog
from app.services.sql_alchemy_service import SQLAlchemyService
from app import db
from flask import jsonify


class BlogService(SQLAlchemyService):
    model = Blog
    db = db

    def __init__(self):
        SQLAlchemyService.__init__(self, self.db, self.model)

    def update(self, id, title, desc):
        to_update = self.__model__.query.get(id)
        if title:
            to_update.title = title
        if desc:
            to_update.description = desc
        self.__db__.session.commit()
        return jsonify(to_update.as_dict())
