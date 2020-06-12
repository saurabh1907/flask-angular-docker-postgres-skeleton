from flask import jsonify
import json


class SQLAlchemyService:

    def __init__(self, db, model):
        self.db = db
        self.model = model

    # Optional: validation before insert in db
    #     def _isinstance(self, obj, raise_error=True):
    #         rv = isinstance(obj, self.__model__)
    #         if not rv and raise_error:
    #             raise ValueError('%s is not of type %s' % (obj, self.__model__))
    #         return rv

    def all(self):
        data = self.model.query.all()
        data_dict = [row.as_dict() for row in data]
        return jsonify(data_dict)

    def get(self, id):
        data = self.model.query.get(id)
        return jsonify(data.as_dict())

    def get_all(self, *ids):
        return self.model.query.filter(self.model.id.in_(ids)).all()

    def save(self, obj):
        # self._isinstance(obj) # validation
        self.db.session.add(obj)
        self.db.session.commit()
        return 1

    def delete(self, id):
        to_delete = self.model.query.get(id)
        self.db.session.delete(to_delete)
        self.db.session.commit()
        return jsonify(to_delete.as_dict())
