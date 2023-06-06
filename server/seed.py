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

        f1 = Forum(
            title = 'Star Trek',
            description = 'Discussing the ends and outs of Star Trek'
        )

        f2 = Forum(
            title = 'Spider-man',
            description = 'Do you love Spider-man? Join our forum!'
        )

        f3 = Forum(
            title = 'Star Wars',
            description = 'May the Forum Be With You.'
        )

        f4 = Forum(
            title = 'The Sims',
            description = 'Sul sul!'
        )

        db.session.add_all([f1, f2, f3, f4])

        p1 = Post(
            title = 'Mr. Spock is my favorite',
            content = 'After watching tng and deep space, I have to say Mr. Spock is still my favorite.',
            user_id = u1.id,
            forum_id = f1.id
        )

        p2 = Post(
            title = 'Best tos episode?',
            content = 'Can someone send me a list of best the original series episodes?',
            user_id = u2.id,
            forum_id = f1.id
        )

        p3 = Post(
            title = 'Who would win in a fight?',
            content = 'Kirk or Piccard?',
            user_id = u3.id,
            forum_id = f1.id
        )

        p4 = Post(
            title = 'Is it Spider-man or Spider man or Spiderman?',
            content = 'Can someone help me??',
            user_id = u5.id,
            forum_id = f2.id
        )

        p5 = Post(
            title = 'Does anyone have a copy of ps2 Spider-man 2?',
            content = 'Trying to play this game again.',
            user_id = u2.id,
            forum_id = f2.id
        )

        p6 = Post(
            title = 'Fisk is actually the worst villain.',
            content = 'Fight me about it',
            user_id = u4.id,
            forum_id = f2.id
        )

        p7 = Post(
            title = 'What are the teddy bears called again?',
            content = 'My friends keep making fun of me, whats the teddy bears in the trees called?',
            user_id = u5.id,
            forum_id = f3.id
        )

        p8 = Post(
            title = 'Pod racing scene',
            content = 'Thoughts?',
            user_id = u3.id,
            forum_id = f3.id
        )

        p9 = Post(
            title = 'Princess Leia is my favorite',
            content = 'Can anybody share their favorite pics?',
            user_id = u4.id,
            forum_id = f3.id
        )

        p10 = Post(
            title = 'Still waiting on cars',
            content = "Does anyone think we'll get cars in the sims 4 before 5 comes out?",
            user_id = u1.id,
            forum_id = f4.id
        )

        p11 = Post(
            title = 'Calculating the total cost of expansion packs',
            content = "I don't even want to think about how much this all costs.",
            user_id = u1.id,
            forum_id = f4.id
        )

        p12 = Post(
            title = 'Secret worlds?',
            content = 'Full list of secret sims 4 worlds',
            user_id = u6.id,
            forum_id = f4.id
        )

        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])

        c1 = Comment(
            content = 'Absolutely ridiculous obviously Data is the best.',
            user_id = u6.id,
            post_id = p1.id,
        )

        c2 = Comment(
            content = 'Have to agree with op, no one holds a candle to Spock',
            user_id = u4.id,
            post_id = p1.id,
        )

        c3 = Comment(
            content = 'Just watch Amok time',
            user_id = u1.id,
            post_id = p2.id,
        )

        c4 = Comment(
            content = "Don't listen to them obviously its Space Seed",
            user_id = u6.id,
            post_id = p2.id,
        )

        c5 = Comment(
            content = 'Kirk no contest',
            user_id = u1.id,
            post_id = p3.id,
        )

        c6 = Comment(
            content = 'How is this a question, Kirks fighting style sucks',
            user_id = u2.id,
            post_id = p3.id,
        )

        c7 = Comment(
            content = 'Its Spider-man',
            user_id = u4.id,
            post_id = p4.id,
        )

        c8 = Comment(
            content = 'Thank you!',
            user_id = u5.id,
            post_id = p4.id,
        )

        c9 = Comment(
            content = 'Ebay has some!',
            user_id = u3.id,
            post_id = p5.id,
        )

        c10 = Comment(
            content = 'I can send you a pirate link',
            user_id = u4.id,
            post_id = p5.id,
        )

        c11 = Comment(
            content = 'Cowards in the forum',
            user_id = u4.id,
            post_id = p6.id,
        )

        c12 = Comment(
            content = "I don't even have the time to tell you how wrong you are",
            user_id = u2.id,
            post_id = p6.id,
        )

        c13 = Comment(
            content = 'Ewoks!',
            user_id = u3.id,
            post_id = p7.id,
        )

        c14 = Comment(
            content = 'An absolute masterpiece',
            user_id = u5.id,
            post_id = p8.id,
        )

        c15 = Comment(
            content = 'I will fight you',
            user_id = u6.id,
            post_id = p8.id,
        )

        c16 = Comment(
            content = 'She really is the best',
            user_id = u5.id,
            post_id = p9.id,
        )

        c17 = Comment(
            content = 'A queen!',
            user_id = u6.id,
            post_id = p9.id,
        )

        c18 = Comment(
            content = "Fat chance, I doubt we'll get any big game play updates again",
            user_id = u6.id,
            post_id = p10.id,
        )

        c19 = Comment(
            content = "Dang, I'm still holding out on hope.",
            user_id = u1.id,
            post_id = p10.id,
        )

        c20 = Comment(
            content = "Should've pirated them!",
            user_id = u2.id,
            post_id = p11.id,
        )

        c21 = Comment(
            content = "There's no reason for logic here sir",
            user_id = u1.id,
            post_id = p11.id,
        )

        c22 = Comment(
            content = "I only know the one in willow creek in the tree",
            user_id = u3.id,
            post_id = p12.id,
        )

        c23 = Comment(
            content = "I think there's one is oasis springs too. Behind a mine",
            user_id = u1.id,
            post_id = p12.id,
        )

        c24 = Comment(
            content = 'Thank you!',
            user_id = u5.id,
            post_id = p7.id,
        )

        db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24])