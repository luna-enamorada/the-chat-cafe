# Remote library imports
from flask_restful import Resource
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

# Local imports
from config import app, db, api
from models import User

# Views go here!

@app.route('/')
def index():
    return '<h1> Testing </h1>'


@app.route('/register', methods=[ 'POST' ])
def register():
    if request.method == 'POST':
        request = request.get_json()

        new_user = User(
            
        )


        avatar = request.files['file']
        upload = upload(filename = avatar.filename, data = avatar.read())

        db.session.add(upload)
        db.session.commit()

        return f'Uploaded: {avatar.filename}'
    return

if __name__ == '__main__':
    app.run(port=5555, debug=True)

