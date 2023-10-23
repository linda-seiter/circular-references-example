#!/usr/bin/env python3

from app import app
from models import db, User, Review, Movie

with app.app_context():

    User.query.delete()
    Review.query.delete()
    Movie.query.delete()

    u1 = User(username='Tal Yuri',_password_hash='secret1')
    u2 = User(username='Raha Rosario',_password_hash='secret2')
    u3 = User(username='Luca Mahan',_password_hash='secret3')
    db.session.add_all([u1, u2, u3])
    db.session.commit()

    m1 = Movie(title='The Movie', year = 2023, creator = u1)
    m2 = Movie(title='Another Movie', year = 2020, creator = u3)
    m3 = Movie(title='Yet Another Movie', year = 2021, creator = u1)
    db.session.add_all([m1, m2, m3])
    db.session.commit()

    db.session.add(Review(content="very funny",  user=u1, movie=m1))
    db.session.add(Review(content="not funny",  user=u2, movie=m1))
    db.session.add(Review(content="boring",  user=u1, movie=m2))
    db.session.add(Review(content="really boring",  user=u3, movie=m2))
    db.session.add(Review(content="too long",  user=u3, movie=m3))

    db.session.commit()
    
    #movies created by user1
    print(f"created by {u1}")
    [print(movie) for movie in u1.created_movies]

    #movies reviewed by user1
    print(f"reviewed by {u1}")
    [print(movie) for movie in u1.reviewed_movies]
