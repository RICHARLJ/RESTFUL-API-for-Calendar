# models.py

from flask_login import UserMixin
from . import db


# Define the User data-model
class User(UserMixin, db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # roles = db.relationship('Role', secondary='user_roles')


# # Define the Role data-model
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(50), unique=True)
