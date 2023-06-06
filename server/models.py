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

    created_at = db.Column( db.DateTime, server_default=db.func.now() )
    updated_at = db.Column( db.DateTime, onupdate=db.func.now() )

    posts = db.relationship( 'Forum', backref = 'user' )
    # forum = association_proxy( 'posts', 'forum' )


    @validates('username')
    def validate_username( self, attr, username ):
        if type(username) is str and len(username) in range(5, 16) and re.match(r'^[A-Za-z0-9_]+$', username):
            return username 
        else:
            abort( "Username must be a string between 5 - 15 characters and not contain any special characters. ")

    @validates('email')
    def validate_email( self, attr, email ):
        if "@" and ".com" not in email:
            abort( "Must be a valid email address.")
        return email
    
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
    
class Post( db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    image = db.Column(db.LargeBinary)

    created_at = db.Column( db.DateTime, server_default=db.func.now() )
    updated_at = db.Column( db.DateTime, onupdate=db.func.now() )

    user_id = db.Column( db.Integer, db.ForeignKey( 'user.id' ) )
    forum_id = db.Column( db.Integer, db.ForeignKey( 'forum.id' ) )

    @validates('image')
    def validate_avatar( self, attr, image ):
        if image is not None:
            file_format = imghdr.what(None, h= image)
            if file_format != 'jpeg':
                abort ("Only JPEG images are permitted.")
        return image.filename

    @validates( 'title' )
    def validate_title( self, attr, title ):
        if type(title) is str and len(title) in range(4, 16):
            return title
        else:
            abort( "Password must be a string between 4 - 15 characters. ")

    def __repr__(self):
        return f'<Post {self.id}: {self.title}>'


# Models go here!
