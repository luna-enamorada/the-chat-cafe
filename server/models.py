from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from flask import abort 
from config import db, metadata


class User( db.Model, SerializerMixin):
    pass

class Forums(db.Model, SerializerMixin):
    __tablename__ = 'forums'

    #serialize_rules = (-'users.forum')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.Blob)
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

    def __repr__(self):
        return f'<Forums {self.id}: {self.title}>'

class Posts(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    #serialize_rules = (-'users.post')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    image = db.Column(db.Blob)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    forum_id = db.Column(db.Integer, db.ForeignKey('forums.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    comments = db.relationship('Comment', backref='post')
    forum = db.relationship('Forum', backref='posts')
    user = db.relationship('User', backref='posts')

    @validates('title')
    def validate_title(self, attr, title):
        if type(title) is str and title: 
            return title
        else: abort('Post titles must be longer than zero characters.')

    def __repr__(self):
        return f'<Posts {self.id}: {self.title}>'

class Comments(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship('User', backref='comments')
    post = db.relationship('Post', backref='comments')

    def __repr__(self):
        return f'<Comments {self.id} >'
# Models go here!
