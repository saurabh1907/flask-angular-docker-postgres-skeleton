# from app import db
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#
#
#
# class Book(Base):
#   __tablename__ = 'book'
#
#   id = Column(Integer, primary_key=True)
#   title = Column(String(250), nullable=False)
#   author = Column(String(250), nullable=False)
#   genre = Column(String(250))
#
#   @property
#   def serialize(self):
#      return {
#         'title': self.title,
#         'author': self.author,
#         'genre': self.genre,
#         'id': self.id,
#      }