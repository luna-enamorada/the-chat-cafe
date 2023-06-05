# Remote library imports
from flask_restful import Resource
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

# Local imports
from config import app, db, api
from models import User, Recipe

# Views go here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)


