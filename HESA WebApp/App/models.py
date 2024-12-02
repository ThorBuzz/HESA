from . import db,loginManager
from datetime import datetime
from flask_login import UserMixin

@loginManager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


# MODELS IF NO DATABASE
class User(db.Model,UserMixin):
   id=db.Column(db.Integer, primary_key=True, nullable=False)
   username=db.Column(db.String(20),unique=True, nullable=False)
   email=db.Column(db.String(100),unique=True, nullable=False)
   password=db.Column(db.String(60), nullable=False)
   profilePic=db.Column(db.String(20),nullable=False,default='default.jpg')
   post=db.relationship('Post', backref='author', lazy=True)
   comment=db.relationship('Comment', backref='author', lazy=True)
   like=db.relationship('Like', backref='liker', lazy=True)
   
   def __repr__(self) -> str:
      return f'User:\nUsername- {self.username}\n'\
               f'Email - {self.email}\n'\
               f'Profile Pic - {self.profilePic}'
               
# MODELS IF DATABASE
class User(db.Model,UserMixin):
   id=db.Column(db.Integer, primary_key=True, nullable=False)
   username=db.Column(db.String(20),unique=True, nullable=False)
   email=db.Column(db.String(100),unique=True, nullable=False)
   password=db.Column(db.String(60), nullable=False)
   profilePic=db.Column(db.String(20),nullable=False,default='default.jpg')
   post=db.relationship('Post', backref='author', lazy=True)
   comment=db.relationship('Comment', backref='author', lazy=True)
   like=db.relationship('Like', backref='liker', lazy=True)
   
   def __repr__(self) -> str:
      return f'User:\nUsername- {self.username}\n'\
               f'Email - {self.email}\n'\
               f'Profile Pic - {self.profilePic}'

class Department(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), nullable=False)
   courses = db.relationship('Course', backref='department', lazy=True)

class Course(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
   description = db.Column(db.Text, nullable=True)
   
class Update(db.Model, UserMixin):
   id=db.Column(db.Integer, primary_key=True, nullable=False)
   title=db.Column(db.String(100), nullable=False)
   date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   content=db.Column(db.Text ,nullable=False)
   author_id=db.Column(db.Integer(),db.ForeignKey('user.id'), nullable=False)
   comment=db.relationship('Comment', backref='update', lazy=True)
   like=db.relationship('Like', backref='update', lazy=True)
   # self representation
   def __repr__(self) -> str:
      return f'Update:\nTitle- {self.title }\n'\
               f'Admin - {self.author.username}\n'\
               f'Date - {self.date}\n'\

class Comment(db.Model, UserMixin):
   id=db.Column(db.Integer, primary_key=True, nullable=False)
   content=db.Column(db.Text ,nullable=False)
   date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   post_id=db.Column(db.Integer(),db.ForeignKey('post.id'), nullable=False)
   author_id=db.Column(db.Integer(),db.ForeignKey('user.id'), nullable=False)
   # self representation
   def __repr__(self) -> str:
      return f'Update:\nContent - {self.content }\n'\
               f'Author - {self.author.username}\n'\
               f'Date - {self.date}\n'\


class Like(db.Model, UserMixin):
   id=db.Column(db.Integer, primary_key=True, nullable=False)
   post_id=db.Column(db.Integer(),db.ForeignKey('post.id'), nullable=False)
   author_id=db.Column(db.Integer(),db.ForeignKey('user.id'), nullable=False)
   # self representation
   def __repr__(self) -> str:
      return f'Like:'\
               f'By - {self.liker.username}\n'\
               f'For - {self.post.title}\n'\


