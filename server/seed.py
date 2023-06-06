#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
# from faker import Faker

# Local imports
from app import app
from models import db, User, Forum, Post, Comment

if __name__ == '__main__':
    # fake = Faker()
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
            _password = 'Marie44',
            bio = 'Looking to chat about Star Trek!'
        )

        u2 = User(
            username = 'brianr',
            email = 'brian.rivera.d@gmail.com',
            _password = 'Marty1996',
            bio = 'Whats up?!'
        )

        u3 = User(
            username = 'MartyMan',
            email = 'martyman123@gmail.com',
            _password = 'chickennuggets',
            bio = 'Really love some chicken nuggets'
        )

        u4 = User(
            username = 'marieantionette',
            email = 'marie.the.sleepy@gmail.com',
            _password = 'Meow987',
            bio = 'Meow'
        )

        u5 = User(
            username = 'theHair',
            email = 'steve.har@gmail.com',
            _password = 'password',
            bio = 'Badass'
        )

        u6 = User(
            username = 'dustybuns',
            email = 'dustinhenderson@gmail.com',
            _password = 'Suzie1234',
            bio = 'Genius'
        )

        f1 = Forum(
            title = 'Cats',
            description = 'meow meow meow meow' 
        )

        f2 = Forum(
            title = 'Dogs',
            description = 'woof woof woof woof' 
        )

        f3 = Forum(
            title = 'Gaming.',
            description = 'Be nice or else.' 
        )

        f4 = Forum(
            title = 'Spiderman',
            description = 'We only talk about peak here' 
        )

        f5 = Forum(
            title = 'Travel',
            description = 'Plan your dream trip' 
        )

        f6 = Forum(
            title = 'Star Trek',
            description = 'For the trekkies by the trekkies. 🖖' 
        )

        f7 = Forum(
            title = 'Manga',
            description = "If it's not in black and white then it doesn't belong here" 
        )

        p1 = Post( 
            title = 'The Best Cat',
            content = "It's obviously my cat",
            user_id = 1,
            forum_id = 1
        )

        p2 = Post( 
            title = 'The Best Dog',
            content = "All dogs are the best :)",
            user_id = 3,
            forum_id = 2
        )

        c1 = Comment( 
            content = "Actually I think my cat is the best.",
            user_id = 4,
            post_id = 1
        )


        db.session.add_all([u1, u2, u3, u4, u5, u6])
        db.session.add_all([f1, f2, f3, f4, f5, f6, f7])
        db.session.add_all([p1, p2])
        db.session.add_all([c1])

        db.session.commit()
        print("added")