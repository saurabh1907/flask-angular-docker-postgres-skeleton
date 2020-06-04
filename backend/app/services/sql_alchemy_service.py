from flask import jsonify
import json


class SQLAlchemyService:
    __db__ = None
    __model__ = None

    #     def _isinstance(self, obj, raise_error=True):
    #         rv = isinstance(obj, self.__model__)
    #         if not rv and raise_error:
    #             raise ValueError('%s is not of type %s' % (obj, self.__model__))
    #         return rv
    def all(self):
        data = self.__model__.query.all()
        data_dict = [row.as_dict() for row in data]
        return jsonify(data_dict)

    def get(self, id):
        data = self.__model__.query.get(id)
        return jsonify(data.as_dict())

    def get_all(self, *ids):
        return self.__model__.query.filter(self.__model__.id.in_(ids)).all()

    def save(self, obj):
        # self._isinstance(obj)
        self.__db__.session.add(obj)
        self.__db__.session.commit()
        # return jsonify(obj.as_dict())
        return 1

    def delete(self, id):
        to_delete = self.__model__.query.get(id)
        self.__db__.session.delete(to_delete)
        self.__db__.session.commit()
        return jsonify(to_delete.as_dict())


