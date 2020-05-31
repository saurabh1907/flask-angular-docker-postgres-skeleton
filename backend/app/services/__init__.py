"""
BaseService - An abstract base class with abstract methods.
SQLAlchemyService - A SQLAlchemy service class that extends the BaseClass.
"""
from abc import ABCMeta, abstractmethod

from flask import jsonify


class BaseService(object):
    __model__ = None


    def _isinstance(self, obj, raise_error=True):
        rv = isinstance(obj, self.__model__)
        if not rv and raise_error:
            raise ValueError('%s is not of type %s' % (obj, self.__model__))
        return rv

    @abstractmethod
    def save(self, obj):
        """
            Commits the object to the database and returns the object.
        """

    @abstractmethod
    def all(self):
        """
            Returns a generator containing all instances of model.
        """

    @abstractmethod
    def get(self, obj):
        """
            Returns an instance of the service's model with the specified id.
        """

    @abstractmethod
    def get_all(self, *ids):
        """
            Returns a list of instances of the service's model with the
            specified ids.
            :param *ids: instance ids
        """


class SQLAlchemyService(BaseService):

    __db__ = None

    def save(self, obj):
        self._isinstance(obj)
        self.__db__.session.add(obj)
        self.__db__.session.commit()
        return obj

    def all(self):
        data = self.__model__.query.all()
        return self.return_response(data)

    def get(self, id):
        return self.__model__.query.get(id)

    def get_all(self, *ids):
        return self.__model__.query.filter(self.__model__.id.in_(ids)).all()

    def return_response(self, data):
        data_dict = [row.as_dict() for row in data]
        return jsonify(data_dict)