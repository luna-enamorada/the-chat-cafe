#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Forum, Post, Comment

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        User.query.delete()
        Forum.query.delete()
        Post.query.delete()
        Comment.query.delete()

        u1 = User(
            username = 'selenaw',
            email = 's.a.williams@gmail.com',
            password = 'Marie44',
            bio = 'Looking to chat about Star Trek!'
        )

        u2 = User(
            username = 'brianr',
            email = 'brian.rivera.d@gmail.com',
            password = 'Marty1996',
            bio = 'Whats up?!'
        )

        u3 = User(
            username = 'MartyMan',
            email = 'martyman123@gmail.com',
            password = 'chickennuggets',
            bio = 'Really love some chicken nuggets'
        )

        u4 = User(
            username = 'marieantionette',
            email = 'marie.the.sleepy@gmail.com',
            password = 'Meow987',
            bio = 'Meow'
        )

        u5 = User(
            username = 'theHair',
            email = 'steve.har@gmail.com',
            password = 'password',
            bio = 'Badass'
        )

        u6 = User(
            username = 'dustybuns',
            email = 'dustinhenderson@gmail.com',
            password = 'Suzie1234',
            bio = 'Genius'
        )

        db.session.add_all([u1, u2, u3, u4, u5, u6])

        
