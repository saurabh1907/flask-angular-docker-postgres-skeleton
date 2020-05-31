from flask_restful import Resource, reqparse, abort
from flask import request
from app.models.blog import Blog
from app.services.blog_service import BlogService

blog_service = BlogService()


def register_view(api):
    api.add_resource(BlogListApi, '/api/blogs')
    api.add_resource(BlogApi, '/api/blogs/<int:id>')


class BlogListApi(Resource):
    def get(self):
        return blog_service.all()

    def post(self):
        if not request.json or not 'title' in request.json:
            abort(400)
        title = request.json['title']
        desc = request.json['description']
        blog_service.save(Blog(title, desc))
        return self.success_response()

    def success_response(self):
        return {'status': 'success'}, 200


class BlogApi(Resource):

    def get(self, id):
        return blog_service.get(id)

    def put(self,id):
        if not request.json:
            abort(400)
        title = request.json['title'] if 'title' in request.json else None
        desc = request.json['description'] if 'description' in request.json else None
        return blog_service.update(id, title,desc)

    def delete(self, id):
        return blog_service.delete(id)

    # def __init__(self):
    # validation example
    # self.reqparse = reqparse.RequestParser()
    # self.reqparse.add_argument('title', type = str, location = 'json', required = True,
    #     help = 'No title provided')
    # self.reqparse.add_argument('description', type = str, location = 'json', required = True,
    #     help = 'No description provided')
    # self.reqparse.add_argument('blog_id', type = int, location = 'json')
