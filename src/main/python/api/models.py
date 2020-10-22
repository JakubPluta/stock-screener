from flask_sqlalchemy import SQLAlchemy
from flask import current_app


SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SECRET_KEY = '12332432432432'

db = SQLAlchemy()


class Symbol(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    ticker = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)

