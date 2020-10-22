from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from api.models import db


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
    app.config['SECRET_KEY'] = '12332432432432'
    db.init_app(app)
    migrate.init_app(app,db)

    from api.routes.main import main
    app.register_blueprint(main)

    from api.models import Symbol
    with app.app_context():
        db.create_all()
    return app