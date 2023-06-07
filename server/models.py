from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from flask import abort 
from config import db, metadata

import re, imghdr

class User( db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    _password = db.Column(db.String)
    avatar = db.Column(db.LargeBinary)
    bio = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # forums = db.relationship('Forum', backref='user')
    forums = association_proxy( 'users', 'forum')
    posts = db.relationship('Post', backref='user')
    comments = db.relationship('Comment', backref='user')

    @classmethod
    def find ( cls, id ) :
        user = User.query.filter( User.id == id ).first()
        return user
    
    validation_errors = []

    @classmethod 
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @classmethod
    def return_validation_errors(cls):
        error = [ *cls.validation_errors ]
        error_list = list( set(error) )
        return error_list
    
    @validates('username')
    def validate_username(self, attr, username):
        un = User.query.filter(User.username.like(f'%{username}%')).first()
        if type(username) is str and username and un == None and len(username) in range(5, 16) and re.match(r'^[A-Za-z0-9_]+$', username):
            return username

        else: self.validation_errors.append( 'Username must be unique string between 5 - 15 characters and not contain any special characters.')

    @validates('email')
    def validate_email(self, attr, email):
        em = User.query.filter(User.email.like(f'%{email}%')).first()
        if type(email) is str and email and em == None and "@" and ".com" in email:
            return email
        else: self.validation_errors.append( 'Must be a valid email or email has already been registered.')

    @validates('avatar')
    def validate_avatar( self, attr, avatar ):
        if avatar is not None:
            file_format = imghdr.what(None, h= avatar)
            if file_format != 'jpeg':
                self.validation_errors.append("Only JPEG images are permitted.")
        return avatar.filename

    @validates( 'password' )
    def validate_password( self, attr, password ):
        if type(password) is str and len(password) in range(4, 16):
            return "Password has been set."
        else:
            self.validation_errors.append( "Password must be a string between 4 - 15 characters. ")

    def user_dict ( self ) :
        return {
            'username': self.username,
            'email': self.email,
            '_password': self._password,
            'bio': self.bio
        }

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

class Forum(db.Model, SerializerMixin):
    __tablename__ = 'forums'

    #serialize_rules = (-'users.forum')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.LargeBinary)
    # favorited_forums = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    posts = db.relationship('Post', backref='forum')
    users = association_proxy('forums', 'users')

    @classmethod
    def find ( cls, id ) :
        forum = Forum.query.filter( Forum.id == id ).first()
        return forum

    validation_errors = []

    @classmethod 
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @classmethod
    def return_validation_errors(cls):
        error = [ *cls.validation_errors ]
        error_list = list( set(error) )
        return error_list

    @validates('title')
    def validate_title(self, attr, title):
        if type(title) is str and title:
            return title
        else: self.validation_errors.append( 'Forum title must be longer than zero characters.')

    @validates('image')
    def validate_avatar( self, attr, image ):
        if image is not None:
            file_format = imghdr.what(None, h= image)
            if file_format != 'jpeg':
                self.validation_errors.append("Only JPEG images are permitted.")
        return image.filename

    def forum_dict ( self ) :
        return {
            'title': self.title,
            'description': self.description,
        }

    def __repr__(self):
        return f'<Forum {self.id}: {self.title}>'

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    #serialize_rules = (-'users.post')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    image = db.Column(db.LargeBinary)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    forum_id = db.Column(db.Integer, db.ForeignKey('forums.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    comments = db.relationship('Comment', backref='post')

    @classmethod
    def find ( cls, id ) :
        forum = Post.query.filter( Post.id == id ).first()
        return forum

    validation_errors = []

    @classmethod 
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @classmethod
    def return_validation_errors(cls):
        error = [ *cls.validation_errors ]
        error_list = list( set(error) )
        return error_list

    @validates('title')
    def validate_title(self, attr, title):
        if type(title) is str and title: 
            return title
        else: self.validation_errors.append('Post titles must be longer than zero characters.')

    @validates('image')
    def validate_avatar( self, attr, image ):
        if image is not None:
            file_format = imghdr.what(None, h= image)
            if file_format != 'jpeg':
                self.validation_errors.append("Only JPEG images are permitted.")
        return image.filename

    @validates( 'user_id')
    def validate_user( self, attr, user_id ):
        user = User.find( user_id )        
        if user:
            return user_id
        else: self.validation_errors.append( "Post not found. ")

    @validates( 'forum_id')
    def validate_user( self, attr, forum_id ):
        forum = Forum.find( forum_id )        
        if forum:
            return forum_id
        else: self.validation_errors.append( "Forum not found. ")

    def post_dict ( self ) :
        return {
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'forum_id': self.forum_id,
        }


    def __repr__(self):
        return f'<Post {self.id}: {self.title}>'

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    validation_errors = []

    @classmethod 
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @classmethod
    def return_validation_errors(cls):
        error = [ *cls.validation_errors ]
        error_list = list( set(error) )
        return error_list

    @validates( 'user_id')
    def validate_user( self, attr, user_id ):
        user = User.find( user_id )        
        if user:
            return user_id
        else: self.validation_errors.append( "Post not found. ")

    @validates( 'forum_id')
    def validate_user( self, attr, forum_id ):
        forum = Forum.find( forum_id )        
        if forum:
            return forum_id
        else: self.validation_errors.append( "Forum not found. ")

    def comment_dict ( self ) :
        return {
            'content': self.content,
            'user_id': self.user_id,
            'post_id': self.post_id
        }


    def __repr__(self):
        return f'<Comment {self.id} >'
# Models go here!
