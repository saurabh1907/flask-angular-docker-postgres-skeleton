from app.models.blog import Blog
from app.services.sql_alchemy_service import SQLAlchemyService
from app import db
from flask import jsonify


class BlogService(SQLAlchemyService):
    __model__ = Blog
    __db__ = db

    def update(self, id, title, desc):
        to_update = self.__model__.query.get(id)
        if title:
            to_update.title = title
        if desc:
            to_update.description = desc
        self.__db__.session.commit()
        return jsonify(to_update.as_dict())
