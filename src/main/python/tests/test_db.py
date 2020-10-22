from api import create_app
from api.models import db, Symbol

app = create_app()


with app.app_context():
    s = Symbol.query.all()



