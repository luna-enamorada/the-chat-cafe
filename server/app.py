# Remote library imports
from flask_restful import Resource
from flask import Flask, request, make_response, jsonify, session, abort
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, Unauthorized


# Local imports
from config import app, db, api
from models import User, Forum, Post, Comment



@app.route('/')
def index():
    return '<h1> Testing </h1>'

class Users( Resource ):
    def get(self):
        users = [ user.user_dict() for user in User.query.all() ]

        response = make_response(
            jsonify(users), 200
        )
        return response
api.add_resource( Users, '/users', endpoint = 'users' )

class Forums( Resource ):
    def get(self):
        forums = [ forum.forum_dict() for forum in Forum.query.all() ]

        response = make_response(
            jsonify(forums), 200
        )
        return response
api.add_resource( Forums, '/forums' )

class Posts( Resource ):
    def get(self):
        posts = [ post.post_dict() for post in Post.query.all() ]

        response = make_response(
            jsonify(posts), 200
        )
        return response
api.add_resource( Posts, '/posts' )

class UserByID( Resource ):
    def get(self, id):
        user = User.find(id)
        if not user:
            abort( 404, "User not found." )

        user_to_dict = user.user_dict()
        user_to_dict['posts'] = [ post.post_dict() for post in user.posts ]
        user_to_dict['comments'] = [ comment.comment_dict() for comment in user.comments ]
        
        response = make_response(
            jsonify(user_to_dict),
            200
        )
        return response

    def patch(self, id ):
        user = User.find(id)
        for attr in request.get_json():
            setattr( user, attr, request.get_json()[attr])
        db.session.add(user)
        db.session.commit()

        user_to_dict = user.user_dict()

        response = make_response(
            jsonify( user_to_dict),
            200
        )
        if User.validation_errors :
            errors = User.return_validation_errors()
            User.clear_validation_errors()
            return { 'errors': errors }, 422
        
        return response
            
    def delete( self, id ):
        user = User.find(id)
        if not user:
            abort(404, "User not found.")
        db.session.delete(user)
        db.session.commit()

        return make_response(' ', 204)
api.add_resource(UserByID, '/users/<int:id>')

class ForumByID( Resource ):
    def get(self, id):
        forum = Forum.find(id)
        if not forum:
            abort( 404, "Forum not found." )

        forum_to_dict = forum.forum_dict()
        forum_to_dict['posts'] = [ post.post_dict() for post in forum.posts ]
        
        response = make_response(
            jsonify(forum_to_dict),
            200
        )
        return response

    def patch(self, id ):
        forum = Forum.find(id)
        for attr in request.get_json():
            setattr( forum , attr, request.get_json()[attr])
        db.session.add(forum)
        db.session.commit()

        forum_to_dict = forum.forum_dict()

        response = make_response(
            jsonify( forum_to_dict),
            200
        )
        if Forum.validation_errors :
            errors = Forum.return_validation_errors()
            Forum.clear_validation_errors()
            return { 'errors': errors }, 422
        
        return response
            
    def delete( self, id ):
        forum = Forum.find(id)
        if not forum:
            abort(404, "Forum not found.")
        db.session.delete(forum)
        db.session.commit()

        return make_response(' ', 204)
api.add_resource(ForumByID, '/forums/<int:id>')

class PostByID( Resource ):
    def get(self, id):
        post  = Post.find(id)
        if not post:
            abort( 404, "Forum not found." )

        forum_to_dict = post.post_dict()
        forum_to_dict['comments'] = [ comment.comment_dict() for comment in post.comments ]
        
        response = make_response(
            jsonify(forum_to_dict),
            200
        )
        return response
# eventually want to add in a way so that only the person who made the post can access patch and delete functions
    def patch(self, id ):
        post  = Post.find(id)
        for attr in request.get_json():
            setattr( post, attr, request.get_json()[attr])
        db.session.add(post)
        db.session.commit()

        post_to_dict = post.forum_dict()

        response = make_response(
            jsonify( post_to_dict ),
            200
        )
        if Post.validation_errors :
            errors = Post.return_validation_errors()
            Post.clear_validation_errors()
            return { 'errors': errors }, 422
        
        return response
            
    def delete( self, id ):
        post  = Post.find(id)
        if not post:
            abort(404, "Forum not found.")
        db.session.delete(post)
        db.session.commit()

        return make_response(' ', 204)
    
    def post( self, id ):
        post  = Post.find(id)
        rq = request.get_json()

        new_comment = Comment(
            content = rq['content'],
            user_id = rq['user_id'],
            post_id = post.id
        )
        response = make_response( 
            jsonify(new_comment.comment_dict(), 201)
        )

        if Comment.validation_errors :
            errors = Comment.return_validation_errors()
            Comment.clear_validation_errors()
            return { 'errors': errors }, 422
        
        db.session.add(new_comment)
        db.session.commit()

        return response
api.add_resource(PostByID, '/posts/<int:id>')

#commented code will be uncommented once we have the front end
class Register( Resource ):
    def post(self):
        rq = request.get_json()
        # file = request.files['file']

        new_user = User(
            username = rq['username'],
            email = rq['email'],
            _password = rq['_password'],
            bio = rq['bio'],
            # avatar = file.read()
        )

        # session[ 'user_id' ] = new_user.id 

        response = make_response( 
            jsonify(new_user.user_dict(), 201)
        )

        if User.validation_errors :
            errors = User.return_validation_errors()
            User.clear_validation_errors()
            return { 'errors': errors }, 422
        
        db.session.add(new_user)
        db.session.commit()

        return response
api.add_resource(Register, '/register')

# user log in, log out, and auth // not set in stone still needs to be tested on front end

class Login( Resource ):
    def post(self):
        rq = request.get_json()
        user = User.query.filter( User.username.like( f"%{ rq[ 'name' ] }%" ) ).first() 

        if user:
            session[ 'user_id' ] = user.id
            return user.user_dict(), 200
        else:
            return { 'errors': [ 'Invalid username/password. Please try again.' ] }, 401
api.add_resource( Login, '/login', endpoint = 'login' )

class Logout( Resource ):
    def delete(self):
        session[ 'user_id' ] = None
        return ' ', 204
api.add_resource( Logout, '/logout', endpoint = 'logout' )

class AuthorizeSession( Resource ):
    def get(self):
        if not session.get('user_id'):
            return { 'errors': 'You must be logged in to do that. Please log in or make an account.' }, 401
        else: 
            user = User.query.filter_by( id = session[ 'user_id'] ).first()
            return user.user_dict(), 200
api.add_resource( AuthorizeSession, '/authorize', endpoint = 'authorize' )


@app.errorhandler(NotFound)
def handle_not_found():
    response = make_response(
        "Not Found: Sorry the resource you are looking for does not exist",
        404
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)