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

    forums = db.relationship('Forum', backref='user')
    posts = db.relationship('Post', backref='user')
    comments = db.relationship('Comment', backref='user')

    @validates('username')
    def validate_username(self, attr, username):
        un = User.query.filter(User.username.like(f'%{username}%')).first()
        if type(username) is str and username and un == None and len(username) in range(5, 16) and re.match(r'^[A-Za-z0-9_]+$', username):
            return username

        else: abort(422, 'Username must be unique string between 5 - 15 characters and not contain any special characters.')

    @validates('email')
    def validate_email(self, attr, email):
        em = User.query.filter(User.email.like(f'%{email}%')).first()
        if type(email) is str and email and em == None and "@" and ".com" not in email:
            return email
        else: abort(422, 'Must be a  valid email or email has already been registered.')

    @validates('avatar')
    def validate_avatar( self, attr, avatar ):
        if avatar is not None:
            file_format = imghdr.what(None, h= avatar)
            if file_format != 'jpeg':
                abort ("Only JPEG images are permitted.")
        return avatar.filename

    @validates( 'password' )
    def validate_password( self, attr, password ):
        if type(password) is str and len(password) in range(4, 16):
            return "Password has been set."
        else:
            abort( "Password must be a string between 4 - 15 characters. ")

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

class Forum(db.Model, SerializerMixin):
    __tablename__ = 'forums'

    #serialize_rules = (-'users.forum')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.LargeBinary)
    favorited_forums = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    posts = db.relationship('Post', backref='forum')
    users = association_proxy('posts', 'users')

    @validates('title')
    def validate_title(self, attr, title):
        if type(title) is str and title:
            return title
        else: abort(422, 'Forum title must be longer than zero characters.')

    @validates('image')
    def validate_avatar( self, attr, image ):
        if image is not None:
            file_format = imghdr.what(None, h= image)
            if file_format != 'jpeg':
                abort ("Only JPEG images are permitted.")
        return image.filename


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

    @validates('title')
    def validate_title(self, attr, title):
        if type(title) is str and title: 
            return title
        else: abort('Post titles must be longer than zero characters.')

    @validates('image')
    def validate_avatar( self, attr, image ):
        if image is not None:
            file_format = imghdr.what(None, h= image)
            if file_format != 'jpeg':
                abort ("Only JPEG images are permitted.")
        return image.filename


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

    def __repr__(self):
        return f'<Comment {self.id} >'
# Models go here!
