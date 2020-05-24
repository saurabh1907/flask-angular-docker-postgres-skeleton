from flask_restful import Resource
from flask import request

blogs = {}

def register_view(app, api):
    api.add_resource(Blog, '/test/<string:book_id>')
    api.add_resource(Todo3, '/hello', '/hello2')

class Blog(Resource):
    def get(self,book_id):
        return {book_id:blogs[book_id]}

    def put(self, book_id):
        blogs[book_id] = request.form['data']
        return {book_id: blogs[book_id]}

    def delete(self, book_id):
        del blogs[book_id]
        return '', 204

class Blogs(Resource):
    def get(self):
        return blogs



class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}