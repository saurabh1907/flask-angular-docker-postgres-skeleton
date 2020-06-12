from flask_restful import Resource, abort
from flask import request
from app.models.blog import Blog
from app.services.blog_service import BlogService

blog_service = BlogService()


def register_view(api):
    api.add_resource(BlogListApi, '/api/blogs')
    api.add_resource(BlogApi, '/api/blogs/<int:id>')


def success_response():
    return {'status': 'success'}, 200


class BlogListApi(Resource):
    def get(self):
        return blog_service.all()

    def post(self):
        if not request.json or not 'title' in request.json:
            abort(400)
        title = request.json['title']
        desc = request.json['description']
        blog_service.save(Blog(title, desc))
        return success_response()


class BlogApi(Resource):
    def get(self, id):
        return blog_service.get(id)

    def put(self, id):
        if not request.json:
            abort(400)
        title = request.json['title'] if 'title' in request.json else None
        desc = request.json['description'] if 'description' in request.json else None
        return blog_service.update(id, title, desc)

    def delete(self, id):
        return blog_service.delete(id)
