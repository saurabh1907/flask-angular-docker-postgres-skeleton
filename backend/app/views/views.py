from flask_restful import Resource, reqparse, abort
from flask import request
from app.models.blog import Blog
from app.services.blog_service import BlogService

blog_service = BlogService()

def register_view(api):
    api.add_resource(BlogListApi, '/api/blogs')
    api.add_resource(BlogApi, '/api/blogs/<int:id>')
    api.add_resource(BlogsDownload, '/api/blogs/download')


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

    # def __init__(self):
    # validation example
    # self.reqparse = reqparse.RequestParser()
    # self.reqparse.add_argument('title', type = str, location = 'json', required = True,
    #     help = 'No title provided')
    # self.reqparse.add_argument('description', type = str, location = 'json', required = True,
    #     help = 'No description provided')
    # self.reqparse.add_argument('blog_id', type = int, location = 'json')


class BlogsDownload(Resource):
    from app.celery import add_dummy_blogs
    def get(self):
        # self.add_dummy_blogs.apply_async(args=[5, 10], countdown=10)
        self.add_dummy_blogs.delay(5,10)
        return success_response()

# Routes approach to create api
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Saurabh'}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts)
