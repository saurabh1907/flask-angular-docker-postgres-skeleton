from flask_restful import Resource, reqparse
from flask import jsonify
import json
from flask import request

from app.models.blog import Blog
from app.services.blog_service import BlogService

blogs = []
blog1 = Blog("title 1", "desc1")
blog2 = Blog("title 2", "desc2 from backend")
blogs.insert(1,blog1)
blogs.insert(2,blog2)
# blogs[2] = blog2

blog_service = BlogService()
def register_view(app, api):
    # views.add_resource(BlogService, '/blogs/<string:book_id>')
    api.add_resource(BlogListApi, '/api/blogs')
    api.add_resource(BlogApi, '/api/blogs/<int:id>')

class BlogListApi(Resource):
    def get(self):
        # return blogs
        return blog_service.all()

    def post(self):
        # return blogs
        # print(request)
        # title = request.form['title']
        # desc = request.form['description']
        blog_service.save(Blog("title", "desc"))
        return "done"

    # def post(self, book_id):
    #     blogs[book_id] = request.form['data']
    #     return {book_id: blogs[book_id]}


class BlogApi(Resource):
    def __init__(self):
        # self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('title', type = str, location = 'json', required = True,
        #     help = 'No title provided')
        # self.reqparse.add_argument('description', type = str, location = 'json', required = True,
        #     help = 'No description provided')
        # self.reqparse.add_argument('blod_id', type = int, location = 'json')
        super(BlogApi, self).__init__()

    def get(self, id):
        # Set the response code to 201 and return custom headers
        # return blogs[id]
        return blog_service.get(id)

    # def put(self, book_id):
    #     task = filter(lambda t: t['id'] == id, tasks)
    #     if len(task) == 0:
    #         abort(404)
    #     task = task[0]
    #     args = self.reqparse.parse_args()
    #     for k, v in args.iteritems():
    #         if v != None:
    #             task[k] = v
    #     return jsonify({'task': make_public_task(task)})

    def delete(self, book_id):
        del blogs[book_id]
        return '', 204