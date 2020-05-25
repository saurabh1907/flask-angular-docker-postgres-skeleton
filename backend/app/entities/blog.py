import json
class Blog(dict):
    def __init__(self, title, description, blog_id):
        self.title = title
        self.description = description
        self.blog_id = blog_id
        dict.__init__(self, title=title, description=description, blog_id=blog_id)


    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)