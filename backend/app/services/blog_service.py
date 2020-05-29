from app.models.blog import Blog
from app.services import SQLAlchemyService


class BlogService(SQLAlchemyService):
    __model__ = Blog

    def __init__(self):
        # Creating a parent class ref to access parent class methods.
        self.parentClassRef = super(BlogService, self)