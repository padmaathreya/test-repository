from app import app
from models.db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db_create_all()
