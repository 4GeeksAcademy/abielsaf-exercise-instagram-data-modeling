import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    def to_dict(self):
            return {}
    
class Follower(Base):
     __tablename__ = 'followers'
     ID = Column(Integer, primary_key=True, nullable=False)
     user_from_id = Column(Integer, ForeignKey('users.id'), nullable=False)
     user_to_id = Column(Integer, ForeignKey('users.id'), nullable=False)

     def to_dict(self):
            return {}


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
            return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(Enum, nullable=False)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))

    def to_dict(self):
            return {}

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, nullable=False)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    def to_dict(self):
            return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
